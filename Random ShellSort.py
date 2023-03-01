from random import randint

def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

data = []
for i in range(10):
    bil = randint(0,100)
    data.append(bil)

print("Sebelum di ShellSort:", data)

size = len(data)
shellSort(data, size)

print("Setelah di ShellSort:", data)
