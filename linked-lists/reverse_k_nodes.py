# 1. The definition of a Node (Standard LeetCode setup)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Helper functions to make testing easier
def create_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    return " -> ".join(vals)

# 3. SOLUTION CODE
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy  # This is our "Anchor" before the group
        
        while True:
            # 1. Find the Kth node (Check if we have a full group)
            kth = groupPrev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next # If not enough nodes, we are done!

            # 2. Save the connection to the REST of the list
            groupNext = kth.next 

            # 3. REVERSE logic (Inside the group only)
            # We want to reverse from 'curr' to 'kth'
            prev = groupNext  # Trick: Point the first reversed node to the NEXT group immediately
            curr = groupPrev.next 
            
            while curr != groupNext:
                temp = curr.next  # Save the next node
                curr.next = prev  # Reverse the link
                prev = curr       # Move prev forward
                curr = temp       # Move curr forward
            
            # 4. GLUE it back together
            # 'kth' is now the HEAD of the reversed group.
            # 'groupPrev.next' was the old head (now tail).
            
            temp = groupPrev.next # Remember the old head (it's now the tail, e.g., 1)
            groupPrev.next = kth  # Connect Anchor -> New Head (Dummy -> 2)
            groupPrev = temp      # Move Anchor to the New Tail (Anchor is now at 1)
            
        return dummy.next

# 4. TEST RUNNER
if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: Standard case (k=2)
    # Expected: 2->1 -> 4->3 -> 5
    arr1 = [1, 2, 3, 4, 5]
    k1 = 2
    head1 = create_linked_list(arr1)
    print(f"Input: {arr1}, k={k1}")
    res1 = solver.reverseKGroup(head1, k1)
    print(f"Result: {print_linked_list(res1)}")
    print("-" * 30)

    # Test Case 2: k equals list length
    # Expected: 3->2->1
    arr2 = [1, 2, 3]
    k2 = 3
    head2 = create_linked_list(arr2)
    print(f"Input: {arr2}, k={k2}")
    res2 = solver.reverseKGroup(head2, k2)
    print(f"Result: {print_linked_list(res2)}")
    print("-" * 30)

    # Test Case 3: k is 1 (Should do nothing)
    # Expected: 1->2->3->4->5
    arr3 = [1, 2, 3, 4, 5]
    k3 = 1
    head3 = create_linked_list(arr3)
    print(f"Input: {arr3}, k={k3}")
    res3 = solver.reverseKGroup(head3, k3)
    print(f"Result: {print_linked_list(res3)}")
