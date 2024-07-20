#! /usr/bin/env python3

import argparse
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path
from typing import Optional


def save_as_waveform_file(t: np.array, v: np.array, output_path: Optional[Path] = None):
    output_path = output_path or Path("./pwl_guess.txt")
    with open(output_path, "w") as f:
        for tt, vv in zip(t, v):
            f.write(f"{tt} {vv}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-path", type=Path)
    parser.add_argument("--plot", action="store_true", default=False)
    args = parser.parse_args()

    # https://www.desmos.com/calculator/lvxrwjouzm
    A = 1.6
    f = 100
    s = 1
    m = -0.3

    t = np.linspace(0.0001, 5, 10000)
    v = A * np.power(np.sin(f * t), 2) * np.exp(-np.power(np.log(t) - m, 2) / (2 * s ** 2)) / (t * s * np.sqrt(2 * np.pi))

    if args.plot:
        plt.plot(t,v)
        plt.show()

    save_as_waveform_file(t, v, output_path=args.output_path)
