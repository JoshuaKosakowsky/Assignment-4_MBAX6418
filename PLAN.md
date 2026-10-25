# Joshua's Assignment 4 completion plan

Branch: `individual/joshua`. Reviewed 2026-10-25 America/Denver.
Status: phase 1 verified (Colab connected, T4 recorded, Drive round trip OK); phase 2 decisions recorded in docs/EXPERIMENT.md.
Priority: preserve a valid completed adapter and prove recovery before spending
time on comparison figures and the report. Main stays frozen.

## 1. Connect and prove persistent storage before training

- Use the course-specified [Colab MCP fork](https://github.com/davedgd/colab-mcp).
  Confirm tools can read the notebook, execute a cell and return its output.
  Connection verified 2026-10-25: notebook read/write/run worked end to end via the fork.
  Start with notebook control and manual GPU selection if needed; optional
  programmatic GPU OAuth is not a prerequisite to the assignment.
- Create a Drive-saved notebook; select T4 and record actual GPU/memory.
- Propose private Drive folder `MyDrive/MBAX6418/Assignment4/joshua/<run-id>/`
  plus local sibling folder `../artifacts/joshua/<run-id>/` outside this public repo.
  Confirm the actual account/path during setup. A Colab URL is not a backup.
- Write/read a small file on Drive, download it locally and compare SHA-256.
  Confirm there is sufficient storage. Do not begin substantive training until
  the notebook and artifact backup paths have been tested.

Acceptance: cell execution works, actual GPU recorded, notebook saved in Drive,
and the storage round trip succeeds. See [adapter recovery](docs/ADAPTER_RECOVERY.md).

## 2. Establish data integrity and agree on the experiment

- Preserve the course starter prompt verbatim; append the missing requirements
  from [ASSIGNMENT](docs/ASSIGNMENT.md), without publishing its credentials.
- Verify supplied train/val/test files against the source selection rules.
  Check prescribed IDs, ordering, class counts, uniqueness and disjointness;
  inspect the actual formatted/tokenized training records and few-shot inputs.
  Joshua personally reviews checks and several complete training examples.
- Choose and justify a small instruct model around 2–5B with Joshua using a
  current Unsloth example and model card. Confirm access, tokenizer/chat template
  and 4-bit QLoRA training/inference fit a T4 16 GB; record exact identifiers,
  revisions, tested package versions, precision and training settings.
- Agree on epochs, learning rate, LoRA settings, sequence length/truncation,
  effective batch size, random seeds, task prompt and balanced few-shot examples
  from training only. Do not use validation or test outcomes for tuning.
- Keep review titles/text unchanged in model inputs. Inspect token lengths so
  truncation cannot silently remove the label or violate the brief.
- Build a separate inference-only notebook path that loads saved artifacts,
  never calls training or the hosted model, and accepts only title/text.

Acceptance: fail-fast data checks pass, choices are documented before test
evaluation, and Joshua approves the actual examples and proposed settings.

## 3. Test saving/recovery, then complete Joshua's training run

- Test the save/package/copy/reload path with a disposable pilot adapter using
  training records only; do not mistake it for the final trained adapter.
- Configure periodic trainer checkpoints with full resumable state and automatic
  persistence outside the VM. Provisional cadence: every 25 optimizer steps plus
  completion, adjusted after timing so the first checkpoint occurs before the
  run ends. Keep at least the two latest verified complete checkpoints.
- Train a fresh final adapter on exactly all 900 prescribed records (300/class)
  with the agreed schedule. Save checkpoint provenance, progress, loss, elapsed
  time, GPU and config. Do not select a checkpoint using test performance.
- Immediately export the completed LoRA adapter in safetensors format; verify
  the config identifies the original base model. Keep tokenizer/template and
  environment metadata separately from the submission ZIP.
- Build `adapter.zip` containing exactly root-level `adapter_model.safetensors`
  and `adapter_config.json`. Copy to Drive, download locally, compare hashes and
  open the backed-up ZIP. Stop on any export, integrity or persistence failure.

Acceptance: a completed, valid adapter ZIP exists in both Drive and local storage,
with matching checksums; substantive training completion is recorded. No base
model merge, GGUF export or extra files inside the two-file submission ZIP.

## 4. Prove the submitted adapter works without retraining

- Extract a verified backup of the exact submission ZIP into a separate folder.
- Release the training model and load a fresh base model instance, exact matching
  tokenizer and adapter. Prefer a fresh Colab runtime for stronger recovery
  evidence; a fresh model in the same runtime satisfies the assignment.
- Run the inference-only path with identical formatting, template, greedy
  decoding, thinking disabled and recorded output limit. Show raw response and
  normalized label on a training example for the recovery smoke test.
- Then use this reloaded adapter to generate all 300 prescribed test predictions
  and three actual test prompts (one per reference class). Save each response
  with its ID as generation proceeds, persist progress and prevent duplicates.
- Save completed predictions and prompt examples to Drive and local storage.
  Compute the fine-tuned scores from the exact backed-up prediction file.

Acceptance: recovery and final inference succeed without training or hosted-model
calls; all 300 unique test IDs match; three recorded prompts match actual inputs.
This is the main adapter milestone. Do not proceed with a missing or untested ZIP.

## 5. Complete hosted comparisons, evaluation and explanation

- Run zero-shot and few-shot using the prescribed hosted model, same 300 test
  reviews and consistent task instructions. Keep credentials out of Git and
  public notebook outputs. Record prompts/settings; cache raw answers persistently.
- Use training-only few-shot examples; freeze prompts before inspecting test
  outcomes. Never adjust model/prompts from those outcomes.
- Align all three predictions by IDs; fail on missing, extra or duplicate IDs.
  Record INVALID answers as incorrect, without guessing replacements.
- Produce balanced accuracy, macro-F1, per-class precision/recall/F1, correct/
  incorrect counts and INVALID counts. Show three row-normalized confusion
  matrices side by side plus enlarged highest-macro-F1 matrix, and exact pairwise
  McNemar tests for all three comparisons using a statistics package.
- Show complete prompts for the same test review across all approaches. Keep
  results in a labeled section separate from generation code. Finish with the
  nontechnical report covering decisions, specific errors, significance limits,
  compute/training tradeoffs, and an agent recommendation Joshua investigated.

Acceptance: every figure/metric/report claim matches final saved outputs.
Fine-tuning need not win; statistical significance is not required.

## 6. Verify, download and submit four matching files

- Execute the notebook top to bottom without errors; ensure the saved-adapter
  section is runnable independently. Define explicit train/resume/inference modes
  so reopening the notebook cannot silently launch a new training run. The final
  notebook retains real training evidence, not merely unexecuted training cells.
- Verify exact schemas, ZIP contents, base identity, 300 test rows and three
  prompt examples; recompute fine-tuned metrics from submitted predictions.
- Download the executed notebook, adapter ZIP, predictions CSV/JSONL and
  prompt_examples.jsonl. Keep verified Drive and local copies of all four.
- Upload the four files to Canvas and check submitted filenames and sizes;
  download and compare checksums if Canvas permits. A Colab link or GitHub branch
  does not replace the required four-file submission. Canvas upload remains a
  later explicit action; it has not been performed by this plan.

Acceptance: four consistent files are durably backed up and the Canvas submission
is confirmed. Keep artifacts/checkpoints outside the public Git repository.

## Decisions and evidence still needed

No model, hyperparameters, prompt examples, Colab account, persistent folder or
training schedule has been selected/tested. No GPU allocation, MCP install,
Drive mount, raw-data verification, notebook run, training or upload occurred.
Requirements/source details are in [ASSIGNMENT](docs/ASSIGNMENT.md); recovery
gates and interruption handling are in [ADAPTER_RECOVERY](docs/ADAPTER_RECOVERY.md).
