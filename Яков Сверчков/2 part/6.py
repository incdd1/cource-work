import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

Sum = A.sum()
B=np.sum(A)
M_sum = np.sum(A, axis=0)/np.sum(A)
A = np.vstack((A,M_sum))
print("Новая матрица:\r\n{}\n".format(A))

