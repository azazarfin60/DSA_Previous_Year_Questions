[⬅️ Previous](./2018_answer.md) | [🏠 Home](./README.md) | [Next ➡️](./2020_answer.md)

---

# 2019 — ECE 2103 Answer Key

---

## Q.1(a) Describe (i) Traversing (ii) Sorting (iii) Searching. (06)

**(i) Traversing:** The process of visiting and accessing each element of a data structure exactly once, in a systematic manner, to process or display the data.

**Example:** Printing all elements of an array A of size N:
```
Procedure TRAVERSE(A, N)
    For I = 1 to N do
        Print A[I]
    End For
End Procedure
```
Time: O(n)

**(ii) Sorting:** The process of arranging elements of a data structure in a specific order — either ascending or descending — based on a key value.

**Example:** Sorting [5, 2, 8, 1] in ascending order → [1, 2, 5, 8]
- Common algorithms: Bubble Sort O(n²), Quick Sort O(n log n), Merge Sort O(n log n)

**(iii) Searching:** The process of finding the location of a specific element (ITEM) within a data structure.

**Example:** Finding element 25 in array [10, 25, 30, 45]:
- **Linear Search:** Check each element sequentially → O(n)
- **Binary Search:** Divide sorted array in half each step → O(log n)

---

## Q.1(b) Merge Sort on Budget[] = {30, 20, 100, 50, 10, 15}. (06)

**Step-by-step splitting (divide):**

```
Level 0: [30, 20, 100, 50, 10, 15]
Level 1: [30, 20, 100]        [50, 10, 15]
Level 2: [30, 20]  [100]      [50, 10]  [15]
Level 3: [30] [20]            [50] [10]
```

**Merging (conquer) — bottom up:**

**Merge [30] and [20]:** Compare 30 vs 20 → [20, 30]
**Merge [20, 30] and [100]:** Compare 20<100, 30<100 → [20, 30, 100]

**Merge [50] and [10]:** Compare 50 vs 10 → [10, 50]
**Merge [10, 50] and [15]:** Compare 10<15, then 15<50 → [10, 15, 50]

**Final Merge [20, 30, 100] and [10, 15, 50]:**

| Compare | Left | Right | Result so far |
|---|---|---|---|
| 20 vs 10 | 20 | **10** | [10] |
| 20 vs 15 | 20 | **15** | [10, 15] |
| **20** vs 50 | 20 | 50 | [10, 15, 20] |
| **30** vs 50 | 30 | 50 | [10, 15, 20, 30] |
| **100** vs 50 | 100 | **50** | [10, 15, 20, 30, 50] |
| Copy 100 | | | [10, 15, 20, 30, 50, 100] |

> **Sorted: [10, 15, 20, 30, 50, 100]**

**Time Complexity:**
- n = 6, levels = ⌈log₂(6)⌉ = 3
- Each level does O(n) merge work
- **Total: O(n log n)** for all cases (best, worst, average)
- Space: O(n) for temporary merge arrays

---

## Q.2(a) Differences between array and linked list. (04)

| Criterion | Array | Linked List |
|---|---|---|
| **Memory Allocation** | Static, contiguous block allocated at compile time | Dynamic, non-contiguous nodes allocated at runtime |
| **Size** | Fixed — cannot grow/shrink | Flexible — grows and shrinks as needed |
| **Random Access** | O(1) — direct index access | O(n) — must traverse from head |
| **Insert/Delete** | O(n) — requires shifting elements | O(1) — only pointer updates (after reaching position) |
| **Memory Overhead** | No extra overhead | Extra space for pointer in each node |
| **Cache Performance** | Better — elements are contiguous | Worse — nodes scattered in memory |

---

## Q.2(b) Algorithm of binary search. (04)

**C++ Style:**
```cpp
int binarySearch(int A[], int N, int ITEM) {
    int BEG = 0; // 0-indexed for C++
    int END = N - 1;
    while (BEG <= END) {
        int MID = BEG + (END - BEG) / 2;
        if (A[MID] == ITEM) {
            cout << "Found at position " << MID << endl;
            return MID;
        } else if (ITEM < A[MID]) {
            END = MID - 1;          // search left half
        } else {
            BEG = MID + 1;          // search right half
        }
    }
    cout << "Item not found" << endl;
    return -1;
}
```

**OR, Textbook Style:**
```
Procedure BINARY_SEARCH(A, N, ITEM)
    // A = sorted array, N = size, ITEM = element to find
    Set BEG = 1
    Set END = N
    While BEG <= END do
        Set MID = FLOOR((BEG + END) / 2)
        If A[MID] = ITEM Then
            Print "Found at position", MID
            Return MID
        Else If ITEM < A[MID] Then
            Set END = MID - 1          // search left half
        Else
            Set BEG = MID + 1          // search right half
        End If
    End While
    Print "Item not found"
    Return -1
End Procedure
```

**Time Complexity:**
- Best: O(1) — found at middle
- Worst/Average: O(log n) — halves search space each step
- **Prerequisite:** Array must be sorted

---

## Q.2(c) Circular Queue with example and advantages. (04)

**Circular Queue:** A linear queue where the last position connects back to the first position, forming a circle. When REAR reaches the end, it wraps around to the beginning if space is available.

**Example:** Circular queue of size 5:
```
Initial:    FRONT = -1, REAR = -1
Insert A:   [A, _, _, _, _]   F=0, R=0
Insert B:   [A, B, _, _, _]   F=0, R=1
Insert C:   [A, B, C, _, _]   F=0, R=2
Delete:     [_, B, C, _, _]   F=1, R=2
Insert D:   [_, B, C, D, _]   F=1, R=3
Insert E:   [_, B, C, D, E]   F=1, R=4
Insert F:   [F, B, C, D, E]   F=1, R=0  ← wraps around!
```

**Formula:** REAR = (REAR + 1) mod SIZE

**Advantages:**
1. **No wasted space** — linear queue wastes space after deletions (FRONT moves forward). Circular queue reuses freed positions.
2. **Efficient memory utilization** — eliminates "false overflow" where queue appears full but has empty slots at the beginning.
3. **Constant time** operations — O(1) for both enqueue and dequeue.

---

## Q.3(a) Bubble sort: Find comparisons and interchanges for PEOPLE. (04)

**Array:** P, E, O, P, L, E → indices 1 to 6

**Pass 1:** (compare adjacent, swap if needed)
- P vs E → swap → **E**, **P**, O, P, L, E (interchange 1)
- P vs O → swap → E, **O**, **P**, P, L, E (interchange 2)
- P vs P → no swap
- P vs L → swap → E, O, P, **L**, **P**, E (interchange 3)
- P vs E → swap → E, O, P, L, **E**, **P** (interchange 4)
After Pass 1: E, O, P, L, E, **P** | Comparisons: 5, Swaps: 4

**Pass 2:**
- E vs O → no swap
- O vs P → no swap
- P vs L → swap → E, O, **L**, **P**, E, P (interchange 5)
- P vs E → swap → E, O, L, **E**, **P**, P (interchange 6)
After Pass 2: E, O, L, E, **P**, P | Comparisons: 4, Swaps: 2

**Pass 3:**
- E vs O → no swap
- O vs L → swap → E, **L**, **O**, E, P, P (interchange 7)
- O vs E → swap → E, L, **E**, **O**, P, P (interchange 8)
After Pass 3: E, L, E, **O**, P, P | Comparisons: 3, Swaps: 2

**Pass 4:**
- E vs L → no swap
- L vs E → swap → E, **E**, **L**, O, P, P (interchange 9)
After Pass 4: E, E, **L**, O, P, P | Comparisons: 2, Swaps: 1

**Pass 5:**
- E vs E → no swap
After Pass 5: **E, E, L, O, P, P** ✓ | Comparisons: 1, Swaps: 0

> **Total Comparisons = 5+4+3+2+1 = 15**
> **Total Interchanges = 4+2+2+1+0 = 9**

---

## Q.3(b) Build minheap from: 44, 30, 50, 22, 60, 55, 77, 55. (04)

**Insert elements one by one, bubble up after each:**

**Insert 44:** Root = 44
**Insert 30:** 30 < 44 → swap
```
    30
   /
  44
```
**Insert 50:** 50 > 30 → no swap
```
    30
   /  \
  44   50
```
**Insert 22:** 22 < 44 → swap, 22 < 30 → swap
```
      22
     /  \
    30   50
   /
  44
```
**Insert 60:** 60 > 30 → no swap
```
      22
     /  \
    30   50
   / \
  44  60
```
**Insert 55:** 55 > 50 → no swap
```
      22
     /  \
    30   50
   / \  /
  44 60 55
```
**Insert 77:** 77 > 50 → no swap
```
       22
      /  \
    30    50
   / \   / \
  44 60 55  77
```
**Insert 55:** 55 > 44 → no swap (placed as left child of 44... wait, 55 > 44 so stays)
Actually: next position is left child of 44. 55 > 44 → no swap needed.
```
         22
        /  \
      30    50
     / \   / \
    44  60 55  77
   /
  55
```

> **Final Min-Heap: [22, 30, 50, 44, 60, 55, 77, 55]**

---

## Q.3(c) Postfix notation of (3+9)² − 4. (04)

**Infix Expression:** (3 + 9) ↑ 2 − 4

**Using stack-based Infix to Postfix conversion:**

| Symbol | Stack | Output |
|---|---|---|
| ( | ( | |
| 3 | ( | 3 |
| + | ( + | 3 |
| 9 | ( + | 3 9 |
| ) | (empty) | 3 9 + |
| ↑ | ↑ | 3 9 + |
| 2 | ↑ | 3 9 + 2 |
| − | − | 3 9 + 2 ↑ |
| 4 | − | 3 9 + 2 ↑ 4 |
| End | (empty) | 3 9 + 2 ↑ 4 − |

> **Postfix: 3 9 + 2 ↑ 4 −**

**Verification (evaluating the postfix):**
- 3 9 + → 12
- 12 2 ↑ → 144
- 144 4 − → **140** ✓

---

## Q.4(a) Properties of recursive procedure. (02)

1. **Base Case:** At least one condition where the function stops calling itself, preventing infinite recursion.

2. **Progressive Approach:** Each recursive call must reduce the problem size, moving closer to the base case.

Example — Tower of Hanoi:
```
Procedure HANOI(N, SOURCE, DEST, AUX)
    If N = 1 Then                              // base case
        Print "Move disk 1 from", SOURCE, "to", DEST
        Return
    End If
    Call HANOI(N-1, SOURCE, AUX, DEST)         // smaller problem
    Print "Move disk", N, "from", SOURCE, "to", DEST
    Call HANOI(N-1, AUX, DEST, SOURCE)         // smaller problem
End Procedure
```

---

## Q.4(b) BST from: 40, 60, 50, 33, 55, 11. (04)

- Insert 40 → root
- Insert 60 → right of 40
- Insert 50 → left of 60
- Insert 33 → left of 40
- Insert 55 → right of 50
- Insert 11 → left of 33

```
       40
      /  \
    33    60
    /    /
   11   50
          \
          55
```

**Traversals:**
- **Inorder (LNR):** 11, 33, 40, 50, 55, 60
- **Preorder (NLR):** 40, 33, 11, 60, 50, 55
- **Postorder (LRN):** 11, 33, 55, 50, 60, 40

---

## Q.4(c) Binary tree representation in memory. (04)

A binary tree can be represented in memory using two methods:

**Method 1: Linked Representation (Most common)**
Each node has three fields: DATA, LEFT (pointer to left child), RIGHT (pointer to right child).

```
Node structure:
[ LEFT | DATA | RIGHT ]

Example tree:    50
                /  \
              30    70

Memory:
Node 1: [→Node2 | 50 | →Node3]
Node 2: [NULL   | 30 | NULL  ]
Node 3: [NULL   | 70 | NULL  ]
```

**Method 2: Array (Sequential) Representation**
Store nodes in an array using index formulas:
- Root at index 1
- Left child of index i = 2i
- Right child of index i = 2i + 1

```
Index: 1    2    3
Array: [50] [30] [70]
```

---

## Q.4(d) What is sparse matrix? (02)

A **sparse matrix** is a matrix in which the majority of elements are **zero**. Only a small number of elements have non-zero values.

**Example:**
```
0  0  0  5
0  8  0  0
0  0  0  0
0  6  0  0
```
Out of 16 elements, only 3 are non-zero → sparse.

**Efficient storage:** Instead of storing all elements, store only non-zero values as triplets: (row, column, value).
```
(0, 3, 5)
(1, 1, 8)
(3, 1, 6)
```
This saves significant memory for large sparse matrices.

---

## Q.5(a) Criterions for best fit algorithm. Why better algorithm needed? (04)

**Criterions for selecting a best fit algorithm:**

1. **Time Complexity** — How fast does it run? Compare best/worst/average cases.
2. **Space Complexity** — How much extra memory does it require?
3. **Input characteristics** — Is data nearly sorted? Random? Size?
4. **Stability** — Does it preserve relative order of equal elements?
5. **Simplicity** — How easy is it to implement and maintain?

**Why a better algorithm is needed:**
A better algorithm can solve the same problem significantly faster. For example, sorting 1 million items:
- Bubble Sort O(n²) → ~10¹² operations → takes hours
- Merge Sort O(n log n) → ~2×10⁷ operations → takes seconds

Choosing the right algorithm can mean the difference between a solution that runs in seconds vs one that takes days. As data sizes grow, algorithm efficiency becomes critical.

---

## Q.5(b) Rate of growth. Technique to find complexity. (04)

**Rate of Growth:** The rate at which the running time of an algorithm increases as the input size n increases. It describes the asymptotic behavior of the function.

Common growth rates (slowest to fastest):
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ)

**Technique — Counting Method:**
Count the number of basic operations as a function of input size n.

**Example:**
```
Sum = 0                    // 1 operation
For I = 1 to N do          // loop runs N times
    For J = 1 to N do      // loop runs N times
        Sum = Sum + 1      // 1 operation
    End For
End For
```
Total operations = 1 + N × N × 1 = N² + 1

**Rate of growth = O(n²)**

We drop constants and lower-order terms, keeping only the dominant term.

---

## Q.5(c) Binary search better than linear search in time complexity. (04)

| Criterion | Linear Search | Binary Search |
|---|---|---|
| Best Case | O(1) | O(1) |
| Worst Case | **O(n)** | **O(log n)** |
| Average Case | O(n) | O(log n) |
| Prerequisite | None | Array must be sorted |
| Approach | Check every element | Halve search space |

**Why Binary Search is better:**

For a sorted array of n = 1,000,000 elements:
- Linear Search: up to **1,000,000** comparisons
- Binary Search: up to **log₂(1,000,000) ≈ 20** comparisons

Binary search eliminates half the remaining elements at each step. After k comparisons, only n/2ᵏ elements remain. So it needs at most ⌈log₂ n⌉ comparisons.

**However:** Binary search requires the array to be **sorted first** (which costs O(n log n)). If searching only once in an unsorted array, linear search may be better overall. Binary search excels when the array is already sorted or when many searches are performed.

---

## Q.6(a) Insertion sort pseudocode with best/worst case. (04)

```
Procedure INSERTION_SORT(A, N)
    For I = 2 to N do
        Set KEY = A[I]
        Set J = I - 1
        While J >= 1 AND A[J] > KEY do    // shift larger elements right
            Set A[J+1] = A[J]
            Set J = J - 1
        End While
        Set A[J+1] = KEY                   // insert KEY at correct position
    End For
End Procedure
```

**Best Case — Already sorted array:**
- Inner while loop never executes (A[J] is never > KEY)
- Only outer loop runs N-1 times
- **Time: O(n)**

**Worst Case — Reverse sorted array:**
- Inner while loop runs maximum times (shifts all previous elements)
- Total shifts: 1 + 2 + 3 + ... + (N-1) = N(N-1)/2
- **Time: O(n²)**

---

## Q.6(b) Solve T(n) = 3T(n/4) + n using substitution. (04)

**Guess:** T(n) = O(n)

**Substitution:** Assume T(k) ≤ c·k for all k < n.

T(n) = 3T(n/4) + n
     ≤ 3·c·(n/4) + n
     = (3c/4)·n + n
     = n·(3c/4 + 1)

For T(n) ≤ c·n, we need:
(3c/4 + 1) ≤ c
1 ≤ c - 3c/4
1 ≤ c/4
**c ≥ 4**

So T(n) ≤ 4n for sufficiently large n.

> **T(n) = O(n)**

---

## Q.6(c) Asymptotic notation. Solve T(n) = 8T(n/2) + Θ(n²). (04)

**Asymptotic Notation:** Mathematical notation to describe the limiting behavior of an algorithm's running time.
- **O(f(n))** — Upper bound (worst case)
- **Ω(f(n))** — Lower bound (best case)
- **Θ(f(n))** — Tight bound (exact growth rate)

**Solving T(n) = 8T(n/2) + Θ(n²) using Master Theorem:**

Here a = 8, b = 2, f(n) = n²

Compute: n^(log_b a) = n^(log₂ 8) = n³

Compare f(n) = n² with n³:
n² = O(n^(3-ε)) for ε = 1

This is **Case 1** of Master Theorem: f(n) = O(n^(log_b a - ε))

> **T(n) = Θ(n³)**

---

## Q.7(a) Prove: (i) 2n²·2ⁿ + n log n = O(n²·2ⁿ), (ii) 3n³+4n² = Ω(n³), (iii) 6n³/(log n+1) = O(n³). (06)

**(i) Prove 2n²·2ⁿ + n log n = O(n²·2ⁿ):**

For large n: n log n ≪ n²·2ⁿ

So: 2n²·2ⁿ + n log n ≤ 2n²·2ⁿ + n²·2ⁿ = 3n²·2ⁿ

Take c = 3, n₀ = 1: For all n ≥ 1, 2n²·2ⁿ + n log n ≤ 3·n²·2ⁿ ✓

> **∴ 2n²·2ⁿ + n log n = O(n²·2ⁿ)** ∎

**(ii) Prove 3n³ + 4n² = Ω(n³):**

3n³ + 4n² ≥ 3n³ for all n ≥ 1

Take c = 3, n₀ = 1: For all n ≥ 1, 3n³ + 4n² ≥ 3·n³ ✓

> **∴ 3n³ + 4n² = Ω(n³)** ∎

**(iii) Prove 6n³/(log n + 1) = O(n³):**

For n ≥ 2: log n + 1 ≥ 1

So: 6n³/(log n + 1) ≤ 6n³/1 = 6n³

Take c = 6, n₀ = 2: For all n ≥ 2, 6n³/(log n + 1) ≤ 6·n³ ✓

> **∴ 6n³/(log n + 1) = O(n³)** ∎

---

## Q.7(b) Real-life applications of Dijkstra's algorithm. (02)

1. **GPS Navigation Systems** — Finding shortest route between two locations on a road map (e.g., Google Maps)
2. **Network Routing** — Internet routers use Dijkstra's (OSPF protocol) to find shortest path for data packets
3. **Airline Route Planning** — Finding cheapest or shortest flights between cities
4. **Social Networks** — Finding shortest connection path between two users

---

## Q.7(c) Dijkstra's: Shortest path from A to D. (04)

**Graph:** A—B(1), B—D(1), A—C(1), C—E(4), B—C(2), D—F(3), E—F(2), E—D(3)

**Initialization:**

| Node | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Dist | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |

**Visit A (dist=0):** A—B(1), A—C(1)

| Node | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Dist | **0** | 1 | 1 | ∞ | ∞ | ∞ |

**Visit B (dist=1):** B—D(1+1=2), B—C(1+2=3 > 1, no update)

| Node | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Dist | **0** | **1** | 1 | 2 | ∞ | ∞ |

**Visit C (dist=1):** C—E(1+4=5)

| Node | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Dist | **0** | **1** | **1** | 2 | 5 | ∞ |

**Visit D (dist=2):** D—F(2+3=5)

| Node | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| Dist | **0** | **1** | **1** | **2** | 5 | 5 |

**Visit E (dist=5):** E—F(5+2=7 > 5), E—D(5+3=8 > 2) → no updates

**Visit F (dist=5):** No updates.

> **Shortest path from A to D = 2, Path: A → B → D**

---

## Q.8(a) Differences between tree and graph. (02)

| Criterion | Tree | Graph |
|---|---|---|
| Structure | Hierarchical | Network |
| Root | Has a root node | No root concept |
| Cycles | No cycles allowed | Cycles may exist |
| Edges | n-1 edges for n nodes | Any number of edges |
| Path | Unique path between nodes | Multiple paths possible |
| Direction | Parent → child | Directed or undirected |

---

## Q.8(b) Adjacency matrix and adjacency list. (04)

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

## Q.8(c) BFS: Minimum path from A to J. (06)

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

<br>

---
[⬅️ Previous](./2018_answer.md) | [🏠 Home](./README.md) | [Next ➡️](./2020_answer.md)
