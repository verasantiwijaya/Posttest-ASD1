from random import randint

def merge_sort (array):
    if len(array) > 1:
        mid = len(array) // 2
        left_arr = array[:mid]
        right_arr = array [mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0       

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
                # k += 1
            else:
                array[k] = right_arr[j]
                j += 1
                # k += 1
            k += 1

        while (i < len(left_arr)):
            array[k] = left_arr[i]
            i += 1
            k += 1
        
        while (j < len(right_arr)):
            array[k] = right_arr[j]
            j += 1
            k += 1

array = []
for i in range(10):
    bil = randint(0,100)
    array.append(bil)


print("Sebelum di MergeSort", array)

merge_sort(array)
print("Setelah di MergeSort", array)