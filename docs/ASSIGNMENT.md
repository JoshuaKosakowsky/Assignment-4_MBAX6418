# Assignment 4 — verified individual-work boundary

Source: local `MBAX 6418 Assignment 4.pdf` in the parent Assignment 4 folder,
reviewed on 2026-10-25 America/Denver. This is a focused workflow summary, not
a replacement for the full assignment specification.

- Submissions are individual; discussion and troubleshooting are permitted.
- Each student must learn to fine-tune, direct and check their agent, evaluate
  results, and explain and repeat the process independently.
- Each student must complete their own training run, reload their submitted
  adapter with a fresh model instance, and generate final predictions and prompt
  examples using that reloaded adapter.
- The task compares zero-shot, few-shot and fine-tuned sentiment classification
  in one Google Colab notebook using prescribed data and fixed splits.
- Four Canvas files are required: an executed notebook, adapter ZIP, fine-tuned
  test predictions, and prompt_examples.jsonl. Keep generated submissions outside
  Git and download them from Colab for submission.
- Model, training settings, prompts and few-shot examples must be chosen and
  justified with the student. Preserve the supplied starter prompt's language.

The full brief additionally governs split selection, data checks, leakage,
decoding settings, evaluation/statistics, figures, report and reproducible
inference. Read it before implementation; this baseline neither encodes all
acceptance criteria nor establishes submission readiness.

Local course sources remain outside Git: the assignment PDF and split_data/
(train.jsonl, val.jsonl, test.jsonl). They have not been published. No training,
dataset validation, hosted-model calls or notebook execution occurred in this migration.
