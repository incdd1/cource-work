import numpy as np

N = 4
M = 5
H = np.random.randint(1, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

bool = A == H
col_sum = np.sum(bool, axis=1)

print("Строки в которых встречается значение {}:".format(H))
print(np.argwhere(col_sum).flatten())
print("Строки в которых нет значения {}:".format(H))
print(np.argwhere(col_sum == 0).flatten())