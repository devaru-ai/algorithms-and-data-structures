from typing import Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def removeNthNode(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    d = ListNode()
    d.next = head
    behind = ahead = d
    for _ in range(n+1):
      ahead = ahead.next
    while ahead:
      ahead = ahead.next
      behind = behind.next
    behind.next = behind.next.next
    return d.next

list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
n = 1
sol = Solution()
sol_head = sol.removeNthNode(list, n)
curr = sol_head
while curr:
  print(curr.val, end = "->")
  curr = curr.next
print("None")
 
