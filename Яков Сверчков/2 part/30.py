import numpy as np

N = 4
M = 5
K = np.random.randint(1, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

M_n = np.sum(A, axis=0) * (-1)
A = np.vstack((A, M_n))

print("Новая матрица:\r\n{}\n".format(A))