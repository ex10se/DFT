import numpy as np
from sympy import fft


def DFT(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)


def FFT(x):
    return fft(x)


# Sequence
sequence = [1, 2, 3, 4, 5, 6, 7, 8]

print("Последовательность: ", sequence)
print("ДПФ\n", DFT(sequence))
print("БПФ\n", FFT(sequence))
