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
      
    spaces = [2**i for i in range(layerc)]
    result_array.insert(0, 0) 
    input_level = 1

    with open('result.txt', 'w') as f:
      for i in spaces:
        for j in range(i):

          tab_before = (2**(layerc - input_level + len(str(randint_spacecalc)))) // 2
          tab_between = (2**(layerc - input_level + len(str(randint_spacecalc))) - 1) // 2
          
          f.write(" " * tab_before)
          printvar = result_array[i:][j]
          isminus = 1 if "-" in str(printvar) else 0

          if len(str(printvar)) >= len(str(randint_spacecalc)):
            f.write(str(printvar) + " " * (tab_between + (len(str(printvar)) - len(str(randint_spacecalc)))) + " " * isminus)
          else:
            f.write(str(printvar) + " " * tab_between + " " * isminus)

        input_level += 1
        f.write("\n")


if __name__ == "__main__":

  print("Creating new tree ...")
  tree = Tree()
  layerc = 4
  randint_lower, randint_upper = -100, 100

  print("Calculating spaces for tree ...")
  randint_spacecalc = median([abs(i) for i in range(randint_lower, randint_upper)])

  print("Filling the tree with random elements in range of [-100;100] ...")
  for i in range(2**layerc - 1):
    tree.add(randint(randint_lower, randint_upper))

  print("Printing the tree to the output file result.txt ...")
  tree.printw_queue(layerc)