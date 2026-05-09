[⬅️ Previous](./pagecontext13.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext15.md)

---

# DSA Class Notes - Page Context 14 (Pages 066-070)

## Page 066
**Dijkstra's Algorithm Trace (Continued)**

- **Target:** Find shortest route from $A$ to $E$.
- **Trace Table:**
  | Visited Node | A | B | C | D | E |
  | :--- | :--- | :--- | :--- | :--- | :--- |
  | A | [0] | $\infty$ | $\infty$ | $\infty$ | $\infty$ |
  | C | | 3 | [2] | 2 | 30 |
  | B | | [3] | | 2 | 7 |
  | D | | | | [2] | 7 |
  | E | | | | | [7] |

- **Final Shortest Route:** $A \to C \to E$
- **Total Weight:** 7

---

## Page 067
**Date:** 1 Apr, 2026  
**Instructor:** Foysal Sir  

### Prim's Algorithm (Minimum Spanning Tree - MST)
- **Rules:**
  1. No self-loops allowed.
  2. For parallel edges, select the one with the lowest weight.
- **Process:**
  - Start from any node (e.g., $A$).
  - Connect the nearest unvisited node that has the smallest edge weight to the current tree.
- **Properties:**
  - Number of vertices in MST ($v'$) = Number of vertices in Graph ($V$).
  - Number of edges in MST ($E'$) = $|V| - 1$.
  - Example calculation: $E' = 6 - 1 = 5$.

---

## Page 068
**Kruskal's Algorithm (Minimum Spanning Tree - MST)**

- **Core Logic:** Sort all edges by weight and add them one by one if they don't create a cycle.
- **Sorted Edges for the Example Graph:**
  1. $E-F \to 2$
  2. $D-E \to 3$
  3. $B-D \to 3$
  4. $A-C \to 4$
  5. $D-F \to 4$
  6. $B-E \to 5$
  7. $A-B \to 6$
  8. $B-C \to 8$
- **MST Selection:** Select the first $|V|-1$ edges that do not form a cycle.

---

## Page 069
**Date:** 5 April, 2026  
**Instructor:** Foysal Sir  

### Bellman-Ford Algorithm
Used for finding the shortest path in a graph that may contain **negative edge weights**.

- **Constraint:** Number of iterations required is $(n-1)$, where $n$ is the number of vertices.
- **Example Graph:** Vertices $A, B, C, D, E, F$ (6 nodes).
- **Required Iterations:** $6 - 1 = 5$.
- **Edges list for relaxation:** $(A,B), (A,C), (A,D), (B,E), (C,B), (C,E), (D,C), (D,F), (E,F)$.

**Iteration 1 (It1):** Initial relaxation shown with distance updates from $\infty$ to specific values.

---

## Page 070
**Bellman-Ford Trace: Iterations 2-4**

- **Iteration 2 (It2):** Further updates to node distances.
- **Iteration 3 (It3):** Values starting to stabilize.
- **Iteration 4 (It4):** Final adjustments.
- The trace shows the node values changing at each step, demonstrating the convergence of the algorithm toward the shortest path distances for all nodes from the source node $A$.

<br>

---
[⬅️ Previous](./pagecontext13.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext15.md)
