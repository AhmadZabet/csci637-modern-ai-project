# Dataset datasheet: SciQ Science Study Assistant

Prepared for CSCI637 Phase 1 by Ahmad Zabet with OpenAI Codex assistance. Updated: 4 November 2026.

## Purpose and intended use

This project uses SciQ to develop an English-language science study assistant for high-school students, introductory undergraduate students, and independent learners. The data supports multiple-choice question answering, subject classification, and retrieval of supporting passages. Phase 1 prepares data and evaluation materials; no model performance has been measured. The assistant is intended for educational study, not professional medical advice or a substitute for authoritative scientific references.

## Source, creators, and license

Source: [allenai/sciq dataset card](https://huggingface.co/datasets/allenai/sciq), distributed by the Allen Institute for AI. Original work: Johannes Welbl, Nelson F. Liu, and Matt Gardner, *Crowdsourcing Multiple Choice Science Questions* (2017). The dataset card describes crowdsourced science examination questions. Downloaded for this project on 2 November 2026.

The dataset card identifies the license as [Creative Commons Attribution-NonCommercial 3.0 Unported](https://creativecommons.org/licenses/by-nc/3.0/). This allows sharing and adaptation subject to its terms, including attribution and noncommercial use. Retain the title, authors, source and license links when sharing these derived materials, and identify the project modifications. This academic project does not claim endorsement by the original creators. The dataset license does not automatically license the project's software.

Project modifications include whitespace normalization, filtering duplicates, adding stable identifiers, collecting distinct passages, selecting evaluation questions, shuffling answer choices, and adding subject labels and review metadata. Cleaned source wording is retained. Evaluation version 2 explicitly adapts 16 items, preserving original questions and choices; three items select exact source excerpts without rewriting the full source passage. Individual passages may retain source attributions or references; these have not been independently audited for rights or completeness.

## Composition and schema

The original dataset contains 13,679 English questions. Each record has question, correct_answer, distractor1, distractor2, distractor3, and support fields. The support field can be empty. Original SciQ records do not include the four subject labels used in this project.

| Split | Original questions | Cleaned questions | Original missing support | Cleaned missing support |
|---|---:|---:|---:|---:|
| Training | 11,679 | 11,577 | 1,198 | 1,190 |
| Validation | 1,000 | 1,000 | 113 | 113 |
| Test | 1,000 | 1,000 | 116 | 116 |
| Total | 13,679 | 13,577 | 1,427 | 1,419 |

The cleaned data contains 12,158 nonempty supporting-passage instances, yielding 12,148 distinct passages after exact text deduplication. Passage IDs are SHA-256 hashes of normalized passage text and map back to source record IDs. Record IDs encode the original split and zero-based row index. Missing passages remain explicitly marked; evidence is not fabricated.

No missing question or answer fields were found by the initial checks. This does not establish that all questions are scientifically correct or have good distractors.

## Preparation and quality control

Raw JSON files remain unchanged. Cleaning collapses repeated whitespace and preserves capitalization and punctuation. Duplicate-question matching ignores capitalization and whitespace; it does not identify all paraphrases or semantic duplicates.

Training exclusions total 102 records: 19 questions also present in validation or test, 54 unreviewed same-answer duplicate copies, 3 duplicates excluded by approved decisions, and 26 records with unresolved answer variants. Twenty answer-variant groups remain unresolved across the original splits; some include held-out records that are retained and flagged. Three groups were resolved with Ahmad's explicit approval; one original training record from each was restored. For ordinary duplicates, a passage-bearing record is preferred, followed by the earliest source index; explicit approved decisions take precedence.

Checks passed for unique normalized question text within cleaned splits, no normalized question-text overlap across splits, accounting for every original record, and preservation of raw-file hashes. Scientific correctness, semantic similarity, and passage quality are not established by these automated checks.

## Evaluation set and annotation

The evaluation set has 100 unique records from the cleaned test split, with answers, shuffled choices, supporting passages, passage IDs, subject labels, reviewer provenance, and limitations. It is stored separately from training data and must not be used to fit models or tune their settings.

The initial pool was sampled with seed 637 from 878 eligible test records with nonempty support, distinct answer strings, and no unresolved answer variants. After reading the questions, alternatives and passages, Codex replaced 28 problematic candidates. Replacements were chosen from unused supported test records with passages shorter than 650 characters, inspected in seed-638 shuffled order. The replacement log identifies every changed selection and reason. Consequently, the final set is editorially curated, not a uniform random test sample.

| Subject | Evaluation examples |
|---|---:|
| Biology | 44 |
| Chemistry | 19 |
| Physics | 19 |
| Earth and Space Science | 18 |

Subject labels reflect the primary knowledge needed to answer. Biology includes living systems and ecology; Chemistry includes composition, reactions and electron configuration; Physics includes forces, waves, electricity and nuclear processes; Earth and Space Science includes geology, Earth systems, fossils and astronomy. Cross-disciplinary assignments are documented in review notes. The evaluation has four subject labels. A separate 95-record training pilot has 94 AI-provisional labels and one unresolved case; full training and validation annotation remains future work. General Science is proposed, not adopted as a fifth evaluated class.

The first reviewed version had two student-confirmed items and 98 AI-reviewed items. A second audit identified 16 issues; version 2 records 16 editorial adaptations, including the originally confirmed first question. Current provenance is therefore one unchanged human-confirmed item, 83 AI-reviewed original items, and 16 AI-reviewed adaptations. This is not independent expert validation. Original support remains intact; evidence_excerpt identifies the selected source span, and full source passages may retain errors. Difficulty remains unassigned. See data/evaluation/evaluation_adaptations_v2.json for exact changes and reports/evaluation.md for the current set.

## Known biases and limitations

- Language: English only; results do not demonstrate performance in Arabic or other languages.
- Subject balance: Biology accounts for 44% of the curated evaluation set. This is not a measurement of the full corpus distribution. Report per-subject metrics and macro-F1 in addition to overall accuracy.
- Selection bias: excluding missing or unrelated evidence, ambiguous alternatives and unresolved answer variants favors cleaner, answerable questions. Short replacement passages and mostly recall questions may make evaluation easier than real student queries.
- Coverage: the set does not yet test missing-evidence refusal, extensive multistep reasoning, paraphrases or adversarial inputs. Later robustness testing should be separate and clearly identified.
- Annotation: AI-generated subject judgments may be inconsistent, especially for biochemistry and astronomy/physics boundaries. No independent annotator agreement was measured.
- Source quality: passages can contain typos, oversimplifications, outdated claims, irrelevant text, figure references without figures, or questions with overlapping choices. Some retained examples carry explicit caveats.
- Leakage: exact normalized question overlap was removed, but paraphrases and shared passages can remain. The retrieval corpus intentionally includes passages from all cleaned splits, including evaluation evidence, for an open-book retrieval setting. Do not include held-out answer labels as model-training examples. Results will not demonstrate generalization to entirely unseen documents.
- Prior exposure: SciQ is public, so pretrained models may already have encountered its questions. This project has not measured pretraining contamination.
- Representation: demographic attributes and author backgrounds have not been audited. No claim of demographic balance or fairness is supported by the current data.
- Privacy and content: no private student records were added. A systematic personal-information audit of the source text has not been performed. Educational passages include health, anatomy and reproduction topics.

## Files, reproduction, and maintenance

Run `src/prepare_data.py` followed by `src/prepare_evaluation.py` using the project environment. The first downloads the pinned source and generates cleaned splits, passage corpus and audit outputs. Use `--skip-download` when raw files already exist. The second reconstructs the final evaluation using the preserved `data/annotations/evaluation_decisions.json`. Shared helpers are in `src/common.py`.

The annotation decisions are inputs, not learned labels. Historical candidate sampling, exploratory pilot and earlier audit files are retained for traceability; the simplified pipeline reproduces current deliverables rather than rebuilding all historical stages. Reports and the PDF are maintained separately. An isolated comparison confirmed identical JSON content for all eight current output artifacts after simplification.

Direct dependencies are listed in requirements.txt; all tested package versions are pinned in requirements-lock.txt. On the project Windows installation, PyYAML required its optional C extension to be disabled during installation (PYYAML_FORCE_LIBYAML=0). The download is pinned to revision 2c94ad3e1aafab77146f384e23536f97a4849815. A fresh Windows/Python 3.15.2 environment with a new dataset cache reproduced all 22 JSON artifacts byte for byte on 4 November 2026. Pip reused its package-download cache; other platforms have not been tested. Raw-file hashes are recorded in data/processed/raw_sha256.json for the downloaded snapshot.

Raw and processed full-data directories are excluded from Git; scripts and source links support regeneration. Evaluation JSON files, approved decisions and reports are intended to accompany the submission with attribution. GitHub publication and release status must be checked separately; this datasheet does not assert a completed release.

Project maintainer: Ahmad Zabet. Record future corrections by source ID, reason, reviewer and date. Keep evaluation membership stable before model development, and document any later changes. AI assistance was used to clarify concepts and help write code. The detailed assistance record is provided in AI_USE.md. The unresolved cases remain excluded or flagged rather than silently resolved.
