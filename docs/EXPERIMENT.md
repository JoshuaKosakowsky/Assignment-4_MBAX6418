# Experiment choices

## Status

Locked 2026-10-25 pending Joshua's review of formatted examples; nothing below
uses validation or test outcomes.

## Model

`Qwen3-4B-Instruct` (~4B, within the 2–5B brief). Rationale: ungated Apache-2.0
(Gemma 3/4 and Llama 3.2 are HF-gated); dense, so 4-bit QLoRA is safe (MoE wants 16-bit LoRA);
full Unsloth support incl. T4-16GB QLoRA guides; Qwen family consistency with the hosted
endpoint (`cyankiwi/Qwen3.6-35B-A3B-AWQ-4bit`) for the report narrative.

## Data

The fixed split_data files; all Phase-2 integrity checks PASS:

- 1500 rows total; 900/300/300 rows in train/val/test.
- 300/100/100 per class in train/val/test.
- Unique `filtered_index` + `original_row` per set.
- No overlap between sets (both keys).
- Train indices ⊂ [1000,19999], val ⊂ [20000,29999], test ⊂ [30000,39999].
- Rating→label mapping consistent.
- No text < 3 chars.
- Review length (title+text): median 104 chars, p99 878, max 1956.

Every few-shot example must come from the 900-row training set; val/test
never used for anything.

## Training settings (QLoRA/Unsloth)

4-bit nf4, double quant, bf16; r=16, lora_alpha=32,
lora_dropout=0, target all linear layers (q,k,v,o,gate,up,down); per_device_train_batch_size=2,
gradient_accumulation_steps=4 (effective 8); 3 epochs ≈ 340 steps over 900 rows; lr=2e-4,
10 warmup steps, cosine; seed 42; `max_seq_length=1024`; Unsloth gradient checkpointing.

## Prompt (identical structure for ALL three approaches)

```
Classify the sentiment of the Amazon product review as POSITIVE, NEUTRAL, or NEGATIVE. Consider only the review title and text. Reply with exactly one of: POSITIVE, NEUTRAL, NEGATIVE.
Title: {title}
Review: {text}
Sentiment:
```

Few-shot = 3 examples, one per reference class, from training only, in the same shape.
Fine-tune trains chat-template versions of the same instruction + review → label, and the
saved-adapter inference section reuses it identically.

## Generation settings (all approaches)

Greedy (temperature 0), max_new_tokens 16, thinking
disabled (Qwen3 emits `think` blocks unless explicitly off — set `enable_thinking=False` /
equivalent), predictions normalized (strip, uppercase), only POSITIVE/NEUTRAL/NEGATIVE accepted,
anything else recorded raw and counted INVALID.

## Reconnect note

Server env `COLAB_NOTEBOOK_PATH=/drive/1GUjxwK8bo6IPnQ_KQP7wujTrGBGIFZ94`;
Drive mount requires the notebook in real Chrome (webview popup blocker); Drive free 9 GiB.
The Hermes preview-pane webview blocks the auth popup
(`MessageError: credential propagation was unsuccessful`).

Notebook saved in Drive: `Assignment4_josh.ipynb`, FILE_ID `1GUjxwK8bo6IPnQ_KQP7wujTrGBGIFZ94`.
Notebook URL: https://colab.research.google.com/drive/1GUjxwK8bo6IPnQ_KQP7wujTrGBGIFZ94
Cell execution via the Colab MCP fork verified (add/run/delete round-trip with output).
GPU recorded: Tesla T4, 15360 MiB (14910 free), torch 2.11.0+cu130, driver 580.82.07.

Storage round trip PASSED: file written+read on Drive at
`MyDrive/MBAX6418/Assignment4/joshua/run-0001/roundtrip.txt`; SHA-256
`cd78a3c86618c4972e98e8ec26b37ec004ecffb0300663153f547e85dc88fe06`
matches the local copy at
`…\Assignments\Assignment 4\artifacts\joshua\run-0001\roundtrip.txt`.

## Next gates

(a) Joshua reviews ~6 formatted training examples + the 3 few-shot picks,
(b) actual tokenizer length check vs max_seq_length=1024,
(c) then Phase 3 pilot-adapter save/reload test before final training.
