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
