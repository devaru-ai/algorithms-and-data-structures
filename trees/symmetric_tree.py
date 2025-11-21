from typing import Optional

# 1. TreeNode Class
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  def __str__(self):
    return str(self.val)

# 2. Your Solution
class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def same(root1, root2):
      # Both empty -> Symmetric
      if not root1 and not root2:
        return True
      # One empty, one not -> Asymmetric
      if not root1 or not root2:
        return False
      # Values don't match -> Asymmetric
      if root1.val != root2.val:
        return False
      
      # MIRROR CHECK:
      # Compare Left child of A with Right child of B
      # Compare Right child of A with Left child of B
      return same(root1.left, root2.right) and same(root1.right, root2.left)
    
    return same(root, root)

# --- TEST CASE 1: A Symmetric Tree ---
#       1
#     /   \
#    2     2
#   / \   / \
#  3   4 4   3

sym_root = TreeNode(1)
sym_root.left = TreeNode(2, TreeNode(3), TreeNode(4))
sym_root.right = TreeNode(2, TreeNode(4), TreeNode(3)) # Note the order: 4, 3

# --- TEST CASE 2: An Asymmetric Tree ---
#       1
#     /   \
#    2     2
#     \     \
#      3     3
# This is NOT symmetric because Node 2 (left) has right child 3,
# but Node 2 (right) has right child 3 (it needs to be a left child to match).

asym_root = TreeNode(1)
asym_root.left = TreeNode(2, None, TreeNode(3))
asym_root.right = TreeNode(2, None, TreeNode(3))

# --- RUN TESTS ---
solver = Solution()

print(f"Test 1 (Symmetric): {solver.isSymmetric(sym_root)} (Expected: True)")
print(f"Test 2 (Asymmetric): {solver.isSymmetric(asym_root)} (Expected: False)")
