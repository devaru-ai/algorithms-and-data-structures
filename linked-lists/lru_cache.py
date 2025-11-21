class Node:
    """
    The Song (Node)
    Holds the data and links to neighbors.
    """
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # The Dictionary (Cheat Sheet)
        
        # Create Dummy Head (MRU side) and Tail (LRU side)
        self.head = Node(0, 0) 
        self.tail = Node(0, 0)
        
        # Connect Head <-> Tail initially
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- HELPER 1: Remove a node from the list ---
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        
        # Stitch the neighbors together, bypassing the current node
        prev_node.next = next_node
        next_node.prev = prev_node

    # --- HELPER 2: Add node to the front (right after Head) ---
    def _add(self, node):
        # Identify the node currently right after head
        head_next = self.head.next
        
        # Connect the new node to Head and the old first node
        node.prev = self.head
        node.next = head_next
        
        # Update Head and the old first node to point to the new node
        self.head.next = node
        head_next.prev = node

    # --- MAIN LOGIC: GET ---
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            # Move to front: remove it, then add it back to the top
            self._remove(node)
            self._add(node)
            
            return node.val
        return -1

    # --- MAIN LOGIC: PUT ---
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If it exists, remove the old version
            self._remove(self.cache[key])
        
        # Create new node and add to front
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node
        
        # If we are over capacity, remove the LRU (item before Tail)
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev # The guy at the back
            self._remove(lru_node)    # Cut from list
            del self.cache[lru_node.key] # Delete from dictionary

    # --- DEBUG HELPER (To visualize the list) ---
    def print_debug_state(self):
        current = self.head.next
        elements = []
        while current != self.tail:
            elements.append(f"[{current.key}:{current.val}]")
            current = current.next
        
        # Print format: HEAD -> [Most Recent] -> ... -> [Least Recent] -> TAIL
        print("Current Cache State: HEAD <-> " + " <-> ".join(elements) + " <-> TAIL")


# ==========================================
# TEST SCENARIO
# ==========================================
if __name__ == "__main__":
    # 1. Create a cache with capacity of 2
    print("--- Initialize LRU Cache (Capacity 2) ---")
    lru = LRUCache(2)
    lru.print_debug_state()
    print("\n")

    # 2. Add Song A (1, 1)
    print("--- Put(1, 1) ---")
    lru.put(1, 1)
    lru.print_debug_state()
    print("\n")

    # 3. Add Song B (2, 2)
    print("--- Put(2, 2) ---")
    lru.put(2, 2)
    lru.print_debug_state()
    print("\n")

    # 4. Play Song A (1) again. 
    # This should move [1:1] to the front, pushing [2:2] to the back.
    print(f"--- Get(1) returned: {lru.get(1)} ---")
    print("Notice [1:1] moved to the front (Left):")
    lru.print_debug_state()
    print("\n")

    # 5. Add Song C (3, 3). 
    # Capacity is 2. We must kill the LRU.
    # Who is LRU? Look at step 4. [2:2] is at the back. It should die.
    print("--- Put(3, 3) -> Should evict key 2 ---")
    lru.put(3, 3)
    lru.print_debug_state()
    print("\n")

    # 6. Verify 2 is gone
    print(f"--- Get(2) returned: {lru.get(2)} (Expected -1) ---")
