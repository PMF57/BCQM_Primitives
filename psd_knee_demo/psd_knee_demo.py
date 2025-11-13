#!/usr/bin/env python3
import argparse
import numpy as np
import matplotlib.pyplot as plt

def simulate_ar1(N, a, sigma=1.0, seed=0):
    rng = np.random.default_rng(seed)
    eps = rng.normal(0.0, sigma, size=N)
    x = np.zeros(N, dtype=float)
    for t in range(1, N):
        x[t] = a * x[t-1] + eps[t]
    return x

def main():
    p = argparse.ArgumentParser(description="PSD knee demo for BCQM Primitives (AR(1) time series).")
    p.add_argument("--W", type=float, default=50.0, help="Coherence horizon W_coh (in samples).")
    p.add_argument("--N", type=int,   default=16384, help="Number of samples.")
    p.add_argument("--seed", type=int, default=0,    help="RNG seed.")
    p.add_argument("--save", type=str, default="example_output.png", help="Output PNG filename.")
    args = p.parse_args()

    # Map W_coh -> AR(1) parameter a ~ 1 - 2π / W_coh
    if args.W <= 0:
        raise SystemExit("W must be positive.")
    a = 1.0 - (2.0 * np.pi) / args.W
    if a <= 0.0:
        # Too small W_coh -> no correlation; fall back to white noise
        a = 0.0

    x = simulate_ar1(args.N, a, sigma=1.0, seed=args.seed)
    x = x - np.mean(x)

    # PSD via rFFT
    X = np.fft.rfft(x)
    psd = (np.abs(X)**2) / len(x)
    freqs = np.fft.rfftfreq(len(x), d=1.0)  # cycles per sample

    # Estimate knee frequency from W
    f_knee = 1.0 / args.W

    plt.figure(figsize=(7, 5))
    plt.loglog(freqs[1:], psd[1:], label="PSD")  # skip DC
    plt.axvline(f_knee, linestyle="--", label="1/W_coh")
    plt.title("PSD with Knee near 1/W_coh (AR(1) demo)")
    plt.xlabel("Frequency (cycles/sample)")
    plt.ylabel("Power")
    plt.legend()
    plt.tight_layout()
    plt.savefig(args.save, dpi=150)
    # no plt.show() in headless run

    print(f"W_coh={args.W:.3f}, a={a:.6f}, knee≈{f_knee:.6f} cycles/sample; saved {args.save}")

if __name__ == '__main__':
    main()
