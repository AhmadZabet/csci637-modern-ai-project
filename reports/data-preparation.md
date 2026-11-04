# Data preparation and reproduction

> Current commands after simplification: `python src/prepare_data.py` and `python src/prepare_evaluation.py` using the project environment. Eight current artifacts match the prior pipeline by JSON content. Script names and byte comparisons in the historical sections below describe the earlier pipeline. Review decisions are preserved as annotation inputs; historical exploratory outputs are retained rather than regenerated.


Current scope: Phase 1. Initial inspection and cleaning stages are followed by the successful fresh-environment reproduction check. This document records stage-specific findings; current evaluation details are in evaluation.md.

## Initial inspection

### Phase 1: Initial SciQ inspection

Source: https://huggingface.co/datasets/allenai/sciq

Original splits are preserved. No records have been cleaned or removed.

| Split | Rows | Missing support | Missing question/answer fields | Repeated questions within split |
|---|---:|---:|---:|---:|
| train | 11679 | 1198 | 0 | 70 |
| validation | 1000 | 113 | 0 | 0 |
| test | 1000 | 116 | 0 | 0 |

### Questions shared across splits

Matching uses case folding and collapsed whitespace; this is not a semantic duplicate check.

- train / validation: 12
- train / test: 7
- validation / test: 0

### First training example

```json
{
  "question": "What type of organism is commonly used in preparation of foods such as cheese and yogurt?",
  "distractor3": "viruses",
  "distractor1": "protozoa",
  "distractor2": "gymnosperms",
  "correct_answer": "mesophilic organisms",
  "support": "Mesophiles grow best in moderate temperature, typically between 25°C and 40°C (77°F and 104°F). Mesophiles are often found living in or on the bodies of humans or other animals. The optimal growth temperature of many pathogenic mesophiles is 37°C (98°F), the normal human body temperature. Mesophilic organisms have important uses in food preparation, including cheese, yogurt, beer and wine."
}
```




## Cleaning and record accounting

### Phase 1: Data cleaning

Source: https://huggingface.co/datasets/allenai/sciq

### Rules

- Preserve raw files; normalize whitespace only in output text. Preserve capitalization and punctuation.
- Match questions using collapsed whitespace and case folding. Paraphrases are not detected.
- Remove training copies of held-out questions, regardless of their answer wording.
- Quarantine remaining training groups with differing answer text pending human review; differences are not necessarily errors.
- Keep one copy of other repeated questions, preferring a supporting passage, then the lowest original row index.
- Keep missing-support questions for classification; mark has_support=false. Do not invent evidence.
- Preserve validation/test records with answer variants but flag needs_answer_review; review before selecting evaluation examples.
- Stable IDs record the original split and zero-based row index.

| Split | Original | Cleaned | Removed/quarantined | Missing support retained | Whitespace changed in original rows |
|---|---:|---:|---:|---:|---:|
| train | 11679 | 11577 | 102 | 1190 | 78 |
| validation | 1000 | 1000 | 0 | 113 | 4 |
| test | 1000 | 1000 | 0 | 116 | 7 |

### Approved duplicate decisions

3 groups resolved using data/answer_review_decisions.json. Keep the explicitly approved record and exclude its duplicates. These approvals do not count toward the evaluation set.

### Exclusion counts

- answer_variant_pending_review: 26
- question_in_heldout_split: 19
- repeated_question: 54
- reviewed_duplicate: 3

Answer-variant groups awaiting review: 20.
Unique nonempty passages: 12148.

The passage corpus includes evidence from all cleaned splits. This supports an open-book retrieval evaluation; question/answer labels from validation and test must not be used for training. Shared passages may remain across splits, so these splits do not establish generalization to unseen documents.

### Verification

Passed: unique normalized questions within each split, no normalized question overlap between splits, all source records accounted for, and unchanged raw file hashes.

Automated checks are not a scientific correctness review. This cleaning stage does not assign subject labels or review evaluation questions; see evaluation.md for the separate evaluation-stage results.

### Reproduce

Run from the project root after the inspection/download script:

```powershell
.\.venv\Scripts\python.exe src\phase1_clean_data.py
```


## Reproduction verification

### Phase 1 reproducibility verification

Date: 4 November 2026

### Result

PASS: eight scripts completed successfully in an isolated virtual environment. All 22 generated JSON artifacts matched the existing project files byte for byte. pip check reported no broken requirements.

### Environment and procedure

- Python: Python 3.15.2
- Platform: Windows-11-10.0.26100-SP0
- SciQ revision: 2c94ad3e1aafab77146f384e23536f97a4849815
- Dependencies: requirements-lock.txt, captured from the original environment.
- Fresh virtual environment and fresh Hugging Face dataset cache. Pip reused previously downloaded package archives.
- Inputs copied: preparation scripts, requirements, and approved duplicate decisions. Original raw, cleaned and evaluation outputs were not copied into the verification workspace.
- Regenerated candidate selection, review, historical audit, adaptations, taxonomy sample and training-label pilot.

### Scripts

1. phase1_inspect_data.py
2. phase1_clean_data.py
3. phase1_prepare_evaluation.py
4. phase1_review_evaluation.py
5. phase1_audit_evaluation.py
6. phase1_adapt_evaluation.py
7. phase1_check_taxonomy.py
8. phase1_label_subject_pilot.py

### Artifact comparisons

| File | Result |
|---|---|
| data/annotations/subject_pilot.json | Exact byte match |
| data/annotations/subject_pilot_summary.json | Exact byte match |
| data/evaluation/evaluation_adaptations_v2.json | Exact byte match |
| data/evaluation/evaluation_replacements.json | Exact byte match |
| data/evaluation/phase1_candidates.json | Exact byte match |
| data/evaluation/phase1_evaluation.json | Exact byte match |
| data/evaluation/phase1_evaluation_v2.json | Exact byte match |
| data/evaluation/quality_audit.json | Exact byte match |
| data/evaluation/review_summary.json | Exact byte match |
| data/evaluation/review_summary_v2.json | Exact byte match |
| data/evaluation/selection_manifest.json | Exact byte match |
| data/processed/answer_review_queue.json | Exact byte match |
| data/processed/cleaning_audit.json | Exact byte match |
| data/processed/passages.json | Exact byte match |
| data/processed/raw_sha256.json | Exact byte match |
| data/processed/sciq_test.json | Exact byte match |
| data/processed/sciq_train.json | Exact byte match |
| data/processed/sciq_validation.json | Exact byte match |
| data/raw/sciq_test.json | Exact byte match |
| data/raw/sciq_train.json | Exact byte match |
| data/raw/sciq_validation.json | Exact byte match |
| data/taxonomy_coverage.json | Exact byte match |

### Limits

This is a data-pipeline reproduction check on one Windows/Python environment. It does not validate the scientific accuracy of labels, constitute human review, establish portability to other systems, or test any trained model. The PDF was generated and visually checked separately. Historical version-1 audit files still describe the earlier findings; version 2 records the editorial corrections.

The isolated verification workspace is retained under tmp/reproduction_check and excluded from Git. Machine-readable hashes and environment details are in reports/reproduction-check.json. Local preparation is complete; GitHub submission requirements remain separate.
