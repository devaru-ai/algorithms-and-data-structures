# 1. LRU Cache

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map key -> Node
        
        # 1. Initialize Left (LRU) and Right (MRU) dummies
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Helper: Remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Helper: Insert node at Right (MRU)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Make it "Fresh" (Remove and Re-insert)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Create new node and insert at Right
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # Capacity Check
        if len(self.cache) > self.cap:
            # The "Real" LRU is the one after the Left Dummy
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key] # Delete from map using the stored key

# 2. Clone Linked List with Random Pointer

def copyRandomList(head):
    if not head:
        return None
    
    # --- Step 1: Interweaving ---
    curr = head
    while curr:
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next
        
    # --- Step 2: Link Random Pointers ---
    curr = head
    while curr:
        if curr.random:
            # The clone (curr.next) points to the clone of the target (curr.random.next)
            curr.next.random = curr.random.next
        curr = curr.next.next # Skip the clone to move to next original
        
    # --- Step 3: Unweave / Restore ---
    curr = head
    dummy = Node(0)
    copy_tail = dummy
    
    while curr:
        # Extract the copy
        copy = curr.next
        copy_tail.next = copy
        copy_tail = copy
        
        # Restore the original list
        curr.next = copy.next
        
        # Move forward
        curr = curr.next
        
    return dummy.next

# 3. Reverse Nodes in k-Group
# Given 1 -> 2 -> 3 -> 4 -> 5 and k = 2.
# Reverse every 2 nodes: [2 -> 1] -> [4 -> 3] -> 5

def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    groupPrev = dummy
    
    while True:
        # 1. Check if we have k nodes left to reverse
        kth = groupPrev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next # Not enough nodes, we are done
        
        # 2. Identify boundaries
        groupNext = kth.next
        
        # 3. Reverse the group
        # 'prev' starts at groupNext so the new tail connects to the next group automatically
        prev = groupNext 
        curr = groupPrev.next
        
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        # 4. Patch the "Left" side connection
        # groupPrev was pointing to the old start (which is now the tail)
        # We need to save that node to be the groupPrev for the next round
        new_group_prev = groupPrev.next 
        
        # Link the outside 'prev' to the new head of the group
        groupPrev.next = prev
        
        # 5. Advance for next iteration
        groupPrev = new_group_prev
        
    return dummy.next


# 4. Merge K Sorted Lists

import heapq

def mergeKLists(lists):
    # Min-Heap to store the current head of each list
    # Format: (node.val, tie_breaker_index, node_object)
    min_heap = []
    
    # 1. Initialize the heap with the head of every list
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l.val, i, l))
            
    dummy = ListNode(0)
    curr = dummy
    
    # 2. Process the heap
    while min_heap:
        # Pop the smallest node (tuple unpacking)
        val, i, node = heapq.heappop(min_heap)
        
        # Add to result
        curr.next = node
        curr = curr.next
        
        # 3. If there is a next node in that specific list, push it to heap
        if node.next:
            # We reuse 'i' as the tiebreaker index for consistency 
            # (or we could increment a counter, doesn't matter)
            heapq.heappush(min_heap, (node.next.val, i, node.next))
            
    return dummy.next
