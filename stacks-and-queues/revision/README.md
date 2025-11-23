# Core concept: Ordering without Sorting.

Sorting takes $O(N \log N)$. Heaps allow you to find the minimum or maximum in $O(1)$ and remove it in $O(\log N)$. 

# 1. The "Top K" Pattern (The Standard)
*Goal: Finding the "best" K items in a large dataset without sorting the whole thing.*
* Kth Largest Element in an Array (Try both Heap and QuickSelect approaches)
* Top K Frequent Elements
* K Closest Points to Origin
* Kth Largest Element in a Stream
* Top K Frequent Words (Tricky because of lexicographical tie-breaking)


# 2. Merging Multiple Sorted Sources
*Goal: Managing multiple streams of data efficiently.*
* Merge k Sorted Lists (The classic "Hard" problem)
* Find K Pairs with Smallest Sums
* Kth Smallest Element in a Sorted Matrix

# 3. The Two-Heap Pattern (Advanced)
*Goal: Maintaining dynamic order statistics (like the Median) by balancing a Min-Heap and a Max-Heap against each other.*
* Find Median from Data Stream (The quintessential interview question for this pattern)
* Sliding Window Median

# 4. Greedy Scheduling & Resource Management
*Goal: Using a Heap to track availability or cost in real-time. This overlaps with Operating System theory.*
* Task Scheduler (CPU scheduling logic)
* Single-Threaded CPU
* IPO (Greedy selection)
* Meeting Rooms II (Can be solved with sorting, but the Heap solution is more intuitive for "available rooms")

# 5. String Manipulation & Reorganizing
*Goal: Constructing strings based on character frequency constraints.*
* Reorganize String (No two adjacent chars are same)
* Minimum Cost to Connect Sticks (Huffman Coding logic)

# 6. Underlying Architecture 
*Goal: Understanding array-based tree representation.*
* Implement a binary heap from scratch (Know how the `swim` and `sink` / `heapify` functions work with array indices `2*i` and `2*i+1`).


# Hard Problems
1.  **Find Median from Data Stream:** 
2.  **Merge k Sorted Lists:**

### **Key Insight**
Be comfortable pushing Objects or Tuples into a heap (e.g., `(frequency, word)`) and knowing exactly how the heap decides which one bubbles to the top, especially when handling tie-breakers.

