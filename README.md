# BCQM-Programs · Primitives Demos

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17513408.svg)](https://doi.org/10.5281/zenodo.17513408)
<sub>**All versions (concept DOI).** For exact reproducibility of this release, cite the version DOI: [10.5281/zenodo.17513409](https://doi.org/10.5281/zenodo.17513409).</sub>

Minimal, self-contained demos that accompany the paper  
**“BCQM Primitives and the Emergence of Spacetime (Foundational Note v1.0)”** · DOI: [10.5281/zenodo.17495038](https://doi.org/10.5281/zenodo.17495038)

---

## Contents

- `psd_knee_demo/`
  - `psd_knee_demo.py` — generates a 1D “tick/jitter” time series (AR(1)) with a **PSD knee** near `1/W_coh`
  - `README.md`, `example_output.png`
- `data_drift_demo/`
  - `drift_path_demo.py` — 2D drift-with-jitter path; trajectory **clusters in the top-right** (NE) quadrant
  - `README.md`, `fig_drift_path.png`

## Quick start

### Requirements
- Python 3.9+  
- `numpy`, `matplotlib`

Install:
```bash
pip install -r requirements.txt
# or:
pip install numpy matplotlib
```

### Run the demos

**PSD knee (default W_coh=50):**
```bash
python primitives/psd_knee_demo/psd_knee_demo.py --W 50 --N 16384 --seed 0 --save primitives/psd_knee_demo/example_output.png
```

**Drift with jitter (n=200, μ=(0.5,0.5), σ=0.2):**
```bash
python primitives/data_drift_demo/drift_path_demo.py --n 200 --mu_x 0.5 --mu_y 0.5 --sigma 0.2 --seed 1 --save primitives/data_drift_demo/fig_drift_path.png
```

> Each script produces **one** Matplotlib figure (no custom colors) and saves a PNG.

## Repro tips

- For CI or batch regen, use a simple `Makefile`:
  ```makefile
  all: primitives/psd_knee_demo/example_output.png primitives/data_drift_demo/fig_drift_path.png

  primitives/psd_knee_demo/example_output.png:
  	python primitives/psd_knee_demo/psd_knee_demo.py --W 50 --N 16384 --seed 0 --save $@

  primitives/data_drift_demo/fig_drift_path.png:
  	python primitives/data_drift_demo/drift_path_demo.py --n 200 --mu_x 0.5 --mu_y 0.5 --sigma 0.2 --seed 1 --save $@
  ```
- Prefer the **version DOI** when citing a specific archived release; use the **concept DOI** for a link that always resolves to the latest.

## Citation

**Software (this release):**  
Ferguson, P. M. *BCQM-Programs: Primitives demos.* Zenodo (software). DOI: [10.5281/zenodo.17513409](https://doi.org/10.5281/zenodo.17513409).  
**All versions:** [10.5281/zenodo.17513408](https://doi.org/10.5281/zenodo.17513408)

**Paper:**  
Ferguson, P. M. *Boundary-Condition Quantum Mechanics (BCQM): Primitives and the Emergence of Spacetime (Foundational Note v1.0).* Zenodo (publication). DOI: [10.5281/zenodo.17495038](https://doi.org/10.5281/zenodo.17495038)

## Related works

- **BCQM I — Boundary-Condition Quantum Mechanics (BCQM)** · DOI: 10.5281/zenodo.17191306  
- **Analytical Proofs for BCQM** · DOI: 10.5281/zenodo.17242311  
- **BCQM II — Boundary-Condition Quantum Mechanics II** · DOI: 10.5281/zenodo.17398294

## License

MIT (or your chosen license). If you prefer a different license, update `LICENSE` and `.zenodo.json` accordingly.
