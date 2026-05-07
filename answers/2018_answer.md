# 2018 — ECE 2103 Answer Key
# Section A

---

## Q1(a) Define (i) Data structure (ii) Linear DS (iii) Non-linear DS. (4.5)

**(i) Data Structure:** A systematic way of organizing, storing, and managing data in a computer so that it can be accessed and modified efficiently.

**(ii) Linear Data Structure:** Elements are arranged sequentially where each element has a unique predecessor and successor (except first and last).
- *Examples:* Array, Linked List, Stack, Queue

**(iii) Non-linear Data Structure:** Elements are not arranged sequentially. Each element can connect to multiple elements forming hierarchical or network structures.
- *Examples:* Tree, Graph

---

## Q1(b) Major operations in data structure. (04)

1. **Traversing** — Visiting each element exactly once (e.g., printing array elements)
2. **Searching** — Finding the location of a given element (e.g., binary search in sorted array)
3. **Inserting** — Adding a new element at a specific position
4. **Deleting** — Removing an element from the structure
5. **Sorting** — Arranging elements in ascending or descending order
6. **Merging** — Combining two sorted data structures into one sorted structure

---

## Q1(c) Complexity of algorithm. Time complexity of linear search. (3.5)

**Complexity of an Algorithm:** A measure of the amount of time and/or space an algorithm requires as a function of the input size n. It tells us how the algorithm's performance scales as input grows.

**Linear Search Algorithm:**
```
Procedure LINEAR_SEARCH(A, N, ITEM)
    Set I = 1
    While I <= N do
        If A[I] = ITEM Then
            Print "Found at position", I
            Return I
        End If
        Set I = I + 1
    End While
    Print "Not Found"
    Return -1
End Procedure
```

**Time Complexity:**
- **Best Case:** O(1) — element found at first position
- **Worst Case:** O(n) — element at last position or not present
- **Average Case:** O(n) — on average, checks n/2 elements

---

## Q2(a) "Complexity analysis is a vital issue" — Explain. (04)

Complexity analysis is vital because it allows us to predict an algorithm's performance **before** running it, enabling us to choose the best algorithm for a given problem.

**Example:** Searching in a sorted array of 1,000,000 elements:
- **Linear Search:** O(n) = 1,000,000 comparisons in worst case
- **Binary Search:** O(log n) = ~20 comparisons in worst case

Without complexity analysis, we might implement linear search, wasting enormous time. Complexity analysis tells us binary search is exponentially better.

**Why it matters:**
1. Helps compare algorithms objectively
2. Predicts scalability — will it work for large inputs?
3. Identifies bottlenecks in the algorithm
4. Guides algorithm selection based on problem constraints

---

## Q2(b) "Quick sort is better than bubble sort." Explain. (04)

| Criterion | Quick Sort | Bubble Sort |
|---|---|---|
| Average Time | O(n log n) | O(n²) |
| Approach | Divide & Conquer | Adjacent comparison |
| Swaps | Fewer (distant) | Many (adjacent only) |
| Practical Speed | Very fast | Very slow |
| In-place | Yes | Yes |

**Example:** Sorting [5, 1, 4, 2, 8]:
- Bubble sort: ~10 comparisons, ~4 swaps per pass, multiple passes
- Quick sort: pivot=5, partition [1,4,2] [5] [8], recurse — far fewer operations

For n=1000: Quick sort ≈ 10,000 ops vs Bubble sort ≈ 1,000,000 ops.

Quick sort is better because its **average O(n log n)** significantly outperforms bubble sort's **O(n²)** for all practical input sizes.

---

## Q2(c) Radix sort: mom, mamuni, dad, daddy, good, god, bat, cat, mad, pat, bar, him (04)

**Step 1: Pad all words to maximum length (6 chars, using blanks '_'):**
```
mom___, mamuni, dad___, daddy_, good__, god___,
bat___, cat___, mad___, pat___, bar___, him___
```

**Step 2: Sort by last character (position 6), then 5, 4, 3, 2, 1:**

**Pass 1 (Position 6 — rightmost):**
Blanks ('_') come first, then 'i':
```
mom, dad, daddy, good, god, bat, cat, mad, pat, bar, him, mamuni
```

**Pass 2 (Position 5):**
```
mom, dad, good, god, bat, cat, mad, pat, bar, him, daddy, mamuni
```

**Pass 3 (Position 4):**
```
mom, dad, god, bat, cat, mad, pat, bar, him, good, daddy, mamuni
```

**Pass 4 (Position 3):**
Sorting by 3rd character: d→d, d→d, m→m, t→t, etc.
```
dad, mad, bar, bat, cat, god, good, him, mom, pat, daddy, mamuni
```

**Pass 5 (Position 2):**
Sorting by 2nd character: a→a→a→a→a, i, o→o→o, etc.
```
bar, bat, cat, dad, mad, pat, daddy, mamuni, him, god, good, mom
```

**Pass 6 (Position 1):**
Sorting by 1st character: b→b, c, d→d, g→g, h, m→m→m, p
```
bar, bat, cat, dad, daddy, god, good, him, mad, mamuni, mom, pat
```

> **Sorted: bar, bat, cat, dad, daddy, god, good, him, mad, mamuni, mom, pat**

---

## Q3(a) Define (i) 2-tree (ii) BST (iii) Tree. (03)

**(i) 2-tree:** A binary tree where every node has either **0 or 2 children** — no node has exactly one child. Also called extended/strictly binary tree. Internal nodes have 2 children; leaf nodes have 0.

**(ii) BST (Binary Search Tree):** A binary tree where for each node: all values in the left subtree are **less than** the node, and all values in the right subtree are **greater than** the node.
```
       20
      /  \
    10    30     (10 < 20 < 30 ✓)
```

**(iii) Tree:** A non-linear hierarchical data structure consisting of nodes connected by edges. It has one **root** node and every other node has exactly one parent. No cycles exist.

---

## Q3(b) Describe (i) Selection sort (ii) Merge sort (iii) Heap sort. (4.5)

**(i) Selection Sort:** Finds the minimum element from the unsorted portion and places it at the beginning. Repeat for remaining elements.
- Time: O(n²) all cases | Space: O(1) | Not stable

**(ii) Merge Sort:** Divides array into two halves recursively until single elements, then merges sorted halves back together.
- Time: O(n log n) all cases | Space: O(n) | Stable
- Uses divide-and-conquer approach

**(iii) Heap Sort:** Builds a max-heap from the array, then repeatedly extracts the maximum element and places it at the end.
- Time: O(n log n) all cases | Space: O(1) | Not stable
- Step 1: Build max-heap — O(n)
- Step 2: Extract max n times — O(n log n)

---

## Q3(c) BST from: 20, 15, 10, 30, 20, 40, 10, 12, 50, 10, 50, 35 (4.5)

Inserting step by step (duplicates ignored):

- 20 → root
- 15 → left of 20
- 10 → left of 15
- 30 → right of 20
- 20 → duplicate, skip
- 40 → right of 30
- 10 → duplicate, skip
- 12 → right of 10
- 50 → right of 40
- 10 → duplicate, skip
- 50 → duplicate, skip
- 35 → left of 40

```
           20
          /  \
        15    30
        /       \
      10        40
        \      /  \
        12   35   50
```

---

## Q4(a) Insert 80, 75 into Max Heap. (04)

**Initial Heap:**
```
       100
      /   \
    50     70
   / \    /
  40  45  60
```

**Insert 80:** Place at next available position (right of 70), bubble up.
- 80 > 70 → swap

```
       100
      /   \
    50     80
   / \    / \
  40  45 60  70
```

**Insert 75:** Place at next position (left child of 40), bubble up.
- 75 > 40 → swap
- 75 > 50 → swap

```
        100
       /    \
     75      80
    / \     / \
   50  45  60  70
  /
 40
```

---

## Q4(b) Draw graph from adjacency matrix (6×6). (04)

Reading edges from matrix (undirected, matrix[3][3]=1 means self-loop):

- 1—2, 1—3, 1—4, 1—6
- 2—3, 2—5
- 3—3 (self-loop)
- 4—5, 4—6
- 5—6
- 6—6 (self-loop)

```
    1 ---- 2
   /|\      \
  / | \      5
 3  |  4    /|
 ↺  |  |   / |
    6--+--+  |
    ↺        |
     \------/
```

**Edges:** {(1,2), (1,3), (1,4), (1,6), (2,3), (2,5), (3,3), (4,5), (4,6), (5,6), (6,6)}

---

## Q4(c) Explain (i) DFS and (ii) BFS. (04)

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

## Q5(a) How is Hash function used for better searching? (03)

A **hash function** h(k) maps a key k directly to an array index, allowing **O(1) average-time** searching instead of O(n) linear search.

**How it works:**
1. Given key k, compute index = h(k) (e.g., h(k) = k mod 10)
2. Go directly to that index in the hash table
3. If key is there, search is done in O(1)

**Example:** Keys: 25, 42, 33. Hash function: h(k) = k mod 10.
- h(25) = 5, h(42) = 2, h(33) = 3
- To find 42: compute h(42) = 2, go to index 2 → found in **1 step**

Without hashing, searching 42 in an unsorted list would take up to O(n) comparisons.

---

## Q5(b) Problems of hash function and solutions. (06)

**Main Problem — Collision:** When two different keys map to the same index.
Example: h(k) = k mod 10. Both h(25)=5 and h(35)=5 → collision at index 5.

**Solution 1 — Separate Chaining:**
Each index stores a linked list. All keys mapping to the same index are chained together.
```
Index 0: → NULL
Index 5: → 25 → 35 → 15 → NULL
Index 2: → 42 → NULL
```
- **Advantage:** Simple, handles unlimited collisions
- **Disadvantage:** Extra memory for pointers

**Solution 2 — Linear Probing (Open Addressing):**
If h(k) is occupied, check h(k)+1, h(k)+2, ... until an empty slot is found.
```
h(25) = 5 → index 5 [25]
h(35) = 5 → occupied → try 6 [35]
h(45) = 5 → occupied → try 6 → occupied → try 7 [45]
```
- **Advantage:** No extra memory for links
- **Disadvantage:** Clustering — consecutive filled slots slow down search

**Solution 3 — Quadratic Probing:**
Instead of checking +1, +2, +3..., check +1², +2², +3²...
- Reduces clustering compared to linear probing

**Solution 4 — Double Hashing:**
Use a second hash function: next = (h1(k) + i × h2(k)) mod size
- Best distribution, minimal clustering

---

## Q5(c) Verify hash table sequence. (03)

**Given:** Hash table size = 10, values at indices: 2→42, 3→23, 4→34, 5→52, 6→46, 7→33.

Assuming h(k) = k mod 10:
- h(42) = 2 → index 2 ✓ (direct)
- h(23) = 3 → index 3 ✓ (direct)
- h(34) = 4 → index 4 ✓ (direct)
- h(52) = 2 → index 2 occupied → linear probe → 3 occupied → 4 occupied → **5** ✓
- h(46) = 6 → index 6 ✓ (direct)
- h(33) = 3 → index 3 occupied → 4 occupied → 5 occupied → 6 occupied → **7** ✓

**Possible insertion sequence:** 42, 23, 34, 52, 46, 33

(42, 23, 34 must come before 52 and 33 since they block their natural positions.)

---

## Q6(a) Define (i) Queue (ii) Priority Queue (iii) Circular Queue. (03)

**(i) Queue:** A linear data structure following **FIFO** (First In First Out) principle. Elements are inserted at REAR and deleted from FRONT.
Example: Queue = [A, B, C] → Delete returns A, Insert D gives [B, C, D]

**(ii) Priority Queue:** A queue where each element has a **priority**. Element with the highest priority is dequeued first, regardless of insertion order.
Example: Emergency room — critical patients served before minor cases.

**(iii) Circular Queue:** A queue where the last position connects back to the first position, forming a circle. This prevents the "false overflow" problem of linear queues.
Example: FRONT=4, REAR=1 in a 5-element array — wraps around.

---

## Q6(b) Priority Queue insert and delete algorithms. (07)

**Data Structures:**
- `PRIORITY_F[K]` — front pointer for priority level K
- `PRIORITY_R[K]` — rear pointer for priority level K
- `QUEUE[K][N]` — data array for priority level K
- `SIZE[K]` — max size of queue at level K

**INSERT Algorithm:**
```
Procedure PQ_INSERT(ITEM, PRIORITY)
    Set K = PRIORITY
    If PRIORITY_R[K] >= SIZE[K] Then
        Print "Overflow at priority level", K
        Return
    End If
    If PRIORITY_F[K] = 0 Then          // queue was empty
        Set PRIORITY_F[K] = 1
    End If
    Set PRIORITY_R[K] = PRIORITY_R[K] + 1
    Set QUEUE[K][PRIORITY_R[K]] = ITEM
End Procedure
```

**DELETE Algorithm:**
```
Procedure PQ_DELETE()
    // Find highest priority (lowest K) non-empty queue
    Set K = 1
    While K <= MAX_PRIORITY do
        If PRIORITY_F[K] != 0 Then     // queue not empty
            Set ITEM = QUEUE[K][PRIORITY_F[K]]
            If PRIORITY_F[K] = PRIORITY_R[K] Then  // last element
                Set PRIORITY_F[K] = 0
                Set PRIORITY_R[K] = 0
            Else
                Set PRIORITY_F[K] = PRIORITY_F[K] + 1
            End If
            Print "Deleted:", ITEM
            Return ITEM
        End If
        Set K = K + 1
    End While
    Print "Underflow — all queues empty"
End Procedure
```

**Operations:**
- INSERT: O(1) — directly insert at rear of correct priority queue
- DELETE: O(P) — may need to scan P priority levels to find non-empty queue (P = number of priority levels, usually small)

---

## Q6(c) How does queue differ from array? (02)

| Criterion | Queue | Array |
|---|---|---|
| Access | FIFO — only front and rear | Random access by index |
| Operations | Enqueue (rear), Dequeue (front) | Insert/delete anywhere |
| Flexibility | Restricted access | Unrestricted access |
| Use case | Scheduling, BFS | General storage |

A queue is a **restricted** data structure — elements can only be added at one end and removed from the other. An array allows access to any element at any index.

---

## Q7(a) Can a tree be stored using linear data structure? (02)

**Yes.** A tree can be stored using an **array** (linear data structure).

For a binary tree, using array index mapping:
- Root is at index 1
- Left child of node at index i → index **2i**
- Right child of node at index i → index **2i + 1**
- Parent of node at index i → index **⌊i/2⌋**

**Example:** Tree with root=50, left=30, right=70:
```
Array: [_, 50, 30, 70]
Index:  0   1   2   3
```
This is commonly used in **heap** implementation.

---

## Q7(b) Dijkstra's from R. (05)

**Graph:** R→D(7), R→B(3), D→C(6), C→T(5), C→D(20), B→D(9), B→P(1), P→B(2), T→D(10), T→P(30)

**Initialization:**

| Node | R | B | C | D | P | T |
|---|---|---|---|---|---|---|
| Dist | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |

**Iteration 1: Visit R (dist=0)**
- R→B: 0+3=3, R→D: 0+7=7

| Node | R | B | C | D | P | T |
|---|---|---|---|---|---|---|
| Dist | **0** | 3 | ∞ | 7 | ∞ | ∞ |

**Iteration 2: Visit B (dist=3)**
- B→D: 3+9=12 > 7 → no update
- B→P: 3+1=4

| Node | R | B | C | D | P | T |
|---|---|---|---|---|---|---|
| Dist | **0** | **3** | ∞ | 7 | 4 | ∞ |

**Iteration 3: Visit P (dist=4)**
- P→B: 4+2=6 > 3 → no update

| Node | R | B | C | D | P | T |
|---|---|---|---|---|---|---|
| Dist | **0** | **3** | ∞ | 7 | **4** | ∞ |

**Iteration 4: Visit D (dist=7)**
- D→C: 7+6=13

| Node | R | B | C | D | P | T |
|---|---|---|---|---|---|---|
| Dist | **0** | **3** | 13 | **7** | **4** | ∞ |

**Iteration 5: Visit C (dist=13)**
- C→T: 13+5=18
- C→D: 13+20=33 > 7 → no update

| Node | R | B | C | D | P | T |
|---|---|---|---|---|---|---|
| Dist | **0** | **3** | **13** | **7** | **4** | 18 |

**Iteration 6: Visit T (dist=18)**
- T→D: 18+10=28 > 7, T→P: 18+30=48 > 4 → no updates

**Final Shortest Paths from R:**

| Destination | Distance | Path |
|---|---|---|
| R → B | 3 | R → B |
| R → P | 4 | R → B → P |
| R → D | 7 | R → D |
| R → C | 13 | R → D → C |
| R → T | 18 | R → D → C → T |

---

## Q7(c) Limitations of Dijkstra's algorithm. (02)

1. **Cannot handle negative edge weights** — Dijkstra assumes once a node is finalized, its distance won't change. Negative edges can violate this. Use Bellman-Ford instead.

2. **Not optimal for dense graphs without min-heap** — Basic implementation is O(V²). Needs priority queue for O((V+E) log V).

3. **Finds only single-source shortest paths** — Does not find all-pairs shortest paths (use Floyd-Warshall for that).

---

## Q7(d) DFS algorithm. (03)

```
Procedure DFS(G, V)
    // G = graph, V = starting vertex
    Create Stack S
    Push V onto S
    While S is not empty do
        Set U = Pop from S
        If U is not visited Then
            Mark U as visited
            Print U
            For each neighbor W of U do
                If W is not visited Then
                    Push W onto S
                End If
            End For
        End If
    End While
End Procedure
```

**Time Complexity:** O(V + E)
**Space Complexity:** O(V)

---

## Q8(a) MST for broadband network. (06)

**Using Kruskal's Algorithm** (sort edges, pick smallest without forming cycle):

**Sorted edges:**
| Edge | Weight |
|---|---|
| H3—H7 | 0.5K |
| H4—H5 | 0.5K |
| H1—H3 | 1K |
| H5—H6 | 1K |
| H1—H2 | 2K |
| H4—H6 | 2K |
| H6—H7 | 2K |
| H1—H7 | 3K |
| H2—H3 | 3K |
| H2—H5 | 3K |
| H3—H6 | 5K |

**Selection (7 nodes → need 6 edges):**

| Step | Edge | Weight | Action |
|---|---|---|---|
| 1 | H3—H7 | 0.5K | ✅ Add |
| 2 | H4—H5 | 0.5K | ✅ Add |
| 3 | H1—H3 | 1K | ✅ Add (connects H1) |
| 4 | H5—H6 | 1K | ✅ Add (connects H6) |
| 5 | H1—H2 | 2K | ✅ Add (connects H2) |
| 6 | H4—H6 | 2K | ✗ Cycle (H4-H5-H6) |
| 7 | H6—H7 | 2K | ✗ Cycle (H6-H5-H4... wait) |

Let me recheck: After step 5, connected = {H1,H2,H3,H7}, {H4,H5,H6}. Need 1 more edge to connect the two components.

| 6 | H4—H6 | 2K | ✗ Cycle (H4,H5,H6 same component) |
| 7 | H6—H7 | 2K | ✅ Add (connects the two components) |

**MST Edges:** H3—H7(0.5K), H4—H5(0.5K), H1—H3(1K), H5—H6(1K), H1—H2(2K), H6—H7(2K)

> **Minimum Cost = 0.5 + 0.5 + 1 + 1 + 2 + 2 = 7K (7,000 Taka)**

---

## Q8(b) Discuss backtracking, NP-Hard, NP-Complete. (03)

**Backtracking:** A systematic algorithmic technique that builds a solution incrementally, one step at a time. If a partial solution cannot lead to a valid complete solution, it **backtracks** (undoes the last step) and tries another path. Used for constraint-satisfaction problems like N-Queens, Subset Sum.

**NP-Hard:** A class of problems that are **at least as hard** as the hardest problems in NP. They may or may not have a polynomial-time verifier. No known polynomial-time algorithm exists. Example: Travelling Salesman Problem (optimization version).

**NP-Complete:** A problem that is both **NP** (solution verifiable in polynomial time) and **NP-Hard** (at least as hard as any NP problem). If any NP-Complete problem is solved in polynomial time, all NP problems can be. Example: Boolean Satisfiability (SAT), Subset Sum (decision version).

---

## Q8(c) N-Queen algorithm. (03)

```
Procedure N_QUEENS(BOARD, ROW, N)
    // Place queens row by row
    If ROW > N Then
        Print BOARD            // all queens placed successfully
        Return
    End If
    For COL = 1 to N do
        If IS_SAFE(BOARD, ROW, COL, N) Then
            Place queen at BOARD[ROW] = COL
            Call N_QUEENS(BOARD, ROW + 1, N)  // try next row
            Remove queen from BOARD[ROW]       // backtrack
        End If
    End For
End Procedure

Procedure IS_SAFE(BOARD, ROW, COL, N)
    For I = 1 to ROW - 1 do
        // Check same column
        If BOARD[I] = COL Then Return FALSE
        // Check diagonals
        If |BOARD[I] - COL| = |I - ROW| Then Return FALSE
    End For
    Return TRUE
End Procedure
```

**Time Complexity:** O(N!) in worst case.
