from collections import deque
from typing import Optional, List

class TreeNode:
  def __init__(self, node=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def levelOrder(self, root: Optional[TreeNode])-> List[List[int]]:
    if root is None:
      return None
    queue = deque()
    queue.append(root)
    ans = []
    while queue:
      level = []
      n = len(queue)
      for i in range(n):
        node = queue.popleft()
        level.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
      ans.append(level)
    return ans


sol = Solution()

# --- Create the example tree ---
#      3
#     / \
#    9  20
#       / \
#      15  7

# Level 3
node_15 = TreeNode(15)
node_7 = TreeNode(7)

# Level 2
node_9 = TreeNode(9)
node_20 = TreeNode(20, left=node_15, right=node_7)

# Level 1 (Root)
root_node = TreeNode(3, left=node_9, right=node_20)

# --- Test Case 1: The standard tree ---
result_1 = sol.levelOrder(root_node)
print(f"Test Case 1 (Standard Tree):")
print(f"Input Tree Root Value: {root_node.val}")
print(f"Expected Output: [[3], [9, 20], [15, 7]]")
print(f"Actual Output: {result_1}\n")

# --- Test Case 2: An empty tree (to test the base case) ---
empty_root = None
result_2 = sol.levelOrder(empty_root)
print(f"Test Case 2 (Empty Tree):")
print(f"Input Tree: None")
print(f"Expected Output: []")
print(f"Actual Output: {result_2}\n")

# --- Test Case 3: A single-node tree ---
single_node = TreeNode(5)
result_3 = sol.levelOrder(single_node)
print(f"Test Case 3 (Single Node):")
print(f"Input Tree Root Value: {single_node.val}")
print(f"Expected Output: [[5]]")
print(f"Actual Output: {result_3}")
