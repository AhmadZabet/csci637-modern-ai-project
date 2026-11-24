"""Train the classical subject baseline; select using validation, never test data."""
import argparse
import hashlib
import json
import platform
import warnings
from importlib.metadata import version
from itertools import product

import joblib
from sklearn.dummy import DummyClassifier
from sklearn.exceptions import ConvergenceWarning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.pipeline import Pipeline

from common import ROOT, key, read, save

MODEL = ROOT / "models/classical.joblib"


def load_split(config, split):
    """Reject changes to the recorded questions, labels, IDs or order."""
    expected = config["splits"][split]
    rows = read(ROOT / expected["path"])
    records = [{"id": r["id"], "question": r["question"], "subject": r["subject"]} for r in rows]
    digest = hashlib.sha256(json.dumps(records, ensure_ascii=False, sort_keys=True,
                                      separators=(",", ":")).encode("utf-8")).hexdigest()
    if digest != expected["model_fields_sha256"] or [r["id"] for r in rows] != expected["record_ids"]:
        raise ValueError(f"{split} data changed: review the experiment setup before training")
    return rows


def metrics(y_true, y_pred, classes):
    """Use one explicit class order, including classes with no predictions."""
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, labels=classes, average="macro", zero_division=0)),
        "per_class": classification_report(y_true, y_pred, labels=classes, output_dict=True, zero_division=0),
        "confusion_matrix": confusion_matrix(y_true, y_pred, labels=classes).tolist(),
        "class_order": classes,
        "confusion_matrix_axes": "rows=true subject, columns=predicted subject",
    }


def train():
    """Fit six predeclared candidates on train; select by validation macro-F1."""
    config = read(ROOT / "data/annotations/phase2_experiment.json")
    settings = config["classical_search"]
    classes = config["classes"]
    # This function deliberately loads only training and validation records.
    training = load_split(config, "train")
    validation = load_split(config, "validation")
    if {key(r["question"]) for r in training} & {key(r["question"]) for r in validation}:
        raise ValueError("Training and validation questions overlap")
    x_train = [r["question"] for r in training]
    y_train = [r["subject"] for r in training]
    x_val = [r["question"] for r in validation]
    y_val = [r["subject"] for r in validation]
    tfidf = dict(config["tfidf"])
    tfidf["ngram_range"] = tuple(tfidf["ngram_range"])
    candidates = []
    best = None
    best_score = None
    # Grid order breaks exact score ties: lower C, then no class weighting.
    for c, weight in product(settings["C"], settings["class_weight"]):
        model = Pipeline([
            ("tfidf", TfidfVectorizer(**tfidf)),
            ("classifier", LogisticRegression(C=c, class_weight=weight,
                solver="lbfgs", max_iter=settings["max_iter"], random_state=config["random_seed"])),
        ])
        with warnings.catch_warnings():
            warnings.simplefilter("error", ConvergenceWarning)
            model.fit(x_train, y_train)
        predicted = model.predict(x_val)
        scores = metrics(y_val, predicted, classes)
        candidates.append({"C": c, "class_weight": weight,
                           "accuracy": scores["accuracy"], "macro_f1": scores["macro_f1"]})
        score = (scores["macro_f1"], scores["accuracy"])
        if best_score is None or score > best_score:
            best_score = score
            best = (model, {"C": c, "class_weight": weight}, scores, predicted)
    model, parameters, scores, predicted = best
    dummy = DummyClassifier(strategy="most_frequent").fit(x_train, y_train)
    report = {
        "stage": "validation_only_test_not_evaluated",
        "random_seed": config["random_seed"],
        "sizes": {"train": len(training), "validation": len(validation)},
        "data_fingerprints": {s: config["splits"][s]["model_fields_sha256"] for s in ["train", "validation"]},
        "tfidf": config["tfidf"], "candidate_results": candidates,
        "selected_parameters": parameters, "validation": scores,
        "majority_reference": metrics(y_val, dummy.predict(x_val), classes),
        "vocabulary_size": len(model.named_steps["tfidf"].vocabulary_),
        "versions": {"python": platform.python_version(), **{p: version(p) for p in ["scikit-learn", "numpy", "scipy", "joblib"]}},
        "predictions": [{"id": r["id"], "true_subject": r["subject"], "predicted_subject": str(p)}
                        for r, p in zip(validation, predicted)],
        "limitation": "39 validation items used for model selection; these are tuning results, not final test performance.",
    }
    MODEL.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL)
    # Confirm that the saved artifact reproduces the selected predictions.
    if joblib.load(MODEL).predict(x_val).tolist() != predicted.tolist():
        raise RuntimeError("Saved model predictions differ")
    save(ROOT / "reports/phase2_classical_validation.json", report)
    print("Selected parameters:", parameters)
    print(f"Validation accuracy: {scores['accuracy']:.4f}; macro-F1: {scores['macro_f1']:.4f}")
    print("Test data was not loaded or scored. Model saved to", MODEL)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predict", metavar="QUESTION", help="Use the saved model for one new question")
    args = parser.parse_args()
    if args.predict is not None:
        if not args.predict.strip():
            parser.error("Provide a nonempty question")
        print(joblib.load(MODEL).predict([args.predict])[0])
    else:
        train()
