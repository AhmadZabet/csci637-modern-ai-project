# SciQ dataset datasheet

Ahmad Zabet | CSCI637 | Updated 17 November 2026

## Purpose and source

The data supports an English-language science study assistant for secondary-school, introductory college and independent study. SciQ by Johannes Welbl, Nelson F. Liu and Matt Gardner, Crowdsourcing Multiple Choice Science Questions (2017), is distributed by AI2. The source contains 13,679 crowdsourced multiple-choice science questions with a correct answer, three distractors and supporting text where available. This is educational reference material, with health and anatomy topics included.

Dataset https://huggingface.co/datasets/allenai/sciq. License https://creativecommons.org/licenses/by-nc/3.0/. CC BY-NC 3.0 allows sharing and adaptation for noncommercial purposes with attribution and license requirements. Retain source links, original author credit and the record of project modifications. The source data license does not automatically license project code. Individual passage attributions remain preserved and have not all been independently audited.

## Snapshot and preparation

The pinned revision and original JSON hashes are recorded in data/source_version.json. Original files remain separate from processed files. Whitespace is normalized, normalized question-text duplicates are removed, and training copies of held-out questions are excluded. Three answer-variant groups have recorded student-approved decisions. Twenty original groups remain unresolved across the source splits and are excluded or flagged. All source records are accounted for.

| Split | Original | Cleaned | Missing support retained |
|---|---:|---:|---:|
| Training | 11,679 | 11,577 | 1,190 |
| Validation | 1,000 | 1,000 | 113 |
| Test | 1,000 | 1,000 | 116 |

The 102 training exclusions comprise 19 overlaps with held-out questions, 54 ordinary duplicates, 3 reviewed duplicates and 26 unresolved answer-variant records. The 12,158 nonempty passage instances yield 12,148 unique normalized texts. SHA-256 passage IDs link evidence to source questions. Matching ignores case and whitespace, but cannot identify every paraphrase or incorrect scientific claim.

## Annotation and splits

SciQ has no native four-subject labels. The 100 main evaluation items were assigned Biology 44, Chemistry 19, Physics 19 and Earth and Space Science 18. Initial seed 637 sampling was followed by 28 replacements and 16 explicit adaptations. Short-passage replacement screening introduces selection bias. Original questions and choices remain recorded alongside adaptations. Three items select exact evidence excerpts from preserved full passages.

AI_USE.md records the actual labeling, review and rewriting assistance. Original AI-review provenance remains retained. On 17 November 2026, Ahmad Zabet reviewed the 100 evaluation questions in chat batches, with their choices, proposed labels, answers and relevant supporting evidence. Original and revised content was shown for all 16 adapted items. He approved all 100 labels, answers and evidence, including all 16 adaptations. He explicitly retained Chemistry for item 14 and the existing wording of item 17. The item-level decisions are recorded in data/annotations/ahmad_evaluation_review.json. This records the student review of the displayed material; broader scientific validation of every full source passage was not performed.

On 17 November, recorded AI-draft annotations generated starter classification subsets of 186 training and 39 validation records. They combine sampled topic annotation with usable earlier four-domain training-pilot labels. Ambiguous and General Science examples were excluded from the sampled classification scope. Topic annotation does not certify source answer accuracy. The complete splits remain partly unlabeled. Student review of the 225 subset labels is complete. Broader class coverage and additional annotation are required for reliable model comparisons. Use only question text as a predictor feature.

The new separate challenge set contains 10 parent-linked paraphrases, 8 controlled no-evidence prompts and 6 out-of-scope requests. Prompts and expected behaviors were authored by Codex and approved by Ahmad on 17 November 2026. They are excluded from training and tuning and are scored by track. The small track sizes require reporting counts. General Science is a potential extension, not a fifth class in the current evaluation.

## Biases and limitations

- English-only material does not demonstrate multilingual performance.
- Biology dominates both the curated main evaluation and starter classification subsets. Validation has only four Chemistry examples. Report per-class scores and avoid overinterpreting small differences.
- Curated supported questions and short replacement passages favor clear answerable items. Most questions test recall.
- AI-assigned labels and adaptations may be wrong or inconsistent. There is no independent annotator-agreement measurement.
- Source passages may contain typos, outdated statements, oversimplifications and figure references without figures. Preserving a passage does not verify its scientific correctness.
- The corpus intentionally includes main evaluation evidence for open-book retrieval. Test labels must not enter classifier fitting, prompt tuning or supervised answer training.
- Exact question overlap was removed, but semantic duplicates and pretrained-model exposure remain possible.
- No demographic-representation audit or full personal-information audit was performed. No private student information was added.
- Challenge cases are synthetic and behavior-specific. They do not establish robust performance across real student traffic.

## Distribution and maintenance

Raw and processed full-data folders are ignored by Git and recreated from the source. Annotation decisions, evaluation files and audit logs accompany the code with attribution. Run prepare_data.py followed by prepare_evaluation.py using the locked environment. Classification annotations and challenge prompts are preserved editorial inputs rather than automatically inferred ground truth. Read reports/data-preparation.md for verification details.

Maintainer Ahmad Zabet should record corrections by source ID, reviewer and date. Preserve the original phase-1 tag, freeze an audited evaluation version before model comparison, and document future changes. Deadline and late status require instructor confirmation.

Ahmad completed primary-subject review of all 186 training and 39 validation subset labels in chat batches by 24 November 2026. The original AI authorship, individual review dates and interdisciplinary decisions are retained in data/annotations/classification_labels.json. Approval covers the displayed question and answer context for subject labeling, not independent validation of every source answer or full passage. The full cleaned SciQ splits remain only partly labeled; broader annotation and class coverage are needed for reliable model comparisons.
