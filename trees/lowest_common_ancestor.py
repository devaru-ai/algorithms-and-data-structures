from typing import Optional
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def lca(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode:
    lca = [root]
    def search(root):
      if not root:
        return
      lca[0] = root
      if root is p or root is q:
        return
      elif root.val < p.val and root.val < q.val:
        search(root.right)
      elif root.val > p.val and root.val > q.val:
        search(root.left)
      else:
        return
    search(root)
    return lca[0]


# --- BUILD A VALID BST ---
# Structure:
#         6
#       /   \
#      2     8
#     / \   / \
#    0   4 7   9
#       / \
#      3   5

root = TreeNode(6)
node2 = TreeNode(2)
node8 = TreeNode(8)
node0 = TreeNode(0)
node4 = TreeNode(4)
node7 = TreeNode(7)
node9 = TreeNode(9)
node3 = TreeNode(3)
node5 = TreeNode(5)

# Connect them
root.left = node2
root.right = node8

node2.left = node0
node2.right = node4

node8.left = node7
node8.right = node9

node4.left = node3
node4.right = node5

# --- TEST CASES ---
solver = Solution()

# Test 1: LCA of 2 and 8 (Should be Root 6)
result1 = solver.lca(root, node2, node8)
print(f"LCA of 2 and 8: {result1.val} (Expected: 6)")

# Test 2: LCA of 2 and 4 (Should be 2)
# Because 2 is the direct parent of 4
result2 = solver.lca(root, node2, node4)
print(f"LCA of 2 and 4: {result2.val} (Expected: 2)")

# Test 3: LCA of 3 and 5 (Should be 4)
# 3 and 5 are siblings under 4
result3 = solver.lca(root, node3, node5)
print(f"LCA of 3 and 5: {result3.val} (Expected: 4)")
