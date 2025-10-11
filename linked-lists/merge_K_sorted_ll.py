from typing import Optional, List
import heapq

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i, node in enumerate(lists):
      if node:
        heapq.heappush(heap, (node.val, i, node))
    D = ListNode()
    cur = D
    while heap:
      val, i, node = heapq.heappop(heap)
      cur.next = node
      cur = node
      node = node.next
      if node:
        heapq.heappush(heap, (node.val, i, node))
    return D.next

# 1. Create multiple sorted linked lists
# List 1: 1 -> 4 -> 5
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

# List 2: 1 -> 3 -> 4
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# List 3: 2 -> 6
l3 = ListNode(2)
l3.next = ListNode(6)

# Put them in a list
lists_to_merge = [l1, l2, l3]

# 2. Instantiate the Solution class
solver = Solution()

# 3. Call the method
merged_list_head = solver.mergeKLists(lists_to_merge)

# 4. Traverse the merged list and print the values
print("Merged Linked List:")
current_node = merged_list_head
while current_node:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")
