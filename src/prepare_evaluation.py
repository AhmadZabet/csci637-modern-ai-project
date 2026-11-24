"""Rebuild the reviewed evaluation set using saved annotation decisions."""

# Create a SHA-256 identifier for each supporting passage.
import hashlib

# Count the number of evaluation questions in each subject.
from collections import Counter

# Import shared paths, JSON helpers, and the text-comparison function.
from common import ROOT, read, save, key


def main():
    """Build, validate, and save the final 100-question evaluation set."""

    # Locate the project's data folder.
    data = ROOT / "data"

    # Load cleaned test records and organize them by question ID.
    sources = {r["id"]: r for r in read(data / "processed/sciq_test.json")}

    # Load supporting passages and organize them by passage ID.
    corpus = {r["passage_id"]: r for r in read(data / "processed/passages.json")}

    # Collect training and validation question keys for overlap checks.
    held_in = {key(r["question"]) for split in ["train", "validation"]
               for r in read(data / f"processed/sciq_{split}.json")}

    # Load the selected questions, subject labels, choices, and recorded edits.
    decisions = read(data / "annotations/evaluation_decisions.json")

    # Store the completed evaluation items.
    result = []

    # Build one evaluation item from each saved decision.
    for decision in decisions:
        # Copy the decision so we can build the output record.
        row = dict(decision)

        # Find the source test record using its original ID when available.
        source = sources[row.get("source_record_id", row["id"])]

        # Apply edited wording if recorded, otherwise use the source question.
        # pop() removes the temporary override field from the output record.
        row["question"] = row.pop("question_override", source["question"])

        # Copy the correct answer and full passage from the source record.
        row["dataset_answer"] = source["correct_answer"]
        row["support"] = source["support"]

        # Calculate the passage ID using the same rule as prepare_data.py.
        row["passage_id"] = "passage_" + hashlib.sha256(row["support"].encode()).hexdigest()

        # Use a saved evidence excerpt if available, otherwise use the full passage.
        row["evidence_excerpt"] = row.pop("evidence_excerpt_override", row["support"])

        # Check that the original question has no matching training/validation key.
        assert key(source["question"]) not in held_in

        # Repeat the overlap check using the final question wording.
        assert key(row["question"]) not in held_in

        # Check that the answer letter points to the source's correct answer.
        assert row["choices"][row["dataset_answer_letter"]] == row["dataset_answer"]

        # Check that there are four distinct normalized answer-choice texts.
        assert len({key(v) for v in row["choices"].values()}) == 4

        # Check that the evidence excerpt appears in the full supporting passage.
        assert row["evidence_excerpt"] in row["support"]

        # Check that the passage ID refers to the same text in the passage collection.
        assert corpus[row["passage_id"]]["text"] == row["support"]

        # Check that the subject belongs to our four evaluation categories.
        assert row["subject"] in {"Biology", "Chemistry", "Physics", "Earth and Space Science"}

        # Keep the completed item after all its checks pass.
        result.append(row)

    # Check that there are exactly 100 items with 100 unique IDs.
    assert len(result) == len({r["id"] for r in result}) == 100

    # Check that all 100 questions have different normalized text.
    assert len({key(r["question"]) for r in result}) == 100

    # Save the final evaluation set as JSON.
    save(data / "evaluation/phase1_evaluation_v2.json", result)

    # Display the total number of evaluation items.
    print("Evaluation items:", len(result))

    # Display the number of questions assigned to each subject.
    print("Subjects:", dict(Counter(r["subject"] for r in result)))


if __name__ == "__main__":
    main()