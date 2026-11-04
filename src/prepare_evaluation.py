"""Rebuild the fixed reviewed evaluation from source data and annotation decisions.

This applies recorded editorial decisions; it does not automatically review science.
Historical sampling and audit artifacts remain in data/evaluation/.
"""
import hashlib
from collections import Counter
from common import ROOT, read, save, key


def main():
    data = ROOT / "data"
    sources = {r["id"]: r for r in read(data / "processed/sciq_test.json")}
    corpus = {r["passage_id"]: r for r in read(data / "processed/passages.json")}
    held_in = {key(r["question"]) for split in ["train", "validation"]
               for r in read(data / f"processed/sciq_{split}.json")}
    decisions = read(data / "annotations/evaluation_decisions.json")
    result = []
    for decision in decisions:
        row = dict(decision)
        source = sources[row.get("source_record_id", row["id"])]
        row["question"] = row.pop("question_override", source["question"])
        row["dataset_answer"] = source["correct_answer"]
        row["support"] = source["support"]
        row["passage_id"] = "passage_" + hashlib.sha256(row["support"].encode()).hexdigest()
        row["evidence_excerpt"] = row.pop("evidence_excerpt_override", row["support"])
        assert key(source["question"]) not in held_in
        assert key(row["question"]) not in held_in
        assert row["choices"][row["dataset_answer_letter"]] == row["dataset_answer"]
        assert len({key(v) for v in row["choices"].values()}) == 4
        assert row["evidence_excerpt"] in row["support"]
        assert corpus[row["passage_id"]]["text"] == row["support"]
        assert row["subject"] in {"Biology", "Chemistry", "Physics", "Earth and Space Science"}
        result.append(row)
    assert len(result) == len({r["id"] for r in result}) == 100
    assert len({key(r["question"]) for r in result}) == 100
    save(data / "evaluation/phase1_evaluation_v2.json", result)
    print("Evaluation items:", len(result))
    print("Subjects:", dict(Counter(r["subject"] for r in result)))


if __name__ == "__main__":
    main()
