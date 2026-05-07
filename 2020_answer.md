# 2020 — ECE 2103 Answer Key

---

## Q.1(a) Why do we need DS? Explain linear and non-linear DS. (03)

**Why we need data structure:**
Data structures organize and manage data efficiently, enabling faster access, insertion, deletion, and searching. Without proper data structures, programs would be slow and consume excessive memory.

**Linear Data Structure:** Elements arranged sequentially with unique predecessor and successor.
- *Examples:* Array (indices), Linked List (pointers), Stack (LIFO), Queue (FIFO)

**Non-linear Data Structure:** Elements arranged hierarchically or in a network — each element may connect to multiple elements.
- *Examples:* Tree (parent-child hierarchy), Graph (nodes and edges)

---

## Q.1(b) Which searching technique for 10 search queries? (04)

**Given:** Array = [1, 2, 7, 5, 1, 2, 10, 8, 11, 12] — **unsorted**.

**Analysis:**
- **Linear Search:** Works on unsorted data, O(n) per query → 10 queries = O(10n)
- **Binary Search:** Requires sorted array first. Sort cost = O(n log n), then O(log n) per query → Total = O(n log n + 10 log n)

**For 10 queries:**
- Linear: 10 × 10 = 100 comparisons (worst case)
- Binary: Sort once (~33 operations) + 10 × 4 = 73 comparisons

**Recommendation:** Since we need **at least 10 queries**, it is better to **sort the array first** using an O(n log n) algorithm and then use **Binary Search**. The one-time sorting cost is amortized over multiple queries.

> **Answer: Sort first, then use Binary Search.**

---

## Q.1(c) Bubble sort pseudocode with example. (05)

```
Procedure BUBBLE_SORT(A, N)
    For I = 1 to N-1 do
        For J = 1 to N-I do
            If A[J] > A[J+1] Then
                Swap A[J] and A[J+1]
            End If
        End For
    End For
End Procedure
```

**Example:** A = [5, 3, 8, 1]

**Pass 1:** Compare adjacent pairs:
- 5>3 → swap → [3, 5, 8, 1]
- 5<8 → no swap
- 8>1 → swap → [3, 5, 1, **8**]

**Pass 2:**
- 3<5 → no swap
- 5>1 → swap → [3, 1, **5**, 8]

**Pass 3:**
- 3>1 → swap → [**1**, **3**, 5, 8] ✓

> **Sorted: [1, 3, 5, 8]**
> **Time: O(n²) worst/avg, O(n) best (with optimization)**

---

## Q.2(a) Implement stack using arrays. (03)

A stack can be implemented using an array with a **TOP** variable tracking the topmost element.

```
Initialize: Set TOP = -1, MAX = size of array

Procedure PUSH(STACK, ITEM)
    If TOP = MAX - 1 Then
        Print "Stack Overflow"
        Return
    End If
    Set TOP = TOP + 1
    Set STACK[TOP] = ITEM
End Procedure

Procedure POP(STACK)
    If TOP = -1 Then
        Print "Stack Underflow"
        Return
    End If
    Set ITEM = STACK[TOP]
    Set TOP = TOP - 1
    Return ITEM
End Procedure
```

---

## Q.2(b) Transfer all queue elements into a stack. (05)

```
Procedure QUEUE_TO_STACK(Q, S)
    // Q = source queue, S = destination stack
    While Q is not empty do
        Set ITEM = DEQUEUE(Q)     // remove from front of queue
        Call PUSH(S, ITEM)         // push onto stack
    End While
End Procedure
```

**Example:**
Queue: [10, 20, 30] (front=10)
Stack: []

| Step | Dequeue | Stack (top→) |
|---|---|---|
| 1 | 10 | [10] |
| 2 | 20 | [10, 20] |
| 3 | 30 | [10, 20, 30] |

**Note:** The order in the stack is reversed relative to the queue (FIFO → LIFO). Top of stack = 30 (last element of queue).

---

## Q.2(c) Store binary tree using array. (04)

**Array Representation Rules:**
- Root at index 1
- Left child of node at index i = **2i**
- Right child of node at index i = **2i + 1**

**Given tree:** A(root), B(left of A), C(right of A), D(left of B), E(right of C), F(left of D), G(right of D), H(left of G)

**Mapping:**

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Node | A | B | C | D | — | — | E | F | — | G | H |

**Explanation:**
- A at 1, B at 2 (left of 1), C at 3 (right of 1)
- D at 4 (left of 2), E at 7 (right of 3)
- F at 8 (left of 4), G at 10 (right of... wait)

The tree structure shows G as right child of D (index 4), so G at 2×4+1 = 9. H as left of G at 2×9 = 18... This requires a larger array but many positions are empty — showing the **disadvantage** of array representation for non-complete trees (wasted space).

---

## Q.3(a) BST from: 30, 50, 20, 40, 25, 15, 45, 60, 46. (04)

Insert step by step:
- 30 → root
- 50 → right of 30
- 20 → left of 30
- 40 → left of 50
- 25 → right of 20
- 15 → left of 20
- 45 → right of 40
- 60 → right of 50
- 46 → left of 45... wait, 46 > 45, so right of 45

```
          30
         /  \
       20    50
      / \   /  \
    15  25 40   60
            \
            45
             \
             46
```

---

## Q.3(b) Traversals and delete root. (04)

**From the BST above:**

**Preorder (NLR):** 30, 20, 15, 25, 50, 40, 45, 46, 60

**Inorder (LNR):** 15, 20, 25, 30, 40, 45, 46, 50, 60

**Postorder (LRN):** 15, 25, 20, 46, 45, 40, 60, 50, 30

**Deleting root (30):**
Root has two children → Replace with **inorder successor** (smallest in right subtree) = **40**.

```
          40
         /  \
       20    50
      / \   /  \
    15  25 45   60
            \
            46
```

---

## Q.3(c) Queue operations: 3 dequeue + 2 enqueue. (04)

**Initial Queue:** [10, 5, 7, 8, 9, 11, 12] (FRONT=10, REAR=12)

**Dequeue 3 times:**
1. Remove 10 → [5, 7, 8, 9, 11, 12]
2. Remove 5 → [7, 8, 9, 11, 12]
3. Remove 7 → [8, 9, 11, 12]

**Enqueue 11, 12:**
4. Add 11 → [8, 9, 11, 12, 11]
5. Add 12 → [8, 9, 11, 12, 11, 12]

> **Final Queue: [8, 9, 11, 12, 11, 12]** (FRONT=8, REAR=12)

---

## Q.4(a) Prove: n nodes, n-1 edges → tree. (03)

**Proof:**
A connected graph G with n nodes and n-1 edges is a tree.

1. A **tree** is defined as a connected acyclic graph.
2. Any connected graph with n nodes needs **at least n-1 edges** (otherwise it's disconnected).
3. Any graph with n nodes and **more than n-1 edges** must contain a cycle.
4. Therefore, a connected graph with **exactly n-1 edges** has the minimum edges for connectivity and cannot have any cycle.
5. Since G is connected and acyclic → G is a tree. ∎

---

## Q.4(b) Paths of length 2 using matrix method. (03)

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

## Q.4(c) MST using Kruskal's. (03)

**Sorted edges:**

| Edge | Weight |
|---|---|
| B—D | 2 |
| D—T | 2 |
| A—C | 3 |
| C—D | 4 |
| B—T | 5 |
| A—B | 6 |
| S—A | 7 |
| S—C | 8 |
| S—B | 9 |

**Selection (6 nodes → 5 edges):**

| Step | Edge | Weight | Action |
|---|---|---|---|
| 1 | B—D | 2 | ✅ Add |
| 2 | D—T | 2 | ✅ Add |
| 3 | A—C | 3 | ✅ Add |
| 4 | C—D | 4 | ✅ Add (connects {A,C} with {B,D,T}) |
| 5 | B—T | 5 | ✗ Cycle |
| 6 | A—B | 6 | ✗ Cycle |
| 7 | S—A | 7 | ✅ Add (connects S) |

> **MST: {B—D(2), D—T(2), A—C(3), C—D(4), S—A(7)} = 18**

---

## Q.4(d) Linear vs Binary search. When each is better. (03)

**Linear Search:** Checks each element one by one from beginning to end. Works on both sorted and unsorted data. Time: O(n).

**Binary Search:** Repeatedly divides sorted array in half, eliminating half the elements each step. Requires sorted data. Time: O(log n).

**When each is better:**
- **Linear** is better for: unsorted data, small arrays (n < 20), single search on unsorted data
- **Binary** is better for: sorted data, large arrays, repeated search queries

---

## Q.5(a) Frequency counts. (04)

**(i) Triple nested loop:**
```
for i:=1 to n do
    for j:=1 to i do
        for k:=1 to j do
            x:=x+1;
```

The innermost statement executes: Σ(i=1 to n) Σ(j=1 to i) j = Σ(i=1 to n) i(i+1)/2

= (1/2) Σ(i=1 to n) (i² + i) = (1/2)[n(n+1)(2n+1)/6 + n(n+1)/2]

> **Frequency ≈ n³/6 = O(n³)**

**(ii) While loop:**
```
i:=1;                   // 1 time
while (i <= n) do       // n+1 times (n true + 1 false)
    x:=x+1;            // n times
    i:=i+1;            // n times
```

> **Frequency = 1 + (n+1) + n + n = 3n + 2 = O(n)**

---

## Q.5(b) Insertion sort pseudocode + time complexity. (04)

```
Procedure INSERTION_SORT(A, N)
    For I = 2 to N do
        Set KEY = A[I]
        Set J = I - 1
        While J >= 1 AND A[J] > KEY do
            Set A[J+1] = A[J]        // shift right
            Set J = J - 1
        End While
        Set A[J+1] = KEY              // place KEY
    End For
End Procedure
```

**Best Case (sorted):** Inner while never executes → **O(n)**
**Worst Case (reverse sorted):** Inner while shifts all → 1+2+...+(n-1) = **O(n²)**
**Average Case:** **O(n²)**

---

## Q.5(c) Recurrence. Show T(n) = T(n-1) + n is O(n²). (04)

**Recurrence** is a mathematical equation that defines a function in terms of its value at smaller inputs.

**Expanding T(n) = T(n-1) + n:**
- T(n) = T(n-1) + n
- T(n-1) = T(n-2) + (n-1)
- T(n-2) = T(n-3) + (n-2)
- ...continuing...
- T(n) = T(1) + 2 + 3 + ... + n
- T(n) = T(1) + n(n+1)/2 - 1

Assuming T(1) = 1:
T(n) = 1 + n(n+1)/2 - 1 = n(n+1)/2

> **T(n) = n(n+1)/2 = O(n²)** ∎

---

## Q.6(a) Master method three cases. Can it solve all? (04)

**Master Theorem** for T(n) = aT(n/b) + f(n), where a ≥ 1, b > 1:

Let c = log_b(a)

**Case 1:** If f(n) = O(n^(c-ε)) for some ε > 0 → **T(n) = Θ(n^c)**
**Case 2:** If f(n) = Θ(n^c) → **T(n) = Θ(n^c · log n)**
**Case 3:** If f(n) = Ω(n^(c+ε)) for some ε > 0 and af(n/b) ≤ kf(n) → **T(n) = Θ(f(n))**

**Can it solve all recurrences? No.**
- Only applies to recurrences of form T(n) = aT(n/b) + f(n)
- Cannot handle: T(n) = T(n-1) + n (subtraction), T(n) = 2T(n/2) + n log n (gap between cases), or unequal subproblem sizes like T(n) = T(n/3) + T(2n/3) + n

---

## Q.6(b) Find maximum in direct-address table. (05)

```
Procedure FIND_MAX(T, M)
    // T = direct-address table of length M
    Set MAX_VAL = -∞
    Set MAX_KEY = -1
    For I = 0 to M-1 do
        If T[I] is not NIL Then
            If T[I].value > MAX_VAL Then
                Set MAX_VAL = T[I].value
                Set MAX_KEY = I
            End If
        End If
    End For
    Return MAX_KEY
End Procedure
```

**Worst-case performance: O(m)** where m is the table length. We must scan every slot because the maximum could be anywhere. There is no shortcut since a direct-address table is unordered.

---

## Q.6(c) Collision in hashing. One method to solve. (03)

**Collision:** When two different keys map to the same index using the hash function.
Example: h(k) = k mod 7. Both h(14)=0 and h(21)=0 → collision at index 0.

**Method: Separate Chaining**
Each slot stores a linked list. All colliding keys are chained together.

Example: h(k) = k mod 7, insert: 14, 21, 7, 35
```
Index 0: → 14 → 21 → 7 → 35 → NULL
Index 1: → NULL
...
```
All four keys hash to 0 and are stored in the chain at index 0.

---

## Q.7(a) NP-Hard, NP-Complete, and TSP. (04)

**NP-Hard:** Problems at least as hard as the hardest NP problems. No known polynomial-time solution exists. They may not even be verifiable in polynomial time.

**NP-Complete:** Problems that are both:
1. In NP (solution can be verified in polynomial time)
2. NP-Hard (at least as hard as any NP problem)

**TSP (Travelling Salesman Problem):**
- **Decision version** ("Is there a tour ≤ k?"): **NP-Complete** — answer is verifiable in polynomial time
- **Optimization version** ("Find shortest tour"): **NP-Hard** — no polynomial-time verification for optimality

---

## Q.7(b) (i) Adjacency matrix/list, (ii) BFS and DFS from A. (08)

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

## Q.8(a) Best, worst, average of linear and binary search. (05)

| Case | Linear Search | Binary Search |
|---|---|---|
| **Best** | O(1) — element at first position | O(1) — element at middle |
| **Worst** | O(n) — element at last or absent | O(log n) — element at deepest level |
| **Average** | O(n) — checks n/2 on average | O(log n) — halves each step |

**Linear Search:** Scans sequentially. For n=1024: worst = 1024 comparisons.

**Binary Search:** Divides sorted array in half. For n=1024: worst = log₂(1024) = 10 comparisons.

Binary search is **exponentially faster** but requires sorted data.

---

## Q.8(b) Big-O notation. Methods to calculate complexity. (04)

**Big-O Notation:** Describes the upper bound of an algorithm's growth rate. f(n) = O(g(n)) means there exist constants c and n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀.

**Methods to calculate complexity:**
1. **Counting method:** Count basic operations as function of n
2. **Recurrence method:** Express T(n) recursively, solve using substitution or Master Theorem
3. **Amortized analysis:** Average cost over sequence of operations

**Example (Counting):**
```
For I = 1 to N do        // N times
    For J = 1 to N do    // N times
        x = x + 1        // 1 operation
```
Total = N × N = N² → **O(n²)**

---

## Q.8(c) Shortest path with negative cycle. (03)

**Bellman-Ford algorithm** should be used when there are negative edge weights. However, if a **negative cycle** exists (a cycle whose total weight is negative), then:

- No shortest path exists — we can keep going around the negative cycle to reduce the distance infinitely
- **Bellman-Ford can detect negative cycles:** After V-1 relaxation iterations, perform one more iteration. If any distance still decreases, a negative cycle exists.

```
Procedure DETECT_NEGATIVE_CYCLE(G)
    Run Bellman-Ford for V-1 iterations
    For each edge (U, V, W) do
        If dist[U] + W < dist[V] Then
            Print "Negative cycle detected"
            Return TRUE
        End If
    End For
    Return FALSE
End Procedure
```

> **Answer: Use Bellman-Ford to detect the negative cycle. If detected, no finite shortest path exists.**
