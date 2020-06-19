import numpy as np


def DFT(x):
    x = np.asarray(x, dtype=float)       # Представить в виде массива
    N = x.shape[0]                       # Длина массива
    n = np.arange(N)                     # Заполнение массива числами от 0 до 7
    k = n.reshape((N, 1))                # Транспонирование массива
    M = np.exp(-2j * np.pi * k * n / N)  # Вычисление по формуле ДПФ
    return np.dot(M, x)                  # Скалярное произведение массивов


# Sequence
sequence = [1, 2, 3, 4, 5, 6, 7, 8]

print(DFT(sequence))
