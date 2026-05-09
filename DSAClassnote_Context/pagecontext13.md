[⬅️ Previous](./pagecontext12.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext14.md)

---

# DSA Class Notes - Page Context 13 (Pages 061-065)

## Page 061
**Introduction to Graphs**

**Definition:**
- A graph is a non-linear data structure consisting of **Vertices (Nodes)** and **Edges (Paths)**.
- Unlike trees, graphs do not maintain a strict hierarchical (parent/child) order.
- **Types:** Weighted and Unweighted Graphs.
- **Real-world application:** Google Maps.

**Adjacency Matrix (A.M.) Calculation:**
- Represents the connections between nodes in a matrix format.
- For an **Undirected Graph**:
  - Matrix is symmetric.
  - `Connection ? 1 : 0`
- For a **Directed Graph**:
  - Connection is only marked from the source to the destination node.

---

## Page 062
**Directed Graph Adjacency Matrix Example**

- A detailed $6 \times 6$ matrix for a directed graph with vertices `{A, B, C, D, E, F}`.
- **Key observations:**
  - Self-loops (e.g., $B \to B$) are represented as a `1` at position `(B, B)`.
  - The matrix is non-symmetric due to the directional nature of edges.

---

## Page 063
**DFS (Depth First Search)**

- **Data Structure Used:** Stack.
- **Core Logic:** Backtracking.
- **Process:** Visit a node, push its unvisited neighbor to the stack, and repeat. If no neighbors are left, pop and backtrack.

**Trace Results:**
1. **Graph `{P, Q, R, S, T, U}`:** Result → `P Q R U T S` (Note: R used instead of handwritten 'r/n').
2. **Numerical Graph `{0-6}`:** Result → `0 1 2 3 4 6 5`.

---

## Page 064
**Date:** 29 Mar, 2026?  
**Instructor:** Foysal Sir  

### BFS (Breadth First Search)
- **Data Structure Used:** Queue (FIFO).
- **Core Logic:** Explore all neighbors at the current level before moving deeper.
- **Process:** Use a queue to keep track of nodes to visit next.

**Trace Results:**
1. **Graph `{P, Q, R, S, T, U}`:**
   - Root Node: `P`.
   - Result: `P Q R T U S`.
2. **Numerical Graph `{0-6}`:**
   - Root Node: `0`.
   - Queue behavior: `0 → [1, 3] → [3, 2, 5, 6] → ...`
   - Result: `0 1 3 2 5 6 4`.

---

## Page 065
**Date:** 30 Mar, 2026?  
**Instructor:** Foysal Sir  

### Dijkstra's Algorithm (Shortest Path)
Used to find the shortest distance from a single source vertex to all other vertices in a weighted graph.

**Algorithm Trace:**
- **Initial State:** Source node distance = 0, all others = $\infty$.
- **Step-by-Step Table:**
  | Node | A | B | C | D | E | F | Visited |
  | :--- | :- | :- | :- | :- | :- | :- | :--- |
  | Init | 0 | $\infty$ | $\infty$ | $\infty$ | $\infty$ | $\infty$ | A |
  | Pass 1| 0 | 10 | 9 | 7 | $\infty$ | $\infty$ | D |
  | ... | ... | ... | ... | ... | ... | ... | ... |

**Shortest Paths Identified:**
- `A → D`: Distance 7.
- `A → F → E`: Distance calculation shown using cumulative weights.
- Path `A F E` distance = 15.
- Path `A C` distance = 9.

<br>

---
[⬅️ Previous](./pagecontext12.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext14.md)
