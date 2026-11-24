# Data preparation and verification

Ahmad Zabet | CSCI637 | Updated 17 November 2026

## Current pipeline

Run using the project environment from the repository root.

```powershell
.\.venv\Scripts\python.exe src\prepare_data.py --skip-download
.\.venv\Scripts\python.exe src\prepare_evaluation.py
```

Omit --skip-download when raw files are missing. The source revision is pinned in data/source_version.json, and requirements-lock.txt records the tested package versions. common.py supplies shared path, JSON and text helpers.

prepare_data.py saves cleaned train, validation and test splits, distinct passages, removal reasons, unresolved answer groups and raw hashes. It also applies data/annotations/classification_labels.json to generate classification_train.json and classification_validation.json. These subsets have AI-drafted subject labels subsequently reviewed and approved by Ahmad. prepare_evaluation.py rebuilds the fixed 100-item evaluation from source records and recorded annotations. It does not create personal verification.

## Cleaning outcome

All original records are accounted for. The cleaned split sizes are 11,577, 1,000 and 1,000. There are 12,148 unique passages. Training excludes 19 held-out overlaps, 54 ordinary duplicates, 3 reviewed duplicates and 26 records awaiting answer review. Missing support is retained and marked when other fields are usable. Normalized question matching ignores case and extra whitespace.

## Verification on 17 November

Both current scripts ran successfully in a separate directory using copies of pinned raw data and annotation inputs. Ten regenerated JSON outputs matched current project values. Classification question keys were checked against each other and against the test evaluation. All 100 main items have unique IDs and valid answer choices and passage references. The 24 challenge cases have the expected 10/8/6 track distribution, and paraphrase source IDs, answers and evidence match their parent evaluation items. All 100 personal-review entries now contain student confirmations, including all 16 adaptations.

Full results are in feedback-verification.json. This technical verification does not certify scientific label quality. An earlier fresh-environment run reproduced the previous eight-script pipeline and 22 historical artifacts byte for byte. After simplification, the current pipeline uses three Python files. Historical verification files refer to their dated versions.

## Submission evidence

The remote phase-1 tag was verified on 17 November. The tag object is 440a223225d536c2a15fe68b4b2904192a2e5f64 and the referenced commit is 6b6a681272bd921292963c42b187d929dff24471. The local annotated tag records 4 November 2026 at 04:31:05 Beirut time. No tag was moved or recreated. The exact deadline and instructor's late-status decision remain to be confirmed. The correction work is local and requires submission after review.

## Remaining prerequisites

Ahmad completed verification of the 100 main labels and 16 adapted questions. Review of all 186 training and 39 validation subset labels is complete; deadline confirmation remains required. All 24 challenge cases were approved by Ahmad on 17 November 2026. The 186/39 labeled subsets are starter data. The full cleaned training and validation splits are not fully annotated, and the small class counts require broader annotation for reliable baseline experiments.

Ahmad completed primary-subject review of all 186 training and 39 validation subset labels in chat batches by 24 November 2026. The original AI authorship, individual review dates and interdisciplinary decisions are retained in data/annotations/classification_labels.json. Approval covers the displayed question and answer context for subject labeling, not independent validation of every source answer or full passage. The full cleaned SciQ splits remain only partly labeled; broader annotation and class coverage are needed for reliable model comparisons.


## Phase 2 reproduction verification (24 November 2026)

A separate folder received copies of the three baseline scripts, common.py, fixed experiment setup, reviewed classification train/validation records and fixed evaluation records. Using the existing project environment, it ran train_classical.py, train_neural.py and evaluate_baselines.py. Both six-candidate searches, chosen parameters, validation metrics/predictions, test metrics/predictions, error IDs and data fingerprints matched the project results exactly. This verifies a separate working directory using the same installed environment, not a fresh dependency installation.

Serialized model hashes differed on retraining although predictions and metrics matched. The evaluation repeat check was corrected to verify fixed data, selected settings and identical results while preserving the original comparison and its original artifact hashes. A reproduction run using the original saved comparison and regenerated models passed. Changed results or data are rejected rather than replacing the historical baseline. The report records observed software versions; cross-platform numerical identity is not guaranteed.

The cumulative PDF was rendered and visually checked on all six pages; Phase 1 and Phase 2 each occupy three pages. There are still four Markdown files in reports/. Local Git history had no Phase 2 commits or phase-2 tag at the submission check. The technical checklist and outstanding submission items are in reports/methodology.md.
