from random import seed, choice
from datetime import datetime
import hashlib
import time

from binary_tree2 import Tree, Node


def genstring(n = 10):
    a = [choice(data) for i in range(n)]
    return "".join(a)


#seed(1)
seed(datetime.now())
hash_tree = Tree()
data = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\()*+,-./:;<=>?@[\\]^_`{|}~' + "'"
temp_hash_tree = []


with open('strings.txt', 'w') as f:
    for i in range(10000):
        output = genstring(40)
        outhash = hash(output) % 10**8
        temp_hash_tree.append(outhash)
        f.write("{} - {}\n".format(output, outhash))

    hash_tree.root = Node(temp_hash_tree[0], offset = 1)
    temp_hash_tree.pop(0)

    for i in range(len(temp_hash_tree)):
        hash_tree.add(temp_hash_tree[i], off = i + 2)
        f.write("{}\n".format(temp_hash_tree[i]))


print("{} - его оффсет = {}".format(hash_tree.root.value, hash_tree.root.offset))
print("{} - его оффсет = {}".format(hash_tree.root.left.value, hash_tree.root.left.offset))
print("{} - его оффсет = {}".format(hash_tree.root.right.value, hash_tree.root.right.offset))
print()


sf = []
for i in range(100):
    sf.append(choice(temp_hash_tree))


print("Будем искать следующие хеши: ", sf)


print("Поиск по дереву:")
start = time.process_time()
for i in range(len(sf)):
    print(hash_tree.search(root = hash_tree.root, key = sf[i]))
print("На поиск данных хешей в бинарном дереве ушло: ", time.process_time() - start)


print("Поиск по файлу:")
f = open('strings.txt').readlines()
start2 = time.process_time()
for i in range(len(sf)):
    j = 1
    for line in f:
        if line.find(str(sf[i])) > 0 :
            break
        else:
            j += 1
print("На поиск хешей напрямую в файле ушло: ", time.process_time() - start2)
