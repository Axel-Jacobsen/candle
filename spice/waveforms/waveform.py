#! /usr/bin/env python3

import argparse
import numpy as np

from pathlib import Path
from typing import Optional


def save_as_waveform_file(t: np.array, v: np.array, output_path: Optional[Path] = None):
    output_path = output_path or Path("./pwl_guess.txt")
    with open(output_path, "w") as f:
        for tt, vv in zip(t, v):
            f.write(f"{tt} {vv}\n")



if __name__ == "__main__":
    parser = argarse.ArgumentParser()
    parser.add_argument("--output-path", type=Path)
    args = parser.parse_args()

    t = np.linspace(0, 3, 10000)
    v = 2 * np.exp(-2 * t) * np.sin(10 * np.pi * t)
    save_as_waveform_file(t, v, output_path=args.output_path)
