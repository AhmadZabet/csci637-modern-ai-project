"""Download pinned SciQ and create traceable cleaned splits and passages."""
import argparse
import hashlib
import json
import os
from collections import defaultdict
from common import ROOT, save, read, normalize, key

# Locations of the original and cleaned dataset files.
RAW = ROOT / "data/raw"
OUT = ROOT / "data/processed"

FIELDS = ["question", "correct_answer", "distractor1", "distractor2", "distractor3", "support"]


def download():
    os.environ["HF_HOME"] = str(ROOT / "data/.hf_cache")
    from datasets import load_dataset
    source = read(ROOT / "data/source_version.json")
    dataset = load_dataset(source["dataset"], revision=source["revision"])
    for split, records in dataset.items():
        save(RAW / f"sciq_{split}.json", [dict(row) for row in records])


"""Clean raw records, apply duplicate rules, and save checked outputs."""
def clean_data():
    OUT.mkdir(parents=True, exist_ok=True)

    # Store normalized records, raw-file fingerprints, and question groups.    
    splits = {}
    hashes = {}
    groups = defaultdict(list)

    # Read and normalize every record in the three raw splits.
    for split in ['train', 'validation', 'test']:
        path = RAW / f'sciq_{split}.json'
        
        # Record the fingerprint before cleaning.
        hashes[split] = hashlib.sha256(path.read_bytes()).hexdigest()
        splits[split] = []
        for index, original in enumerate(json.loads(path.read_text(encoding='utf-8'))):

            # Confirm that all expected fields contain strings.
            assert all(isinstance(original.get(f), str) for f in FIELDS), (split, index)

            # Remove extra whitespace from every field.
            row = {f: normalize(original[f]) for f in FIELDS}

            # Preserve the record's source location and passage availability.
            row.update(id=f'sciq_{split}_{index:05d}', original_split=split, original_index=index,
                       has_support=bool(row['support']))

          # Add the normalized record to its split.
            splits[split].append(row)

        # Group copies of the same question using a key that ignores case and extra whitespace.
            groups[key(row['question'])].append(row)

    # Identify matching questions with different recorded answers.
    variants = {q for q, rows in groups.items() if len({key(r['correct_answer']) for r in rows}) > 1}
        # Load saved decisions about which conflicting training records to keep.
    decision_path = ROOT / 'data' / 'answer_review_decisions.json'
    decisions = {d['question_key']: d for d in json.loads(decision_path.read_text(encoding='utf-8'))} if decision_path.exists() else {}
    # Check that every saved decision refers to a valid training group.
    for q, decision in decisions.items():
        assert q in variants
        assert any(r['id'] == decision['keep_id'] for r in groups[q])
        assert all(r['original_split'] == 'train' for r in groups[q]), 'Reviewed restoration supports training-only groups'
       
    # Conflicting groups without saved decisions still need review.
    pending = variants - decisions.keys()
    review = [dict(question_key=q, records=groups[q], reason='Different answer text; may be equivalent or context-dependent. Human review pending.') for q in sorted(pending)]

    # Collect validation and test question keys to prevent training overlap.
    heldout = {key(r['question']) for s in ['validation', 'test'] for r in splits[s]}
    clean = {}
    audit = []
    
    # Apply cleaning rules to each split.
    for split, rows in splits.items():
        clean[split] = []
        seen = set()
        # Prefer a passage-bearing copy when otherwise deduplicating a question.
        ordered = sorted(rows, key=lambda r: (not r['has_support'], r['original_index']))
        for row in ordered:
            q = key(row['question'])
            reason = None
            # Check for missing required fields.
            if any(not row[f] for f in FIELDS[:-1]):
                reason = 'missing_required_field'
            elif split == 'train' and q in heldout:
                reason = 'question_in_heldout_split'
            elif q in decisions and row['id'] != decisions[q]['keep_id']:
                reason = 'reviewed_duplicate'
            elif split == 'train' and q in pending:
                reason = 'answer_variant_pending_review'
            elif q in seen:
                reason = 'repeated_question'
            if reason:
                audit.append(dict(id=row['id'], split=split, reason=reason))
                continue
            
            # Keep the record and mark any unresolved answer conflict.
            seen.add(q)
            row['needs_answer_review'] = q in pending
            clean[split].append(row)
        
        # Restore the original order before saving.
        clean[split].sort(key=lambda r: r['original_index'])
        save(OUT / f'sciq_{split}.json', clean[split])
    
    # Confirm that the records selected by saved decisions were retained.
    kept_ids = {r['id'] for rows in clean.values() for r in rows}
    assert all(d['keep_id'] in kept_ids for d in decisions.values())
    
    # Collect distinct passages and link each one to its question IDs.
    passages = defaultdict(list)
    for rows in clean.values():
        for row in rows:
            if row['support']:
                passages[row['support']].append(row['id'])
    
    # Give every passage a stable identifier based on its text.
    corpus = [dict(passage_id='passage_' + hashlib.sha256(text.encode()).hexdigest(), text=text, source_ids=ids) for text, ids in passages.items()]
    
    # Save the passage collection and cleaning records.
    save(OUT / 'passages.json', corpus)
    save(OUT / 'answer_review_queue.json', review)
    save(OUT / 'cleaning_audit.json', audit)
    save(OUT / 'raw_sha256.json', hashes)
    
    # Build sets of question keys for the final consistency checks.
    sets = {s: {key(r['question']) for r in rows} for s, rows in clean.items()}
    assert all(len(sets[s]) == len(clean[s]) for s in clean)
    
    # Check that every split contains unique normalized questions.
    assert not (sets['train'] & sets['validation'] or sets['train'] & sets['test'] or sets['validation'] & sets['test'])
    
    # Account for every original record as either retained or excluded.
    assert sum(map(len, splits.values())) == sum(map(len, clean.values())) + len(audit)

    # Confirm that raw files stayed intact during cleaning.
    assert all(hashlib.sha256((RAW / f'sciq_{s}.json').read_bytes()).hexdigest() == hashes[s] for s in splits)
    
    # Confirm that raw files match the recorded SciQ source snapshot.
    expected = read(ROOT / "data/source_version.json")["raw_sha256"]
    assert hashes == expected, "Source data differs from the pinned snapshot"
    
    # Display the number of retained questions in each split.
    print({split: len(rows) for split, rows in clean.items()})



def prepare_classification():
    """Build labeled training and validation subsets using recorded annotations."""
    labels = read(ROOT / "data/annotations/classification_labels.json")
    summaries = {}
    question_sets = {}
    for split in ["train", "validation"]:
        sources = {row["id"]: row for row in read(OUT / f"sciq_{split}.json")}
        selected = [label for label in labels if label["split"] == split]
        if len({label["id"] for label in selected}) != len(selected):
            raise ValueError("Duplicate classification annotations")
        rows = []
        for label in selected:
            if label["subject"] not in {"Biology", "Chemistry", "Physics", "Earth and Space Science"}:
                raise ValueError("Invalid classification subject")
            row = dict(sources[label["id"]])
            row.update(label)
            rows.append(row)
        question_sets[split] = {key(row["question"]) for row in rows}
        save(OUT / f"classification_{split}.json", rows)
        summaries[split] = {subject: sum(row["subject"] == subject for row in rows)
                            for subject in sorted({row["subject"] for row in rows})}
    if question_sets["train"] & question_sets["validation"]:
        raise ValueError("Classification split overlap")
    save(ROOT / "data/annotations/classification_summary.json", {
        "counts": summaries, "input": "question text only", "labels": "subject",
        "status": "Review status recorded per annotation",
        "human_confirmed_counts": {split: sum(label.get("annotation_status") == "human_confirmed" for label in labels if label["split"] == split) for split in ["train", "validation"]},
        "scope": "Four-class starter subsets, not full-dataset annotation. No Phase 2 model results yet."
    })
    print("Classification subject counts:", summaries)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-download", action="store_true", help="Use existing raw JSON files")
    args = parser.parse_args()
    if not args.skip_download:
        download()
    clean_data()

    prepare_classification()
