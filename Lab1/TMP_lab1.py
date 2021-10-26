from random import randint
from statistics import median


class Node(object):
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
      return str(self.value)


class Tree():

  def __init__(self):
    self.root = None

  def add(self, value):
    if self.root is None:
      self.root = Node(value)

  def add(self, val):
    if self.root is None:
        self.root = Node(val)
    else:
        self.__add(val, self.root)

  def __add(self, val, node):
    if val < node.value:
        if node.left is not None:
            self.__add(val, node.left)
        else:
            node.left = Node(val)
    else:
        if node.right is not None:
            self.__add(val, node.right)
        else:
            node.right = Node(val)
  

  # реализация генерации массива сверху-вниз слева-направо с помощью двух очередей
  def printw_queue(self, layerc):
    queue_1 = []
    queue_2 = [self.root]
    result_array = []
   
    while True:     
      for i in queue_2:
        if i is not None:      
          queue_1.append(i.left)
          queue_1.append(i.right)
      
      queue_1, queue_2 = queue_2, queue_1

      for i in queue_1:
        if i is not None:  
          result_array.append(i.value)
          
      queue_1 = []

      if len(queue_2) == 0:
        break
      
    spaces = [2**i for i in range(layerc)] # сколько элементов будет в слое для стандартного бинарного дерева
    result_array.insert(0, 0) 
    input_level = 1 # уровень вхождения по дереву; с переходом на новый слой дерева переменная += 1

    with open('result.txt', 'w') as f:
      for i in spaces:
        for j in range(i):

          tab_before = (2**(layerc - input_level + len(str(randint_spacecalc)))) // 2
          tab_between = (2**(layerc - input_level + len(str(randint_spacecalc))) - 1) // 2
          
          f.write(" " * tab_before)
          printvar = result_array[i:][j]
          isminus = 1 if "-" in str(printvar) else 0

          # измеряю доп расстояние, если элемент отклоняется от медианного и содержит в себе минус
          if len(str(printvar)) >= len(str(randint_spacecalc)):
            f.write(str(printvar) + " " * (tab_between + (len(str(printvar)) - len(str(randint_spacecalc)))) + " " * isminus)
          else:
            f.write(str(printvar) + " " * tab_between + " " * isminus)

        input_level += 1
        f.write("\n")

if __name__ == "__main__":

  tree = Tree()
  layerc = int(input("Количество уровней дерева: "))
  randint_lower, randint_upper = -100, 100

  # медианная диапазона
  randint_spacecalc = median([abs(i) for i in range(randint_lower, randint_upper)])

  for i in range(2**layerc - 1):
    tree.add(randint(randint_lower, randint_upper))

  tree.printw_queue(layerc)
