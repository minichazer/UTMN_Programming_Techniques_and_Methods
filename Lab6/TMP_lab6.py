from datetime import datetime
import random
import string
from multiprocessing.dummy import Pool as ThreadPool


def write_to_file(x):
    with open(f"{x}_output.txt", "w") as file:
        for i in range(100000):
            file.write(f"{x} - {''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=m))}\n")


def read_from_write_to(x):
    with open(f"{x}_output.txt", "r") as file_r, open(f"final_output.txt", "a") as file_w:
        file_w.write(''.join(file_r.readlines()))


def calculate_timings(func, n):
    st = datetime.now()
    results = pool.map(func, [i for i in range(1, n + 1)])
    return (datetime.now() - st).total_seconds()


n = int(input("Количество файлов: "))
m = int(input("Количество случайных букв латиницы: "))
pool = ThreadPool(n)


print(f"Потоки ({n}) завершили запись в файлы ({n}) за {calculate_timings(write_to_file, n)} секунд\n")
print(f"Потоки ({n}) завершили чтение из файлов ({n}) в один за {calculate_timings(read_from_write_to, n)} секунд\n")
