"""Genera los archivos de datos para fig_gibbs.tex.

Suma parcial de la serie de Fourier del tren periódico de pulsos
rectangulares con tau = T_0/4, T_0 = 1:

    hat_x_N(t) = 1/4 + sum_{k=1}^{N} (2 sin(k pi/4) / (k pi)) cos(2 pi k t)

Los términos con k múltiplo de 4 se anulan por sin(k pi/4) = 0.

Cada .dat tiene dos columnas separadas por espacios: t y hat_x_N(t).
"""

import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

N_VALUES = [5, 10, 20, 40, 80, 160]
T_MIN, T_MAX = 0.0, 0.25
N_SAMPLES = 1500


def partial_sum(t: np.ndarray, N: int) -> np.ndarray:
    y = np.full_like(t, 0.25)
    for k in range(1, N + 1):
        if k % 4 == 0:
            continue
        y += (2.0 * np.sin(k * np.pi / 4) / (k * np.pi)) * np.cos(2 * np.pi * k * t)
    return y


def main() -> None:
    t = np.linspace(T_MIN, T_MAX, N_SAMPLES)
    for N in N_VALUES:
        y = partial_sum(t, N)
        path = os.path.join(HERE, f"gibbs_N{N}.dat")
        with open(path, "w") as f:
            for ti, yi in zip(t, y):
                f.write(f"{ti:.6f} {yi:.6f}\n")
        print(f"escribí {path}  ({len(t)} puntos)")


if __name__ == "__main__":
    main()
