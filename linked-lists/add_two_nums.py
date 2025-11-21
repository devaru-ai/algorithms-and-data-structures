# --- 1. THE SETUP (Helper Code) ---
# This part builds the Linked List structure so we can test it.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(numbers):
    """Turns a list like [2, 4, 3] into a Linked List: 2 -> 4 -> 3"""
    dummy = ListNode(0)
    curr = dummy
    for num in numbers:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_list(node):
    """Turns the Linked List back into a string so we can read it"""
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    return " -> ".join(result)

# --- 2. SOLUTION ---
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values (use 0 if the list ran out)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Math
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Write it down
            curr.next = ListNode(digit)
            curr = curr.next
            
            # Move pointers
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next

# --- 3. THE TEST ---
if __name__ == "__main__":
    solver = Solution()

    # TEST 1: The Classic Example
    # Math: 342 + 465 = 807
    # Input lists are reversed: [2,4,3] and [5,6,4]
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    
    print("Test 1:")
    print(f"List 1: {print_list(l1)}")
    print(f"List 2: {print_list(l2)}")
    
    result = solver.addTwoNumbers(l1, l2)
    print(f"Result: {print_list(result)}") 
    # Expected Result: 7 -> 0 -> 8 (Which matches 807)
    print("-" * 20)

    # TEST 2: The "Carry Over" Example
    # Math: 99 + 1 = 100
    # Input lists: [9,9] and [1]
    l1 = create_linked_list([9, 9])
    l2 = create_linked_list([1])
    
    print("Test 2:")
    print(f"List 1: {print_list(l1)}")
    print(f"List 2: {print_list(l2)}")
    
    result = solver.addTwoNumbers(l1, l2)
    print(f"Result: {print_list(result)}")
    # Expected Result: 0 -> 0 -> 1 (Which matches 100)
