#! /usr/bin/env python3

import argparse
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from typing import Optional


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--output-path", type=Path, default=Path("./spice/waveforms/pwl_guess.txt")
    )
    parser.add_argument("-N", type=int, default=10000, help="number of points in plot")
    parser.add_argument("-A", type=float, default=1.6, help="amplitude of wave (before noise)")
    parser.add_argument("-f", type=float, default=80.0, help="frequency of the wave")
    parser.add_argument("-s", type=float, default=1.0, help="std. dev of the gaussians")
    parser.add_argument("-m", type=float, default=0.3, help="mean of the gaussians")
    parser.add_argument("--noise", type=float, default=0.1, help="variance of the noise")
    parser.add_argument("--plot", action="store_true", default=False, help="show the plot")
    args = parser.parse_args()

    # https://www.desmos.com/calculator/lvxrwjouzm
    V = lambda t: (
        args.A
        * (np.random.randn(t.size) * args.noise + 1)
        * np.power(np.sin(2 * np.pi * args.f * t), 2)
        * np.exp(-np.power(np.log(t) - args.m, 2) / (2 * args.s**2))
        / (t * args.s * np.sqrt(2 * np.pi))
    )

    t = np.linspace(0.0001, 10, args.N)
    t_first = np.linspace(0.0001, 5, args.N // 2)
    v_fin = np.concatenate([V(t_first), V(t_first)])

    if args.plot:
        plt.xlabel("t")
        plt.ylabel("V")
        plt.plot(t, v_fin)
        plt.show()

    with open(args.output_path, "w") as f:
        for tt, vv in zip(t, v_fin):
            f.write(f"{tt} {vv}\n")
