import numpy as np

N = 4
M = 5
L = np.random.randint(1, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

L_arr = np.array(A[L-1, :])
print("L страка: \r\n{}\n".format(L_arr))
A = A + L_arr

print("Новая матрица:\r\n{}\n".format(A))