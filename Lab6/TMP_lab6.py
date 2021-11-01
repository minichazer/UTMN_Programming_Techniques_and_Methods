import threading
from datetime import datetime
import random
import string

global_lock = threading.Lock()


def write_to_file(x):
    with global_lock:
        with open(f"{x}_output.txt", "w") as file:
            for i in range(100000):
                file.write(f"{x} - {''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=m))}\n")


def read_from_write_to(x):
    with global_lock:
        with open(f"{x}_output.txt", "r") as file_r, open(f"final_output.txt", "a") as file_w:
            file_w.write(''.join(file_r.readlines()))


threads = []
st = datetime.now()
n = int(input("Количество файлов: "))
m = int(input("Количество случайных букв латиницы: "))
print()

for i in range(n):
    t = threading.Thread(target=write_to_file(i))
    threads.append(t)
    t.start()
[thread.join() for thread in threads]
nd = datetime.now()
print(f"Потоки ({n}) завершили запись в файлы ({n}) за {(nd - st).total_seconds()} секунд\n")


with open(f"final_output.txt", "w") as f:
    f.write("Result:\n")


threads = []
st = datetime.now()

for i in range(n):
    t = threading.Thread(target=read_from_write_to(i))
    threads.append(t)
    t.start()
[thread.join() for thread in threads]
nd = datetime.now()
print(f"Потоки ({n}) завершили слияние из нескольких файлов ({n}) в 1 за {(nd - st).total_seconds()} секунд\n")
