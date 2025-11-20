from typing import Optional
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isvalidBST(self, root: Optional[TreeNode]) -> bool:
    def is_valid(node, minn, maxx):
      if not node:
        return True
      if node.val <= minn or node.val >=maxx:
        return False
      return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)
    return is_valid(root, float('-inf'), float('inf'))

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

solver = Solution()
result = solver.isvalidBST(A)

print(f"Validity of BST: {result}")
