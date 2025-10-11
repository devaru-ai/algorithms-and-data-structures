from typing import Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def middleLL(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    return slow

# 1. Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 2. Instantiate the Solution class
solver = Solution()

# 3. Call the method with the head of your linked list
middle_node = solver.middleLL(head)

# 4. Print the value of the middle node
if middle_node:
    print(f"The value of the middle node is: {middle_node.val}")
else:
    print("The linked list is empty.")

