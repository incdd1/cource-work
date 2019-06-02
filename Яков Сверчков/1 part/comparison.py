import random
import algorithms

DIM = 40
bubble_arr = []
insert_arr = []
select_arr = []

CTotal = [0, 0, 0]
MTotal = [0, 0, 0]

for i in range(1, DIM+1):
    select_arr.append(i)
    bubble_arr.append(i)
    insert_arr.append(i)

myfile = open("sort_methods.txt", "w") # Все результаты запишем в файл

print("\nУПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ: Исходный массив")
print(select_arr)

count = [0, 0]
count = algorithms.select(select_arr, DIM)
print("\nУПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ: Результирующий массив")
print(select_arr)
CTotal[0] = count[0]
MTotal[0] = count[1]

count = [0, 0]
count = algorithms.insert(insert_arr, DIM)
CTotal[1] = count[0]
MTotal[1] = count[1]

count = [0, 0]
count = algorithms.bubble(bubble_arr, DIM)
CTotal[2] = count[0]
MTotal[2] = count[1]
print("УПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ:\n")
print("Размер массива: ", DIM)
print("Сравнений:    ", CTotal[0], " ", CTotal[1], " ", CTotal[2])
print("Перестановок: ", MTotal[0], " ", MTotal[1], " ", MTotal[2])


select_arr.clear()
bubble_arr.clear()
insert_arr.clear()

for i in range(DIM, 0, -1):
    select_arr.append(i)
    bubble_arr.append(i)
    insert_arr.append(i)

print("\nОБРАТНО УПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ: Исходный массив")
print(select_arr)

count = [0, 0]
count = algorithms.select(select_arr, DIM)
print("\nОБРАТНО УПОРЯДОЧЕННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ: Результирующий массив")
print(select_arr)
CTotal[0] = count[0]
MTotal[0] = count[1]

count = [0, 0]
count = algorithms.insert(insert_arr, DIM)
CTotal[1] = count[0]
MTotal[1] = count[1]

count = [0, 0]
count = algorithms.bubble(bubble_arr, DIM)
CTotal[2] = count[0]
MTotal[2] = count[1]
print("Размер массива: ", DIM)
print("Сравнений:    ", CTotal[0], " ", CTotal[1], " ", CTotal[2])
print("Перестановок: ", MTotal[0], " ", MTotal[1], " ", MTotal[2])


NUM = 1500
CTotal.clear()
MTotal.clear()

CTotal = [0, 0, 0]
MTotal = [0, 0, 0]

for n in range(0, NUM):

    select_arr.clear()
    bubble_arr.clear()
    insert_arr.clear()

    select_arr = [random.randint(0, 100) for i in range(DIM)]
    for i in range(0, DIM):
        bubble_arr.append(select_arr[i])
        insert_arr.append(select_arr[i])

    count = [0, 0]
    count = algorithms.select(select_arr, DIM)
    CTotal[0] += count[0]
    MTotal[0] += count[1]

    count = [0, 0]
    count = algorithms.insert(insert_arr, DIM)
    CTotal[1] += count[0]
    MTotal[1] += count[1]

    count = [0, 0]
    count = algorithms.bubble(bubble_arr, DIM)
    CTotal[2] += count[0]
    MTotal[2] += count[1]

print("\nСЛУЧАЙНАЯ РЕАЛИЗАЦИЯ:")
print("Проведено экспериментов: ", NUM)
print("Размер массива: ", DIM)
print("Сравнений:    ", CTotal[0]/NUM, " ", CTotal[1]/NUM, " ", CTotal[2]/NUM)
print("Перестановок: ", MTotal[0]/NUM, " ", MTotal[1]/NUM, " ", MTotal[2]/NUM)