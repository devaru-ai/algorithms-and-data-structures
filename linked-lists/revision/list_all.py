# Print/visit all nodes
def traverse(head):
  current = head
  while current:
    print(current.val)
    current = current.next
    
# Find Middle of Linked List (fast/slow ptr)
def middle(head):
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow
    
# Reverse a Linked List (iterative/recursive)	
def reverseList(head):
  prev = None
  curr = head
  while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
  return prev
  
# Merge Two Sorted Lists	
def merge(l1, l2):
  dummy = ListNode(-1)
  tail = dummy
  while l1 and l2:
    if l1.val < l2.val:
      tail.next = l1
      l1 = l1.next
    else:
      tail.next = l2
      l2 = l2.next
    if l1:
      tail.next = l1
    elif l2:
      tail.next = l2
  return dummy.next
      
# Remove N-th Node from End	
def removeNthNode(head, n):
  dummy = ListNode(0, head)
  slow = dummy
  fast = dummy
  for _ in range(n):
    fast = fast.next
  while fast.next:
    slow = slow.next
    fast = fast.next
  slow.next = slow.next.next
  return dummy.next

#	Detect Cycle (Floyd’s algo)	
def hasCycle(head):
  slow = head
  fast = head
  
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
    if slow == fast:
      return True
    return False
  
#	Find Start Node of Cycle	
def detectStartCycle(head):
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      slow = head
      while slow != fast:
        slow = slow.next
        fast = fast.next
      return slow
  return None

# Find Intersection Point of Two Lists	
def getIntesectionNode(headA, headB):
  if not headA or not headB:
    return None
  ptrA = headA
  ptrB = headB
  while ptrA != ptrB:
    ptrA = ptrA.next if ptrA else headB
    ptrB = ptrB.next if ptrB else headA
  return ptrA
  
# Remove Duplicates from Sorted List	
def deleteDuplicates(head):
  current = head
  while current and current.next:
    if current.val == current.next.val:
      current.next = current.next.next
    else:
      current = current.next
  return head
  
# Check if Palindrome Linked List	
def isPalindrome(head):
  def reverse(node):
    prev = None
    curr = node
    while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
    return temp
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  right_half_start = reverse(slow)
  left = head
  right = right_half_start
  while right:
    if left.val != right.val:
      return False
    left = left.next
    right = right.next
  return True
      
# Add Two Numbers 
def addTwoNumbers(l1, l2):
  dummy = ListNode(0)
  curr = dummy()
  carry = 0
  while l1 or l2 or carry:
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    total = val1 + val2 + carry
    carry = total // 10
    curr.next = ListNode(total % 10)
    curr = curr.next
    if l1: l1 = l1.next
    if l2: l2 = l2.next
  return dummy.next
    













