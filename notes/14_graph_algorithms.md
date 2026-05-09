[⬅️ Previous](./13_graphs.md) | [🏠 Home](./README.md) | [Next ➡️](./15_advanced_topics.md)

---

# 📘 Chapter 14: Graph Algorithms — Dijkstra, Bellman-Ford, Prim's, Kruskal's

> **Exam Frequency:** 7/8 years (Dijkstra, MST) | **Typical Marks:** 04–06 | **Section:** B
> **These are the HIGHEST-VALUE topics in the exam.**

---

## 1. Dijkstra's Shortest Path Algorithm

### Problem
Find the shortest path from a **source vertex** to all other vertices in a **weighted graph with non-negative edge weights**.

### Algorithm (Greedy)

```
Procedure DIJKSTRA(G, source)
    For each vertex v do
        dist[v] = ∞
        visited[v] = FALSE
        prev[v] = NULL
    End For
    dist[source] = 0
    
    Repeat V times:
        u = unvisited vertex with minimum dist[u]
        visited[u] = TRUE
        
        For each neighbor v of u do
            If NOT visited[v] AND dist[u] + weight(u,v) < dist[v] Then
                dist[v] = dist[u] + weight(u,v)    // relaxation
                prev[v] = u
            End If
        End For
    End Repeat
End Procedure
```

### Intuition
Think of **spreading paint** from the source. The paint always flows through the shortest unused path first. Once a vertex is "painted" (visited), its shortest distance is finalized.

### Complete Trace

**Graph:**
```
      A ---10--- B
      |         / |
      5       3   2
      |     /     |
      C ---1--- D ---7--- E
      |
      8
      |
      F
```

**Edges:** A-B:10, A-C:5, B-D:2, C-B:3, C-D:1, C-F:8, D-E:7

**Dijkstra from source A:**

| Step | Current | dist[A] | dist[B] | dist[C] | dist[D] | dist[E] | dist[F] | Action |
|---|---|---|---|---|---|---|---|---|
| Init | — | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | |
| 1 | **A** | **0** | 10 | 5 | ∞ | ∞ | ∞ | Update B(0+10), C(0+5) |
| 2 | **C** | 0 | 8 | **5** | 6 | ∞ | 13 | Update B(5+3=8<10), D(5+1=6), F(5+8=13) |
| 3 | **D** | 0 | 8 | 5 | **6** | 13 | 13 | Update E(6+7=13) |
| 4 | **B** | 0 | **8** | 5 | 6 | 8 | 13 | Update E via B: 8+2=10? Wait, B-D:2, but D already visited. Check B→D: D visited. No update for E via B. Actually B→D:2, D already finalized. |
| 5 | **E** | 0 | 8 | 5 | 6 | **13** | 13 | No updates (E has no outgoing unvisited) |

Wait, let me redo this more carefully with the correct graph.

Let me use a classic exam graph:

**Graph (appeared in 2017 and 2024 — source A):**
```
         B
       / | \
     1   |   4
    /    |    \
   A     3     D ---2--- E
    \    |    /
     2   |   1
      \  | /
         C
```

**Edges:** A-B:1, A-C:2, B-C:3, B-D:4, C-D:1, D-E:2

**Dijkstra from A:**

| Step | Select | dist[A] | dist[B] | dist[C] | dist[D] | dist[E] | Visited |
|---|---|---|---|---|---|---|---|
| Init | — | 0 | ∞ | ∞ | ∞ | ∞ | {} |
| 1 | A (d=0) | **0** | 1 | 2 | ∞ | ∞ | {A} |
| 2 | B (d=1) | 0 | **1** | 2 | 5 | ∞ | {A,B} |
| 3 | C (d=2) | 0 | 1 | **2** | 3 | ∞ | {A,B,C} |
| 4 | D (d=3) | 0 | 1 | 2 | **3** | 5 | {A,B,C,D} |
| 5 | E (d=5) | 0 | 1 | 2 | 3 | **5** | {A,B,C,D,E} |

**Step-by-step explanation:**
1. **Select A (d=0):** Update neighbors: B = 0+1 = 1, C = 0+2 = 2
2. **Select B (d=1):** Smallest unvisited. Update: C = min(2, 1+3=4) = 2 (no change), D = 1+4 = 5
3. **Select C (d=2):** Update: D = min(5, 2+1=3) = **3** (improved!)
4. **Select D (d=3):** Update: E = 3+2 = 5
5. **Select E (d=5):** No unvisited neighbors. Done.

**Shortest paths from A:**

| Vertex | Distance | Path |
|---|---|---|
| A | 0 | A |
| B | 1 | A → B |
| C | 2 | A → C |
| D | 3 | A → C → D |
| E | 5 | A → C → D → E |

### Complexity
| Implementation | Time |
|---|---|
| Adjacency matrix | **O(V²)** |
| Adjacency list + min-heap | O((V + E) log V) |

### Limitation
**Cannot handle negative edge weights.** Use Bellman-Ford instead.

---

## 2. Bellman-Ford Algorithm

### Problem
Find shortest paths from source to all vertices, works with **negative edge weights**. Can detect **negative weight cycles**.

### Algorithm

```
Procedure BELLMAN_FORD(G, source)
    For each vertex v do
        dist[v] = ∞
    End For
    dist[source] = 0
    
    // Relax all edges V-1 times
    For i = 1 to V-1 do
        For each edge (u, v, w) do
            If dist[u] + w < dist[v] Then
                dist[v] = dist[u] + w
            End If
        End For
    End For
    
    // Check for negative weight cycles
    For each edge (u, v, w) do
        If dist[u] + w < dist[v] Then
            Print "Negative weight cycle exists!"
        End If
    End For
End Procedure
```

### Why V−1 Iterations?
In a graph with V vertices, the shortest path can have at most V−1 edges. Each iteration guarantees that paths of length `i` edges are correctly computed.

### Trace Example

**Graph with negative edge:**
```
  A --6-→ B --(-2)-→ C
  |       ↑          |
  7       |         (-3)
  |       5          |
  ↓       |          ↓
  D --(-4)→ E ←--9-- F
```

Edges: A→B:6, A→D:7, B→C:-2, C→F:-3, D→E:-4, E→B:5, F→E:9

**Source: A**

| Iteration | dist[A] | dist[B] | dist[C] | dist[D] | dist[E] | dist[F] |
|---|---|---|---|---|---|---|
| Init | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | 0 | 6 | 4 | 7 | 3 | 1 |
| 2 | 0 | 6 | 4 | 7 | 3 | 1 |

**Explanation of iteration 1 (process all edges):**
- A→B: dist[B] = min(∞, 0+6) = 6
- A→D: dist[D] = min(∞, 0+7) = 7
- B→C: dist[C] = min(∞, 6+(-2)) = 4
- C→F: dist[F] = min(∞, 4+(-3)) = 1
- D→E: dist[E] = min(∞, 7+(-4)) = 3
- E→B: dist[B] = min(6, 3+5=8) = 6 (no change)
- F→E: dist[E] = min(3, 1+9=10) = 3 (no change)

No changes in iteration 2 → converged.

### Negative Weight Cycles (Instructor's Note)
If the graph contains a **Negative Weight Cycle**, the path cost can be reduced infinitely by repeatedly traversing the cycle. In this case, the Bellman-Ford algorithm will **fail to converge**. 
- **Bengali Note:** "কখনোই Converge করবে না" (Will never converge) if such a loop exists.

### Dijkstra vs Bellman-Ford

| Criterion | Dijkstra | Bellman-Ford |
|---|---|---|
| Negative weights | ❌ Cannot handle | ✅ Can handle |
| Negative cycles | ❌ Cannot detect | ✅ Can detect |
| Time | O(V²) or O((V+E)log V) | **O(VE)** |
| Approach | Greedy | Dynamic Programming |
| Use when | Non-negative weights, need speed | Negative weights exist |

---

## 3. Minimum Spanning Tree (MST)

### Definition
A **Minimum Spanning Tree** of a weighted, connected, undirected graph is a subset of edges that:
1. **Connects all vertices** (spanning)
2. **Forms a tree** (no cycles, V−1 edges)
3. Has **minimum total weight** among all spanning trees

### Intuition
You want to connect all cities with roads using the **least total road length**. The MST gives you exactly that — the cheapest way to connect everything.

---

## 4. Prim's Algorithm (Greedy — vertex-based)

### Concept
Start from any vertex. At each step, add the **cheapest edge** that connects a visited vertex to an unvisited vertex.

### Algorithm
```
Procedure PRIM(G, start)
    Set MST = empty set
    Set Visited = {start}
    
    While |Visited| < V do
        Find minimum weight edge (u, v) such that
            u ∈ Visited AND v ∉ Visited
        Add edge (u, v) to MST
        Add v to Visited
    End While
    
    Return MST
End Procedure
```

### Trace

**Graph:**
```
    A ---4--- B ---2--- C
    |       / |         |
    1     3   5         6
    |   /     |         |
    D ---7--- E ---8--- F
```

**Prim's starting from A:**

| Step | Visited | Edge Added | Weight | MST Weight |
|---|---|---|---|---|
| Init | {A} | — | — | 0 |
| 1 | {A, D} | A-D | 1 | 1 |
| 2 | {A, D, B} | D-B (3) or A-B (4)? → D-B:3 | 3 | 4 |
| 3 | {A, D, B, C} | B-C | 2 | 6 |
| 4 | {A, D, B, C, E} | B-E | 5 | 11 |
| 5 | {A, D, B, C, E, F} | C-F | 6 | 17 |

**MST edges:** A-D(1), D-B(3), B-C(2), B-E(5), C-F(6)
**Total MST weight: 17**

```
MST:
    A       B ---2--- C
    |     /   |       |
    1   3     5       6
    |  /      |       |
    D         E       F
```

### Complexity
| Implementation | Time |
|---|---|
| Adjacency matrix | **O(V²)** |
| Adjacency list + min-heap | O(E log V) |

---

## 5. Kruskal's Algorithm (Greedy — edge-based)

### Concept
Sort all edges by weight. Add edges one by one (smallest first), **skipping any edge that would create a cycle**.

### Algorithm
```
Procedure KRUSKAL(G)
    Sort all edges by weight (ascending)
    Set MST = empty set
    Initialize Union-Find with V components
    
    For each edge (u, v, w) in sorted order do
        If u and v are in DIFFERENT components Then
            Add (u, v, w) to MST
            UNION(u, v)                    // merge components
        Else
            Skip (would create cycle)
        End If
        
        If |MST| = V - 1 Then Break       // tree complete
    End For
    
    Return MST
End Procedure
```

### Cycle Detection: Union-Find
Use **Union-Find (Disjoint Set)** to check if two vertices are already connected:
- **FIND(x):** Returns the root/representative of x's component
- **UNION(x, y):** Merges the components containing x and y
- If FIND(u) = FIND(v), they're in the same component → adding edge creates cycle

### Trace (same graph)

**Sorted edges:**

| Edge | Weight |
|---|---|
| A-D | 1 |
| B-C | 2 |
| D-B | 3 |
| A-B | 4 |
| B-E | 5 |
| C-F | 6 |
| D-E | 7 |
| E-F | 8 |

**Kruskal's execution:**

| Step | Edge | Weight | Components | Action |
|---|---|---|---|---|
| 1 | A-D | 1 | {A,D} {B} {C} {E} {F} | ✅ Add |
| 2 | B-C | 2 | {A,D} {B,C} {E} {F} | ✅ Add |
| 3 | D-B | 3 | {A,D,B,C} {E} {F} | ✅ Add (D and B in different sets) |
| 4 | A-B | 4 | — | ❌ Skip (A and B same component) |
| 5 | B-E | 5 | {A,D,B,C,E} {F} | ✅ Add |
| 6 | C-F | 6 | {A,D,B,C,E,F} | ✅ Add (5 edges = V-1, DONE) |

**MST:** A-D(1), B-C(2), D-B(3), B-E(5), C-F(6) → **Total: 17** (same as Prim's ✓)

### Complexity
```
Sorting: O(E log E)
Union-Find operations: O(E × α(V)) ≈ O(E)
Total: O(E log E) = O(E log V)    (since E ≤ V²)
```

---

## 6. Prim's vs Kruskal's

| Criterion | Prim's | Kruskal's |
|---|---|---|
| **Approach** | Vertex-based (grow tree) | Edge-based (sort & add) |
| **Data structure** | Priority queue / min-heap | Union-Find |
| **Start** | From a specific vertex | No starting vertex |
| **Time** | O(V²) or O(E log V) | O(E log E) |
| **Better for** | **Dense graphs** (E ≈ V²) | **Sparse graphs** (E << V²) |
| **Cycle avoidance** | Naturally avoided (tree grows) | Union-Find checks |

---

## 7. Exam-Ready Summary

### Quick Revision Points
1. **Dijkstra:** Greedy, select min-dist unvisited → relax neighbors. O(V²). No negative weights.
2. **Bellman-Ford:** Relax ALL edges V−1 times. O(VE). Handles negative weights + detects negative cycles.
3. **Prim's:** Start from vertex, always add cheapest crossing edge. O(V²). Good for dense graphs.
4. **Kruskal's:** Sort edges, add smallest non-cycle-forming edge. O(E log E). Good for sparse graphs.
5. **Dijkstra and MST are the HIGHEST-SCORING topics** — 5–6 marks each.

### Most Common Exam Questions
- Dijkstra full trace with table (2017, 2018, 2019, 2021–2024, 04–06 marks)
- MST using Prim's OR Kruskal's (2017–2024, 03–06 marks)
- Bellman-Ford with negative edges (2020, 2021, 2022, 2023, 03–04 marks)

---

## 8. Practice Problems (From Past Exams)

### Problem 1 [2017, 2024, 06 marks]
**Q:** Apply Dijkstra's algorithm on a graph with source A. Show the distance table at each step.

**Approach:** Draw table with columns for each vertex, rows for each step. Show selected vertex, updated distances.

### Problem 2 [2022, 2024, 04–05 marks]
**Q:** Find MST using Kruskal's algorithm. Show edge selection at each step.

**Approach:** Sort edges → table showing each edge, whether accepted/rejected, and component state.

### Problem 3 [2023, CLO5, 04 marks]
**Q:** Apply Bellman-Ford on graph with negative weight edges from source S.

**Approach:** Show distance array after each of V−1 iterations. Check for negative cycle in final pass.

---

*← [13 — Graphs](13_graphs.md) | Next: [15 — Advanced Topics →](15_advanced_topics.md)*

<br>

---
[⬅️ Previous](./13_graphs.md) | [🏠 Home](./README.md) | [Next ➡️](./15_advanced_topics.md)
