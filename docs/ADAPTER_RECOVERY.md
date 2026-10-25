# Adapter saving and recovery plan

Joshua's priority is to avoid losing completed training when a Colab session ends.
This is a planned procedure, not evidence that an adapter already exists.

## What persists and what does not

A Drive-saved notebook preserves code and saved outputs. Colab's VM, RAM, installed
packages and runtime files are temporary; saving the notebook does not back up
its adapter. A completed backed-up adapter can be loaded with the original base
model without repeating training. See [Colab FAQ](https://research.google.com/colaboratory/faq.html).

An adapter contains learned changes, not the whole original model. Preserve its
base model/tokenizer identifiers and revisions, template, package versions and
generation settings. See [PEFT checkpoint format](https://huggingface.co/docs/peft/developer_guides/checkpoint).

## Two kinds of save, for two purposes

| Artifact | Purpose | Planned durable storage |
|---|---|---|
| Completed adapter ZIP | Required submission and inference without retraining | Private Drive plus verified local copy |
| Full trainer checkpoint | Continue interrupted training from saved progress | Private Drive; optional local snapshot |
| Run manifest/tokenizer/template | Rebuild the matching inference environment | Private Drive plus local copy, outside the ZIP |
| Notebook and saved responses | Preserve execution evidence and evaluation progress | Private Drive plus local copies |

The two-file adapter ZIP does not preserve optimizer/scheduler/RNG/trainer state
for an exact training resume. Checkpoints must contain the state required by the
selected trainer, with matching code/data/config. Use the trainer's resume path,
not a fresh adapter. [Unsloth checkpoint guidance](https://unsloth.ai/docs/basics/finetuning-from-last-checkpoint)
describes periodic saves and checkpoint resume. Its generic validation/early-
stopping examples do not override this assignment's unused-validation rule.

## Before substantive training

1. Save notebook in Drive. Create a unique run folder; never overwrite the last
   known-good adapter or reuse another student's run folder.
2. Verify Drive write/read and a local download with matching SHA-256. Reserve
   space for at least two complete checkpoints, the adapter ZIP and outputs.
3. Test export/reload with a disposable pilot before the final run. Make the
   final run fresh, with verified data and agreed settings.
4. Set periodic saves and persist complete checkpoint directories. Copy to a
   staging destination, verify all required files and hashes, then mark complete.
   Never treat a partially copied directory as recoverable; retain the previous
   verified checkpoint until its replacement is verified. Do not rely on an exit
   callback: a killed runtime may never execute one.

## Immediately after final training

1. Export the LoRA adapter, explicitly ensuring the required safetensors file was
   produced. Fail if the export only contains .bin or merged full-model weights.
2. Validate the adapter config's base-model identity and that the weights load.
   Keep tokenizer/template and package manifest separately for reconstruction.
3. Build the submission ZIP from an allowlist of two root-level members only:
   `adapter_model.safetensors` and `adapter_config.json`. Check ZIP integrity,
   member names, nonempty files and checksum; do not zip the whole working folder.
4. Copy the ZIP and manifest to Drive, verify the copy, download locally and
   independently compare its SHA-256. A browser download prompt is not proof that
   the local copy exists. Check the actual file.
5. Extract the backed-up submission ZIP to a new folder and load it with a fresh
   base model and matching tokenizer. Run a title/text example without training
   or hosted calls, then generate final test predictions with that loaded adapter.
6. Preserve each generation result by ID; checkpoint prediction progress to Drive
   and resume only missing IDs with the same ZIP hash/config. Never mix runs.
7. Back up the four final submission files and confirm the Canvas upload later.

If inference export/reload fails, stop and fix it before evaluation/reporting.
A successful save call or a ZIP filename alone does not establish recovery.

## If Colab disconnects

| State when runtime was lost | Recovery |
|---|---|
| Final ZIP verified on Drive/local | Recreate environment, extract ZIP, reload base/tokenizer/adapter; no retraining needed |
| Only a verified full checkpoint exists | Restore matching code/data/environment and resume remaining training; export final ZIP when complete |
| Predictions partly saved with final ZIP hash | Reload that ZIP and continue missing test IDs only |
| Only notebook or URL saved | Recover code/evidence, but lost weights require retraining if no adapter/checkpoint backup exists |
| Trained on incorrect/unverifiable rows | Start from original base with a fresh adapter, as the assignment requires |

Google Drive is the proposed primary backup; a local downloaded copy is the
second. No public model upload is needed for the assignment, and adapter binaries
stay outside Git. A private model-hub upload is optional later, not a substitute
for the required two-file ZIP or the Canvas submission.
