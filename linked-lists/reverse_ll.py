from typing import Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def reverseLL(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return prev

# 1. Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# 2. Instantiate the Solution class
solver = Solution()

# 3. Call the method to get the new head of the reversed list
result = solver.reverseLL(head)

# 4. Traverse the new list and print each node's value
while result:
    print(result.val, end=" -> ")
    result = result.next
print("None")
