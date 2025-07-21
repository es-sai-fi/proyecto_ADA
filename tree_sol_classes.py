from auxiliar_functions import *

class Tree:
  def __init__(self, root, nodes):
    self.root = root
    self.nodes = nodes
  
class Node:
  def __init__(self, parent, left, right, key):
    self.parent = parent
    self.left = left
    self.right = right
    self.key = key
