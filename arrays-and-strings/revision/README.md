# **1. Two Pointers (The "Convergence" Logic)**
*Goal: Master manipulation of indices from different ends or speeds.*

1.  **Valid Palindrome** (Easy) – *Do you know how to move pointers inward?*
2.  **Two Sum II - Input Array Is Sorted** (Medium) – *The classic sorted array optimization.*
3.  **3Sum** (Medium) –  Handles duplicates and triplet logic.
4.  **Container With Most Water** (Medium) – *Teaches "greedy" pointer movement (deciding which side to shrink).*
5.  **Trapping Rain Water** (Hard) – *Combines pre-computation or two-pointers with complex logic.*
6.  **Move Zeroes** (Easy) – *In-place manipulation (read/write pointers).*

# **2. Sliding Window (The "Subarray" Logic)**
*Goal: Master dynamic window resizing (expand right, shrink left).*

7.  **Best Time to Buy and Sell Stock** (Easy) – *The simplest window (size 1 to n).*
8.  **Longest Substring Without Repeating Characters** (Medium) – *The absolute standard for dynamic windows using a Set/Map.*
9.  **Longest Repeating Character Replacement** (Medium) – *Teaches valid window logic: `(window_len - max_count <= k)`.*
10. **Permutation in String** (Medium) – *Fixed-size window sliding.*
11. **Minimum Window Substring** (Hard) – *Requires managing a frequency map and shrinking logic perfectly.*
12. **Sliding Window Maximum** (Hard) – *Uses a Deque (Monotonic Queue). Advanced optimization.*

# **3. Hashing & Frequency Maps (The "Lookup" Logic)**
*Goal: Master O(1) lookups and counting.*

13. **Contains Duplicate** (Easy) – *Basic Hash Set usage.*
14. **Valid Anagram** (Easy) – *Frequency array (size 26) vs. Hash Map.*
15. **Two Sum** (Easy) – *Complement lookup.*
16. **Group Anagrams** (Medium) – *Key generation (sorting string or counting chars as key).*
17. **Top K Frequent Elements** (Medium) – *Bucket Sort optimization or Heap usage.*
18. **Longest Consecutive Sequence** (Medium) – *Using a Set to find "start of sequence" intelligently.*

# **4. Prefix Sum (The "Range" Logic)**
*Goal: Master O(1) range queries.*

19. **Range Sum Query - Immutable** (Easy) – *The definition of Prefix Sum.*
20. **Find Pivot Index** (Easy) – *Balancing left vs. right sums.*
21. **Product of Array Except Self** (Medium) – *Prefix & Suffix products combined (no division allowed).*
22. **Subarray Sum Equals K** (Medium) – *Prefix Sum + Hash Map.*
23. **Contiguous Array** (Medium) – *Using `+1` for 1 and `-1` for 0 to find balance.*

# **5. String Manipulation (The "Parsing" Logic)**
*Goal: Master traversing specific string formats.*

24. **Longest Common Prefix** (Easy) – *Vertical vs. Horizontal scanning.*
25. **String to Integer (atoi)** (Medium) – *Handling overflow, whitespace, and signs (messy but necessary).*
26. **Encode and Decode Strings** (Medium) – *Designing your own delimiter protocol.*
27. **Text Justification** (Hard) – *Pure implementation heavy. Good for testing coding speed/cleanliness.*

# **6. 2D Arrays / Matrix (The "Grid" Logic)**
*Goal: Master coordinate manipulation.*

28. **Set Matrix Zeroes** (Medium) – *Using the first row/col as storage to save space.*
29. **Spiral Matrix** (Medium) – *Simulation; managing boundaries (top, bottom, left, right).*
30. **Rotate Image** (Medium) – *In-place matrix rotation (transpose + reverse).*
31. **Search a 2D Matrix** (Medium) – *Treating 2D matrix as a flattened sorted 1D array (Binary Search).*


# Checklist
* [ ] **Two Pointers:** Solve **3Sum** without looking up how to skip duplicates.
* [ ] **Sliding Window:** Qrite the `while` loop for **Longest Substring** without an off-by-one error.
* [ ] **Prefix Sum:** Why `Map<Sum, Count>` is used in **Subarray Sum Equals K**.
* [ ] **Matrix:** Traverse a matrix in **Spiral Order** without crashing on the last element.
