#!/usr/bin/env python3
import argparse
import numpy as np
import matplotlib.pyplot as plt

def simulate_path(n=200, mu=(0.5, 0.5), sigma=0.2, seed=1):
    rng = np.random.default_rng(seed)
    steps = rng.normal(0.0, sigma, size=(n, 2)) + np.array(mu)[None, :]
    x = np.cumsum(steps, axis=0)
    # start at (0,0) by prepending a zero row for plotting convenience
    x = np.vstack([np.zeros((1,2)), x])
    return x

def main():
    p = argparse.ArgumentParser(description="Drift path demo for BCQM Primitives (2D biased random walk).")
    p.add_argument("--n", type=int, default=200, help="Number of steps")
    p.add_argument("--mu_x", type=float, default=0.5, help="Drift x-component")
    p.add_argument("--mu_y", type=float, default=0.5, help="Drift y-component")
    p.add_argument("--sigma", type=float, default=0.2, help="Jitter std. dev.")
    p.add_argument("--seed", type=int, default=1, help="RNG seed")
    p.add_argument("--save", type=str, default="fig_drift_path.png", help="Output PNG filename")
    args = p.parse_args()

    path = simulate_path(n=args.n, mu=(args.mu_x, args.mu_y), sigma=args.sigma, seed=args.seed)

    plt.figure(figsize=(6, 6))
    # Plot continuous path line
    plt.plot(path[:,0], path[:,1])
    # Overlay markers for each step (semi-transparent, default color)
    plt.plot(path[:,0], path[:,1], marker='o', linestyle='None', alpha=0.5, markersize=3)

    plt.title(f"Data-driven drift with jitter (n={args.n} steps)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.tight_layout()
    plt.savefig(args.save, dpi=150)
    # No plt.show() to keep headless execution happy

    print(f"Saved {args.save} (n={args.n}, mu=({args.mu_x},{args.mu_y}), sigma={args.sigma}, seed={args.seed})")

if __name__ == "__main__":
    main()
