import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

iu = np.triu_indices(N, 1)
a = A[iu]
a = np.sum(np.array(a))
print("\nCумма элементов выше главной диагонали = " + str(a))
b = np.fliplr(A)[iu]
b = np.prod(np.array(b))
print("\nПроизведение элементов выше побочной диагонали = " + str(b))