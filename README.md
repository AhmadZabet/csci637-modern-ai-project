# Science Study Assistant

**CSCI637 - Core Foundations of Modern AI | Fall 2026**  
**Student:** Ahmad Zabet | **Instructor:** Dr. Maysaa Khalil

## Phase 1 overview

This project prepares an English-language science study assistant using the instructor-approved SciQ dataset. The planned system will answer multiple-choice science questions with supporting evidence and classify questions into Biology, Chemistry, Physics, or Earth and Space Science.

Phase 1 delivers the problem definition, cleaned data, a 100-item labeled evaluation set, and data documentation. Model training and performance evaluation belong to later phases. Performance targets in the report are proposed goals, not measured results.

## Reading order

| Order | Deliverable | Contents |
|---|---|---|
| 1 | [Phase 1 report](reports/project-report.pdf) | Three-page account of the problem, methods, findings and limitations |
| 2 | [Dataset datasheet](reports/dataset-datasheet.md) | Sources, license, preparation, annotation and known biases |
| 3 | [Evaluation review](reports/evaluation.md) | Readable questions, labels, evidence and review notes |
| 4 | [Evaluation data](data/evaluation/phase1_evaluation_v2.json) | Machine-readable 100-item evaluation set |
| 5 | [AI-use disclosure](AI_USE.md) | Assistance provided and distinction between student and AI review |

The four supporting Markdown reports are [methodology](reports/methodology.md), [dataset datasheet](reports/dataset-datasheet.md), [evaluation](reports/evaluation.md), and [data preparation and reproduction](reports/data-preparation.md). Detailed decisions remain in the JSON audit files. The cumulative PDF currently contains Phase 1 only; later phases will be appended when completed.

## Data and current results

Source: [SciQ, Allen Institute for AI](https://huggingface.co/datasets/allenai/sciq). Credit: Johannes Welbl, Nelson F. Liu, and Matt Gardner, *Crowdsourcing Multiple Choice Science Questions* (2017). License: [CC BY-NC 3.0](https://creativecommons.org/licenses/by-nc/3.0/). Project modifications are documented in the datasheet; preserve attribution and license information when sharing derived data.

| Split | Original questions | Cleaned questions |
|---|---:|---:|
| Training | 11,679 | 11,577 |
| Validation | 1,000 | 1,000 |
| Test | 1,000 | 1,000 |

The corpus contains 12,148 distinct nonempty supporting passages. The evaluation subset contains 100 test questions: Biology 44, Chemistry 19, Physics 19, and Earth and Space Science 18. The evaluation set has four subject labels. A separate training pilot has 94 AI-provisional labels and one unresolved record; full training/validation annotation remains future work.

**Review provenance:** Version 2 has one unchanged human-confirmed item, 83 AI-reviewed original items and 16 AI-reviewed adaptations. The first item was confirmed before its wording was adapted; no approval of the revised wording is inferred. Original text and all changes are preserved. Twenty original duplicate-answer groups remain unresolved and are excluded or flagged as documented.


## Reproduce the data preparation

Run these commands in PowerShell from the repository root. Python must be installed. Activation is optional because the commands explicitly select the project environment.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
```

On the current Windows/Python installation, PyYAML needed its optional C extension disabled. If installation fails while building that extension, retry in the same terminal:

```powershell
$env:PYYAML_FORCE_LIBYAML = '0'
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
```

Run these two commands from the repository root:

```powershell
.\.venv\Scripts\python.exe src\prepare_data.py
.\.venv\Scripts\python.exe src\prepare_evaluation.py
```

If the pinned raw JSON files are already present, use `prepare_data.py --skip-download` to avoid downloading again. `common.py` contains shared helpers and is not run separately.

The evaluation script applies the recorded labels, chosen options and adaptations in `data/annotations/evaluation_decisions.json` to the cleaned test data. This annotation input is intentionally preserved: the script does not automatically judge scientific answers or regenerate human/AI decisions. Historical candidate, review, taxonomy-pilot and audit files remain provenance artifacts, not additional pipeline steps. The two commands reproduce the current cleaned outputs and final evaluation. They do not rebuild historical exploratory outputs or the curated reports/PDF.

| Location | Role |
|---|---|
| `src/` | Inspection, cleaning, selection and review scripts |
| `data/raw/` | Original downloaded JSON; excluded from Git |
| `data/processed/` | Cleaned splits, passage corpus, audit and review queue; excluded from Git |
| `data/evaluation/` | Original candidates, reviewed set, selection metadata and replacement log |
| `reports/` | Main PDF report and supporting documentation |

The initial download requires internet access. The dataset revision is pinned in the download script and data/source_version.json. requirements-lock.txt records all installed package versions. A fresh Windows/Python 3.15.2 environment reproduced all 22 JSON artifacts byte for byte; see reports/data-preparation.md.

## Interpretation and limitations

The curated evaluation favors clear, supported questions and is mostly recall-based. It does not measure missing-evidence refusal or broad reasoning ability. Subject imbalance and AI annotation may affect results. The corpus includes passages from held-out questions for open-book retrieval; held-out answers must not be used for training. Normalized question-text overlap was removed, but paraphrases, shared passages and pretrained-model exposure remain possible.

## Planned agent: PEAS

| Element | Description |
|---|---|
| Performance | Correct answers, supported explanations, useful retrieval and subject classification; measured on held-out examples |
| Environment | Students asking science questions over a searchable SciQ passage collection |
| Actuators | Display an answer, explanation, passage citation and subject; indicate insufficient evidence |
| Sensors | Receive question and four choices; read retrieved evidence |

## Methodology and coverage

The [methodology note](reports/methodology.md) explains subject boundaries, split protection, selection bias and provisional targets. The [coverage assessment](reports/methodology.md) and [training pilot](reports/methodology.md) support considering General Science, but a fifth model class is not yet adopted. The current evaluation measures four subjects only.

## Version history and audit trail

The original candidate pool, first reviewed set, and [first quality audit](reports/evaluation.md) are historical artifacts. That audit identified 16 issues. The [adaptation log](data/evaluation/evaluation_adaptations_v2.json) records their editorial resolutions in the current version. Three items select exact evidence excerpts; full source passages are preserved and may contain defects. Specify the evidence field when reporting future scores.

Current files: `data/evaluation/phase1_evaluation_v2.json`, `data/evaluation/review_summary_v2.json`, and `reports/evaluation.md`. Subject counts and membership are unchanged by adaptation. The historical version-1 audit is retained as data; it is not independent scientific validation of version 2.

## Submission status

Documentation and the three-page PDF reflect evaluation version 2. The quality audit and recorded editorial corrections are complete within their stated AI-review scope. Local Phase 1 preparation and the fresh-environment data reproduction check are complete within the documented review limitations. Git commit-history checks, instructor access verification and the `phase-1` release remain outstanding; the submission is not complete.

Reproduction evidence: [verification report](reports/data-preparation.md) and [file hashes](reports/reproduction-check.json). The optional coverage pilot is retained as historical annotation data.

Report organization: four Markdown documents in reports/ and one cumulative project-report.pdf. Per-phase GitHub tags can preserve the report at each submission stage.

## Simplified source layout

- `src/common.py`: shared paths and JSON/text helpers.
- `src/prepare_data.py`: pinned download, cleaning, split checks and passage collection.
- `src/prepare_evaluation.py`: apply recorded annotations and validate the final 100 items.

An isolated check of the simplified pipeline reproduced all eight current output artifacts with identical JSON content. Key ordering may differ; this check compares values rather than serialized bytes. The earlier eight-script/22-artifact verification remains a historical check of the previous pipeline.
