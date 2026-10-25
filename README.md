# csci637-modern-ai-project
CSCI637 — Science Study Assistant

Course: CSCI637 — Core Foundations of Modern AI
Instructor: Dr. Maysaa Khalil
Student: Ahmad Zabet
Semester: Fall 2026

Project Overview

This project aims to develop an intelligent Science Study Assistant capable of answering science-related questions using machine learning, transformer models, retrieval-augmented generation (RAG), and AI agent techniques.

The system will be developed incrementally across five phases, progressing from classical machine learning models to an evaluated, evidence-grounded AI assistant.

Dataset

Name: SciQ
Provider: Allen Institute for AI (AI2)
Source: https://huggingface.co/datasets/allenai/sciq
License: Creative Commons Attribution-NonCommercial 3.0 (CC BY-NC 3.0)

SciQ contains 13,679 multiple-choice science questions covering topics including Physics, Chemistry, and Biology.

Each record contains a question, one correct answer, three incorrect answer options, and a supporting passage when available.

The dataset provides three predefined splits:

Split

Samples

Training

11,679

Validation

1,000

Testing

1,000

Subject labels will be prepared for the classification task. A reviewed evaluation set containing at least 100 examples will also be developed.

**Agent:** SciQ Science Study Assistant

| PEAS element | Project description |
|---|---|
| **Performance** | Correctly answer science multiple-choice questions; select relevant supporting evidence; give a clear explanation grounded in that evidence. Measure answer accuracy on at least 100 held-out questions, and measure topic-classification accuracy if topic labels are added. |
| **Environment** | A student asks questions about science topics such as biology, chemistry, and physics. The agent works with a searchable collection of SciQ’s supporting passages and is evaluated against SciQ questions and correct answers. |
| **Actuators** | Display the selected answer, a short explanation, the supporting passage, and—if implemented—the question’s topic. Indicate when the available evidence is insufficient. |
| **Sensors** | Receive the student’s question and four answer choices. Read retrieved supporting passages from the corpus and, if the interface includes it, receive student feedback. |