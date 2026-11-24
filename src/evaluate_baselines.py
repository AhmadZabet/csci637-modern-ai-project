"""Score the two validation-selected baselines without fitting or tuning."""
import hashlib
from collections import Counter

import joblib
import numpy as np

from common import ROOT, key, read, save
from train_classical import load_split, metrics

OUTPUT = ROOT / "reports/phase2_test_comparison.json"


def evaluate():
    """Verify frozen models and data, then score the reserved classification test."""
    config = read(ROOT / "data/annotations/phase2_experiment.json")
    training = load_split(config, "train")
    validation = load_split(config, "validation")
    models, provenance = {}, {}
    for name in ["classical", "neural"]:
        model_path = ROOT / f"models/{name}.joblib"
        report_path = ROOT / f"reports/phase2_{name}_validation.json"
        report = read(report_path)
        if report["selected_parameters"] != config["selected_parameters"][name]:
            raise ValueError(f"{name} selection differs from the recorded setup")
        if report["tfidf"] != config["tfidf"]:
            raise ValueError(f"{name} TF-IDF configuration changed")
        for split in ["train", "validation"]:
            if report["data_fingerprints"][split] != config["splits"][split]["model_fields_sha256"]:
                raise ValueError(f"{name} used different {split} data")
        model = joblib.load(model_path)
        params = model.named_steps["classifier"].get_params()
        expected = config["selected_parameters"][name]
        actual = ({"C": params["C"], "class_weight": params["class_weight"]} if name == "classical"
                  else {"hidden_units": params["hidden_layer_sizes"][0], "alpha": params["alpha"]})
        if actual != expected or params["random_state"] != config["random_seed"]:
            raise ValueError(f"{name} saved model settings changed")
        vectorizer = model.named_steps["tfidf"]
        for setting, value in config["tfidf"].items():
            if vectorizer.get_params()[setting] != (tuple(value) if setting == "ngram_range" else value):
                raise ValueError(f"{name} saved vectorizer settings changed")
        predicted = model.predict([r["question"] for r in validation]).tolist()
        if predicted != [r["predicted_subject"] for r in report["predictions"]]:
            raise ValueError(f"{name} no longer reproduces validation predictions")
        models[name] = model
        provenance[name] = {
            "model_sha256": hashlib.sha256(model_path.read_bytes()).hexdigest(),
            "validation_report_sha256": hashlib.sha256(report_path.read_bytes()).hexdigest(),
            "selected_parameters": expected,
        }
    first, second = [models[name].named_steps["tfidf"] for name in ["classical", "neural"]]
    if first.vocabulary_ != second.vocabulary_ or not np.array_equal(first.idf_, second.idf_):
        raise ValueError("Baselines have different fitted text representations")
    fingerprints = {s: config["splits"][s]["model_fields_sha256"] for s in ["train", "validation", "test"]}
    if OUTPUT.exists():
        previous = read(OUTPUT)
        if previous["data_fingerprints"] != fingerprints or any(
            previous["provenance"][name]["selected_parameters"] != provenance[name]["selected_parameters"]
            for name in models
        ):
            raise ValueError("A final comparison already exists for different data or selected settings")
    # Load held-out records only after checking the selected models.
    test = load_split(config, "test")
    question_sets = [{key(r["question"]) for r in rows} for rows in [training, validation, test]]
    if any(question_sets[i] & question_sets[j] for i,j in [(0,1),(0,2),(1,2)]):
        raise ValueError("Normalized question overlap between splits")
    x_test = [r["question"] for r in test]
    y_test = [r["subject"] for r in test]
    results = {}
    predictions = {}
    for name, model in models.items():
        predicted = model.predict(x_test)
        predictions[name] = predicted.tolist()
        results[name] = metrics(y_test, predicted, config["classes"])
    majority = Counter(r["subject"] for r in training).most_common(1)[0][0]
    results["majority_reference"] = metrics(y_test, [majority]*len(test), config["classes"])
    rows = [{"id": row["id"], "true_subject": row["subject"],
             **{name: predictions[name][i] for name in models}} for i,row in enumerate(test)]
    report = {
        "stage": "fixed_test_evaluated_no_further_tuning", "evaluation_date": "2026-11-24",
        "task": "Four-class question subject classification only",
        "sizes": {"train": len(training), "validation": len(validation), "test": len(test)},
        "random_seed": config["random_seed"], "data_fingerprints": fingerprints,
        "provenance": provenance, "results": results, "predictions": rows,
        "error_ids": {name: [r["id"] for r in rows if r[name] != r["true_subject"]] for name in models},
        "acceptance_targets": {name: {"accuracy_at_least_0.85": r["accuracy"] >= .85,
            "macro_f1_at_least_0.80": r["macro_f1"] >= .80} for name,r in results.items() if name in models},
        "limitations": ["Small imbalanced training and validation subsets; one seed.",
            "Curated, previously reviewed test questions are not a random unseen-content benchmark.",
            "Classical search includes class weighting; neural search does not. This compares complete pipelines.",
            "No answer-generation, learning-outcome, retrieval or challenge-behavior performance measured.",
            "Do not use these test scores to tune these baselines; preserve this test set for Phase 3."],
    }
    if OUTPUT.exists():
        # Retraining may serialize different bytes despite identical predictions.
        # Verify the results while retaining the original scoring provenance.
        previous = read(OUTPUT)
        if {k: v for k, v in previous.items() if k != "provenance"} != {
            k: v for k, v in report.items() if k != "provenance"
        }:
            raise ValueError("Repeated evaluation differs from the saved final comparison")
        print("Reproduced the recorded results; preserved original report and artifact hashes.")
    else:
        save(OUTPUT, report)
    for name, result in results.items():
        print(f"{name}: test accuracy={result['accuracy']:.4f}; macro-F1={result['macro_f1']:.4f}")
    print("No models were fitted or tuned. Saved", OUTPUT)


if __name__ == "__main__":
    evaluate()
