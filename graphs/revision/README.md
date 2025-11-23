# 1. The Basics: BFS & DFS Traversals
*Goal: Learn how to move through a graph and avoid infinite loops (visited sets).*
* Clone Graph
* Find if Path Exists in Graph
* All Paths From Source to Target
* Number of Provinces (Classic "Connected Components" problem)

# 2. Matrix Graphs (Implicit Graphs)
*Goal: Treating a 2D Grid like a graph where neighbors are Up, Down, Left, Right.*
* Number of Islands
* Max Area of Island
* Flood Fill
* Pacific Atlantic Water Flow
* Word Search (Backtracking + DFS)

# 3. Topological Sort (Dependencies)
*Goal: Ordering items where "Order Matters" (A must happen before B). Essential for build systems and task scheduling.*
* Course Schedule I (Detecting cycles)
* Course Schedule II (Returning the valid order)
* Alien Dictionary (The ultimate Topo Sort test)

# 4. Union-Find (Disjoint Set)
*Goal: Efficiently grouping items and detecting cycles in undirected graphs.*
* Redundant Connection
* Number of Operations to Make Network Connected
* Accounts Merge
* Longest Consecutive Sequence (Can be solved with Union-Find)

# 5. Shortest Path Algorithms
*Goal: Finding the fastest route in weighted graphs (Dijkstra & Bellman-Ford).*
* Network Delay Time (The standard Dijkstra template)
* Cheapest Flights Within K Stops (Bellman-Ford or Dijkstra modification)
* Path With Minimum Effort
* Find the City With the Smallest Number of Neighbors at a Threshold Distance (Floyd-Warshall logic)


# 6. Minimum Spanning Tree (MST)
*Goal: Connecting all points with the cheapest total cost (Prim’s or Kruskal’s).*
* Min Cost to Connect All Points
* Critical Connections in a Network (Finding "Bridges" - Advanced)


# Hard Problems
They combine multiple concepts:
1.  **Word Ladder II** (Requires optimized BFS to find *all* shortest paths).
2.  **Alien Dictionary** (Requires converting strings into a graph + Topological Sort).

### List
* **Basics** teaches you recursion and queue management.
* **Matrix** problems are the most common "Phone Screen" questions because they are easy to visualize.
* **Topo Sort & Union-Find** cover 90% of the "System Design" style algorithm questions (e.g., "How do you build a dependency resolver?").
* **Shortest Path** ensures you aren't scared of weighted edges.
