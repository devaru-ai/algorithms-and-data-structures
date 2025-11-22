# **Category 1: Traversals & Views (The "Visual" Problems)**
*Goal: Master visiting nodes in specific geometric orders. These test your ability to manipulate BFS/DFS queues and hash maps.*

**Concept:** "How do I print/capture the tree if I look at it from [angle]?"

* **Standard Traversals**
    * Binary Tree Inorder Traversal (Iterative & Recursive)
    * Binary Tree Preorder Traversal (Iterative & Recursive)
    * Binary Tree Postorder Traversal (Iterative & Recursive)
    * **Morris Traversal** (Inorder traversal with O(1) space - *Advanced*)
* **Level-Based (BFS)**
    * Binary Tree Level Order Traversal
    * Binary Tree Zigzag Level Order Traversal
    * Average of Levels in Binary Tree
    * Find Largest Value in Each Tree Row
* **Geometric Views (Vertical/Horizontal)**
    * Binary Tree Right Side View (DFS or BFS)
    * Left View of Binary Tree
    * Top View of Binary Tree (Requires Map + Horizontal Distance)
    * Bottom View of Binary Tree
    * **Vertical Order Traversal of a Binary Tree** (*Boss Level: Sorting by column, then row, then value*)
    * Boundary Traversal of Binary Tree (Left boundary + Leaves + Right boundary)


# **Category 2: Path, Sum & Ancestry (The "Navigation" Problems)**
*Goal: Master passing information **down** (from root to child) and bubbling information **up** (from child to root).*

**Concept:** "Find a route that satisfies condition X."

* **Root-to-Leaf Paths**
    * Path Sum I (Does path exist?)
    * Path Sum II (Return all paths)
    * Sum Root to Leaf Numbers (e.g., 1->2->3 becomes 123)
    * Binary Tree Paths (Return all strings "1->2->5")
* **Arbitrary Paths (The Hardest Category)**
    * Path Sum III (Path can start/end anywhere - requires Prefix Sum Map)
    * **Binary Tree Maximum Path Sum** (*Boss Level: Standard "Hard" interview benchmark*)
    * Longest Univalue Path
* **Ancestry & Distance**
    * Lowest Common Ancestor (LCA) of a Binary Tree
    * LCA of Deepest Leaves
    * Distance Between Two Nodes in a Binary Tree
    * **All Nodes Distance K in Binary Tree** (*Boss Level: Convert tree to graph/add parent pointers*)


# **Category 3: Construction & Serialization (The "Architect" Problems)**
*Goal: Master mapping array indices to tree nodes. If you can't build the tree, you can't solve the problem.*

**Concept:** "Rebuild the tree from this flat data."

* **From Traversals**
    * Construct Binary Tree from Preorder and Inorder Traversal
    * Construct Binary Tree from Inorder and Postorder Traversal
    * Construct Binary Tree from Preorder and Postorder Traversal
* **Serialization**
    * Serialize and Deserialize Binary Tree (BFS or DFS string conversion)
    * Serialize and Deserialize BST (Can be optimized)
    * **Verify Preorder Serialization of a Binary Tree** (Verify without building - *Boss Level*)



# **Category 4: Structure & Validation (The "Health Check" Problems)**
*Goal: Master recursive boolean checks (`left_valid AND right_valid`).*

**Concept:** "Does this tree follow the rules?"

* **Basic Properties**
    * Maximum Depth of Binary Tree
    * Minimum Depth of Binary Tree (Watch out for skewed trees)
    * Balanced Binary Tree (Height difference ≤ 1)
    * Diameter of Binary Tree (Longest path between any two nodes)
* **Symmetry & Shape**
    * Same Tree (Are A and B identical?)
    * Symmetric Tree (Is A a mirror of itself?)
    * Subtree of Another Tree (Is A inside B?)
    * Check Completeness of a Binary Tree
    * **Flip Equivalent Binary Trees** (*Boss Level: Can A become B by flipping children?*)



# **Category 5: Binary Search Tree (BST) Specifics**
*Goal: Master the property `Left < Root < Right`. If you don't use this property, your solution is inefficient.*

**Concept:** "Find/Sort efficient data using the BST invariant."

* **Validation & Search**
    * Validate Binary Search Tree (Must use range `min < node < max`)
    * Search in a Binary Search Tree
    * Lowest Common Ancestor of a Binary Search Tree (Easier than standard LCA)
* **Modification**
    * Insert into a Binary Search Tree
    * Delete Node in a BST (Complex: involves finding successor/predecessor)
    * Trim a Binary Search Tree
    * Convert Sorted Array to Binary Search Tree
    * Convert Sorted List to Binary Search Tree
* **Order Properties**
    * Kth Smallest Element in a BST
    * **Recover Binary Search Tree** (Two nodes swapped - fix in O(1) space - *Boss Level*)



# **Category 6: Tree Modification (The "Surgery" Problems)**
*Goal: Master changing pointers without losing track of the rest of the tree.*

**Concept:** "Rearrange the nodes in place."

* **Inversion & Flattening**
    * Invert Binary Tree
    * Flatten Binary Tree to Linked List (Preorder traversal in-place)
* **Pruning & Linking**
    * Populating Next Right Pointers in Each Node (Connect levels)
    * Binary Tree Pruning (Remove subtrees that don't satisfy condition)
    * **Burn a Tree** (Time to burn tree from target node - *Boss Level*)


# **Category 7: Advanced & Special Trees**
*Goal: These often appear in specialized roles (ML Infra, Systems) or very hard rounds.*

* **Trie (Prefix Tree)**
    * Implement Trie (Prefix Tree)
    * Design Add and Search Words Data Structure
* **Segment Tree / Fenwick Tree** (Range Queries)
    * Range Sum Query - Mutable
* **N-Ary Trees**
    * N-ary Tree Level Order Traversal
    * Encode N-ary Tree to Binary Tree

### **Execution Plan**
Do not go top-to-bottom. Follow this loop:
1. Category 1 (Traversals) + Category 4 (Validation).
2. Category 2 (Paths) + Category 5 (BST).
3. Category 3 (Construction).
4. Category 6 (Modification).
5. "Boss Levels" (Max Path Sum, Vertical Order, Recover BST).
