# PSD Knee Demo (BCQM Primitives)

This minimal demo generates a 1D “tick/jitter” time series with an AR(1) process
whose power spectral density (PSD) exhibits a **knee** at approximately `f_knee ≈ 1/W_coh`.
It is intended as a lightweight, reproducible companion for the *BCQM Primitives* note.

## How it works
We simulate an AR(1) process
```
x[t] = a * x[t-1] + ε[t],  with  ε ~ N(0, σ²)
```
Choosing
```
a = 1 - 2π / W_coh
```
(for `W_coh` large enough that `a ∈ (0,1)`)
yields a low-pass PSD with a knee at roughly `f_knee ≈ (1 - a) / (2π) ≈ 1 / W_coh` (cycles per sample).

## Usage
```bash
python psd_knee_demo.py --W 50 --N 16384 --seed 0 --save example_output.png
```
- `--W` is the coherence horizon `W_coh` in *samples* (default: 50).
- `--N` is the number of samples (default: 16384).
- `--seed` seeds the RNG for reproducibility (default: 0).
- `--save` path to save the PNG (also shows the plot interactively if a display is available).

The figure shows the PSD on log–log axes and a vertical marker at `1/W_coh`.

## Notes
- No external dependencies beyond NumPy and Matplotlib.
- One plot per figure; no custom colors set.
- The series is mean-removed before the FFT-based PSD estimate.
- If `W_coh ≤ 2π`, the process defaults to white noise (no knee), which is expected.

## License
MIT (or your preferred; update as needed).
