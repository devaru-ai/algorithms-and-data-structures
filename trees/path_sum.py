from typing import Optional
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def has_sum(root, cur_sum):
      if not root:
        return False
      cur_sum += root.val
      if not root.left and not root.right:
        return cur_sum == targetSum
      return has_sum(root.left, cur_sum) or has_sum(root.right, cur_sum)
    return has_sum(root, 0)

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
result = solver.hasPathSum(A, 14)

print(f"PathSum == TargetSum: {result}")
