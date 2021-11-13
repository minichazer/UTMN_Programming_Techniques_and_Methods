from random import randint

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        is_sorted = True

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False

        if is_sorted:
            break
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1 

        arr[j + 1] = temp
    return arr


def quicksort(arr):
    if len(arr) < 2:
        return arr

    low, same, high = [], [], []
    pivot = arr[randint(0, len(arr) - 1)]

    for i in arr:
        if i < pivot:
            low.append(i)
        elif i == pivot:
            same.append(i)
        elif i > pivot:
            high.append(i)
    return quicksort(low) + same + quicksort(high)

def selection_sort(arr):
    for i in range(len(arr)):
        min_value_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value_index]:
                min_value_index = j
        arr[i], arr[min_value_index] = arr[min_value_index], arr[i]
