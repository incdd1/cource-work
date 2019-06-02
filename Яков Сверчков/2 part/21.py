import numpy as np

N = 4
M = 4

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

B = (A + A.T)/2
print("Новая матрица:\r\n{}\n".format(B))