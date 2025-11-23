Dynamic Programming (DP) is not about memorizing code; it is about recognizing **sub-problems**.


**1. 1D DP (Linear Recurrence)**
*Goal: "Current value depends on previous 1 or 2 values." (Fibonacci style).*
* Climbing Stairs
* House Robber
* House Robber II (Circular logic)
* Decode Ways
* Word Break (Dictionary lookup)

**2. 2D Grid DP**
*Goal: "To reach cell (i, j), I must come from (i-1, j) or (i, j-1)."*
* Unique Paths
* Unique Paths II (Obstacles)
* Minimum Path Sum
* Dungeon Game (Reverse DP - calculating from target back to start)
* Cherry Pickup (Two paths simultaneously - Advanced)



**3. The Knapsack Pattern (Subsets & Combinations)**
*Goal: "Should I include this item or not to reach target T?"*
* Partition Equal Subset Sum (0/1 Knapsack)
* Coin Change (Unbounded Knapsack - Min items)
* Coin Change II (Unbounded Knapsack - Number of ways)
* Target Sum
* Ones and Zeroes

**4. Longest Common Subsequence (LCS) & Strings**
*Goal: "Compare two strings index by index. Match? Diagonal + 1. No Match? Max(Up, Left)."*
* Longest Common Subsequence
* Edit Distance (The ultimate String DP problem)
* Distinct Subsequences
* Interleaving String
* Delete Operation for Two Strings

**5. Longest Increasing Subsequence (LIS)**
*Goal: "Find the longest chain. Requires O(N^2) DP or O(N log N) Binary Search."*
* Longest Increasing Subsequence
* Russian Doll Envelopes (2D LIS - Sorting + LIS)
* Number of Longest Increasing Subsequence
* Largest Divisible Subset

**6. Palindromes (Center Expansion vs. DP)**
*Goal: "Check inside out or outside in."*
* Longest Palindromic Substring
* Longest Palindromic Subsequence
* Palindromic Substrings (Count them)
* Minimum Insertion Steps to Make a String Palindrome

**7. Intervals & Matrix Chain (Merging)**
*Goal: "Optimization problems on subarrays/subranges." (The hardest category).*
* Burst Balloons (Classic "Hard")
* Minimum Cost Tree From Leaf Values
* Matrix Chain Multiplication (Classic textbook problem)

**8. State Machine (Stocks)**
*Goal: "Finite states (Holding, Not Holding, Cooldown)."*
* Best Time to Buy and Sell Stock with Cooldown
* Best Time to Buy and Sell Stock IV (k transactions)


### Hard Problems
1.  **Burst Balloons**: It requires you to think in reverse (which balloon is popped *last*?).
2.  **Edit Distance**: If you can implement this and explain the table cells clearly, you understand 2D DP.
