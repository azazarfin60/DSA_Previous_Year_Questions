[⬅️ Previous](./2023_answer.md) | [🏠 Home](./README.md)

---

# 2024 — ECE 2103 Answer Key (OBE)

---

## Q.1(a) Define linear/non-linear DS. Major operations. (CO1, 04)

**Linear Data Structure:** Elements arranged sequentially where each element has a unique predecessor and successor (except first and last).
- *Examples:* Array, Linked List, Stack, Queue

**Non-linear Data Structure:** Elements arranged hierarchically or in a network; each element can connect to multiple elements.
- *Examples:* Tree, Graph

**Major Operations:**
1. **Traversing** — Visiting each element exactly once
2. **Searching** — Finding the location of a specific element
3. **Inserting** — Adding a new element
4. **Deleting** — Removing an existing element
5. **Sorting** — Arranging elements in order
6. **Merging** — Combining two sorted structures into one

---

## Q.1(b) Time complexity of linear search. (CO1, 03)

**Time Complexity:** A measure of how the running time of an algorithm grows as the input size n increases. Expressed using asymptotic notation (Big-O).

**Linear Search:** Scans each element one by one until the target is found or the array ends.

```
Procedure LINEAR_SEARCH(A, N, ITEM)
    For I = 1 to N do
        If A[I] = ITEM Then
            Return I
        End If
    End For
    Return -1
End Procedure
```

- **Best Case: O(1)** — element found at first position
- **Worst Case: O(n)** — element at last position or absent
- **Average Case: O(n)** — on average checks n/2 elements

---

## Q.1(c) Properties of recursive procedure. (CO1, 03)

A recursive procedure must satisfy:

1. **Base Case (Stopping Condition):** At least one condition where the function does not call itself, preventing infinite recursion.

2. **Progressive Approach:** Each recursive call must reduce the problem size, moving closer to the base case.

3. **Self-similarity:** The problem at each level must have the same structure as the original, solvable by the same method.

**Example — Factorial:**
```
Procedure FACTORIAL(N)
    If N <= 1 Then
        Return 1                        // base case
    Else
        Return N × FACTORIAL(N - 1)     // smaller problem
    End If
End Procedure
```
FACTORIAL(4) = 4 × 3 × 2 × 1 = 24

---

## Q.2(a) Define linked list. Benefits over array. (CO2, 03)

**Linked List:** A linear data structure where elements (nodes) are stored in non-contiguous memory locations. Each node contains DATA and a LINK (pointer) to the next node.

**Benefits over Array:**
1. **Dynamic size** — grows/shrinks at runtime, no fixed size declaration
2. **Efficient insert/delete** — O(1) pointer update after reaching position, vs O(n) shifting in arrays
3. **No wasted memory** — allocates exactly what is needed
4. **No overflow** — can add nodes as long as memory exists

---

## Q.2(b) Infix→Postfix: A + (B * C − (D / E ↑ F) * G) * H (CO2, 04)

| Step | Symbol | Stack | Output (P) |
|---|---|---|---|
| 1 | A | | A |
| 2 | + | + | A |
| 3 | ( | + ( | A |
| 4 | B | + ( | A B |
| 5 | * | + ( * | A B |
| 6 | C | + ( * | A B C |
| 7 | − | + ( − | A B C * |
| 8 | ( | + ( − ( | A B C * |
| 9 | D | + ( − ( | A B C * D |
| 10 | / | + ( − ( / | A B C * D |
| 11 | E | + ( − ( / | A B C * D E |
| 12 | ↑ | + ( − ( / ↑ | A B C * D E |
| 13 | F | + ( − ( / ↑ | A B C * D E F |
| 14 | ) | + ( − | A B C * D E F ↑ / |
| 15 | * | + ( − * | A B C * D E F ↑ / |
| 16 | G | + ( − * | A B C * D E F ↑ / G |
| 17 | ) | + | A B C * D E F ↑ / G * − |
| 18 | * | + * | A B C * D E F ↑ / G * − |
| 19 | H | + * | A B C * D E F ↑ / G * − H |
| 20 | End | | A B C * D E F ↑ / G * − H * + |

> **Postfix P: A B C * D E F ↑ / G * − H * +**

---

## Q.2(c) Insert into linked list after LOC. (CO2, 03)

```
Procedure INSERT_AFTER(START, LOC, ITEM, AVAIL)
    If AVAIL = NULL Then
        Print "Overflow"
        Return
    End If
    Set NEW = AVAIL                    // get free node
    Set AVAIL = LINK[AVAIL]            // update free list
    Set INFO[NEW] = ITEM               // store data
    Set LINK[NEW] = LINK[LOC]          // point to LOC's next
    Set LINK[LOC] = NEW                // LOC now points to NEW
End Procedure
```

**Example:** Insert 25 after node containing 20:
```
Before: [10] → [20] → [30] → NULL
After:  [10] → [20] → [25] → [30] → NULL
```

---

## Q.3(a) BST structure. Advantages over unsorted list. (CO2, 03)

**BST Structure:** A binary tree where for each node:
- All values in the **left** subtree are **less than** the node
- All values in the **right** subtree are **greater than** the node
```
       20
      /  \
    10    30    (10 < 20 < 30 ✓)
```

**Advantages over unsorted list:**

| Operation | Unsorted List | BST (balanced) |
|---|---|---|
| Search | O(n) | **O(log n)** |
| Insert | O(1) at head | **O(log n)** |
| Delete | O(n) find + O(1) | **O(log n)** |
| Sorted order | O(n log n) sort | **O(n)** inorder |

BST provides logarithmic search time while maintaining dynamic structure.

---

## Q.3(b) Time complexity of nested loop. (CO2, 03)

```
for i = 1 to n:
    for j = 1 to n:
        print(i, j)
```

- Outer loop runs **n** times
- Inner loop runs **n** times for each iteration of outer loop
- `print(i,j)` executes n × n = **n²** times

> **Time Complexity: O(n²)**

---

## Q.3(c) Define 2-tree. Kruskal's MST. (CO2, 04)

**2-tree (Extended Binary Tree):** A binary tree where every node has either **0 or 2 children** — no node has exactly one child. Internal nodes have 2 children; leaf nodes (external) have 0.

**Kruskal's MST:**

**Sorted edges:**

| Edge | Weight |
|---|---|
| (3,4) | 1 |
| (0,1) | 2 |
| (2,4) | 2 |
| (1,2) | 3 |
| (2,3) | 5 |
| (1,4) | 6 |
| (0,4) | 7 |

**Selection (5 nodes → 4 edges):**

| Step | Edge | Weight | Action |
|---|---|---|---|
| 1 | (3,4) | 1 | ✅ Add |
| 2 | (0,1) | 2 | ✅ Add |
| 3 | (2,4) | 2 | ✅ Add |
| 4 | (1,2) | 3 | ✅ Add (connects {0,1} with {2,3,4}) |
| 5 | (2,3) | 5 | ✗ Cycle |

> **MST: {(3,4)=1, (0,1)=2, (2,4)=2, (1,2)=3} = 8**

---

## Q.4(a) BST from: 14,20,40,10,30,15,5,35,50,45. Traversals. Delete 20. (CO2, 05)

**(i) Build BST:**
```
           14
          /  \
        10    20
       /     /  \
      5    15    40
                /  \
              30    50
                \   /
                35 45
```

**(ii) Traversals:**

**Preorder (NLR):** 14, 10, 5, 20, 15, 40, 30, 35, 50, 45

**Inorder (LNR):** 5, 10, 14, 15, 20, 30, 35, 40, 45, 50

**Postorder (LRN):** 5, 10, 15, 35, 30, 45, 50, 40, 20, 14

**(iii) Delete 20 (two children):**
Inorder successor of 20 = **30** (smallest in right subtree).
Replace 20 with 30. Delete original 30 (30 has child 35 → 35 takes 30's place).

```
           14
          /  \
        10    30
       /     /  \
      5    15    40
                /  \
              35    50
                   /
                  45
```

---

## Q.4(b) Min-Heap from: 34,30,40,22,50,2,55,77,55. Insert 60, Delete 22. (CO2, 05)

**Building Min-Heap (insert one by one, bubble up):**

Insert 34: [34]
Insert 30: 30<34 → swap → [30, 34]
Insert 40: 40>30 → [30, 34, 40]
Insert 22: 22<34 → swap, 22<30 → swap → [22, 30, 40, 34]
Insert 50: 50>30 → [22, 30, 40, 34, 50]
Insert 2: 2<40 → swap, 2<22 → swap → [2, 30, 22, 34, 50, 40]
Insert 55: 55>22 → [2, 30, 22, 34, 50, 40, 55]
Insert 77: 77>34 → [2, 30, 22, 34, 50, 40, 55, 77]
Insert 55: 55>30 → [2, 30, 22, 34, 50, 40, 55, 77, 55]

**Final Min-Heap:**
```
            2
          /   \
        30     22
       / \    /  \
      34  50 40   55
     / \
    77  55
```

**(i) Insert 60:**
Place at index 10. Parent = index 5 (50). 60 > 50 → no swap.

```
            2
          /   \
        30     22
       / \    /  \
      34  50 40   55
     / \  /
    77 55 60
```

**(ii) Delete 22:**
Replace 22 with last element (60). Remove last. Heapify down.
- 60 at index 3. Children: 40(6), 55(7). Min child = 40.
- 60 > 40 → swap.

```
            2
          /   \
        30     40
       / \    /  \
      34  50 60   55
     / \
    77  55
```

---

# Section B

---

## Q.5(a) Quicksort on BANGLADESH — find N's position. (CO1, 04)

**Array:** B, A, N, G, L, A, D, E, S, H (indices 1–10)

**Pivot = B (first element)**

Partition: Scan from left for element > B, scan from right for element ≤ B.

**Left pointer (i):** Start at index 2
**Right pointer (j):** Start at index 10

- i=3 (N > B), j=10 (H > B) → j=9 (S > B) → j=8 (E > B) → j=7 (D > B) → j=6 (A ≤ B) → swap N and A
  Array: B, A, **A**, G, L, **N**, D, E, S, H

- i=4 (G > B), j=5 (L > B) → j=4 → j=3 (A ≤ B) → i > j → STOP

- j=3, swap pivot (B at index 1) with A[j=3]:
  Array: **A**, A, **B**, G, L, N, D, E, S, H

**B is now at final position 3.**

Now find N's final position — N is in right partition: [G, L, N, D, E, S, H]

**Pivot = G:**
- Array segment: G, L, N, D, E, S, H
- i→L(>G), j→H(>G)→S(>G)→E(≤G) → swap L and E
  → G, E, N, D, L, S, H... wait, let me re-index.

Subarray indices 4–10: G, L, N, D, E, S, H
- Pivot=G. i=5(L>G), j=10(H>G)→9(S>G)→8(E>G? E<G)→swap L,E
  → G, **E**, N, D, **L**, S, H
- i=6(N>G), j=7(D<G)→ swap N,D
  → G, E, **D**, **N**, L, S, H
- i=7(N>G), j=6→ j < i → STOP
- Swap pivot G with A[j=6]: **D**, E, **G**, N, L, S, H

**G at final position 6.** N is in right partition: [N, L, S, H]

**Pivot = N:**
Subarray: N, L, S, H
- i→S(>N), j→H(<N)→ swap S,H
  → N, L, **H**, **S**
- i→S(>N), j→H→ j < i → STOP
- Swap N with A[j]: **H**, L, **N**, S

> **N is at final position 9 in the original array.**
> **Interchanges: approximately 5 swaps** (B↔A, N↔A, L↔E, N↔D, G↔D, S↔H, N↔H)

---

## Q.5(b) Dijkstra's from A. (CO3, 06)

**Graph:** A→B(6), A→D(10), A→C(12), B→D(3), C→E(5), D→B(7), D→E(5), D→C(4)

**Initialization:**

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | 0 | ∞ | ∞ | ∞ | ∞ |

**Iteration 1: Visit A (dist=0)**
- A→B: 6, A→D: 10, A→C: 12

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | 6 | 12 | 10 | ∞ |

**Iteration 2: Visit B (dist=6)**
- B→D: 6+3=9 < 10 → update D=9

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | **6** | 12 | 9 | ∞ |

**Iteration 3: Visit D (dist=9)**
- D→B: 9+7=16 > 6
- D→E: 9+5=14
- D→C: 9+4=13 > 12

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | **6** | 12 | **9** | 14 |

**Iteration 4: Visit C (dist=12)**
- C→E: 12+5=17 > 14

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | **6** | **12** | **9** | 14 |

**Iteration 5: Visit E (dist=14)** — no outgoing updates.

**Final Shortest Paths from A:**

| Destination | Distance | Path |
|---|---|---|
| A → B | 6 | A → B |
| A → D | 9 | A → B → D |
| A → C | 12 | A → C |
| A → E | 14 | A → B → D → E |

---

## Q.6(a) What is B-tree? Structure and operations. (CO2, 03)

**B-tree:** A self-balancing search tree where each node can have more than two children. Designed for systems that read/write large blocks of data (databases, file systems).

**Structure (B-tree of order m):**
- Each node has at most **m children** and **m-1 keys**
- Each node (except root) has at least **⌈m/2⌉ children**
- All **leaf nodes are at the same level**
- Keys within a node are sorted

**Example (order 3):**
```
        [30]
       /    \
   [10,20]  [40,50]
```

**Operations:**
1. **Search** — similar to BST but with multi-way branching → O(log n)
2. **Insertion** — insert in leaf; if node overflows (>m-1 keys), split and push median up
3. **Deletion** — remove key; if underflow, borrow from sibling or merge nodes

---

## Q.6(b) Reverse a singly linked list. (CO1, 04)

```
Procedure REVERSE_LIST(HEAD)
    Set PREV = NULL
    Set CURR = HEAD
    While CURR ≠ NULL do
        Set NEXT_NODE = LINK[CURR]     // save next
        Set LINK[CURR] = PREV          // reverse pointer
        Set PREV = CURR                // advance PREV
        Set CURR = NEXT_NODE           // advance CURR
    End While
    Set HEAD = PREV                    // new head
    Return HEAD
End Procedure
```

**Trace:** 1 → 2 → 3 → 4 → NULL

| Step | PREV | CURR | NEXT | List State |
|---|---|---|---|---|
| 1 | NULL | 1 | 2 | NULL ← 1, 2→3→4 |
| 2 | 1 | 2 | 3 | NULL ← 1 ← 2, 3→4 |
| 3 | 2 | 3 | 4 | NULL ← 1 ← 2 ← 3, 4 |
| 4 | 3 | 4 | NULL | NULL ← 1 ← 2 ← 3 ← 4 |
| End | 4 | NULL | — | HEAD = 4 |

> **Output: 4 → 3 → 2 → 1 → NULL** ✓
> **Time: O(n), Space: O(1)**

---

## Q.6(c) "Performance analysis is far better than performance measurement." (CO2, 03)

**Performance Analysis (a priori):** Uses mathematical tools (Big-O, recurrence) to evaluate algorithm efficiency **before** coding. Machine-independent.

**Performance Measurement (a posteriori):** Measures actual execution time **after** implementation. Machine-dependent.

**Why analysis is better:**
1. **Machine-independent** — valid across all hardware configurations
2. **Done early** — choose the best algorithm before investing coding effort
3. **Predicts scalability** — shows behavior for any input size n
4. **Fair comparison** — two algorithms compared on equal theoretical footing

Measurement is useful for fine-tuning but cannot replace theoretical analysis for algorithm selection.

---

## Q.7(a) Define spanning tree. Prim's MST. (CO3, 03)

**Spanning Tree:** A subgraph of a connected graph that includes **all vertices**, is connected, has no cycles, and contains exactly **V-1 edges**.

**Prim's MST (starting from node 1):**

| Step | Add Node | Edge | Cost | MST Nodes |
|---|---|---|---|---|
| 1 | 1 | — | — | {1} |
| 2 | 2 | (1,2) | 10 | {1,2} |
| 3 | 6 | (6,1) | 30 | {1,2,6} |
| 4 | 4 | (4,6) | 15 | {1,2,4,6} |
| 5 | 7 | (6,7) | 20 | {1,2,4,6,7} |
| 6 | 5 | (4,5) | 25 | {1,2,4,5,6,7} |
| 7 | 3 | (3,4) | 35 | {1,2,3,4,5,6,7} |

> **MST: {(1,2)=10, (6,1)=30, (4,6)=15, (6,7)=20, (4,5)=25, (3,4)=35} = 135**

---

## Q.7(b) Adjacency matrix and adjacency list. (CO3, 04)

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

## Q.7(c) Advantages of Header linked list. (CO2, 03)

A **Header Linked List** has a special node at the beginning (header node) that doesn't store actual data.

**Advantages:**

1. **Simplified operations** — list is never empty (START always points to header). No special case for inserting/deleting the first element.

2. **Metadata storage** — header can store count of nodes, making length queries O(1).

3. **Uniform algorithms** — all insertions happen after some node, no need to update START pointer.

**Example:**
```
Header → [count=3] → [10] → [20] → [30] → NULL
```
Insert 5 at beginning: just insert after header node — no START pointer change.

---

## Q.8(a) NP-Hard, NP-Complete, and backtracking. (CO3, 03)

**NP-Hard:** Problems at least as hard as any NP problem. No known polynomial-time algorithm exists. May not have polynomial-time verification.

**NP-Complete:** Problems that are both in NP (verifiable in polynomial time) and NP-Hard. If any NP-Complete problem is solved in polynomial time, all NP problems can be.

**Relation to Backtracking:**
Since NP-Hard/NP-Complete problems have no known efficient solution, **backtracking** is used as a practical approach. It systematically explores all possible solutions, pruning branches that violate constraints. Examples:
- **N-Queens** (NP) — backtracking tries all placements, prunes conflicts
- **Subset Sum** (NP-Complete) — backtracking explores include/exclude for each element
- **TSP** (NP-Hard) — backtracking explores all permutations of cities

---

## Q.8(b) Two-way vs singly linked list. (CO3, 03)

| Criterion | Singly Linked List | Doubly Linked List |
|---|---|---|
| Pointers per node | 1 (NEXT only) | 2 (NEXT + PREV) |
| Traversal | Forward only | Both directions |
| Delete given node | O(n) — need predecessor | **O(1)** — PREV available |
| Memory | Less per node | More per node |
| Insertion before node | O(n) | **O(1)** |
| Complexity | Simpler | More complex |

**Example:**
```
Singly: [10|→] → [20|→] → [30|NULL]

Doubly: [NULL←|10|→] ↔ [←|20|→] ↔ [←|30|NULL→]
```

In doubly linked list, deleting node 20 requires only updating 10's NEXT and 30's PREV — O(1).

---

## Q.8(c) 4-Queens backtracking. (CO2, 04)

**Problem:** Place 4 queens on 4×4 board — no two share row, column, or diagonal.

**Backtracking trace:**

**Try Row 1, Col 1:** Place Q1
- Row 2, Col 1: ✗ (same col) | Col 2: ✗ (diagonal) | Col 3: Place Q2
  - Row 3, Col 1: ✗ (diagonal Q2) | Col 2: ✗ (diagonal Q1) | Col 3: ✗ (col Q2) | Col 4: ✗ (diagonal Q2)
  - **Backtrack** Row 2
- Row 2, Col 4: Place Q2
  - Row 3, Col 1: ✗ (diagonal Q1) | Col 2: Place Q3
    - Row 4, Col 1: ✗ (col Q1) | Col 2: ✗ (col Q3) | Col 3: ✗ (diagonal) | Col 4: ✗ (col Q2)
    - **Backtrack**
  - **Backtrack** Row 1

**Try Row 1, Col 2:** Place Q1
- Row 2, Col 4: Place Q2
  - Row 3, Col 1: Place Q3
    - Row 4, Col 3: Place Q4 ✓ **SOLUTION 1!**

**Solution 1: [2, 4, 1, 3]**
```
  1 2 3 4
1 . Q . .
2 . . . Q
3 Q . . .
4 . . Q .
```

**Solution 2: [3, 1, 4, 2]**
```
  1 2 3 4
1 . . Q .
2 Q . . .
3 . . . Q
4 . Q . .
```

> **Two solutions exist for the 4-Queens problem.**

<br>

---
[⬅️ Previous](./2023_answer.md) | [🏠 Home](./README.md)
