from collections import deque

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.val)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D 
B.right = E
C.left = F

def pre_order(node):
  if not node:
    return
  print(node)
  pre_order(node.left)
  pre_order(node.right)

def in_order(node):
  if not node:
    return
  in_order(node.left)
  print(node)
  in_order(node.right)

def post_order(node):
  if not node:
    return
  post_order(left)
  post_order(right)
  print(node)

# Iterative pre order
def iterative_pre_order(node):
  stk = [node]
  while stk:
    node = stk.pop()
    if node.right: stk.append(node.right)
    if node.left: stk.append(node.left)
    print(node)
    
def level_order(node):
  q = deque()
  q.append(node)
  while q:
    node = q.popleft()
    print(node)
    if node.left: q.append(node.left)
    if node.right: q.append(node.right)

def search_bst(node, target):
  if not node:
    return False
  if node.val == target:
    return True
  if target < node.val: return search_bst(node.left, target)
  else: return search_bst(node.right, target)














  
