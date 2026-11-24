"""Train a small MLP subject baseline using validation selection only."""
import argparse
import platform
import warnings
from importlib.metadata import version
from itertools import product

import joblib
from sklearn.exceptions import ConvergenceWarning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from threadpoolctl import threadpool_limits

from common import ROOT, key, read, save
from train_classical import load_split, metrics

MODEL = ROOT / "models/neural.joblib"


def train():
    """Compare the recorded hidden-layer and regularization settings."""
    config = read(ROOT / "data/annotations/phase2_experiment.json")
    settings = config["neural_search"]
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
    candidates, best, best_score = [], None, None
    # Grid order resolves exact ties: fewer neurons, then stronger regularization.
    for neurons, alpha in product(settings["hidden_units"], settings["alpha"]):
        model = Pipeline([
            ("tfidf", TfidfVectorizer(**tfidf)),
            ("classifier", MLPClassifier(hidden_layer_sizes=(neurons,), alpha=alpha,
                activation="relu", solver="lbfgs", max_iter=settings["max_iter"],
                max_fun=settings["max_fun"], tol=settings["tol"],
                early_stopping=False, random_state=config["random_seed"])),
        ])
        # Small matrices need no large thread pool; fail on unfinished optimization.
        with warnings.catch_warnings(), threadpool_limits(limits=1):
            warnings.simplefilter("error", ConvergenceWarning)
            model.fit(x_train, y_train)
        predicted = model.predict(x_val)
        scores = metrics(y_val, predicted, config["classes"])
        classifier = model.named_steps["classifier"]
        candidates.append({"hidden_units": neurons, "alpha": alpha,
            "accuracy": scores["accuracy"], "macro_f1": scores["macro_f1"],
            "iterations": int(classifier.n_iter_), "training_loss": float(classifier.loss_)})
        score = (scores["macro_f1"], scores["accuracy"])
        if best_score is None or score > best_score:
            best_score = score
            best = model, {"hidden_units": neurons, "alpha": alpha}, scores, predicted
        print(f"Hidden units={neurons}, alpha={alpha}: validation macro-F1={scores['macro_f1']:.4f}", flush=True)
    model, parameters, scores, predicted = best
    classical = read(ROOT / "reports/phase2_classical_validation.json")
    if classical["tfidf"] != config["tfidf"] or any(
        classical["data_fingerprints"][s] != config["splits"][s]["model_fields_sha256"]
        for s in ["train", "validation"]
    ):
        raise ValueError("Classical baseline used a different representation or dataset")
    report = {
        "stage": "validation_only_test_not_evaluated", "random_seed": config["random_seed"],
        "sizes": {"train": len(training), "validation": len(validation)},
        "data_fingerprints": {s: config["splits"][s]["model_fields_sha256"] for s in ["train", "validation"]},
        "tfidf": config["tfidf"], "candidate_results": candidates,
        "selected_parameters": parameters, "fixed_settings": {k: settings[k] for k in ["max_iter", "max_fun", "tol"]},
        "architecture": "One ReLU hidden layer and a four-class softmax output; L-BFGS optimization; no class or sample weighting.",
        "validation": scores, "classical_validation": classical["validation"],
        "majority_reference": classical["majority_reference"],
        "training": metrics(y_train, model.predict(x_train), config["classes"]),
        "vocabulary_size": len(model.named_steps["tfidf"].vocabulary_),
        "versions": {"python": platform.python_version(), **{p: version(p) for p in ["scikit-learn", "numpy", "scipy", "joblib", "threadpoolctl"]}},
        "predictions": [{"id": r["id"], "true_subject": r["subject"], "predicted_subject": str(p)}
                        for r, p in zip(validation, predicted)],
        "limitation": "Small validation set used for tuning, one random seed, unequal weighting strategies across model families; no final test result or robust superiority claim.",
    }
    MODEL.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL)
    if joblib.load(MODEL).predict(x_val).tolist() != predicted.tolist():
        raise RuntimeError("Saved neural model predictions differ")
    save(ROOT / "reports/phase2_neural_validation.json", report)
    print("Selected parameters:", parameters)
    print(f"Validation accuracy: {scores['accuracy']:.4f}; macro-F1: {scores['macro_f1']:.4f}")
    print("Test data was not loaded or scored. Model saved to", MODEL)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predict", metavar="QUESTION", help="Use the saved MLP for a new question")
    args = parser.parse_args()
    if args.predict is not None:
        if not args.predict.strip():
            parser.error("Provide a nonempty question")
        print(joblib.load(MODEL).predict([args.predict])[0])
    else:
        train()
