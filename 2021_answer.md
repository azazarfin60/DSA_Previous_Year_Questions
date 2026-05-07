# 2021 — ECE 2103 Answer Key

---

## Q.1(a) What is DS? Describe four basic operations. (04)

**Data Structure:** A systematic way of organizing, storing, and managing data in a computer so that it can be accessed and modified efficiently.

**Four Basic Operations:**

1. **Traversing** — Visiting each element exactly once to process or display it. Example: printing all elements of an array.
2. **Searching** — Finding the location of a specific element. Example: binary search in a sorted array → O(log n).
3. **Inserting** — Adding a new element at a specified position. Example: inserting a node in a linked list.
4. **Deleting** — Removing an element from the structure. Example: deleting a node from a BST.

---

## Q.1(b) Binary search recursive pseudocode + time complexity. (05)

```
Procedure BINARY_SEARCH(A, BEG, END, ITEM)
    If BEG > END Then
        Print "Item not found"
        Return -1
    End If
    Set MID = FLOOR((BEG + END) / 2)
    If A[MID] = ITEM Then
        Return MID                              // found
    Else If ITEM < A[MID] Then
        Return BINARY_SEARCH(A, BEG, MID-1, ITEM)  // left half
    Else
        Return BINARY_SEARCH(A, MID+1, END, ITEM)  // right half
    End If
End Procedure
```

**Time Complexity Analysis:**
- Each call halves the search space: T(n) = T(n/2) + O(1)
- **Best Case: O(1)** — element found at middle on first check
- **Worst Case: O(log n)** — element at deepest level or absent. After k calls, n/2^k = 1 → k = log₂n
- **Average Case: O(log n)** — on average, searches log₂n levels

**Space Complexity:** O(log n) due to recursion stack.

---

## Q.1(c) "DS can reduce time and space complexity" — justify. (03)

**Example 1 — Time reduction:**
Searching 1,000,000 items:
- Using unsorted array (linear search): O(n) = 1,000,000 comparisons
- Using BST: O(log n) = ~20 comparisons
- Using Hash Table: O(1) = 1 comparison average

Choosing the right data structure reduces time drastically.

**Example 2 — Space reduction:**
Storing a sparse matrix (1000×1000 with only 50 non-zero elements):
- Using 2D array: 1,000,000 memory cells (wasteful)
- Using linked list of triplets (row, col, value): only 50 × 3 = 150 cells

Proper data structure choice saves both time and space.

---

## Q.2(a) What is linked list? Benefits over array. (03)

**Linked List:** A linear data structure where elements (nodes) are stored in non-contiguous memory locations. Each node contains a DATA field and a LINK (pointer) field pointing to the next node.

**Benefits over Array:**
1. **Dynamic size** — grows/shrinks at runtime; no need to declare fixed size
2. **Efficient insertion/deletion** — O(1) pointer update vs O(n) shifting in arrays
3. **No wasted memory** — allocates exactly as much as needed
4. **No overflow** — can keep adding nodes as long as memory is available

---

## Q.2(b) Can binary search be applied on sorted linked list? (02)

**No**, binary search cannot be efficiently applied on a linked list.

**Reason:** Binary search requires **random access** to the middle element in O(1) time. Linked lists only support **sequential access** — reaching the middle element requires traversing n/2 nodes, which is O(n). This eliminates the advantage of binary search, making it O(n log n) overall — worse than simple linear search O(n).

---

## Q.2(c) Insert into linked list after node at LOC. (03)

```
Procedure INSERT_AFTER(START, LOC, ITEM, AVAIL)
    // Insert ITEM after the node at location LOC
    If AVAIL = NULL Then
        Print "Overflow — no free space"
        Return
    End If
    Set NEW = AVAIL                    // take node from free pool
    Set AVAIL = LINK[AVAIL]            // update free pool
    Set INFO[NEW] = ITEM               // store data
    Set LINK[NEW] = LINK[LOC]          // new node points to LOC's next
    Set LINK[LOC] = NEW                // LOC now points to new node
End Procedure
```

**Example:** Insert 25 after node at LOC (which has value 20):
```
Before: ... → [20|→30] → [30|→40] → ...
After:  ... → [20|→25] → [25|→30] → [30|→40] → ...
```

---

## Q.2(d) Pseudocode for adding two polynomials. (04)

```
Procedure ADD_POLYNOMIALS(P1, P2)
    // P1, P2 are linked lists: each node has [COEFF | EXPO | NEXT]
    // RESULT is the output polynomial (linked list)
    Set PTR1 = P1, PTR2 = P2
    Create empty list RESULT

    While PTR1 ≠ NULL AND PTR2 ≠ NULL do
        If EXPO[PTR1] = EXPO[PTR2] Then
            Set SUM = COEFF[PTR1] + COEFF[PTR2]
            If SUM ≠ 0 Then
                Append (SUM, EXPO[PTR1]) to RESULT
            End If
            Set PTR1 = NEXT[PTR1]
            Set PTR2 = NEXT[PTR2]
        Else If EXPO[PTR1] > EXPO[PTR2] Then
            Append (COEFF[PTR1], EXPO[PTR1]) to RESULT
            Set PTR1 = NEXT[PTR1]
        Else
            Append (COEFF[PTR2], EXPO[PTR2]) to RESULT
            Set PTR2 = NEXT[PTR2]
        End If
    End While

    // Copy remaining terms
    While PTR1 ≠ NULL do
        Append (COEFF[PTR1], EXPO[PTR1]) to RESULT
        Set PTR1 = NEXT[PTR1]
    End While
    While PTR2 ≠ NULL do
        Append (COEFF[PTR2], EXPO[PTR2]) to RESULT
        Set PTR2 = NEXT[PTR2]
    End While

    Return RESULT
End Procedure
```

**Result for given polynomials:**
P₁(x) = 3x⁵ − 4x³ + 6x − 5
P₂(x) = 2x⁸ + 7x⁵ − 3x²

**P₁ + P₂ = 2x⁸ + 10x⁵ − 4x³ − 3x² + 6x − 5**

---

## Q.3(a) Infix→Postfix: A + (B * C − (D/E ↑ F) * G) * H (04)

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

## Q.3(b) Queue operations. (04)

**Initial Queue:** [10, 20, 30, 40] (FRONT=10, REAR=40)

**Dequeue 2 times:**
1. Remove 10 → [20, 30, 40]
2. Remove 20 → [30, 40]

**Enqueue 5, 15, 25:**
3. Add 5 → [30, 40, 5]
4. Add 15 → [30, 40, 5, 15]
5. Add 25 → [30, 40, 5, 15, 25]

**Dequeue 4 times:**
6. Remove 30 → [40, 5, 15, 25]
7. Remove 40 → [5, 15, 25]
8. Remove 5 → [15, 25]
9. Remove 15 → [25]

> **Final Queue: [25]**

---

## Q.3(c) Priority Queue — array and heap representation. (04)

**Given:** AAA|1, BBB|2, CCC|2, DDD|4, EEE|4, FFF|4, GGG|5

**Array Representation (one array per priority level):**
```
Priority 1: [AAA]
Priority 2: [BBB, CCC]
Priority 3: (empty)
Priority 4: [DDD, EEE, FFF]
Priority 5: [GGG]
```

**Disadvantages of array:**
1. Wasted space for empty priority levels
2. Fixed size — cannot dynamically add elements
3. Deletion from front requires shifting elements O(n)

**Heap Representation (Min-Heap by priority):**
```
         AAA|1
        /     \
    BBB|2     CCC|2
    /   \     /   \
 DDD|4 EEE|4 FFF|4 GGG|5
```

**Advantages of heap:**
1. Insert: O(log n) — add at end, bubble up
2. Delete-min: O(log n) — remove root, heapify down
3. No wasted space — compact array representation
4. Much faster than array's O(n) for deletions

---

## Q.4(a) Complete binary tree. Array representation. (04)

**Complete Binary Tree:** A binary tree where all levels are completely filled **except possibly the last level**, and the last level has all nodes **as far left as possible**.

**Conditions:**
1. All levels 0 to h-1 are fully filled
2. At level h, nodes are filled from left to right without gaps

**Array representation of given tree:**

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value | 45 | 22 | 77 | 11 | 30 | 25 | 90 | 15 | — | 25 | — | — | — | 88 |

**Note:** This tree is **not** a complete binary tree because there are gaps (index 9, 11, 12, 13 are empty while index 10, 14 have values). A complete binary tree would have no gaps.

---

## Q.4(b) Importance of BST over array and linked list. (03)

| Operation | Sorted Array | Linked List | BST (balanced) |
|---|---|---|---|
| Search | O(log n) | O(n) | **O(log n)** |
| Insert | O(n) — shifting | O(n) — finding position | **O(log n)** |
| Delete | O(n) — shifting | O(n) — finding node | **O(log n)** |
| Dynamic size | No (fixed) | Yes | **Yes** |

**BST combines the advantages of both:**
- Fast search like sorted array (O(log n))
- Dynamic size like linked list (no fixed size)
- Fast insert/delete unlike both (O(log n))

---

## Q.4(c) BST: J,R,D,G,T,E,M,H,P,A,F,Q — build and delete D. (05)

**(i) Building the BST:**

- J → root
- R → right of J
- D → left of J
- G → right of D
- T → right of R
- E → left of G
- M → left of R
- H → right of G
- P → right of M
- A → left of D
- F → right of E
- Q → left of T... wait, Q > R but Q < T → left of T

```
            J
           / \
          D    R
         / \  / \
        A  G M   T
          /\ \  /
         E  H P Q
          \
           F
```

**(ii) Delete node D (has two children):**
Replace D with its **inorder successor** = E (smallest in D's right subtree).
Then delete E from its original position (E has one child F, so F takes E's place).

```
            J
           / \
          E    R
         / \  / \
        A  G M   T
          /\ \  /
         F  H P Q
```

---

# Section B

---

## Q.5(a) Insert 11 into min heap. (03)

**Initial Min Heap:** [8, 22, 33, 25, 44, 40, 55, 55, 33]

```
          8
        /   \
      22     33
     / \    /  \
    25  44 40  55
   / \
  55  33
```

**Insert 11:** Place at next position (left child of 44, index 10), then bubble up.

- 11 < 44 → swap with 44
- 11 < 22 → swap with 22

```
          8
        /   \
      11     33
     / \    /  \
    25  22 40  55
   / \  /
  55 33 44
```

> **Result: [8, 11, 33, 25, 22, 40, 55, 55, 33, 44]**

---

## Q.5(b) Linked representation of directed graph. (02)

**Graph:** A→D, B→C, D→E, D→C

**Adjacency List (Linked Representation):**
```
A → D → NULL
B → C → NULL
C → NULL
D → E → C → NULL
E → NULL
```

---

## Q.5(c) DFS iterative on the graph. (04)

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

## Q.5(d) MST of graph G. (03)

**Edges sorted:** D—E(1), D—G(1), A—D(2), A—B(2), B—E(2), B—D(2), A—G(2), F—G(2), G—H(2), C—F(3), E—H(3)

**Kruskal's (8 nodes → 7 edges):**

| Step | Edge | Weight | Action |
|---|---|---|---|
| 1 | D—E | 1 | ✅ Add |
| 2 | D—G | 1 | ✅ Add |
| 3 | A—D | 2 | ✅ Add (connects A) |
| 4 | A—B | 2 | ✅ Add (connects B) |
| 5 | B—E | 2 | ✗ Cycle (A-B, A-D-E) |
| 6 | B—D | 2 | ✗ Cycle |
| 7 | A—G | 2 | ✗ Cycle |
| 8 | F—G | 2 | ✅ Add (connects F) |
| 9 | G—H | 2 | ✅ Add (connects H) |
| 10 | C—F | 3 | ✅ Add (connects C) |

> **MST: {D—E(1), D—G(1), A—D(2), A—B(2), F—G(2), G—H(2), C—F(3)} = 13**

---

## Q.6(a) "Performance analysis is far better than performance measurement." (03)

**Performance Analysis (a priori):** Determines algorithm efficiency **before** implementation using mathematical analysis (Big-O, recurrence). It is machine-independent and gives a general measure.

**Performance Measurement (a posteriori):** Measures actual running time **after** implementation on a specific machine. Depends on hardware, compiler, OS, and load.

**Why analysis is better:**
1. **Machine-independent** — results valid across all computers
2. **Done early** — before spending time coding; helps choose the best algorithm upfront
3. **Predicts scalability** — shows how performance changes with larger inputs
4. **Objective comparison** — two algorithms can be compared without implementation bias

Measurement is useful for fine-tuning but cannot replace theoretical analysis.

---

## Q.6(b) Bellman-Ford algorithm. When to use it. (04)

**Bellman-Ford Algorithm:** A single-source shortest path algorithm that finds shortest distances from a source vertex to all other vertices, even with **negative edge weights**.

**How it works:**
1. Initialize: dist[source] = 0, dist[all others] = ∞
2. Repeat **V-1 times**: For each edge (u, v, w), if dist[u] + w < dist[v], update dist[v]
3. **Negative cycle check:** Do one more iteration. If any distance decreases, a negative cycle exists.

**When to use:**
- When the graph has **negative edge weights** (Dijkstra fails here)
- When you need to **detect negative cycles**
- Works on both directed and undirected graphs

**Time Complexity:** O(V × E)

---

## Q.6(c) Detect cycle in directed graph using DFS. (03)

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

## Q.6(d) Head recursion and tail recursion. (02)

**Head Recursion:** The recursive call is the **first** statement in the function. Processing happens **after** the recursive call returns.
```
Procedure HEAD_EXAMPLE(N)
    If N > 0 Then
        Call HEAD_EXAMPLE(N - 1)    // recursive call first
        Print N                      // processing after
    End If
End Procedure
```
HEAD_EXAMPLE(3) prints: 1 2 3

**Tail Recursion:** The recursive call is the **last** statement in the function. Processing happens **before** the recursive call.
```
Procedure TAIL_EXAMPLE(N)
    If N > 0 Then
        Print N                      // processing first
        Call TAIL_EXAMPLE(N - 1)    // recursive call last
    End If
End Procedure
```
TAIL_EXAMPLE(3) prints: 3 2 1

---

## Q.7(a) Why hashing? How does it overtake BST? (03)

**Why we need hashing:**
We need O(1) average-time operations. Even a balanced BST takes O(log n). For millions of records, even log n can be significant.

**How hashing overtakes BST:**

| Operation | BST (balanced) | Hash Table |
|---|---|---|
| Search | O(log n) | **O(1)** avg |
| Insert | O(log n) | **O(1)** avg |
| Delete | O(log n) | **O(1)** avg |

Hashing uses a hash function h(k) to map keys directly to array indices, providing constant-time access. For n = 1,000,000: BST needs ~20 comparisons; hash table needs ~1.

**Trade-off:** Hash tables don't support ordered operations (finding min/max, range queries) — BST is better for those.

---

## Q.7(b) Collision in hashing. One resolution method. (04)

**Collision:** When two different keys map to the same hash table index.
Example: h(k) = k mod 10. h(25) = 5 and h(35) = 5 → collision at index 5.

**Method: Separate Chaining**
Each slot stores a linked list. All keys that hash to the same index are stored in the chain.

**Example:** h(k) = k mod 7, insert: 10, 17, 24, 31

- h(10) = 3, h(17) = 3, h(24) = 3, h(31) = 3 → all at index 3

```
Index 0: → NULL
Index 1: → NULL
Index 2: → NULL
Index 3: → 10 → 17 → 24 → 31 → NULL
Index 4: → NULL
Index 5: → NULL
Index 6: → NULL
```

Search for 24: go to index 3, traverse chain (3 comparisons).
**Average search: O(1 + α)** where α = n/m (load factor).

---

## Q.7(c) Merge sort pseudocode + time complexity. (04)

```
Procedure MERGE_SORT(A, LOW, HIGH)
    If LOW < HIGH Then
        Set MID = FLOOR((LOW + HIGH) / 2)
        Call MERGE_SORT(A, LOW, MID)         // sort left half
        Call MERGE_SORT(A, MID+1, HIGH)      // sort right half
        Call MERGE(A, LOW, MID, HIGH)        // merge two halves
    End If
End Procedure

Procedure MERGE(A, LOW, MID, HIGH)
    Create temporary arrays L and R
    Copy A[LOW..MID] into L, A[MID+1..HIGH] into R
    Set I = 1, J = 1, K = LOW
    While I <= size(L) AND J <= size(R) do
        If L[I] <= R[J] Then
            Set A[K] = L[I], I = I + 1
        Else
            Set A[K] = R[J], J = J + 1
        End If
        Set K = K + 1
    End While
    Copy remaining elements of L or R into A
End Procedure
```

**Time Complexity:**
- T(n) = 2T(n/2) + O(n)
- By Master Theorem: a=2, b=2, f(n)=n, n^(log₂2) = n = f(n) → Case 2
- **Best Case: O(n log n)**
- **Worst Case: O(n log n)**
- Space: O(n) for temporary arrays

---

## Q.7(d) What is garbage collection? (01)

**Garbage Collection:** The automatic process of identifying and reclaiming memory cells (nodes) that are no longer referenced by any pointer in the program, returning them to the AVAIL (free space) list for reuse.

---

## Q.8(a) Dijkstra's from S. (04)

**Graph:** S→t(3), S→y(5), t→x(6), t→y(1), x→z(7), y→t(4), y→x(2), y→z(6)

**Initialization:**

| Node | S | t | x | y | z |
|---|---|---|---|---|---|
| Dist | 0 | ∞ | ∞ | ∞ | ∞ |

**Visit S (dist=0):** S→t(3), S→y(5)

| Node | S | t | x | y | z |
|---|---|---|---|---|---|
| Dist | **0** | 3 | ∞ | 5 | ∞ |

**Visit t (dist=3):** t→x(3+6=9), t→y(3+1=4 < 5)

| Node | S | t | x | y | z |
|---|---|---|---|---|---|
| Dist | **0** | **3** | 9 | 4 | ∞ |

**Visit y (dist=4):** y→t(4+4=8 > 3), y→x(4+2=6 < 9), y→z(4+6=10)

| Node | S | t | x | y | z |
|---|---|---|---|---|---|
| Dist | **0** | **3** | 6 | **4** | 10 |

**Visit x (dist=6):** x→z(6+7=13 > 10)

| Node | S | t | x | y | z |
|---|---|---|---|---|---|
| Dist | **0** | **3** | **6** | **4** | 10 |

**Visit z (dist=10):** No outgoing edges to update.

**Final Shortest Paths from S:**

| Destination | Distance | Path |
|---|---|---|
| S → t | 3 | S → t |
| S → y | 4 | S → t → y |
| S → x | 6 | S → t → y → x |
| S → z | 10 | S → t → y → z |

---

## Q.8(b) 4-Queens backtracking. (04)

Place 4 queens on a 4×4 board so no two queens share a row, column, or diagonal.

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

**Backtracking trace (abbreviated):**
- Row 1, Col 1: Place Q → Row 2, Col 3: Place Q → Row 3: no safe col → **backtrack**
- Row 2, Col 4: Place Q → Row 3, Col 2: safe? diagonal conflict → Row 3, Col 1: conflict → **backtrack**
- Row 1, Col 2: Place Q → Row 2, Col 4: Place Q → Row 3, Col 1: Place Q → Row 4, Col 3: Place Q → **Solution 1 found!** ✓

> **Two solutions exist: [2,4,1,3] and [3,1,4,2]**

---

## Q.8(c) Insert 90 into two heaps. (04)

**(i) Max Heap — Insert 90:**

Initial:
```
        910
       /   \
     77     66
    / \    / \
   68  1  33  11
```

Insert 90 at next position (left child of 68). Bubble up:
- 90 > 68 → swap
- 90 > 77 → swap... wait, 90 < 910 → stop

Actually: 90 > 68 → swap. Now 90 is at 77's left child. 90 > 77 → swap.

```
        910
       /   \
     90     66
    / \    / \
   77  1  33  11
  /
 68
```

**(ii) Min Heap — Insert 90:**

Initial:
```
      70
     /  \
    60   40
   / \   /
  50  55 20
```

Insert 90 at next position (right child of 40). Bubble up:
- 90 > 40 → no swap needed (min heap — parent must be smaller)

```
      70
     /  \
    60   40
   / \  / \
  50 55 20 90
```

> 90 stays at position since it is larger than its parent (40). No bubbling needed.
