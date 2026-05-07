# BFS & DFS — Traversal, Cycle Detection, Connected Components


---

## [2017] 7(b) DFS on directed graph. (04)

**Graph:** BD→UAE, BD→UK, UAE→USA, UAE→AUS, UK→JAP, AUS→RUS, RUS→UAE

**DFS starting from BD (visit left/first neighbor first):**

1. Visit **BD** → neighbors: UAE, UK
2. Visit **UAE** → neighbors: USA, AUS
3. Visit **USA** → no unvisited neighbors, backtrack
4. Visit **AUS** → neighbor: RUS
5. Visit **RUS** → neighbor: UAE (already visited), backtrack
6. Backtrack to BD → visit **UK** → neighbor: JAP
7. Visit **JAP** → no unvisited neighbors

> **DFS Order: BD → UAE → USA → AUS → RUS → UK → JAP**

---


---

## [2017] 7(c) Connected component and BFS proof. (04)

**Connected Component:** A connected component of an undirected graph G is a maximal subgraph in which every pair of vertices is connected by a path. A graph may have one or more connected components.

**Proof that BFS(v) visits all vertices in v's connected component:**

1. BFS starts at vertex v, marks it visited, and adds it to a queue.
2. For each dequeued vertex u, BFS visits all unvisited neighbors of u and enqueues them.
3. Since the component is connected, for any vertex w in the same component, there exists a path v → ... → w.
4. BFS explores vertices layer by layer (by distance). At each layer, it discovers all vertices at distance d before moving to distance d+1.
5. Since a path exists from v to every vertex w in the component, BFS will eventually reach w through some sequence of edges.
6. Vertices outside v's component have no path to v, so they are never reached.

Therefore, BFS(v) visits **exactly** all vertices in v's connected component. ∎

---


---

## [2018] Q4(c) Explain (i) DFS and (ii) BFS. (04)

**(i) DFS (Depth First Search):**
Explores a graph by going as **deep** as possible along each branch before backtracking. Uses a **Stack** (or recursion).

```
Procedure DFS(V)
    Mark V as visited
    Print V
    For each neighbor W of V do
        If W is not visited Then
            Call DFS(W)
        End If
    End For
End Procedure
```
- Time: O(V + E) | Space: O(V)
- Applications: Cycle detection, topological sorting, path finding

**(ii) BFS (Breadth First Search):**
Explores a graph level by level, visiting all neighbors before moving deeper. Uses a **Queue**.

```
Procedure BFS(S)
    Create empty Queue Q
    Mark S as visited
    Enqueue S into Q
    While Q is not empty do
        Set V = Dequeue from Q
        Print V
        For each neighbor W of V do
            If W is not visited Then
                Mark W as visited
                Enqueue W into Q
            End If
        End For
    End While
End Procedure
```
- Time: O(V + E) | Space: O(V)
- Applications: Shortest path (unweighted), level-order traversal

---

# Section B

---


---

## [2019] Q.8(c) BFS: Minimum path from A to J. (06)

**Graph:** A→{F,C,B}, B→{G}, C→{E,B}, D→{C,E,J}, E→{J,K}, F→{C,D}, G→{E,K}

**BFS Traversal from A:**

| Step | Dequeue | Queue (after processing) | Visited |
|---|---|---|---|
| 0 | — | [A] | {A} |
| 1 | A | [F, C, B] | {A, F, C, B} |
| 2 | F | [C, B, D] | {A, F, C, B, D} |
| 3 | C | [B, D, E] | {A, F, C, B, D, E} |
| 4 | B | [D, E, G] | {A, F, C, B, D, E, G} |
| 5 | D | [E, G, J] | {A, F, C, B, D, E, G, J} |
| 6 | **J found!** | — | — |

**Tracing the path back:**
- J was discovered from D
- D was discovered from F
- F was discovered from A

> **Minimum Path: A → F → D → J**
> **Path Length: 3 edges**

---

## [2021] Q.5(c) DFS iterative on the graph. (04)

**Graph:** A→D, B→C, D→E, D→C

**DFS from A (iterative using stack):**

| Step | Pop | Stack | Visited | Action |
|---|---|---|---|---|
| 0 | — | [A] | {} | Start |
| 1 | A | [D] | {A} | Push neighbor D |
| 2 | D | [E, C] | {A, D} | Push neighbors E, C |
| 3 | C | [E] | {A, D, C} | C has no unvisited neighbors |
| 4 | E | [] | {A, D, C, E} | E has no unvisited neighbors |

**Note:** Node B is not reachable from A.

Starting fresh DFS from B:

| 5 | B | [C] | {A,D,C,E,B} | C already visited |
| 6 | — | [] | {A,D,C,E,B} | Done |

> **DFS Order from A: A → D → C → E**
> **DFS Order from B: B** (C already visited)

---


---

## [2021] Q.6(c) Detect cycle in directed graph using DFS. (03)

**Graph:** A→B, B→D, C→A, C→D

**DFS from A:**
- Visit A (state: in-progress)
- Visit B (state: in-progress)
- Visit D (state: in-progress) → D has no outgoing edges → mark D as done
- Backtrack to B → mark B as done
- Backtrack to A → mark A as done

**DFS from C:**
- Visit C (state: in-progress)
- Check A → A is already **done** (not in-progress) → no cycle
- Check D → D is already **done** → no cycle
- Mark C as done

**A cycle would be detected if we encounter a node that is still "in-progress" (on the current DFS path).**

> **Result: No cycle is present in this graph.** ✓

---


---

## [2022] Q.6(a) BFS: minimum path A to J. (CO3, 04)

**Graph:** A→{F,C,B}, B→{G,C}, C→{E,G}, D→{C,E,J}, E→{J,K}, F→{C,D}, G→{E,K}

**BFS from A:**

| Step | Dequeue | Queue | Visited |
|---|---|---|---|
| 0 | — | [A] | {A} |
| 1 | A | [F, C, B] | {A,F,C,B} |
| 2 | F | [C, B, D] | {A,F,C,B,D} |
| 3 | C | [B, D, E, G] | {A,F,C,B,D,E,G} |
| 4 | B | [D, E, G] | (G already visited) |
| 5 | D | [E, G, J] | {A,F,C,B,D,E,G,J} |

**J found!** Trace back: J ← D ← F ← A

> **Minimum Path: A → F → D → J (3 edges)**

---


---

## [2023] Q.6(c) BFS: minimum path A to J. (CLO1, 04)

**Graph:** A→{B,C,F}, B→{C,G}, C→{E,G}, D→{C,E,J}, E→{J,K}, F→{C,D}, G→{E,K}

| Step | Dequeue | Queue | Visited |
|---|---|---|---|
| 0 | — | [A] | {A} |
| 1 | A | [B, C, F] | {A,B,C,F} |
| 2 | B | [C, F, G] | {A,B,C,F,G} |
| 3 | C | [F, G, E] | {A,B,C,F,G,E} |
| 4 | F | [G, E, D] | {A,B,C,F,G,E,D} |
| 5 | G | [E, D, K] | {A,B,C,F,G,E,D,K} |
| 6 | E | [D, K, J] | {A,B,C,F,G,E,D,K,J} |

**J found at level 3!** But let's trace the shortest path.

Actually checking level by level:
- Level 0: {A}
- Level 1: {B, C, F}
- Level 2: {G, E, D} (from B→G, C→E, F→D)
- Level 3: {K, J} (from E→J, D→J, G→K)

Trace back: J ← D ← F ← A (or J ← E ← C ← A)

> **Minimum Path: A → F → D → J (3 edges)**
> (Also valid: A → C → E → J)

---


---

## 📊 Exam Priority
**Priority: 2/5** (Should Prepare)
**Appeared in:** 6/8 years
**Typical marks:** 03–04 per question
