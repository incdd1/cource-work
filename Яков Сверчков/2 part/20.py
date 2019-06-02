import numpy as np

N = 4
M = 5

A = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}\n".format(A))

a = b = np.fliplr(A).diagonal(1)
a_prod = a.prod()
print("Элементы которые выше побочной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_prod))
b = np.fliplr(A).diagonal(-1)
b_prod = b.prod()
print("Элементы которые ниже побочной диагонали: \n" + str(b) + "\nИх сумма = " + str(b_prod))