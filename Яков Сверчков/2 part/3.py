import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(A))

sum = A.sum(axis=0)
index = sum.argmin(axis=0)
min = A.min(axis=0)
min = min[index]

print("Наименьшее значение: {}".format(min))