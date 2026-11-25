# Tokens per update — worksheet (draft, Emeka, 13 Nov)

| Run | Effective batch | Seq len | Tokens/update | Recipe tokens/update | Change |
|---|---|---|---|---|---|
| FT-CLM-07 | 512 | 4096 | 2,097,152 | 2,097,152 | +0.0% |
| FT-UW-03 | 256 | 2048 | 524,288 | 524,288 | +0.0% |
| FT-FNOL-11 | 128 | 2560 | 327,680 | 262,144 | +25.0% |
| FT-SUB-02 | 256 | 4096 | 1,048,576 | 1,048,576 | +0.0% |

Effective batch here is micro-batch x accumulation x GPUs from the registry rows.
FNOL-11 is the only one over 10%; LR becomes 3.0e-5 x sqrt(1.25) = 3.35e-5 (three significant figures).
