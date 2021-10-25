class Node(object):
    def __init__(self, value=None, left=None, right=None, offset=None):
        self.value = value # значение корня узла
        self.left = left # левый дочерний узел
        self.right = right # правый дочерний узел
        self.offset = offset # номер строки
    
    def __str__(self):
      return str(self.value)


class Tree():

  def __init__(self):
    self.root = None

  def add(self, value):
    if self.root is None:
      self.root = Node(value)

  def add(self, val, off):
    if self.root is None:
        self.root = Node(val)
        self.offset = off
    else:
        self.__add(val, self.root, off)

  def __add(self, val, node, off):
    if val < node.value:
        if node.left is not None:
            self.__add(val, node.left, off)
        else:
            node.left = Node(val, offset = off)
    else:
        if node.right is not None:
            self.__add(val, node.right, off)
        else:
            node.right = Node(val, offset = off)

  def search(self,root, key):
    if root is None or root.value == key:
        return "Искомый хеш {} имеет оффсет (номер строки в файле) - {}".format(root, root.offset)
    if root.value < key:
        return self.search(root.right, key)
    return self.search(root.left, key)
