# QA-TRN-031 Mean kinetic temperature - worked guidance for reviewers

Training note, Quality Assurance. Version 2 (June 2025). Not a controlled procedure; QA-SOP-114 governs.

## Formula
MKT = (dH/R) / ( -ln( mean of exp(-dH/(R*Tk)) ) ) - 273.15

- Tk in kelvin: degC + 273.15.
- R = 8.3144 J/(mol K).
- dH: activation energy. The training example below uses 83.144 kJ/mol, so dH/R = 10 000 K, which makes the arithmetic easy.

## Worked example (training data only)
Six readings 5.0, 5.0, 6.0, 9.0, 5.0, 4.0 degC with dH/R = 10 000 K give MKT = 5.83 degC, against an arithmetic mean
of 5.67 degC. MKT always sits at or above the arithmetic mean because the exponential weights warm readings more.

## Points reviewers get wrong
1. Using the arithmetic mean instead of MKT.
2. Leaving readings in degF.
3. Rounding each reading before averaging (do not; round only the result).
4. Applying the training dH to every product. Products with an established activation energy use their own value.
5. Mixing loggers: a lot is judged on its own shipment's logger.
