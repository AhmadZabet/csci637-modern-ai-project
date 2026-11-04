# Project methodology

Current scope: Phase 1. This combines the task definition, design rationale and exploratory subject-label work. The four-class evaluation remains current; General Science is a proposed extension. Later sections preserve exploratory findings, not additional submission requirements.

## Task and success criteria

### Phase 1 — Problem Definition

### 1. Task Definition

The goal of this project is to develop an intelligent Science Study Assistant using the SciQ dataset.

The system will perform two main tasks:

1. **Science Subject Classification:** Automatically classify science-related questions into subjects such as Biology, Chemistry, Physics, and Earth & Space Science.

2. **Science Question Answering:** Provide accurate answers to science questions. In later phases, the system will use retrieval-augmented generation (RAG) to retrieve relevant scientific passages and generate evidence-supported answers.

The project aims to help students access scientific knowledge more easily and improve their understanding of science concepts.

### 2. Target Users

The target users of the Science Study Assistant are:

- High school students studying science subjects.
- Undergraduate students reviewing introductory science topics.
- Independent learners interested in scientific knowledge.

The assistant will allow users to ask science questions and receive relevant answers.

### 3. Success Criteria

The project's success will be measured using the following proposed metrics:

- **Subject Classification Accuracy:** At least 85%.
- **Classification Macro-F1 Score:** At least 0.80.
- **Question Answering Accuracy:** At least 80%.
- **Retrieval Recall@5:** At least 90% of evaluated questions with known supporting passages should retrieve the correct passage within the top five results.
- **Answer Faithfulness:** At least 90% of evaluated answers should be supported by their retrieved passages.

These success criteria will be evaluated during the later phases of the project, using a reviewed evaluation set and clearly defined evaluation procedures.
### 4. Interpretation of targets

These thresholds are provisional project goals, not measured results or externally validated benchmarks. See [methodological justification](methodology.md) for the taxonomy, cleaning rationale, selection tradeoffs and planned scoring procedures.


## Methodological rationale

### Phase 1 methodological justification

> Status update, 4 November 2026: This note records the earlier analysis. The 16 evaluation issues referenced below now have documented editorial resolutions in version 2; see evaluation.md. The current review provenance is one unchanged human-confirmed item and 99 AI-reviewed items (16 adapted). The proposed fifth subject remains unimplemented.


Ahmad Zabet | CSCI637 | 3 November 2026

This note explains the choices behind the current Phase 1 artifacts. Proposed evaluation procedures below are specifications for later implementation, not completed experiments.

### 1. Task formulation and dataset fit

SciQ was selected with instructor approval. Its question, four choices, correct answer and available supporting passage provide a practical foundation for both answer selection and evidence retrieval. The initial interface is explicitly multiple-choice: this gives a reproducible answer-accuracy measure and avoids claiming that the dataset alone establishes performance on unrestricted student questions.

Subject classification is a separate, complementary sub-task that can be compared across classical, neural and transformer models. It can later support query routing. Classification accuracy does not establish question-answering ability, and a successful retrieval step does not establish answer faithfulness. These outcomes will be measured separately.

### 2. Subject taxonomy and labeling policy

The four subjects are a project-defined educational taxonomy, not native SciQ labels or an externally validated ontology. They provide interpretable categories at a manageable scope for this course. They do not cover every possible scientific-method or interdisciplinary question; ambiguous items must be flagged rather than forced into a category.

| Subject | Decision rule | Boundary example |
|---|---|---|
| Biology | The question principally asks about living systems, physiology, genetics, evolution or ecology. | Protein function and membrane transport are Biology. |
| Chemistry | The question principally asks about substances, composition, chemical bonding, reactions or electron configuration. | Molecular composition of fatty acids is Chemistry even in a biological passage. |
| Physics | The question principally asks about forces, energy, waves, electricity or nuclear processes. | Radioactivity is Physics; atomic electron configuration is Chemistry under this project's convention. |
| Earth and Space Science | The question principally asks about Earth systems, geology, weather, fossils or astronomy. | Telescope use in astronomy is Earth and Space Science; general optical laws are Physics. |

Assign one primary label based on the knowledge needed to answer, rather than isolated words or the passage's general topic. Read the options and evidence to resolve context, then record a boundary note if needed. If two labels remain equally defensible, flag the item for adjudication or exclusion. These conventions should be reused when annotating training and validation data. Only the 100 evaluation items are currently labeled. No inter-annotator agreement has been measured; labels remain subject to audit.

### 3. Cleaning and split protection

Original files and source indices are retained to make changes inspectable. Whitespace normalization removes formatting variation without rewriting scientific claims. Matching normalized question text is a conservative and reproducible duplicate check, but cannot identify semantic duplicates or prove complete leakage prevention.

When a question occurs in training and a held-out split, remove the training copy to protect the evaluation question. Ordinary duplicates retain a passage-bearing copy where possible. Differing answer text can reflect a synonym, typo or genuinely different interpretation, so unresolved variants are quarantined rather than automatically reconciled. Three groups have explicit student-approved decisions; remaining cases are documented.

Missing support is not sufficient reason to discard a question for classification. Those records remain marked in the cleaned data, while the retrieval evaluation requires identifiable evidence. This creates different eligible populations for different tasks and must be reflected in result descriptions.

### 4. Evaluation selection and its tradeoffs

The 100-item minimum comes from the course requirements. A fixed seed makes the initial candidate selection repeatable; it does not guarantee representativeness or remove annotation bias. The initial random pool was subsequently curated, with 28 replacements. Short-passage replacement screening improves review practicality but favors simpler evidence and changes the sampling distribution.

The resulting distribution is Biology 44, Chemistry 19, Physics 19, and Earth and Space Science 18. We will report these counts, per-subject scores, and macro-F1 rather than describe the set as balanced. Each error changes overall accuracy by one percentage point; one error within an 18-item subject changes its accuracy by approximately 5.6 percentage points. Small score differences should therefore not be overinterpreted.

This set estimates performance on curated, supported multiple-choice questions, not the full SciQ distribution, real student traffic, missing-evidence cases or robust reasoning. Additional challenge sets can test those behaviors separately. The current items are predominantly recall questions; no unsupported claim of difficult or adversarial coverage is made.

Two examples were confirmed by Ahmad; 98 were reviewed by Codex. Student authorization is not equivalent to individual human verification of those 98 examples. The next quality audit should inspect label consistency, unique answer choices and evidential support, recording any corrections before the evaluation version is frozen.

### 5. Targets and planned scoring

The existing thresholds are provisional engineering acceptance goals. They are not published SciQ benchmarks, empirically calibrated expectations, or promises of achieved performance. Baselines will provide evidence about feasibility; any target revision should be justified using training/validation evidence and recorded before final test scoring, never adjusted after seeing test results to declare success.

| Measure | Existing target | Planned interpretation |
|---|---|---|
| Subject accuracy | At least 85% | Number of correct primary-subject predictions divided by the number evaluated. |
| Subject macro-F1 | At least 0.80 | Compute F1 for each of the four subjects and take their unweighted mean; declare the treatment of zero denominators. |
| Answer accuracy | At least 80% | Exactly one selected answer matching the answer key; abstentions or invalid selections count as incorrect and are additionally reported. |
| Retrieval recall@5 | At least 90% | Fraction of eligible questions whose designated source passage appears in the top five distinct retrieved passage IDs. With one designated source, this is also a hit-rate measure. |
| Answer faithfulness | At least 90% | Fraction of substantive generated answers whose factual explanation claims are all supported by their cited passages, assessed with an explicit rubric. |

The accuracy and macro-F1 goals jointly discourage high aggregate scores that conceal weak minority-subject performance. Retrieval and faithfulness receive stricter goals because the planned study assistant should expose relevant evidence and avoid unsupported explanation. This motivates the direction of the targets, not their exact numerical values; the exact thresholds remain a project choice requiring validation.

For context, uniform random selection among four choices has 25% expected answer accuracy. Always predicting Biology on this particular curated set would score 44% subject accuracy. These are analytical reference points, not trained-model results. Model baselines must be developed on training data and tuned on validation data.

Faithfulness is distinct from correctness: a response can repeat an erroneous source faithfully. Pure abstentions should not inflate faithfulness; report answer coverage and abstention rate separately. The later rubric should allow supported, unsupported, and uncertain judgments, with unresolved judgments reported and excluded from claims of confirmed support. Record assessor provenance and disagreement resolution.

Exact passage-ID retrieval scoring is reproducible but may undercount alternate passages that genuinely support an answer. Inspect such cases separately rather than silently changing the reference after scoring. If passages are chunked later, preserve a chunk-to-source mapping and define a source-level hit before evaluating.

### 6. Open-book retrieval and scope of claims

The passage collection intentionally includes evidence associated with validation and test questions. This simulates a study assistant consulting a known reference collection. It does not test retrieval from unseen documents. Test questions and answer keys must stay out of classifier fitting, prompt tuning and supervised model training. Shared passages, paraphrases and public-dataset exposure during model pretraining remain possible sources of optimistic results.

Before model development, freeze the audited evaluation membership and label version. Use validation examples for model and prompt choices, evaluate all compared systems under the same input and evidence conditions, and record any subsequent data changes. The subsequent 4 November 2026 check pinned the source revision and reproduced all 22 JSON artifacts in a fresh Windows environment; see data-preparation.md.

### Supporting artifacts

- [Problem definition and original targets](methodology.md)
- [Dataset datasheet and source links](dataset-datasheet.md)
- [Cleaning decisions and counts](data-preparation.md)
- [Evaluation review and item-level caveats](evaluation.md)

This note adds rationale and planned procedures. It does not change existing data, labels or targets. Its key conclusions should be incorporated into the concise PDF report after the quality audit, so the final report and data version agree.


## Exploratory subject coverage

### Subject coverage assessment

> Status update, 4 November 2026: This note records the earlier analysis. The 16 evaluation issues referenced below now have documented editorial resolutions in version 2; see evaluation.md. The current review provenance is one unchanged human-confirmed item and 99 AI-reviewed items (16 adapted). The proposed fifth subject remains unimplemented.


3 November 2026 | Exploratory review by OpenAI Codex

### Finding

The four current labels cover many questions but do not adequately describe all observed topics. Add General Science to the proposed taxonomy for domain-independent scientific methods, experimental design, evidence and general technological design. This is a recommendation for the next annotation version, not a claim that the existing four-class evaluation has been migrated.

### Evidence and method

Inspected question text in a seeded sample of 90 cleaned records: 30 from each split, seed 637. Also searched the full cleaned question text for scientific-method, hypothesis, experimental-variable and technology terms. The search returned 35 training, 5 validation and 2 test candidates. These are keyword matches, not class frequencies. Read the first 12 training matches and all validation/test matches with answer and passage context (displayed passages were limited to 700 characters).

Examples supporting the proposed category:

| Source ID | Question topic | Proposed classification |
|---|---|---|
| sciq_train_01540 | Scientific method and observation | General Science |
| sciq_train_02667 | Keeping controlled variables constant | General Science |
| sciq_train_03429 | Data needed to test a hypothesis | General Science |
| sciq_validation_00367 | Communication of investigation results | General Science |
| sciq_validation_00672 | Inductive and deductive reasoning | General Science |
| sciq_test_00486 | Technological design | General Science |

Counterexamples prevent indiscriminate keyword labeling: sciq_train_00665 concerns biotechnology applications (Biology); sciq_train_03572 concerns rare-earth elements used in technology (Chemistry); sciq_test_00511 concerns sonar (Physics). A hypothesis about evolution still belongs to Biology if the question tests evolutionary knowledge.

### Proposed labeling rule

Use General Science only when answering requires knowledge of scientific practice or a broadly applicable concept without a dominant domain. It is not an Other category for unclear or poor-quality questions. Flag ambiguous records separately. Assign cross-disciplinary questions by the central concept required to answer and document boundary decisions.

Existing domains retain their scope: Biology includes health and anatomy as educational topics; Chemistry includes substances and reactions; Physics includes physical laws and instruments; Earth and Space Science includes geology, weather, oceans and astronomy. Technology-related questions belong to their substantive domain when one is evident. Measurement of a physical quantity such as temperature ordinarily remains Physics; generic experimental uncertainty or research procedure may fit General Science.

### Limits and next implementation step

This exploratory check establishes the existence of coverage gaps, not complete coverage or reliable class prevalence. The 90 sampled records have not all received final subject annotations. Reviewing held-out material while designing the taxonomy also limits claims that the existing test set was never inspected.

Before switching to five-class modeling, annotate and count an initial training sample under the expanded rubric, check whether General Science has sufficient examples, and resolve ambiguous boundaries. Do not infer adequacy from the 42 keyword candidates. If the category is too sparse for fair model comparison, keep a four-class classifier with an explicit scope limit and route general-science questions directly to retrieval; this still allows the assistant to answer them.

The existing evaluation set remains four-class (44 Biology, 19 Chemistry, 19 Physics, 18 Earth and Space Science). It cannot measure General Science performance. If five classes are adopted for modeling, revise evaluation membership and labels, define five-class macro-F1, and update the problem definition, datasheet, review scripts and PDF together. The 16 outstanding quality corrections should be handled in that same versioned revision. No existing evaluation labels or counts were changed by this assessment.

Evidence is saved in data/taxonomy_coverage.json. Reproduce the sample and keyword candidate collection with src/phase1_check_taxonomy.py. The assistant's retrieval corpus can cover all topics regardless of whether a classifier supports every category.


## Training annotation pilot

### Training subject-label pilot

> Status update, 4 November 2026: This note records the earlier analysis. The 16 evaluation issues referenced below now have documented editorial resolutions in version 2; see evaluation.md. The current review provenance is one unchanged human-confirmed item and 99 AI-reviewed items (16 adapted). The proposed fifth subject remains unimplemented.


3 November 2026 | AI-provisional annotation by OpenAI Codex

### Design and results

Reviewed question and answer text for 60 randomly sampled cleaned training records (seed 637) and 35 targeted keyword candidates from training. Supporting passages were inspected for selected ambiguous cases. The groups do not overlap: 95 unique records, with 94 provisional labels and one unresolved record. This is a taxonomy pilot, not a quality-approved model-training dataset.

| Subject | Random sample (60) | Targeted group (35) |
|---|---:|---:|
| Biology | 35 | 8 |
| Chemistry | 6 | 1 |
| Physics | 10 | 2 |
| Earth and Space Science | 7 | 2 |
| General Science | 1 | 22 |
| Unresolved | 1 | 0 |

The random sample contains one General Science item about models. Targeted inspection finds another 22 about observation, hypothesis testing, controls, scientific reasoning and technological design. These establish that the category exists. They do not establish its full prevalence or sufficient independent examples for reliable classifier training. Keyword matches are not automatic labels: eight targeted items belong to Biology and five to other domains.

### Boundary and quality findings

- The vague question 'What are the poles labeled?' has no supporting passage. Its primary subject remains unassigned rather than guessed.
- Questions about ultrasound and thermodynamic laws are Physics even when their applications concern medicine or ecology.
- Environmental water treatment is assigned Earth and Space Science; its engineering/chemistry overlap is documented.
- Models and experimental controls are General Science when the question tests scientific practice, regardless of a passage's illustrative domain.
- Subject labels do not certify answer correctness. Several questions have imprecise wording or simplified scientific-method claims and need a separate quality check.
- Two Earth-system hypothesis questions are near-duplicates despite surviving exact-text deduplication. Record counts therefore overstate independent topic coverage.

### Decision for this phase

Retain General Science in the proposed annotation taxonomy and keep its examples in the assistant's knowledge scope. Do not yet declare a five-class model configuration or change the existing four-class evaluation. The 23 observed General Science records are a small, enriched, provisionally labeled group; adequacy for learning and fair evaluation remains unestablished.

Before Phase 2, expand training annotation across all five proposed subjects, inspect label consistency and quality, and count usable independent examples. Allocate model-selection examples from validation without borrowing final test items. If General Science remains too sparse, document a four-class classifier scope and allow the retrieval assistant to handle general-science questions without forcing a subject prediction. It is unnecessary to resolve that modeling choice by inventing examples or treating uncertain labels as ground truth.

For Phase 1, this pilot documents the labeling plan and coverage gap. The immediate unfinished evaluation work remains the 16 flagged quality corrections, followed by consistency updates and the reproduction check. A five-class evaluation, if adopted later, needs explicitly selected and reviewed General Science examples; the current set cannot measure that class.

### Artifacts and reproducibility

- data/annotations/subject_pilot.json: source IDs, text, provisional labels, sampling flags, provenance and notes.
- data/annotations/subject_pilot_summary.json: separate random and targeted counts.
- src/phase1_label_subject_pilot.py: reproduces selection and the recorded annotation decisions; it is not an automatic subject classifier. Run after src/phase1_check_taxonomy.py.

No validation or test items were added to training. No student review of these 95 labels is claimed. The pilot has not trained a model or estimated its performance.
