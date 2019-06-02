import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(A))

sum = A.sum(axis=0)
index = sum.argmax(axis=0)
max = A.max(axis=0)
max = max[index]

print("Наибольшее значение: {}".format(max))