import numpy as np

N = 4
M = 5
K = np.random.randint(1, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))
print("K = " + str(K))
A = np.delete(A, (K-1), axis=1)
print("Новая матрица:\r\n{}\n".format(A))
