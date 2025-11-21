class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def getIntersectionNode(headA, headB):
  if not headA or not headB:
    return None
  ptrA = headA
  ptrB = headB
  while ptrA != ptrB:
    ptrA = headB if ptrA is None else ptrA.next
    ptrB = headA if ptrB is None else ptrB.next
  return ptrA



# --- DRIVER CODE ---

# 1. Create the "Shared" part (The Intersection)
# Structure: 8 -> 4 -> 5
intersect = ListNode(8)
intersect.next = ListNode(4)
intersect.next.next = ListNode(5)

# 2. Create List A (Unique part)
# Structure: 4 -> 1 -> (jumps to 8)
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = intersect  # <--- The Merge

# 3. Create List B (Unique part)
# Structure: 5 -> 6 -> 1 -> (jumps to 8)
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = intersect # <--- The Merge

# 4. Run the Program
result = getIntersectionNode(headA, headB)

if result:
    print(f"Intersected at node with value: {result.val}")
else:
    print("No intersection found.")













    
