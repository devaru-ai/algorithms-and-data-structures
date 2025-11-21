from typing import Optional
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
 
class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    count = [k]
    ans = [0]

    def dfs(node):
      if not node:
        return
      
      dfs(node.left)

      if count[0] == 1:
        ans[0] = node.val

      count[0] = count[0] - 1
      if count[0] > 0:
        dfs(node.right)
    dfs(root)
    return ans

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
result = solver.kthSmallest(A, 5)

print(f"kth Smallest element: {result}")
