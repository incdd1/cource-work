import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

bool = A == 0
col = np.sum(bool, axis=1)
A = np.insert(A, M, col, axis=1)
row = np.append(np.sum(bool, axis=0), 0)
A = np.insert(A, N, row, axis=0)
print("Новая матрица:\r\n{}\n".format(A))