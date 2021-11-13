from algorithms import bubble_sort, insertion_sort, quicksort, selection_sort
from random import randint
from datetime import datetime
import os
import psutil


def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss
 
 
def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory()
        start = datetime.now()
        result = func(*args, **kwargs)
        exec_time = (datetime.now() - start).total_seconds()
        mem_after = get_process_memory() - mem_before
        print(f"Функция {func.__name__}: затрачено памяти на работу: {mem_after}, время на выполнение: {exec_time}\n")
        return result
    return wrapper


bubble_sort = profile(bubble_sort)
insertion_sort = profile(insertion_sort)
quicksort = profile(quicksort)
selection_sort = profile(selection_sort)


if __name__ == '__main__':

    a = [randint(-2048, 2048) for i in range(1000)]

    bubble_sort(a[:])
    insertion_sort(a[:])
    quicksort(a[:])
    selection_sort(a[:])
