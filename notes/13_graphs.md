[⬅️ Previous](./12_hashing.md) | [🏠 Home](./README.md) | [Next ➡️](./14_graph_algorithms.md)

---

# 📘 Chapter 13: Graphs — Representation, BFS, DFS

> **Exam Frequency:** 7/8 (representation), 6/8 (BFS/DFS) | **Typical Marks:** 02–06 | **Section:** B
> **Key Topics:** Adjacency Matrix/List, BFS, DFS — full traces with pseudocode

---

## 1. What is a Graph?

A **graph** G = (V, E) consists of:
- **V** = set of **vertices** (nodes)
- **E** = set of **edges** (connections between vertices)

### Types

| Type | Description | Example |
|---|---|---|
| **Undirected** | Edges have no direction (A—B means both ways) | Road between two cities |
| **Directed (Digraph)** | Edges have direction (A→B is one-way) | One-way street |
| **Weighted** | Edges have costs/distances | Road with distance labels |
| **Unweighted** | All edges have equal weight | Simple connections |

```
Undirected:          Directed:           Weighted:
  A --- B            A → B              A --5-- B
  |     |            ↑     ↓            |       |
  C --- D            C ← D             3       2
                                        |       |
                                        C --4-- D
```

### Terminology

| Term | Definition |
|---|---|
| **Adjacent** | Two vertices connected by an edge |
| **Degree** | Number of edges incident to a vertex |
| **Path** | Sequence of vertices connected by edges |
| **Cycle** | Path that starts and ends at the same vertex |
| **Connected** | Path exists between every pair of vertices |
| **Complete graph** | Every vertex connected to every other vertex |

---

## 2. Graph Representation

### 2.1 Adjacency Matrix

A **V × V matrix** where entry `M[i][j] = 1` if edge (i, j) exists, else 0. For weighted graphs, store the weight instead of 1.

**Example — Undirected Graph:**
```
  A --- B
  |   / |
  | /   |
  C --- D

Adjacency Matrix:
     A  B  C  D
  A [ 0  1  1  0 ]
  B [ 1  0  1  1 ]
  C [ 1  1  0  1 ]
  D [ 0  1  1  0 ]
```

**Properties:**
- **Symmetric** for undirected graphs (M[i][j] = M[j][i])
- **Not symmetric** for directed graphs
- **Space:** O(V²) — regardless of number of edges
- **Edge check:** O(1) — just check M[i][j]
- **Find all neighbors:** O(V) — scan entire row

**Example — Weighted Directed Graph:**
```
  A --5→ B
  |       ↓
  3       2
  ↓       ↓
  C ←-4-- D

Adjacency Matrix (∞ = no edge):
     A   B   C   D
  A [ 0   5   3   ∞ ]
  B [ ∞   0   ∞   2 ]
  C [ ∞   ∞   0   ∞ ]
  D [ ∞   ∞   4   0 ]
```

---

### 2.2 Adjacency List

Each vertex stores a **linked list** of its neighbors.

**Example — Same undirected graph:**
```
  A → [B] → [C] → NULL
  B → [A] → [C] → [D] → NULL
  C → [A] → [B] → [D] → NULL
  D → [B] → [C] → NULL
```

**For weighted graph, store (neighbor, weight) pairs:**
```
  A → [(B,5)] → [(C,3)] → NULL
  B → [(D,2)] → NULL
  D → [(C,4)] → NULL
  C → NULL
```

**Properties:**
- **Space:** O(V + E) — proportional to actual edges
- **Edge check:** O(degree(v)) — must search neighbor list
- **Find all neighbors:** O(degree(v)) — direct access

---

### 2.3 Comparison

| Criterion | Adjacency Matrix | Adjacency List |
|---|---|---|
| **Space** | O(V²) | O(V + E) |
| **Check if edge (u,v) exists** | **O(1)** | O(degree(u)) |
| **List all neighbors of u** | O(V) | **O(degree(u))** |
| **Add edge** | O(1) | O(1) |
| **Dense graphs** (E ≈ V²) | **Better** | More overhead |
| **Sparse graphs** (E << V²) | Wastes memory | **Better** |
| **BFS/DFS traversal** | O(V²) | **O(V + E)** |

---

## 3. Breadth-First Search (BFS)

### Concept
BFS explores a graph **level by level** — visit all neighbors of the current vertex before moving to the next level. Uses a **queue**.

### Intuition
Think of **ripples in a pond** — when you drop a stone, waves spread outward in concentric circles. BFS visits nodes in order of their distance from the starting point.

### Algorithm
**C++ Style:**
```cpp
#include <queue>
#include <vector>

void BFS(vector<vector<int>>& adj, int V, int start) {
    vector<bool> visited(V, false);
    queue<int> q;
    
    visited[start] = true;
    q.push(start);
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        cout << u << " "; // Process u
        
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
}
```

**OR, Textbook Style:**
```
Procedure BFS(G, start)
    Create Queue Q
    Create Visited array (all FALSE)
    
    Set Visited[start] = TRUE
    ENQUEUE(Q, start)
    
    While Q is not empty do
        Set u = DEQUEUE(Q)
        Process u (print, etc.)
        
        For each neighbor v of u do
            If Visited[v] = FALSE Then
                Set Visited[v] = TRUE
                ENQUEUE(Q, v)
            End If
        End For
    End While
End Procedure
```

### C Code
```c
void BFS(int adj[][MAX], int V, int start) {
    int visited[MAX] = {0};
    int queue[MAX], front = 0, rear = -1;
    
    visited[start] = 1;
    queue[++rear] = start;
    
    while (front <= rear) {
        int u = queue[front++];         // dequeue
        printf("%d ", u);
        
        for (int v = 0; v < V; v++) {
            if (adj[u][v] && !visited[v]) {
                visited[v] = 1;
                queue[++rear] = v;      // enqueue
            }
        }
    }
}
```

### BFS Trace Example (appeared in 2019, 2022, 2023)

**Graph:**
```
  A --- B --- E
  |   / |     |
  | /   |     |
  C --- D --- F
  |           |
  G --- H --- I --- J
```

**BFS from A (alphabetical neighbor order):**

| Step | Dequeue | Queue (after processing) | Visited |
|---|---|---|---|
| Init | — | [A] | {A} |
| 1 | A | [B, C] | {A, B, C} |
| 2 | B | [C, D, E] | {A, B, C, D, E} |
| 3 | C | [D, E, G] | {A, B, C, D, E, G} |
| 4 | D | [E, G, F] | {A, B, C, D, E, F, G} |
| 5 | E | [G, F] | (no new neighbors) |
| 6 | G | [F, H] | {A, B, C, D, E, F, G, H} |
| 7 | F | [H, I] | {A, B, C, D, E, F, G, H, I} |
| 8 | H | [I] | (no new) |
| 9 | I | [J] | {A, B, C, D, E, F, G, H, I, J} |
| 10 | J | [] | (done) |

> **BFS order: A, B, C, D, E, G, F, H, I, J** ✅

**Time:** O(V + E)  **Space:** O(V) for queue and visited array.

---

## 4. Depth-First Search (DFS)

### Concept
DFS explores a graph by going as **deep as possible** along each branch before **backtracking**. Uses a **stack** (or recursion).

### Intuition
Think of exploring a **maze** — you go down one path as far as possible, and when you hit a dead end, you backtrack to the last fork and try another path.

### Algorithm (Recursive)
**C++ Style:**
```cpp
#include <vector>

void DFS(vector<vector<int>>& adj, int u, vector<bool>& visited) {
    visited[u] = true;
    cout << u << " "; // Process u
    
    for (int v : adj[u]) {
        if (!visited[v]) {
            DFS(adj, v, visited);
        }
    }
}
```

**OR, Textbook Style:**
```
Procedure DFS(G, u, Visited)
    Set Visited[u] = TRUE
    Process u
    
    For each neighbor v of u do
        If Visited[v] = FALSE Then
            DFS(G, v, Visited)
        End If
    End For
End Procedure
```

### Algorithm (Iterative with Stack)
**C++ Style:**
```cpp
#include <stack>
#include <vector>

void dfsIterative(vector<vector<int>>& adj, int V, int start) {
    vector<bool> visited(V, false);
    stack<int> s;
    
    s.push(start);
    
    while (!s.empty()) {
        int u = s.top();
        s.pop();
        
        if (!visited[u]) {
            visited[u] = true;
            cout << u << " "; // Process u
            
            // Push neighbors in reverse order so they are visited in normal order
            for (auto it = adj[u].rbegin(); it != adj[u].rend(); ++it) {
                int v = *it;
                if (!visited[v]) {
                    s.push(v);
                }
            }
        }
    }
}
```

**OR, Textbook Style:**
```
Procedure DFS_ITERATIVE(G, start)
    Create Stack S
    Create Visited array (all FALSE)
    
    PUSH(S, start)
    
    While S is not empty do
        Set u = POP(S)
        If Visited[u] = FALSE Then
            Set Visited[u] = TRUE
            Process u
            
            For each neighbor v of u (in reverse order) do
                If Visited[v] = FALSE Then
                    PUSH(S, v)
                End If
            End For
        End If
    End While
End Procedure
```

### DFS Trace (same graph)

**DFS from A (alphabetical, recursive):**
```
DFS(A): Visit A → neighbors B, C
  DFS(B): Visit B → neighbors A(visited), C, D, E
    DFS(C): Visit C → neighbors A(v), B(v), D, G
      DFS(D): Visit D → neighbors B(v), C(v), F
        DFS(F): Visit F → neighbors D(v), E, I
          DFS(E): Visit E → neighbors B(v), F(v) → backtrack
          DFS(I): Visit I → neighbors F(v), H, J
            DFS(H): Visit H → neighbors G, I(v)
              DFS(G): Visit G → neighbors C(v), H(v) → backtrack
            DFS(J): Visit J → neighbors I(v) → backtrack
```

> **DFS order: A, B, C, D, F, E, I, H, G, J** ✅

**Time:** O(V + E)  **Space:** O(V) for recursion stack.

---

## 5. BFS vs DFS

| Criterion | BFS | DFS |
|---|---|---|
| **Data structure** | Queue (FIFO) | Stack/Recursion (LIFO) |
| **Traversal pattern** | Level by level (wide) | Branch by branch (deep) |
| **Shortest path** | ✅ Yes (unweighted graphs) | ❌ No guarantee |
| **Memory** | O(V) — can be large for wide graphs | O(V) — deep graphs |
| **Complete?** | Yes | Yes (for finite graphs) |
| **Use cases** | Shortest path, level-order, social network | Cycle detection, topological sort, maze |
| **Time** | O(V + E) | O(V + E) |

---

## 6. Applications of BFS and DFS

| Application | Algorithm | Why |
|---|---|---|
| Shortest path (unweighted) | BFS | Visits nodes in order of distance |
| Level-order traversal | BFS | Naturally visits level by level |
| Connected components | BFS or DFS | Mark all reachable nodes |
| Cycle detection | DFS | Back edges indicate cycles |
| Topological sorting | DFS | Post-order gives reverse topological order |
| Path finding in maze | DFS | Explores one complete path before backtracking |

---

## 7. Exam-Ready Summary

### Quick Revision Points
1. **Adjacency Matrix:** O(V²) space, O(1) edge check, good for dense graphs
2. **Adjacency List:** O(V+E) space, O(degree) edge check, good for sparse graphs
3. **BFS:** Queue-based, level-by-level, finds shortest path in unweighted graph
4. **DFS:** Stack/recursion-based, goes deep first, good for cycle detection
5. **Both:** O(V + E) time complexity
6. **BFS from A to J** — appears in 2019, 2022, 2023 exams!

---

## 8. Practice Problems (From Past Exams)

### Problem 1 [2019, 2022, 2023, 03–06 marks]
**Q:** Perform BFS from A on the graph with vertices A–J. Show queue state at each step.

**Answer:** See Section 3 trace above.

### Problem 2 [Typical, 03 marks]
**Q:** Represent the following graph using adjacency matrix AND adjacency list.

**Approach:** Draw V×V matrix with 1s for edges → draw linked lists per vertex.

### Problem 3 [2020, 08 marks]
**Q:** Perform both BFS and DFS on a given graph. Show traversal order.

**Approach:** BFS with queue trace + DFS with stack/recursion trace.

---

*← [12 — Hashing](12_hashing.md) | Next: [14 — Graph Algorithms →](14_graph_algorithms.md)*

<br>

---
[⬅️ Previous](./12_hashing.md) | [🏠 Home](./README.md) | [Next ➡️](./14_graph_algorithms.md)
