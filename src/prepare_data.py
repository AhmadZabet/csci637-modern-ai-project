"""Download pinned SciQ and create traceable cleaned splits and passages."""
import argparse
import hashlib
import json
import os
from collections import defaultdict
from common import ROOT, save, read, normalize, key

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


def clean_data():
    OUT.mkdir(parents=True, exist_ok=True)
    splits = {}
    hashes = {}
    groups = defaultdict(list)
    for split in ['train', 'validation', 'test']:
        path = RAW / f'sciq_{split}.json'
        hashes[split] = hashlib.sha256(path.read_bytes()).hexdigest()
        splits[split] = []
        for index, original in enumerate(json.loads(path.read_text(encoding='utf-8'))):
            assert all(isinstance(original.get(f), str) for f in FIELDS), (split, index)
            row = {f: normalize(original[f]) for f in FIELDS}
            row.update(id=f'sciq_{split}_{index:05d}', original_split=split, original_index=index,
                       has_support=bool(row['support']))
            splits[split].append(row)
            groups[key(row['question'])].append(row)
    variants = {q for q, rows in groups.items() if len({key(r['correct_answer']) for r in rows}) > 1}
    decision_path = ROOT / 'data' / 'answer_review_decisions.json'
    decisions = {d['question_key']: d for d in json.loads(decision_path.read_text(encoding='utf-8'))} if decision_path.exists() else {}
    for q, decision in decisions.items():
        assert q in variants
        assert any(r['id'] == decision['keep_id'] for r in groups[q])
        assert all(r['original_split'] == 'train' for r in groups[q]), 'Reviewed restoration supports training-only groups'
    pending = variants - decisions.keys()
    review = [dict(question_key=q, records=groups[q], reason='Different answer text; may be equivalent or context-dependent. Human review pending.') for q in sorted(pending)]
    heldout = {key(r['question']) for s in ['validation', 'test'] for r in splits[s]}
    clean = {}
    audit = []
    for split, rows in splits.items():
        clean[split] = []
        seen = set()
        # Prefer a passage-bearing copy when otherwise deduplicating a question.
        ordered = sorted(rows, key=lambda r: (not r['has_support'], r['original_index']))
        for row in ordered:
            q = key(row['question'])
            reason = None
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
            seen.add(q)
            row['needs_answer_review'] = q in pending
            clean[split].append(row)
        clean[split].sort(key=lambda r: r['original_index'])
        save(OUT / f'sciq_{split}.json', clean[split])
    kept_ids = {r['id'] for rows in clean.values() for r in rows}
    assert all(d['keep_id'] in kept_ids for d in decisions.values())
    passages = defaultdict(list)
    for rows in clean.values():
        for row in rows:
            if row['support']:
                passages[row['support']].append(row['id'])
    corpus = [dict(passage_id='passage_' + hashlib.sha256(text.encode()).hexdigest(), text=text, source_ids=ids) for text, ids in passages.items()]
    save(OUT / 'passages.json', corpus)
    save(OUT / 'answer_review_queue.json', review)
    save(OUT / 'cleaning_audit.json', audit)
    save(OUT / 'raw_sha256.json', hashes)
    sets = {s: {key(r['question']) for r in rows} for s, rows in clean.items()}
    assert all(len(sets[s]) == len(clean[s]) for s in clean)
    assert not (sets['train'] & sets['validation'] or sets['train'] & sets['test'] or sets['validation'] & sets['test'])
    assert sum(map(len, splits.values())) == sum(map(len, clean.values())) + len(audit)
    assert all(hashlib.sha256((RAW / f'sciq_{s}.json').read_bytes()).hexdigest() == hashes[s] for s in splits)
    expected = read(ROOT / "data/source_version.json")["raw_sha256"]
    assert hashes == expected, "Source data differs from the pinned snapshot"
    print({split: len(rows) for split, rows in clean.items()})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-download", action="store_true", help="Use existing raw JSON files")
    args = parser.parse_args()
    if not args.skip_download:
        download()
    clean_data()
