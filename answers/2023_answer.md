# 2023 — ECE 2103 Answer Key (OBE)

---

## Q.1(a) Define DS. Time complexity for array insert/delete at various positions. (CLO2, 04)

**Data Structure:** A systematic way of organizing, storing, and managing data so that operations like insertion, deletion, searching, and traversal can be performed efficiently.

**Time Complexity for Linear Array (size N):**

| Operation | 1st Position | Any Position (ith) | Last Position |
|---|---|---|---|
| **Insert** | O(n) — shift all right | O(n) — shift n-i elements | O(1) — place at end |
| **Delete** | O(n) — shift all left | O(n) — shift n-i elements | O(1) — remove last |

**Example:** Array = [10, 20, 30, 40, 50], N=5

- **Insert 5 at 1st:** Shift all → [5, 10, 20, 30, 40, 50] — 5 shifts = O(n)
- **Insert 25 at pos 3:** Shift 30,40,50 right → [10, 20, 25, 30, 40, 50] — 3 shifts = O(n)
- **Insert 60 at last:** [10, 20, 30, 40, 50, 60] — 0 shifts = O(1)

---

## Q.1(b) Complete BinarySearch recursive function + time complexity. (CLO3, 06)

```
Procedure BinarySearch(A, l, h, x)
    If l > h Then
        Return -1                              // not found
    End If
    Set mid = FLOOR((l + h) / 2)
    If A[mid] = x Then
        Return mid                             // found at mid
    Else If x < A[mid] Then
        Return BinarySearch(A, l, mid - 1, x)  // search left
    Else
        Return BinarySearch(A, mid + 1, h, x)  // search right
    End If
End Procedure
```

**Time Complexity:**
- Each call halves the problem: T(n) = T(n/2) + O(1)
- By Master Theorem: a=1, b=2, f(n)=O(1), n^(log₂1) = n⁰ = 1 = f(n) → Case 2
- **T(n) = O(log n)**
- Best: O(1), Worst: O(log n), Average: O(log n)
- Space: O(log n) for recursion stack

---

## Q.2(a) Postfix, infix, prefix binary tree from A*(B+C)/D+(E/2). (CLO1, 03)

**Expression Tree:**
```
           +
          / \
         /   \
        /     /
       *     E/2
      / \
     A   +
        / \
       B   C
      (divided by D)
```

More precisely, parsing A*(B+C)/D + (E/2):

```
            +
          /   \
         /     \
        /       /
       /       E  2
      *
     / \
    /   D
   A
    \
    (+)
   / \
  B   C
```

Let me restructure properly. The expression is: ((A*(B+C))/D) + (E/2)

```
              +
            /   \
           /     ÷
          ÷     / \
         / \   E   2
        *   D
       / \
      A   +
         / \
        B   C
```

**Inorder (LNR):** A * B + C / D + E / 2
**Preorder (NLR):** + / * A + B C D / E 2
**Postorder (LRN):** A B C + * D / E 2 / +

---

## Q.2(b) Huffman Tree from weights: 4, 3, 8, 2, 15, 25, 40. (CLO2, 03)

**Step-by-step (combine two smallest each time):**

**Step 1:** Sort: 2, 3, 4, 8, 15, 25, 40
Combine 2+3 = 5 → {4, 5, 8, 15, 25, 40}

**Step 2:** Combine 4+5 = 9 → {8, 9, 15, 25, 40}

**Step 3:** Combine 8+9 = 17 → {15, 17, 25, 40}

**Step 4:** Combine 15+17 = 32 → {25, 32, 40}

**Step 5:** Combine 25+32 = 57 → {40, 57}

**Step 6:** Combine 40+57 = 97 (root)

**Huffman Tree:**
```
            97
          /    \
        57      40
       /  \
      32   25
     /  \
    15   17
        /  \
       8    9
           / \
          4   5
             / \
            2   3
```

---

## Q.2(c) Dijkstra's: node 1 to node 8. (CLO3, 04)

**Graph:** 1→2(2), 1→3(1), 1→4(1), 2→5(5), 3→2(1), 3→5(2), 4→3(1), 4→6(4), 5→7(2), 5→8(10), 6→7(7), 7→8(6)

| Step | Visit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Init | — | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | 1 | **0** | 2 | 1 | 1 | ∞ | ∞ | ∞ | ∞ |
| 2 | 3(d=1) | 0 | 2 | **1** | 1 | 3 | ∞ | ∞ | ∞ |
| 3 | 4(d=1) | 0 | 2 | 1 | **1** | 3 | 5 | ∞ | ∞ |
| 4 | 2(d=2) | 0 | **2** | 1 | 1 | 3 | 5 | ∞ | ∞ |
| 5 | 5(d=3) | 0 | 2 | 1 | 1 | **3** | 5 | 5 | 13 |
| 6 | 6(d=5) | 0 | 2 | 1 | 1 | 3 | **5** | 5 | 13 |
| 7 | 7(d=5) | 0 | 2 | 1 | 1 | 3 | 5 | **5** | 11 |
| 8 | 8(d=11) | 0 | 2 | 1 | 1 | 3 | 5 | 5 | **11** |

> **Shortest path from 1 to 8 = 11**
> **Path: 1 → 3 → 5 → 7 → 8** (or 1 → 4 → 3 → 5 → 7 → 8, same cost)

---

## Q.3(a) Deque operations. LEFT=7, RIGHT=2, size=8. (CLO3, 03)

**Initial:** [ _ | _ | yy | zz | _ | _ | ww | xx ] (indices 0–7), LEFT=7, RIGHT=2

Occupied: index 7=ww, 0=xx, 1=yy, 2=zz. Wait — LEFT=7 means leftmost is at 7.
Reading left to right (circular): ww(7), xx(0), yy(1), zz(2)

**(i) Add "FF" to right:** RIGHT = (2+1) mod 8 = 3
→ [ xx | yy | zz | FF | _ | _ | _ | ww ], LEFT=7, RIGHT=3

**(ii) Add "KK" and "LL" to left:**
KK: LEFT = (7-1) mod 8 = 6 → index 6 = KK, LEFT=6
LL: LEFT = (6-1) mod 8 = 5 → index 5 = LL, LEFT=5
→ [ xx | yy | zz | FF | _ | LL | KK | ww ], LEFT=5, RIGHT=3

**(iii) Delete one from left:**
Remove index 5 (LL), LEFT = (5+1) mod 8 = 6
→ [ xx | yy | zz | FF | _ | _ | KK | ww ], LEFT=6, RIGHT=3

---

## Q.3(b) Insertion sort: 77,33,44,11,88,22,66,55. (CLO2, 05)

```
Procedure INSERTION_SORT(A, N)
    For I = 2 to N do
        Set KEY = A[I]
        Set J = I - 1
        While J >= 1 AND A[J] > KEY do
            Set A[J+1] = A[J]
            Set J = J - 1
        End While
        Set A[J+1] = KEY
    End For
End Procedure
```

**Trace:**

| Pass | KEY | Array State | Comparisons |
|---|---|---|---|
| Initial | — | [77, 33, 44, 11, 88, 22, 66, 55] | — |
| I=2 | 33 | [**33**, 77, 44, 11, 88, 22, 66, 55] | 1 |
| I=3 | 44 | [33, **44**, 77, 11, 88, 22, 66, 55] | 1 |
| I=4 | 11 | [**11**, 33, 44, 77, 88, 22, 66, 55] | 3 |
| I=5 | 88 | [11, 33, 44, 77, **88**, 22, 66, 55] | 1 |
| I=6 | 22 | [11, **22**, 33, 44, 77, 88, 66, 55] | 4 |
| I=7 | 66 | [11, 22, 33, 44, **66**, 77, 88, 55] | 2 |
| I=8 | 55 | [11, 22, 33, 44, **55**, 66, 77, 88] | 2 |

> **Sorted: [11, 22, 33, 44, 55, 66, 77, 88]**

**Complexity:** Best O(n) (sorted), Worst O(n²) (reverse), Average O(n²)

---

## Q.3(c) Path vs Simple Path. (CLO1, 02)

**Path:** A sequence of vertices v₁, v₂, ..., vₖ where each consecutive pair (vᵢ, vᵢ₊₁) is connected by an edge. Vertices **may repeat**.

**Simple Path:** A path where **no vertex is repeated** (except possibly the first and last for a cycle).

**Example:** In graph A—B—C—D—B—E:
- A→B→C→D→B→E is a **path** (B repeats)
- A→B→C→D is a **simple path** (no repeat)

---

## Q.4(a) C function to split linked list at point loc. (CLO4, 04)

```
Procedure SPLIT_LIST(inList, loc, outList1, outList2)
    // Split inList into outList1 (first loc nodes) and outList2 (rest)
    Set outList1 = inList
    Set PTR = inList
    Set COUNT = 1

    // Traverse to the loc-th node
    While COUNT < loc AND PTR ≠ NULL do
        Set PREV = PTR
        Set PTR = NEXT[PTR]
        Set COUNT = COUNT + 1
    End While

    // PTR is now at loc-th node
    Set outList2 = NEXT[PTR]       // second list starts after loc
    Set NEXT[PTR] = NULL            // terminate first list
End Procedure
```

**Example:** inList = (10→20→30→40→50), loc=3
- Traverse to 3rd node (30)
- outList1 = 10→20→30→NULL
- outList2 = 40→50→NULL ✓

---

## Q.4(b) BST: J,R,D,G,T,E,M,H,P,A,F,Q — build, inorder, delete D. (CLO3, 06)

**(i) Build BST:**

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

**(ii) Inorder traversal (LNR):**
> **A, D, E, F, G, H, J, M, P, Q, R, T**

**(iii) Delete D (has two children):**
Inorder successor of D = **E** (smallest in right subtree).
Replace D with E. Delete original E (E has child F → F takes E's place).

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

## Q.5(a) Define: Root, Child, Depth, Leaf, Parent. (CLO1, 03)

```
         A          ← Root, Parent of B and C
        / \
       B   C        ← B is Child of A, Parent of D,E
      / \    \
     D   E    F     ← D, E, F are Leaf nodes
```

1. **Root:** The topmost node with no parent. (A)
2. **Child Node:** A node directly connected below another node. (B, C are children of A)
3. **Depth:** The number of edges from the root to a node. (Depth of D = 2)
4. **Leaf:** A node with no children. (D, E, F)
5. **Parent Node:** A node directly above another node. (A is parent of B and C)

---

## Q.5(b) Array representation of binary tree. (CLO3, 03)

**Tree:** A(root), B(left of A), C(right of A), D(left of B), E(right of B), F(right of C), I(left of D), G(right of D), J(left of E), H(left of F)

**Array (1-indexed):**

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value | A | B | C | D | E | — | F | I | G | J | — | — | H |

Rules: Left child of i = 2i, Right child of i = 2i+1

---

## Q.5(c) Kruskal's MST. (CLO3, 04)

**Sorted edges:**

| Edge | Weight |
|---|---|
| (1,6) | 10 |
| (3,4) | 12 |
| (2,7) | 14 |
| (2,3) | 16 |
| (4,7) | 18 |
| (4,5) | 22 |
| (5,7) | 24 |
| (5,6) | 25 |
| (1,2) | 28 |

**Selection (7 nodes → 6 edges):**

| Step | Edge | Weight | Action | Components |
|---|---|---|---|---|
| 1 | (1,6) | 10 | ✅ Add | {1,6} |
| 2 | (3,4) | 12 | ✅ Add | {1,6}, {3,4} |
| 3 | (2,7) | 14 | ✅ Add | {1,6}, {3,4}, {2,7} |
| 4 | (2,3) | 16 | ✅ Add | {1,6}, {2,3,4,7} |
| 5 | (4,7) | 18 | ✗ Cycle | — |
| 6 | (4,5) | 22 | ✅ Add | {1,6}, {2,3,4,5,7} |
| 7 | (5,7) | 24 | ✗ Cycle | — |
| 8 | (5,6) | 25 | ✅ Add | {1,2,3,4,5,6,7} |

> **MST: {(1,6)=10, (3,4)=12, (2,7)=14, (2,3)=16, (4,5)=22, (5,6)=25} = 99**

---

## Q.6 Memory space for complexity analysis. (CLO2, 03)

Memory space must be considered because:

1. **Limited resources** — RAM is finite. An algorithm using O(n²) space may crash for large inputs even if it's time-efficient.
2. **Cache performance** — algorithms using less memory have better cache utilization, running faster in practice.
3. **Trade-offs** — some algorithms trade space for time (e.g., hash tables use extra space for O(1) access). We must evaluate whether the space cost is justified.

**Example:** Merge sort uses O(n) extra space vs Quick sort's O(log n). For memory-constrained systems, quick sort is preferred despite similar time complexity.

---

## Q.6(a) T(n) = 2T(n/2) + Θ(n) using Master method. (CLO2, 03)

**Master Theorem:** T(n) = aT(n/b) + f(n)

Here: a = 2, b = 2, f(n) = Θ(n)

Compute: n^(log_b a) = n^(log₂ 2) = n¹ = n

Compare f(n) = Θ(n) with n^(log_b a) = n → they are **equal**.

This is **Case 2:** f(n) = Θ(n^(log_b a))

> **T(n) = Θ(n log n)**

---

## Q.6(b) Prim's MST. (CLO2, 03)

**Graph:** (1,2)=10, (1,6)=30, (2,3)=50, (2,5)=40, (2,6)=45, (3,4)=15, (3,5)=35, (4,5)=25, (4,6)=20, (5,6)=35

**Starting from node 1:**

| Step | Add | Edge | Cost | MST Nodes |
|---|---|---|---|---|
| 1 | 1 | — | — | {1} |
| 2 | 2 | (1,2) | 10 | {1,2} |
| 3 | 6 | (1,6) | 30 | {1,2,6} |
| 4 | 4 | (4,6) | 20 | {1,2,4,6} |
| 5 | 3 | (3,4) | 15 | {1,2,3,4,6} |
| 6 | 5 | (4,5) | 25 | {1,2,3,4,5,6} |

> **MST: {(1,2)=10, (1,6)=30, (4,6)=20, (3,4)=15, (4,5)=25} = 100**

---

## Q.6(c) BFS: minimum path A to J. (CLO1, 04)

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

## Q.7(a) Why binary search not applicable for sorted linked list? (CLO1, 02)

Binary search requires **O(1) random access** to the middle element. Linked lists only support **sequential access** — finding the middle requires traversing n/2 nodes (O(n)). This makes each "halving" step O(n) instead of O(1), giving total O(n log n) — worse than simple linear search O(n).

---

## Q.7(b) Performance analysis vs performance measurement. (CLO1, 02)

| Criterion | Performance Analysis | Performance Measurement |
|---|---|---|
| When | Before implementation (a priori) | After implementation (a posteriori) |
| Method | Mathematical (Big-O, recurrence) | Actual timing on hardware |
| Dependency | Machine-independent | Machine-dependent |
| Input | Theoretical input size n | Actual test data |
| Use | Compare algorithms abstractly | Fine-tune implementation |

---

## Q.7(c) Bellman-Ford shortest paths from A. (CLO3, 03)

**Graph:** A→B(5), A→C(1), A→D(2), B→D(2), B→E(-2), C→D(4), D→C(-1), D→E(4), E→C(3)

**Source = A, V=5 → V-1=4 iterations**

**Init:** dist = [A:0, B:∞, C:∞, D:∞, E:∞]

**Iteration 1:**
- A→B: 0+5=5, A→C: 0+1=1, A→D: 0+2=2
- B→D: 5+2=7 > 2, B→E: 5+(-2)=3
- C→D: 1+4=5 > 2
- D→C: 2+(-1)=1 = 1 (no change), D→E: 2+4=6 > 3
- E→C: 3+3=6 > 1

dist = [A:0, B:5, C:1, D:2, E:3]

**Iteration 2:**
- B→E: 5+(-2)=3 = 3 (no change)
- D→C: 2+(-1)=1 = 1 (no change)
- All others: no improvement

dist = [A:0, B:5, C:1, D:2, E:3] — **converged**

**Final Shortest Paths from A:**

| Node | Distance | Path |
|---|---|---|
| A → B | 5 | A → B |
| A → C | 1 | A → C |
| A → D | 2 | A → D |
| A → E | 3 | A → B → E |

No negative cycle detected. ✓

---

## Q.7(d) Time complexity of nested loop code. (CLO3, 03)

```
for x = 1 to n do
    y = x
    while (y > 1) do
        y = y / 2
```

**Inner loop analysis:** For a given x, the while loop divides y by 2 until y ≤ 1. Starting from y = x, this takes ⌊log₂ x⌋ iterations.

**Total:** Σ(x=1 to n) log₂(x) = log₂(1) + log₂(2) + ... + log₂(n) = log₂(n!) ≈ n log₂ n (by Stirling's approximation)

> **Time Complexity: Θ(n log n)**

---

## Q.8(a) Spanning tree definition + MST of grid graph. (CLO3, 04)

**Spanning Tree:** A subgraph of a connected graph G that includes **all vertices** and is a **tree** (connected, acyclic). It has exactly V-1 edges.

**Graph edges:** TL-TM(2), TM-TR(1), BL-BM(3), BM-BR(3), TL-BL(2), TM-BM(1), TR-BR(3), TL-BM(2), TM-BR(1), BM-TR(2)

**Kruskal's (6 nodes → 5 edges):**

| Step | Edge | Weight | Action |
|---|---|---|---|
| 1 | TM-TR | 1 | ✅ |
| 2 | TM-BM | 1 | ✅ |
| 3 | TM-BR | 1 | ✅ |
| 4 | TL-TM | 2 | ✅ |
| 5 | TL-BL | 2 | ✅ (connects BL) |

> **MST: {TM-TR(1), TM-BM(1), TM-BR(1), TL-TM(2), TL-BL(2)} = 7**

---

## Q.8(b) Max Heap: array, delete max, insert Q. (CLO3, 05)

**Given Max Heap:** W, M, O, J, L, D, K, A, G, I, E, B, C

**(i) Array representation:**

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value | W | M | O | J | L | D | K | A | G | I | E | B | C |

**(ii) Delete maximum (W):**
Replace root with last element (C). Remove last. Heapify down.
- C vs M, O → O is larger → swap C and O
- C vs D, K → K is larger → swap C and K

```
         O
        / \
       M    K
      /\   / \
     J  L D   C
    /\ /\  /
   A G I E B
```
Array: [O, M, K, J, L, D, C, A, G, I, E, B]

**(iii) Insert Q:**
Place Q at next position (index 13). Bubble up.
- Q > C → swap
- Q > K → swap (actually Q > O? Q < O alphabetically, so stop... wait, Q > O alphabetically)

Actually alphabetically: A<B<C<D<E<...O<P<Q<...W
So Q > O → swap. Q > ... Q < W (but W was deleted). Now root is O. Q > O → swap.

After insert Q at index 13, bubble up:
- Q at index 13, parent = index 6 (D). Q > D → swap
- Q now at index 6, parent = index 3 (K). Q > K → swap
- Q now at index 3, parent = index 1 (O). Q > O → swap
- Q is now root.

```
         Q
        / \
       M    O
      /\   / \
     J  L D   C
    /\ /\  /
   A G I E B
```
Hmm, but K was at index 3 before. Let me redo from the post-deletion state:

Post-deletion array: [O, M, K, J, L, D, C, A, G, I, E, B]

Insert Q at index 13: [O, M, K, J, L, D, C, A, G, I, E, B, Q]
- Index 13, parent = 6 (D). Q > D → swap → [O, M, K, J, L, Q, C, A, G, I, E, B, D]
- Index 6, parent = 3 (K). Q > K → swap → [O, M, Q, J, L, K, C, A, G, I, E, B, D]
- Index 3, parent = 1 (O). Q > O → swap → [Q, M, O, J, L, K, C, A, G, I, E, B, D]

> **Final Array: [Q, M, O, J, L, K, C, A, G, I, E, B, D]**

---

## Q.8(c) Define algorithm. (CLO1, 01)

**Algorithm:** A finite, well-defined sequence of instructions or steps designed to solve a specific problem or perform a computation. It takes input, processes it through defined steps, and produces output in finite time.
