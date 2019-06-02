import numpy as np

N = 4
M = 5
L = np.random.randint(1, 3)
K = np.random.randint(1, 3)

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))
# Разделение матрицы на 4 части и нахождение среднее арифметическое
x = A[0:L ,0:K]
x_sum = x.mean()
print("Вверхняя левая часть: среднее арифметическое = " + str(x_sum) + "\n" + str(x))
y = A[L: ,0 :K]
y_sum = y.mean()
print("\nНижняя левая часть: среднее арифметическое = " + str(y_sum) + "\n" + str(y))
z = A[0:L ,K:]
z_sum = z.mean()
print("\nВверхняя правая часть: среднее арифметическое = " + str(z_sum) + "\n" + str(z))
a = A[L: ,K:]
a_sum = a.mean()
print("\nНижняя правая часть: среднее арифметическое = " + str(a_sum) + "\n" + str(a))