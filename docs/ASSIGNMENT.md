# Assignment 4 — verified requirements for Joshua

Source: local MBAX 6418 Assignment 4.pdf, five pages, in the parent assignment
folder; reviewed 2026-10-25 America/Denver. This checklist paraphrases the brief;
the original remains authoritative. Do not publish its service credentials.

## Ownership, tools and deliverables (pages 1–2, 4–5)

- Individual submission; discussion/troubleshooting permitted. Joshua must direct
  and check the agent and explain/repeat the process independently.
- One Google Colab notebook compares hosted zero-shot and few-shot against a small
  open-weight model trained with Unsloth/QLoRA. Use the prescribed hosted model
  `cyankiwi/Qwen3.6-35B-A3B-AWQ-4bit`; retrieve endpoint/key from private course
  configuration. Use the [specified MCP fork](https://github.com/davedgd/colab-mcp).
- Preserve the starter prompt's existing language and append missing requirements.
  Choose/justify model, settings, prompts and examples with Joshua. First fine-tune
  should start around 2–5B; training and inference must fit T4 16 GB. Report actual
  GPU and whether T4 compatibility was directly tested if using other hardware.
- Four Canvas files: executed notebook; adapter ZIP with only root-level
  adapter_model.safetensors and adapter_config.json (identifying original base);
  fine-tuned test predictions CSV/JSONL; prompt_examples.jsonl.

## Fixed source and selection (page 2)

Use Amazon Reviews '23 Gift Cards from the course-specified source. Preserve file
order and 1-based original line number as original_row. Skip blank lines and text
shorter than three characters after trimming; missing text is empty. Assign
0-based filtered_index after filtering. Stars 4–5 => POSITIVE; 3 => NEUTRAL;
1–2 => NEGATIVE. Inclusive ranges below refer to filtered_index, not original_row.

| Set | Inclusive pool | Required selection |
|---|---|---|
| Train | 1,000–19,999 | 300/class, 900 total |
| Validation | 20,000–29,999 | First 100/class, 300 total; reserve but do not use |
| Test | 30,000–39,999 | First 100/class, 300 total; same IDs for all approaches |

Initialize Python random.Random(43) once. Sample each file-ordered training class
pool in POSITIVE, NEUTRAL, NEGATIVE order, then shuffle combined samples with that
same generator. Do not substitute rows or use another random split. Supplied
split_data files are verification aids; personally check IDs/counts/overlap.

Before training: verify selected IDs against these rules, show sizes/class counts,
assert uniqueness/disjointness and inspect the actual prepared 900 training records
and actual few-shot examples (training only). Failed checks stop training.
An adapter trained on incorrect/unverifiable rows must be retrained fresh from the
original base; changing data afterward does not repair it.

## Fair comparison and response handling (pages 2–4)

- Train on all 900 required reviews. Input only title/text, never target rating
  or reference label. Preserve supplied titles/text, including 'Five Stars.'
- No test data in training/few-shot examples; no tuning from test outcomes.
  Validation is reserved and unused, including for early stopping/model selection.
- Consistent task instructions across approaches; request exactly one of POSITIVE,
  NEUTRAL, NEGATIVE. Fine-tuned training/inference share prompt structure/formatting.
- Temperature 0 or greedy decoding, small output-token limit, thinking disabled;
  record settings for each approach.
- Show complete prompts for the same test review, including every few-shot example.
- Before scoring, assert one prediction for every required test ID for each
  approach, align by ID, and keep passing checks in the notebook. Failures stop scoring.
- Strip response whitespace and normalize case. Accept only the three exact
  sentiment labels; anything else is INVALID. Keep raw answers, count INVALID
  as incorrect and never discard or guess replacements.

## Results and report (pages 3–4)

- For each approach: balanced accuracy, macro-F1, class precision/recall/F1,
  correct/incorrect prediction counts and INVALID counts. Average class metrics
  over the three sentiment reference classes, not INVALID as a fourth class.
- Three confusion matrices side by side: reference rows, prediction columns,
  each row sums to 1; add INVALID column if any invalid answers occur.
  Enlarge the approach with highest macro-F1.
- All three exact pairwise McNemar tests using a statistics package; p-values and
  interpretation of paired correctness differences and limitations.
- Labeled comparison results separate from generation code; concise nontechnical
  report at the bottom with model/parameter counts (hosted: 35B total/about 3B active),
  settings, actual GPU/time, rationale for choices, specific errors, statistical
  limits, resource tradeoffs, and an agent decision Joshua investigated/evaluated.
  Fine-tuning need not win; significance is not required for full credit.

## Adapter recovery and submission consistency (pages 4–5)

- Complete Joshua's own training run. Extract the submitted adapter ZIP to a
  separate folder and load with a fresh model instance; same runtime is permitted.
- Provide a labeled runnable saved-adapter inference section: exact base, matching
  tokenizer, evaluation prompt/settings, title/text input, raw response and label
  (or INVALID). No retraining or hosted calls needed for that section.
- Record model/tokenizer identifiers, tested package versions and generation
  settings; the adapter alone requires the original base model.
- Generate final test predictions and prompt examples using the reloaded submitted
  adapter. Compute fine-tuned scores from that prediction file; report/figures/files
  must agree. Notebook must run top to bottom without errors; nonconsecutive
  execution counts and Markdown edits after execution are permitted.
- Download all four files before leaving Colab; runtime storage is temporary.

Prediction fields exactly: original_row, filtered_index, title, text,
reference_label, prediction, raw_response. Exactly 300 records; allowed prediction
labels or INVALID; raw_response is the unprocessed answer.

Prompt examples: three JSON objects, one actual fine-tuned test prompt per reference
class, with original_row, filtered_index, reference_label and messages (complete
ordered roles/contents), or prompt for a single text prompt. Match prediction rows
and actual inference inputs. Reference label is metadata, never target model input.
These evaluation records are not training data.

Implementation milestones: [PLAN](../PLAN.md). Persistence/recovery procedure:
[ADAPTER_RECOVERY](ADAPTER_RECOVERY.md). None of these requirements has yet been
validated against an implemented notebook or training run.
