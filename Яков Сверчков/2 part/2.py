import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(A))

Average = A.mean(axis=1)
index = Average.argmax(axis=0)
max = Average.max(axis=0)

print("Наибольшее среднее значение: {}".format(max))