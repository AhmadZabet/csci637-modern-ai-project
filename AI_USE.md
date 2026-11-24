# AI Tool Disclosure

**Student:** Ahmad Zabet  
**AI tool:** OpenAI Codex

OpenAI Codex assisted with clarifying concepts, writing and debugging preparation code, inspecting and cleaning SciQ, drafting the task definition and documentation, assigning subject labels, selecting evaluation candidates, reviewing answers against supporting passages, and preparing the report.

During evaluation preparation, Codex replaced 28 candidates and adapted 16 questions or answer-choice sets. Original wording, source IDs, and change logs are retained for traceability.

Codex also drafted the classification subset labels and 24 additional challenge cases covering paraphrased questions, insufficient evidence, and out-of-scope requests.

The earlier brief disclosure did not fully describe this assistance. This statement provides the additional detail requested in the instructor’s feedback.

On 17 November 2026, Ahmad Zabet reviewed the 100 evaluation questions in chat batches, with their choices, proposed labels, answers and relevant supporting evidence. Original and revised content was shown for all 16 adapted items. He approved all 100 labels, answers and evidence, including all 16 adaptations. He explicitly retained Chemistry for item 14 and the existing wording of item 17. The item-level decisions are recorded in data/annotations/ahmad_evaluation_review.json. This records the student review of the displayed material; broader scientific validation of every full source passage was not performed.

Ahmad Zabet is responsible for understanding, reviewing, and verifying the submitted work.

The classification subset labels were AI-drafted and subsequently reviewed and approved by Ahmad. Ahmad approved all 24 AI-drafted challenge cases in chat on 17 November 2026 after seeing the prompts, answers or expected behavior, labels and evidence summaries.


On 17 November 2026, Ahmad approved the primary subject labels of all 39 validation-subset questions after viewing their question and dataset-answer context in chat. He retained Biology for the catalysis-in-organisms item, with Chemistry recorded as an overlap. This approval covers subject labels. The 186 training-subset labels were subsequently reviewed and approved by 24 November 2026.

Ahmad completed primary-subject review of all 186 training and 39 validation subset labels in chat batches by 24 November 2026. The original AI authorship, individual review dates and interdisciplinary decisions are retained in data/annotations/classification_labels.json. Approval covers the displayed question and answer context for subject labeling, not independent validation of every source answer or full passage. The full cleaned SciQ splits remain only partly labeled; broader annotation and class coverage are needed for reliable model comparisons.
