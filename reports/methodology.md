# Phase 1 methodology and corrections

Student Ahmad Zabet. Correction date 17 November 2026. The original grade was 7.0 out of 10. This ledger responds to the instructor's own Ahmad Zabet section on pages 6 and 7.

| Feedback | Correction and evidence | Remaining student action |
|---|---|---|
| Training and validation need subject labels | Recorded AI-draft labels and reproducible classification subsets added | All 225 subset labels reviewed; expand coverage before relying on model comparisons |
| Missing and understated AI disclosure | AI_USE.md added with specific labeling, review and rewriting disclosure | Read and verify the disclosure |
| Personally verify 100 labels and 16 adaptations | All 100 questions and 16 adaptations approved in chat and recorded | Complete for displayed questions and evidence |
| PDF missing or broken link | PDF report supplied and linked in README | Review the corrected report |
| Missing edge cases | 24 separately scored challenge cases added with expected behavior | Review expected behavior and phrasing |
| Missing phase-1 tag and late status | Existing local and remote tag verified at 6b6a681, dated 4 November 04:31:05 Beirut | Ask instructor to confirm deadline and late status |

The tag evidence supports a clarification request about submission mechanics. The disclosure, PDF and challenge-set corrections support a request to re-evaluate corrected deliverables. Personal verification of the main set is now recorded. Classification-subset label review is complete for all 225 labels. The 24 challenge cases have recorded student approval. No score recovery is guaranteed.

## Acceptance targets

The project adopts these measurable acceptance criteria before Phase 2 training. They are engineering goals to assess later, with no current performance claims.

| Measure | Target | Scoring |
|---|---|---|
| Subject accuracy | At least 85% | Correct primary-subject predictions divided by all scored questions |
| Subject macro-F1 | At least 0.80 | Unweighted average F1 over four subjects |
| QA accuracy | At least 80% | Correct selected answers divided by all 100 main evaluation items |
| Retrieval recall at 5 | At least 90% | Designated source passage in the five distinct retrieved source IDs |
| Answer faithfulness | At least 90% | Substantive answers with all factual claims supported by cited passages |
| Citation traceability | 100% | Cited IDs resolve to the stated source text |
| Missing-evidence handling | At least 90% | Correct abstention or request for details in the controlled no-evidence track |
| Out-of-scope handling | At least 90% | Scope redirection on the out-of-scope track |

Report coverage and abstentions separately. Pure refusals do not increase the faithfulness score. Small challenge tracks give coarse percentages, so always report raw counts. Paraphrases are grouped with their parent questions and are scored separately rather than as independent test samples. No-evidence tests supply an empty context with retrieval disabled, which distinguishes missing context from a retrieval failure.


## Classification rubric and scope

Assign the subject by the knowledge needed to answer. Biology covers living systems, anatomy, ecology and evolution. Chemistry covers substances, bonding, electron configuration and chemical reactions. Physics covers forces, energy, waves, electricity and nuclear processes. Earth and Space Science covers geology, weather and astronomy. Biochemistry boundaries are noted where needed. General Science remains outside the current classifier, with ambiguous examples excluded rather than forced into a class.

The classifier's input must be question text only. Answer keys, review notes and evidence fields must not be model features. Fit only on classification_train.json, select settings on classification_validation.json, and reserve the 100 main questions for final comparison. The labeled starter sample has 186 training and 39 validation records, with AI-drafted labels subsequently approved by Ahmad. Broader annotation remains necessary for reliable model comparisons. No trained-model result is claimed.

## Planned agent and environment

The target users are high-school students, introductory undergraduates and independent learners. The main task is selecting an answer and providing a cited science explanation. Classification is a complementary subject-identification task. PEAS performance covers correct answers, subject labels, evidence retrieval and uncertainty behavior. The environment is a student interacting with the SciQ reference collection. Actuators display answers, explanations, citations and clarification requests. Sensors receive question text, answer choices and retrieved passages. The task is partially observable and sequential, because user intent and future follow-up questions are uncertain.

## Evaluation design

The main 100-item set is curated from the cleaned test split, with source and passage IDs retained. Selection seed 637 produced the initial pool, with 28 replacements and 16 recorded adaptations. It is recall-heavy, supported and Biology-heavy. The added 24 cases are a separately scored challenge set, authored by Codex and approved by Ahmad on 17 November 2026. Paraphrases share evaluation parents. Empty-context no-evidence tests cannot establish retrieval recall. Report each track independently and disclose all review provenance.

## Discussion of the deducted marks

The instructor awarded 2.0/2.0 for cleaning and 1.5/1.5 for the datasheet. Corrections focus on the remaining categories. The targets are now adopted as explicit acceptance criteria with uncertainty-handling measures added. The main set now has recorded personal verification. Evaluation gains also depend on the quality of the separate challenge items, now approved by Ahmad. Report/documentation gains are supported by an actual PDF, a concise current README and a detailed AI disclosure. The existing phase-1 tag can be shown as evidence for reconsideration of the tag comment. A revised grade remains the instructor's decision and late status requires the actual deadline.

## Completed main-set personal review

On 17 November 2026, Ahmad Zabet reviewed the 100 evaluation questions in chat batches, with their choices, proposed labels, answers and relevant supporting evidence. Original and revised content was shown for all 16 adapted items. He approved all 100 labels, answers and evidence, including all 16 adaptations. He explicitly retained Chemistry for item 14 and the existing wording of item 17. The item-level decisions are recorded in data/annotations/ahmad_evaluation_review.json. This records the student review of the displayed material; broader scientific validation of every full source passage was not performed.

Ahmad completed primary-subject review of all 186 training and 39 validation subset labels in chat batches by 24 November 2026. The original AI authorship, individual review dates and interdisciplinary decisions are retained in data/annotations/classification_labels.json. Approval covers the displayed question and answer context for subject labeling, not independent validation of every source answer or full passage. The full cleaned SciQ splits remain only partly labeled; broader annotation and class coverage are needed for reliable model comparisons.

## Phase 2 experiment setup (24 November 2026)

The first Phase 2 step checks the reviewed classification data and fixes the comparison protocol. No baseline has been trained or scored yet. The machine-readable setup, source IDs and SHA-256 fingerprints of model-relevant fields are in data/annotations/phase2_experiment.json. Future training should verify these fingerprints before fitting; any dataset revision must be documented before final test scoring.

| Subject | Training | Validation | Test |
|---|---:|---:|---:|
| Biology | 110 | 23 | 44 |
| Chemistry | 27 | 4 | 19 |
| Physics | 26 | 7 | 19 |
| Earth and Space Science | 23 | 5 | 18 |
| Total | 186 | 39 | 100 |

All sets have unique IDs and normalized question keys, no empty questions and no cross-split normalized question overlap. This is an exact-text check, not a semantic leakage guarantee. Training and validation subject labels have recorded student approval. The existing curated 100-question evaluation supplies test subject labels; its answer-generation fields will not be used as classifier inputs.

Use question text as input and subject as target. Compare TF-IDF plus logistic regression against TF-IDF plus an MLP neural baseline, with the same representation settings. Fit the vocabulary and IDF on training questions only. Use seed 637 and retain the existing source splits. Record the candidate hyperparameter grid before training, select on validation macro-F1, break ties by accuracy and then simplicity, and evaluate selected models on the test set after tuning. Preserve the same test set for Phase 3. Do not use test scores for further tuning.

Report accuracy, macro-F1, per-class precision/recall/F1/support and a confusion matrix, alongside a training-majority dummy reference. The 186/39 training/validation subsets are small and imbalanced: only four validation examples are Chemistry. Initial experiments are feasible, but broader reviewed annotation is advisable before strong model-comparison claims. No model result or target achievement is asserted.

## Phase 2 classical baseline: validation results

On 24 November 2026, src/train_classical.py trained six TF-IDF plus logistic regression candidates, using only the fixed 186 training questions. The six settings were recorded before training: C in {0.1, 1, 10} and class_weight in {None, balanced}. TF-IDF uses word unigrams and bigrams, at most 5,000 features, min_df=1 and sublinear term frequency. Vocabulary and IDF are fitted within the training pipeline only. Selection uses validation macro-F1, then accuracy, then the declared grid order. Convergence warnings fail the run rather than silently accepting an unfinished fit.

Selected parameters: `{"C": 0.1, "class_weight": "balanced"}`. Validation set: 39 questions.

| Model | Validation accuracy | Validation macro-F1 |
|---|---:|---:|
| Logistic regression | 66.67% | 0.5412 |
| Training-majority reference | 58.97% | 0.1855 |

| Subject | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Biology | 0.704 | 0.826 | 0.760 | 23 |
| Chemistry | 0.500 | 0.500 | 0.500 | 4 |
| Physics | 0.571 | 0.571 | 0.571 | 7 |
| Earth and Space Science | 1.000 | 0.200 | 0.333 | 5 |

Validation confusion matrix; rows are true labels, columns are predictions:

| True / predicted | Biology | Chemistry | Physics | Earth and Space Science |
|---|---:|---:|---:|---:|
| Biology | 19 | 1 | 3 | 0 |
| Chemistry | 2 | 2 | 0 | 0 |
| Physics | 2 | 1 | 4 | 0 |
| Earth and Space Science | 4 | 0 | 0 | 1 |

These are validation results used for selection, not final test results or evidence of a neural-model comparison. The test records were not loaded by the training script. With 39 validation cases, each question changes accuracy by about 2.56 percentage points. Minority-class estimates are especially uncertain. No additional tuning was performed after viewing these results. Candidate scores, individual validation predictions, environment versions and fingerprints are in reports/phase2_classical_validation.json. The pipeline is saved locally as models/classical.joblib, which is ignored by Git and can be regenerated using the locked environment. Reloading the saved model reproduced all validation predictions. The neural baseline, final test comparison and cumulative Phase 2 PDF section remain unfinished.

## Phase 2 neural baseline: validation comparison

On 24 November 2026, src/train_neural.py trained six predeclared MLP candidates using the same training-only TF-IDF settings, fixed split fingerprints and seed 637 as the classical baseline. The network has one ReLU hidden layer (16 or 32 neurons), a four-class softmax output and L-BFGS optimization. L2 alpha was searched in {1.0, 0.1, 0.01}. The search was recorded after observing classical validation scores but before any neural fitting. No test results were used. Early stopping is disabled, so no extra internal holdout reduces the 186 training examples. Convergence warnings fail the run.

Both searches contain six candidates selected by validation macro-F1, then accuracy, with the declared simplicity tie-break. The classical search includes class weighting, whereas the neural search has no sample weighting; the comparison therefore covers the selected complete pipelines rather than isolating architecture alone. It also uses only one random seed. Source: https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html.

Selected MLP: `{"hidden_units": 32, "alpha": 0.01}`.

| Model | Validation accuracy | Validation macro-F1 |
|---|---:|---:|
| Logistic regression | 66.67% | 0.5412 |
| MLP | 64.10% | 0.3987 |
| Training-majority reference | 58.97% | 0.1855 |

MLP per-subject validation results:

| Subject | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Biology | 0.656 | 0.913 | 0.764 | 23 |
| Chemistry | 0.333 | 0.250 | 0.286 | 4 |
| Physics | 0.750 | 0.429 | 0.545 | 7 |
| Earth and Space Science | 0.000 | 0.000 | 0.000 | 5 |

MLP validation confusion matrix; rows=true, columns=predicted:

| True / predicted | Biology | Chemistry | Physics | Earth and Space Science |
|---|---:|---:|---:|---:|
| Biology | 21 | 1 | 1 | 0 |
| Chemistry | 3 | 1 | 0 | 0 |
| Physics | 3 | 1 | 3 | 0 |
| Earth and Space Science | 5 | 0 | 0 | 0 |

The selected MLP's training accuracy is 100.00%, versus 64.10% on validation. This gap is consistent with overfitting on the small training sample, but does not establish its cause. Logistic regression is stronger on this validation set. These validation scores were used for selection and are not final performance estimates. No additional settings were tried after viewing these results. Both selected settings are now recorded in the experiment setup.

Candidate results, iteration counts, training loss, environment versions and validation predictions are in reports/phase2_neural_validation.json. The saved pipeline is models/neural.joblib (ignored by Git, reproducible from code). The neural script reuses load_split and metrics from train_classical.py without running classical training. The test set remains unscored. Next: verify and evaluate both selected pipelines on the reserved test set, then update the cumulative PDF with the complete Phase 2 comparison.


## Phase 2 final test outcome

| Model | Test accuracy | Test macro-F1 |
|---|---:|---:|
| Logistic regression | 53.00% | 0.4104 |
| MLP | 53.00% | 0.3561 |
| Training-majority reference | 44.00% | 0.1528 |

The 100 fixed test questions were evaluated after validation selection, without further fitting or tuning. Both subject-classification acceptance targets remain unmet. Full per-class scores, confusion matrices and error counts are in reports/evaluation.md; exact predictions and artifact hashes are in reports/phase2_test_comparison.json. The baselines and test set are retained for Phase 3. The cumulative PDF now includes the three-page Phase 2 section. Phase 2 commit/upload and release-tag actions remain pending.


## Phase 2 submission checklist (24 November 2026)

- [x] Classical model trained and evaluated.
- [x] Neural baseline trained and evaluated.
- [x] Training/validation/test protocol, source IDs, seed and fingerprints documented.
- [x] Metrics comparison, per-class scores and confusion matrices reported.
- [x] Trained-model regeneration code and exact dependencies available.
- [x] README reproduction instructions updated.
- [x] Three-page Phase 2 section included in the cumulative PDF (pages 4-6).
- [x] AI-tool disclosure updated.
- [x] Separate-folder retraining reproduced model selection and predictions.
- [ ] Phase 2 changes committed and uploaded.
- [ ] Release tagged phase-2; deadline compliance confirmed.
- [ ] Regular commits throughout Phase 2 evidenced in Git history (none found at the local check).

The modeling and local report work is prepared. Submission completion and deadline compliance are separate. Classification targets remain unmet, as reported; the models are retained without test-driven retuning for Phase 3 comparison.
