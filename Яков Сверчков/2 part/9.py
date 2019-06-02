import numpy as np

N = 4
M = 5
L = np.random.randint(0, 3)
K = np.random.randint(0, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

n = 0
for i in range(0, L):
    for j in range(0, M):
        if A[i,j] == 0:
            n += 1
print("Количество нулевых элементов в верхних L солбцах: {}\n".format(n))
m = 0
for i in range(0, K):
    for j in range(0, N):
        if A[j,i] == 0:
            m += 1
print("Количество нулевых элементов в левых L солбцах: {}\n".format(m))