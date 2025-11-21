# 1. Define the ListNode (standard for LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. The Solution Class (The logic we discussed)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # Find Middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse Second Half
        prev = None
        curr = slow
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
            
        # Compare
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True

# --- HELPER FUNCTIONS FOR TESTING ---

def create_linked_list(arr):
    """Converts a Python list [1, 2, 3] into a Linked List 1->2->3"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    """Helper to visualize the list"""
    vals = []
    current = head
    while current:
        vals.append(str(current.val))
        current = current.next
    return " -> ".join(vals)

# --- RUNNING THE TESTS ---

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1: Even length palindrome
    input_list_1 = [1, 2, 2, 1]
    ll_1 = create_linked_list(input_list_1)
    print(f"Input: {input_list_1}")
    print(f"Is Palindrome? {solver.isPalindrome(ll_1)}") 
    print("-" * 20)

    # Test Case 2: Odd length palindrome
    input_list_2 = [1, 0, 1]
    ll_2 = create_linked_list(input_list_2)
    print(f"Input: {input_list_2}")
    print(f"Is Palindrome? {solver.isPalindrome(ll_2)}")
    print("-" * 20)

    # Test Case 3: Not a palindrome
    input_list_3 = [1, 2, 3]
    ll_3 = create_linked_list(input_list_3)
    print(f"Input: {input_list_3}")
    print(f"Is Palindrome? {solver.isPalindrome(ll_3)}")
