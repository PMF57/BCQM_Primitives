# Data-Driven Drift with Jitter (BCQM Primitives)

This demo generates a short 2D path that exhibits **inertia-like straight-line drift with jitter**,
matching the "Data-driven drift with jitter (n=200 steps)" figure in the BCQM Primitives note.

## Model
We use a biased 2D random walk:
```
x_{t+1} = x_t + μ + ε_t
```
- `μ` is a constant drift vector (e.g., `[dx, dy]` with `dx, dy > 0`).
- `ε_t ~ N(0, σ^2 I)` is isotropic jitter.

With small `σ` and `μ` pointing to the northeast, the path clusters in the **top-right** of the plot,
illustrating steady drift with noise.

## Usage
```bash
python drift_path_demo.py --n 200 --mu_x 0.5 --mu_y 0.5 --sigma 0.2 --seed 1 --save fig_drift_path.png
```
- `--n` number of steps (default: 200)
- `--mu_x, --mu_y` drift components (default: 0.5, 0.5)
- `--sigma` jitter standard deviation (default: 0.2)
- `--seed` RNG seed (default: 1)
- `--save` output PNG filename (default: `fig_drift_path.png`)

The script outputs a single figure with the path and faint markers. It uses only NumPy and Matplotlib,
and does not set any custom colors.
