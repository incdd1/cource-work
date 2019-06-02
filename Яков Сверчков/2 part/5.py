import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

Average_line = A.mean(axis=1)
Average_column = A.mean(axis=0)
Average_line = Average_line[: , np.newaxis]
A = np.hstack((A, Average_line))
Average_column = np.hstack((Average_column, [0.]))
A = np.vstack((A, Average_column))

print("Новая матрица:\r\n{}\n".format(A))