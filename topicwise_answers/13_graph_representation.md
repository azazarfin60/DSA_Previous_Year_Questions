# Graph Representation — Adjacency Matrix, Adjacency List


---

## [2017] 7(a) Draw graph from adjacency matrix. (04)

**Matrix indicates an undirected graph (symmetric). Self-loop at node 3.**

Edges from matrix:
- 1—2, 1—3, 1—4
- 2—3, 2—5
- 3—3 (self-loop)
- 4—5
```
    1 --- 2
   /|     |
  / |     |
 3--+     5
 ↺  |    /
    4---+
```
Edges: {(1,2), (1,3), (1,4), (2,3), (2,5), (3,3), (4,5)}
Node 3 has a self-loop (matrix[3][3]=1).

---


---

## [2019] Q.8(b) Adjacency matrix and adjacency list. (04)

**Graph:** 1—4, 1—2, 3—6, 4—6, 2—8, 5—7

**(i) Adjacency Matrix (8×8):**

|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 4 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| 6 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| 8 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

**(ii) Adjacency List:**
```
1 → 2 → 4
2 → 1 → 8
3 → 6
4 → 1 → 6
5 → 7
6 → 3 → 4
7 → 5
8 → 2
```

---


---

## [2020] Q.4(b) Paths of length 2 using matrix method. (03)

**Adjacency Matrix A:**

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 0 | 1 | 0 | 1 |
| B | 0 | 0 | 0 | 1 | 0 |
| C | 0 | 0 | 0 | 0 | 1 |
| D | 1 | 1 | 1 | 0 | 1 |
| E | 0 | 0 | 0 | 0 | 0 |

**A² = A × A** gives paths of length 2:

Computing A²[i][j] = Σ A[i][k] × A[k][j]:

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 0 | 0 | 0 | 1 |
| B | 1 | 1 | 1 | 0 | 1 |
| C | 0 | 0 | 0 | 0 | 0 |
| D | 0 | 0 | 1 | 1 | 2 |
| E | 0 | 0 | 0 | 0 | 0 |

**Paths of length 2:**
- A→?→E: 1 path (A→C→E)
- B→?→A: 1 path (B→D→A)
- B→?→B: 1 path (B→D→B)
- B→?→C: 1 path (B→D→C)
- B→?→E: 1 path (B→D→E)
- D→?→C: 1 path (D→A→C)
- D→?→D: 1 path (D→B→D)
- D→?→E: 2 paths (D→A→E, D→C→E)

---


---

## [2020] Q.7(b) (i) Adjacency matrix/list, (ii) BFS and DFS from A. (08)

**Graph:** A—B(1), A—D(2), B—D(3), B—E(4), C—D(2), D—E(2)

**(i) Adjacency Matrix:**

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 1 | 0 | 2 | 0 |
| B | 1 | 0 | 0 | 3 | 4 |
| C | 0 | 0 | 0 | 2 | 0 |
| D | 2 | 3 | 2 | 0 | 2 |
| E | 0 | 4 | 0 | 2 | 0 |

**Adjacency List:**
```
A → B(1) → D(2)
B → A(1) → D(3) → E(4)
C → D(2)
D → A(2) → B(3) → C(2) → E(2)
E → B(4) → D(2)
```

**(ii) BFS from A:**
Queue: [A] → visit A, enqueue B,D
Queue: [B,D] → visit B, enqueue E (D already queued)
Queue: [D,E] → visit D, enqueue C
Queue: [E,C] → visit E, visit C

> **BFS order: A → B → D → E → C**

**DFS from A:**
Stack: [A] → visit A, push B,D
Stack: [B,D] → visit D, push C,E
Stack: [B,C,E] → visit E (no new)
Stack: [B,C] → visit C (no new)
Stack: [B] → visit B (no new)

> **DFS order: A → D → E → C → B** (or A → B → E → D → C depending on neighbor ordering)

---


---

## [2022] Q.4(c) Drawbacks and advantages of adjacency list. (CO1, 02)

**Advantages:**
1. Space-efficient for sparse graphs — O(V + E) vs O(V²) for matrix
2. Iterating over neighbors is fast — O(degree) per vertex

**Drawbacks:**
1. Checking if edge (u,v) exists takes O(degree) — not O(1) like matrix
2. More complex to implement — uses linked lists/dynamic arrays
3. Not cache-friendly for dense graphs

---

# Section B

---


---

## [2024] Q.7(b) Adjacency matrix and adjacency list. (CO3, 04)

**Graph:** 1—4, 1—6, 2—4, 2—5, 3—6, 4—6, 5—7, 5—8, 7—8

**(i) Adjacency Matrix (8×8):**

|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| 2 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| 4 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 5 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 |
| 6 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| 8 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |

**(ii) Adjacency List:**
```
1 → 4 → 6
2 → 4 → 5
3 → 6
4 → 1 → 2 → 6
5 → 2 → 7 → 8
6 → 1 → 3 → 4
7 → 5 → 8
8 → 5 → 7
```

---


---

## 📊 Exam Priority
**Priority: 2/5** (Should Prepare)
**Appeared in:** 7/8 years
**Typical marks:** 02–04 per question
