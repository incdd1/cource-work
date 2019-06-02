import numpy as np

file = open('nympy-gauss-slau.csv', 'wb+')
file.truncate()
for i in range(1, 6):
    task_file = "slau_" + str(i) + ".csv"

    m = np.genfromtxt(task_file, delimiter=';')
    myA = np.genfromtxt(task_file, delimiter=';', usecols=(range(len(m-1))))
    myB = np.genfromtxt(task_file, delimiter=';', usecols=(len(m)))

    print("Система " + str(i))
    print("Матрица A: \n" + str(myA))
    print("Матрица B: \n" + str(myB))

    slau = np.linalg.solve(myA, myB)

    print("Решение ", slau)
    np.savetxt(file, np.array([slau]), delimiter=',')
file.close()