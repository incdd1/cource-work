import numpy as np

N = 4
M = 5
L = np.random.randint(1, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

print("L = " + str(L))
A = np.delete(A, (L-1), axis=0)

print("Новая матрица:\r\n{}\n".format(A))