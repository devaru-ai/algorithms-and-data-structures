from typing import Optional

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next
    
class Solution:
  def mergeSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    d = ListNode()
    cur = d
    
    while list1 and list2:
      if list1.val > list2.val:
        cur.next = list1
        cur = list1
        list1 = list1.next
      else:
        cur.next = list2
        cur = list2
        list2 = list2.next
    cur.next = list1 if list1 else list2
    
    return d.next
  


# 1. Create the linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(5)

list2 = ListNode(4)
list2.next = ListNode(5) 
list2.next.next = ListNode(6) 

# 2. Instantiate the Solution class
solver = Solution()

# 3. Call the method to get the head of the merged list
merged_head = solver.mergeSortedLists(list1, list2)

# 4. Traverse the merged list and print the values
print("Merged List:")
cur = merged_head
while cur:
    print(cur.val, end=" -> ")
    cur = cur.next
print("None")
