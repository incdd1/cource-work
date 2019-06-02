def select(arr, dim):
    k = 0
    alg_count = [0, 0]

    for k in range(0, dim - 1):
        m = k
        i = k + 1
        for i in range(i, dim):
            alg_count[0] += 1
            if arr[i] < arr[m]:
                m = i
        if k != m:
            t = arr[k]
            arr[k] = arr[m]
            arr[m] = t
            alg_count[1] += 1
    return alg_count



def insert(arr, dim):
    alg_count = [0, 0]

    for i in range(1, dim):
        temp = arr[i]
        j = i - 1
        while j >= 0:
            alg_count[0] += 1
            if arr[j] > temp:
                alg_count[1] += 1
                arr[j + 1] = arr[j]
                arr[j] = temp
            j -= 1
    return alg_count


def bubble(arr, dim):
    n = 1
    alg_count = [0, 0]

    while n < dim:
        for i in range(dim - n):
            alg_count[0] += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                alg_count[1] += 1
        n += 1
    return alg_count