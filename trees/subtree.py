from typing import Optional
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
 
class Solution:
  def isSubtree(self, root:Optional[TreeNode], subroot:Optional[TreeNode])->bool:
    def sameTree(p, q):
      if not p and not q:
        return True
      if (p and not q) or (q and not p):
        return False
      if p.val != q.val:
        return False
      return sameTree(p.left, q.left) and sameTree(p.right, q.right)

    def has_subtree(root):
      if not root:
        return False
      if sameTree(root, subroot):
        return True
      return has_subtree(root.left) or has_subtree(root.right)
    return has_subtree(root)


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

X = TreeNode(3)
Y = TreeNode(10)

X.left = Y

solver = Solution()
result = solver.isSubtree(A, X)

print(f"Subtree present: {result}")
