from typing import Optional
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def maxDepth(self, root:Optional[TreeNode]) -> int:
    if not root:
      return 0
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return 1 + max(left, right)

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
result = solver.maxDepth(A)

print(f"The Maximum Depth of the tree is: {result}")
