from random import randint

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]       
        right = [x for x in arr[1:] if x >= pivot]
        return quickSort(left) + [pivot] + quickSort(right)
    
arr = []
for i in range(10):
    bil = randint(0,100)
    arr.append(bil)

print(f"Sebelum di QuickSort {arr}")

result = quickSort(arr)

print(f"Setelah di QuickSort {result}")