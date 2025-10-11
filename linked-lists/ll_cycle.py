from typing import Optional
class ListNode:
  def __init__(self, val=0, next = None):
    self.val = val
    self.next = next

class Solution:
  def llCycle(self, head: Optional[ListNode]) -> bool:
    dummy = ListNode()
    dummy.next = head
    fast = slow = dummy
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
      if slow is fast:
        return True

# Create a linked list with a cycle: 1 -> 2 -> 3 -> 4 -> 5 -> 3 (cycle)
head_with_cycle = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head_with_cycle.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3 # This creates the cycle

# Instantiate the Solution class
solver = Solution()

# Check the list with a cycle and print the result
result = solver.llCycle(head_with_cycle)
print(f"List with cycle has a cycle: {result}")

