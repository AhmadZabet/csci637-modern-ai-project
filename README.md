# Science Study Assistant

Ahmad Zabet | CSCI637 | Dr. Maysaa Khalil | Fall 2026

## Current correction status

This repository prepares SciQ for an evidence-grounded science study assistant and four-class subject classification. Corrections to the 10 November Phase 1 feedback are dated 17 November. Phase 2 data checks and classical-baseline validation are complete; both baselines have fixed-test results and the cumulative PDF includes Phase 2. Phase 2 commits, upload and release tagging remain pending. Personal review of the 100 main questions and 16 adaptations is complete. Classification-label review is complete for the starter subsets. Deadline confirmation remains open. All 24 challenge cases have student approval.

## Deliverables

| File | Purpose |
|---|---|
| [Project report](reports/project-report.pdf) | Cumulative report: Phase 1 (pages 1-3) and Phase 2 (pages 4-6) |
| [Methodology](reports/methodology.md) | Task, PEAS, subject rubric, fixed targets and correction ledger |
| [Dataset datasheet](reports/dataset-datasheet.md) | Sources, license, preparation and biases |
| [Evaluation](reports/evaluation.md) | Main evaluation, adaptations, challenge tracks and personal-review instructions |
| [Data preparation](reports/data-preparation.md) | Cleaning, reproduction and current verification |
| [AI disclosure](AI_USE.md) | Detailed assistance and review provenance |

## Run from the project root

```powershell
python -m venv .venv
$env:PYYAML_FORCE_LIBYAML = '0'
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe src\prepare_data.py
.\.venv\Scripts\python.exe src\prepare_evaluation.py
```

Use `src\prepare_data.py --skip-download` when pinned raw files already exist. The preparation step also generates labeled classification subsets from data/annotations/classification_labels.json. Data files in data/processed are regenerated rather than committed. Both scripts use common.py. The source revision and hashes are in data/source_version.json.

## Current data

Cleaned splits contain 11,577 training, 1,000 validation and 1,000 test records, with 12,148 unique supporting passages. The main evaluation has 100 test questions, with 44 Biology, 19 Chemistry, 19 Physics and 18 Earth and Space Science labels. The separate challenge set has 10 paraphrases, 8 no-evidence cases and 6 out-of-scope cases. These challenge prompts and expected behaviors were AI-drafted and approved by Ahmad in chat on 17 November 2026.

Only a documented subset of training and validation has subject labels. Use data/processed/classification_train.json and classification_validation.json for starter classification experiments with question text as input and subject as target. Their class counts are in data/annotations/classification_summary.json. The complete SciQ splits are not fully annotated. The subset label review is complete; broader sample coverage remains necessary. General Science is outside the current four-class classifier scope, but may be handled through retrieval later.

## Student evaluation review completed

On 17 November 2026, Ahmad Zabet reviewed the 100 evaluation questions in chat batches, with their choices, proposed labels, answers and relevant supporting evidence. Original and revised content was shown for all 16 adapted items. He approved all 100 labels, answers and evidence, including all 16 adaptations. He explicitly retained Chemistry for item 14 and the existing wording of item 17. The item-level decisions are recorded in data/annotations/ahmad_evaluation_review.json. This records the student review of the displayed material; broader scientific validation of every full source passage was not performed.

All 186 training and 39 validation subset labels now have recorded student approval. All 24 challenge cases have recorded student approval.

## Submission evidence

The existing annotated phase-1 tag points to commit 6b6a681272bd921292963c42b187d929dff24471 and is present on origin. Its recorded timestamp is 4 November 2026 at 04:31:05 Beirut time. Corrections preserve that tag. The exact course deadline and the instructor's late-status decision must be confirmed. Local correction files must still be committed and submitted for re-review. No grade increase is asserted.

## Source and limits

SciQ by Johannes Welbl, Nelson F. Liu and Matt Gardner, Crowdsourcing Multiple Choice Science Questions (2017), distributed by AI2. [Dataset](https://huggingface.co/datasets/allenai/sciq). [CC BY-NC 3.0](https://creativecommons.org/licenses/by-nc/3.0/). The source and derived noncommercial data retain attribution. Evaluation curation, AI annotation, English-only coverage and recall-heavy questions limit the results. The passage collection includes evaluation evidence for open-book retrieval. Classical validation results are documented in reports/methodology.md; final test results are in reports/evaluation.md.

Ahmad completed primary-subject review of all 186 training and 39 validation subset labels in chat batches by 24 November 2026. The original AI authorship, individual review dates and interdisciplinary decisions are retained in data/annotations/classification_labels.json. Approval covers the displayed question and answer context for subject labeling, not independent validation of every source answer or full passage. The full cleaned SciQ splits remain only partly labeled; broader annotation and class coverage are needed for reliable model comparisons.

## Phase 2 progress

The reviewed 186/39/100 classification splits passed structural and normalized-overlap checks. The experiment setup is recorded in data/annotations/phase2_experiment.json and reports/methodology.md. The TF-IDF logistic regression baseline has been trained and selected using validation results. The MLP baseline is also trained with the same TF-IDF settings. Both selected models have now been evaluated on the reserved test set, without further tuning. The final scores are recorded below.

### Classical baseline commands

```powershell
.\.venv\Scripts\python.exe src\train_classical.py
.\.venv\Scripts\python.exe src\train_classical.py --predict "Which organ pumps blood?"
```

Training verifies the fixed training/validation data fingerprints, evaluates the predeclared six candidates and saves the selected pipeline to models/classical.joblib. It does not read or score test records. Validation metrics, per-class results, confusion matrix and predictions are saved in reports/phase2_classical_validation.json. Install the updated requirements-lock.txt before running on another machine. The saved model is regenerated locally rather than committed.

### Neural baseline commands

```powershell
.\.venv\Scripts\python.exe src\train_neural.py
.\.venv\Scripts\python.exe src\train_neural.py --predict "Which organ pumps blood?"
```

Run the classical baseline first because the neural script verifies and includes its validation comparison. The neural script reuses its data and metric helpers. Neural results are saved in reports/phase2_neural_validation.json, and the pipeline in models/neural.joblib. Both models now have fixed-test results; the cumulative PDF now includes the three-page Phase 2 section. The validation JSON files preserve the earlier model-selection stage.

### Fixed-test evaluation

```powershell
.\.venv\Scripts\python.exe src\evaluate_baselines.py
```

Run both training commands first when reproducing from scratch. Evaluation verifies the selected artifacts and data, then scores without fitting. A repeat evaluation verifies unchanged selected settings, data and results and preserves the original comparison and artifact hashes. Retrained model serialization may have different hashes even when predictions match. Final predictions, confusion matrices, data fingerprints and model hashes are in reports/phase2_test_comparison.json. Keep the selected settings and fixed test set for Phase 3; do not retune these baselines from test scores.

| Model | Test accuracy | Test macro-F1 |
|---|---:|---:|
| Logistic regression | 53.00% | 0.4104 |
| MLP | 53.00% | 0.3561 |
| Training-majority reference | 44.00% | 0.1528 |

Neither model reaches the 85% accuracy / 0.80 macro-F1 subject-classification targets. The small, imbalanced training sample and curated test set limit interpretation. These are classification scores, not science-answer accuracy.

## Phase 2 completion and submission

Local technical deliverables are prepared: both baselines, fixed splits and searches, validation and final test metrics, per-class results and confusion matrices, exact dependencies, reproduction instructions, AI disclosure and the cumulative PDF. Phase 2 occupies pages 4-6 (three pages), within the required 2-4 page phase-report length. The existing four Markdown reports were retained.

A separate-folder run in the current locked environment reproduced both candidate searches, selected parameters and all validation/test predictions and metrics. This was not a fresh environment installation or cross-platform check. Re-evaluation with regenerated artifacts also passed while preserving the original comparison.

The local Git check on 24 November found no Phase 2 commits or phase-2 tag. Commit/upload and tag creation remain pending. The course requires regular commits throughout the phase; that item is not marked complete. Confirm the actual deadline before claiming an on-time release. Keep the existing phase-1 tag unchanged.
