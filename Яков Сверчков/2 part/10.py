import numpy as np

N = 4
M = 5
K = np.random.randint(1, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

K_arr = np.array(A[:, K-1])
K_arr = K_arr[: , np.newaxis]
print("K-ый столбец: \r\n{}\n".format(K_arr))
A = A * K_arr

print("Новая матрица:\r\n{}\n".format(A))