import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

Sum = A.sum()
print("Сумма элементов всей матрицы: " + str(Sum) + "\n")
Sum_column = A.sum(axis=1)
X = []
for i in range(0, N):
    n = Sum_column[i] / Sum
    X.append(n)
X = np.array(X)[: , np.newaxis]
A = np.hstack((A, X))

print(A)