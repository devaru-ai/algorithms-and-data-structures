from typing import Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

class Solution:
  def removeDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    while cur and cur.next:
      if cur.val == cur.next.val:
        cur.next = cur.next.next
      else:
        cur = cur.next
    return head

list = ListNode(1)
list.next = ListNode(1)
list.next.next = ListNode(2)

sol = Solution()

result = sol.removeDuplicates(list)

cur = result
while cur:
  print(cur.val, end = "->")
  cur = cur.next
print("None")
