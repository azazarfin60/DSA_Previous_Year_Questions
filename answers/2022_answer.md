[⬅️ Previous](./2021_answer.md) | [🏠 Home](./README.md) | [Next ➡️](./2023_answer.md)

---

# 2022 — ECE 2103 Answer Key (OBE)

---

## Q.1(a) Define DS. Tower of Hanoi code. (CO1, 03)

**Data Structure:** A systematic way of organizing, storing, and managing data so that it can be accessed and modified efficiently.

**Tower of Hanoi — Recursive Pseudocode:**
```
Procedure TOWER_OF_HANOI(N, SOURCE, DEST, AUX)
    If N = 1 Then
        Print "Move disk 1 from", SOURCE, "to", DEST
        Return
    End If
    Call TOWER_OF_HANOI(N-1, SOURCE, AUX, DEST)
    Print "Move disk", N, "from", SOURCE, "to", DEST
    Call TOWER_OF_HANOI(N-1, AUX, DEST, SOURCE)
End Procedure
```

For N=3, SOURCE=A, DEST=C, AUX=B:
1. Move disk 1 from A to C
2. Move disk 2 from A to B
3. Move disk 1 from C to B
4. Move disk 3 from A to C
5. Move disk 1 from B to A
6. Move disk 2 from B to C
7. Move disk 1 from A to C

**Total moves = 2ⁿ − 1 = 7**

---

## Q.1(b) Merge two sorted arrays. Time complexity. (CO2, 04)

```
Procedure MERGE_SORTED(A, N, B, M, C)
    // A = sorted array of size N, B = sorted array of size M
    // C = output merged sorted array
    Set I = 1, J = 1, K = 1
    While I <= N AND J <= M do
        If A[I] <= B[J] Then
            Set C[K] = A[I]
            Set I = I + 1
        Else
            Set C[K] = B[J]
            Set J = J + 1
        End If
        Set K = K + 1
    End While
    // Copy remaining elements
    While I <= N do
        Set C[K] = A[I]
        Set I = I + 1, K = K + 1
    End While
    While J <= M do
        Set C[K] = B[J]
        Set J = J + 1, K = K + 1
    End While
End Procedure
```

**Time Complexity: O(N + M)** — each element is compared and copied exactly once. We traverse both arrays once linearly.

**Space Complexity: O(N + M)** — for the output array C.

---

## Q.1(c) Advantages of two-way list over one-way for searching. (CO1, 03)

**Two-way (Doubly) Linked List** has both NEXT and PREV pointers in each node.

**Advantages for searching an unsorted list for ITEM:**

1. **Bidirectional traversal** — can search from both ends simultaneously, potentially halving search time.
2. **Easier backtracking** — if we overshoot while searching, we can move backward without restarting from the head.
3. **Deletion after finding** — once ITEM is found, deletion is O(1) because we have the PREV pointer. In a one-way list, we'd need to traverse again to find the predecessor.
4. **Reverse traversal** — can search from tail to head, useful if ITEM is more likely near the end.

**However:** Extra space is needed for the PREV pointer in each node — a trade-off of space for convenience.

---

## Q.2(a) Max-Heap from: 34,30,40,22,50,2,55,77,55. Insert 70, Delete 22. (CO1, 05)

**Building Max-Heap (insert one by one, bubble up):**

Insert 34: [34]
Insert 30: [34, 30]
Insert 40: 40 > 34 → swap → [40, 30, 34]
Insert 22: [40, 30, 34, 22]
Insert 50: 50 > 30 → swap, 50 > 40 → swap → [50, 40, 34, 22, 30]
Insert 2: [50, 40, 34, 22, 30, 2]
Insert 55: 55 > 34 → swap, 55 > 50 → swap → [55, 40, 50, 22, 30, 2, 34]
Insert 77: 77 > 22 → swap, 77 > 40 → swap, 77 > 55 → swap → [77, 55, 50, 40, 30, 2, 34, 22]
Insert 55: 55 > 30 → swap, 55 > 55 → no swap → [77, 55, 50, 40, 55, 2, 34, 22, 30]

**Final Max-Heap:**
```
            77
          /    \
        55      50
       / \     / \
      40  55  2   34
     / \
    22  30
```

**(i) Insert 70:**
Place at index 10 (left child of 55). Bubble up:
- 70 > 55 → swap
- 70 > 55 → swap (now at level 2)
- 70 < 77 → stop

```
            77
          /    \
        70      50
       / \     / \
      40  55  2   34
     / \  /
    22 30 55
```

**(ii) Delete 22:**
Find 22 (index 8). Replace with last element (55 at index 10). Remove last. Bubble up/down:
- 55 replaces 22 at position. 55 > 40 → swap with parent.

```
            77
          /    \
        70      50
       / \     / \
      55  55  2   34
     / \
    40  30
```

---

## Q.2(b) Dequeue operations. (CO1, 03)

**Initial:** Dequeue: [_, A, C, D, _, _], left=2, right=4, size=6

**(i) F added to right:**
right = (4+1) mod 6 = 5 → Dequeue[5] = F
→ [_, A, C, D, F, _], left=2, right=5

**(ii) Two letters deleted from right:**
Delete Dequeue[5] = F, right = 4
Delete Dequeue[4] = D, right = 3
→ [_, A, C, _, _, _], left=2, right=3

**(iii) K, L, M added to left:**
Add K: left = (2-1) mod 6 = 1 → Dequeue[1] = K
→ [_, K, A, C, _, _], left=1, right=3... 

Actually left moves backward: left = left - 1.
Add K: left = 2-1 = 1 → Dequeue[1] = K, left=1
Add L: left = 1-1 = 0 → Dequeue[0] = L, left=0
Add M: left = 0-1 = 5 (wrap) → Dequeue[5] = M, left=5

→ **[L, K, A, C, _, M]**, left=5, right=3

---

## Q.2(c) Why is a good hash function important? (CO1, 02)

A good hash function is important because:

1. **Minimizes collisions** — distributes keys uniformly across the table, reducing the chance of multiple keys mapping to the same index.
2. **Ensures O(1) performance** — poor hash functions cause clustering, degrading search/insert from O(1) to O(n).
3. **Uniform distribution** — every slot has equal probability of being filled, maximizing table utilization.

A bad hash function (e.g., h(k) = 1 for all k) makes the hash table degenerate into a linked list with O(n) operations.

---

## Q.3(a) Complete Binary Search recursive code. (CO3, 03)

```
Procedure BINARY_SEARCH(ARR, L, R, X)
    If L > R Then
        Return -1                        // not found
    End If
    Set MID = FLOOR((L + R) / 2)
    If ARR[MID] = X Then
        Return MID                       // found
    Else If X < ARR[MID] Then
        Return BINARY_SEARCH(ARR, L, MID-1, X)
    Else
        Return BINARY_SEARCH(ARR, MID+1, R, X)
    End If
End Procedure
```

---

## Q.3(b) Quicksort time complexity when all elements are same. (CO2, 03)

When all elements have the **same value**, quicksort's pivot selection results in the **worst possible partitioning**.

**Analysis:**
- Pivot = any element (all are equal)
- Partition: one side has n-1 elements, other side has 0
- Recurrence: T(n) = T(n-1) + T(0) + O(n) = T(n-1) + O(n)
- Expanding: T(n) = O(n) + O(n-1) + ... + O(1) = O(n²)

> **Time Complexity: O(n²)** — worst case, same as reverse-sorted input.

This can be avoided using **3-way partitioning** (Dutch National Flag), which handles duplicates in O(n).

---

## Q.3(c) Implement stack using two queues. (CO2, 04)

**Approach: Make PUSH costly**

```
// Use two queues: Q1 (main), Q2 (helper)

Procedure PUSH(ITEM)
    Enqueue ITEM into Q2
    While Q1 is not empty do
        Enqueue DEQUEUE(Q1) into Q2
    End While
    Swap Q1 and Q2              // Q1 now has newest on front
End Procedure

Procedure POP()
    If Q1 is empty Then
        Print "Stack Underflow"
        Return
    End If
    Return DEQUEUE(Q1)
End Procedure
```

**Example:** Push 1, 2, 3:
- Push 1: Q2=[1], Q1=[] → swap → Q1=[1]
- Push 2: Q2=[2], move Q1→Q2: Q2=[2,1] → swap → Q1=[2,1]
- Push 3: Q2=[3], move Q1→Q2: Q2=[3,2,1] → swap → Q1=[3,2,1]
- Pop: returns 3 ✓ (LIFO)

**Time:** PUSH = O(n), POP = O(1)

---

## Q.4(a) Hash table h(k) = k mod 7 for 19,26,13,48,17. (CO2, 04)

**(i) Separate Chaining:**

| Index | Chain |
|---|---|
| 0 | → 48 → NULL |
| 1 | → 43... |

Let me compute: h(19)=19%7=5, h(26)=26%7=5, h(13)=13%7=6, h(48)=48%7=6, h(17)=17%7=3

| Index | Chain |
|---|---|
| 0 | NULL |
| 1 | NULL |
| 2 | NULL |
| 3 | → 17 → NULL |
| 4 | NULL |
| 5 | → 19 → 26 → NULL |
| 6 | → 13 → 48 → NULL |

**(ii) Linear Probing:**

| Insert | h(k) | Probe | Final Index |
|---|---|---|---|
| 19 | 5 | — | 5 |
| 26 | 5 | 5 occupied → 6 | 6 |
| 13 | 6 | 6 occupied → 0 | 0 |
| 48 | 6 | 6 occupied → 0 occupied → 1 | 1 |
| 17 | 3 | — | 3 |

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Value | 13 | 48 | — | 17 | — | 19 | 26 |

---

## Q.4(b) Evaluate postfix: 9 4 3 2 / 1 5 + * / * + (CO1, 04)

Processing left to right:

| Step | Symbol | Stack | Action |
|---|---|---|---|
| 1 | 9 | 9 | Push |
| 2 | 4 | 9, 4 | Push |
| 3 | 3 | 9, 4, 3 | Push |
| 4 | 2 | 9, 4, 3, 2 | Push |
| 5 | / | 9, 4, 1 | 3/2 = 1 (integer division) |
| 6 | 1 | 9, 4, 1, 1 | Push |
| 7 | 5 | 9, 4, 1, 1, 5 | Push |
| 8 | + | 9, 4, 1, 6 | 1+5 = 6 |
| 9 | * | 9, 4, 6 | 1×6 = 6 |
| 10 | / | 9, 0 | 4/6 = 0 (integer) |
| 11 | * | 0 | 9×0 = 0 |
| 12 | + | — | insufficient operands |

Assuming real division at step 5: 3/2 = 1.5

| 5 | / | 9, 4, 1.5 | 3/2=1.5 |
| 8 | + | 9, 4, 1.5, 6 | 1+5=6 |
| 9 | * | 9, 4, 9 | 1.5×6=9 |
| 10 | / | 9, 0.44 | 4/9=0.44 |
| 11 | * | 4 | 9×0.44=4 |

> **Result ≈ 4** (with real division)

---

## Q.4(c) Drawbacks and advantages of adjacency list. (CO1, 02)

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

## Q.5(a) Dijkstra's: shortest path 1 to 8. (CO3, 04)

**Graph:** 1→2(1), 1→4(1), 2→3(2), 2→5(1), 3→5(2), 3→8(10), 4→1(3), 4→6(4), 5→7(3), 6→7(7), 7→8(7)

| Step | Visit | Dist 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Init | — | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | 1 | **0** | 1 | ∞ | 1 | ∞ | ∞ | ∞ | ∞ |
| 2 | 2 (d=1) | 0 | **1** | 3 | 1 | 2 | ∞ | ∞ | ∞ |
| 3 | 4 (d=1) | 0 | 1 | 3 | **1** | 2 | 5 | ∞ | ∞ |
| 4 | 5 (d=2) | 0 | 1 | 3 | 1 | **2** | 5 | 5 | ∞ |
| 5 | 3 (d=3) | 0 | 1 | **3** | 1 | 2 | 5 | 5 | 13 |
| 6 | 6 (d=5) | 0 | 1 | 3 | 1 | 2 | **5** | 5 | 13 |
| 7 | 7 (d=5) | 0 | 1 | 3 | 1 | 2 | 5 | **5** | 12 |
| 8 | 8 (d=12) | 0 | 1 | 3 | 1 | 2 | 5 | 5 | **12** |

> **Shortest path from 1 to 8 = 12**
> **Path: 1 → 2 → 5 → 7 → 8**

---

## Q.5(b) BST insertion code. (CO2, 03)

```
Procedure BST_INSERT(ROOT, ITEM)
    Create new node NEW with DATA = ITEM, LEFT = NULL, RIGHT = NULL
    If ROOT = NULL Then
        Set ROOT = NEW
        Return ROOT
    End If
    Set PTR = ROOT
    While TRUE do
        If ITEM < DATA[PTR] Then
            If LEFT[PTR] = NULL Then
                Set LEFT[PTR] = NEW
                Return ROOT
            Else
                Set PTR = LEFT[PTR]
            End If
        Else
            If RIGHT[PTR] = NULL Then
                Set RIGHT[PTR] = NEW
                Return ROOT
            Else
                Set PTR = RIGHT[PTR]
            End If
        End If
    End While
End Procedure
```

---

## Q.5(c) Binary tree height recursive. (CO2, 03)

```
Procedure HEIGHT(ROOT)
    If ROOT = NULL Then
        Return -1                    // empty tree has height -1
    End If
    Set LEFT_H = HEIGHT(LEFT[ROOT])
    Set RIGHT_H = HEIGHT(RIGHT[ROOT])
    Return MAX(LEFT_H, RIGHT_H) + 1
End Procedure
```

**Example:** For tree with root only → HEIGHT = MAX(-1,-1)+1 = 0.
For tree with depth 3 → returns 3.

---

## Q.6(a) BFS: minimum path A to J. (CO3, 04)

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

## Q.6(b) Prim's MST. (CO2, 03)

**Graph:** (1,2)=10, (1,4)=30, (2,3)=50, (2,5)=40, (2,4)=45, (3,4)=35, (3,5)=25, (4,5)=15, (4,6)=20, (5,6)=55

**Starting from node 1:**

| Step | Add Node | Edge Added | Cost | MST Nodes |
|---|---|---|---|---|
| 1 | 1 | — | — | {1} |
| 2 | 2 | (1,2) | 10 | {1,2} |
| 3 | 4 | (1,4) | 30 | {1,2,4} |
| 4 | 5 | (4,5) | 15 | {1,2,4,5} |
| 5 | 6 | (4,6) | 20 | {1,2,4,5,6} |
| 6 | 3 | (5,3) | 25 | {1,2,3,4,5,6} |

> **MST: {(1,2)=10, (1,4)=30, (4,5)=15, (4,6)=20, (5,3)=25} = 100**

---

## Q.6(c) Recurrence: T(n) = 2T(n/2) + n, T(1)=2. (CO2, 03)

**Substitution method:**

T(n) = 2T(n/2) + n
     = 2[2T(n/4) + n/2] + n = 4T(n/4) + 2n
     = 4[2T(n/8) + n/4] + 2n = 8T(n/8) + 3n
     ...
     = 2^k · T(n/2^k) + k·n

When n/2^k = 1 → k = log₂n:
T(n) = n · T(1) + n·log₂n = 2n + n·log₂n

> **T(n) = n log n + 2n = O(n log n)**

---

## Q.7(a) Bellman-Ford: node 4 to 1. Discuss result. (CO3, 04)

**Graph:** 1→3(5), 2→1(4), 2→4(7), 3→4(-15), 4→1(7)

**Source = 4:**

**Initialization:** dist[4]=0, dist[1]=∞, dist[2]=∞, dist[3]=∞

**Iteration 1 (relax all edges):**
- 4→1: 0+7=7 → dist[1]=7
- 1→3: 7+5=12 → dist[3]=12
- 3→4: 12+(-15)=-3 → dist[4]=-3
- 2→1: ∞ (skip), 2→4: ∞ (skip)

**Iteration 2:**
- 4→1: -3+7=4 < 7 → dist[1]=4
- 1→3: 4+5=9 < 12 → dist[3]=9
- 3→4: 9+(-15)=-6 < -3 → dist[4]=-6

**Iteration 3 (V-1 = 3):**
- 4→1: -6+7=1 < 4 → dist[1]=1
- 1→3: 1+5=6 < 9 → dist[3]=6
- 3→4: 6+(-15)=-9 < -6 → dist[4]=-9

**Negative Cycle Check (one more iteration):**
- Distances still decrease → **Negative cycle detected!**

> **Result: A negative cycle exists (4→1→3→4 with total weight 7+5-15 = -3). No finite shortest path exists from 4 to 1.**

---

## Q.7(b) N-Queen + 4-Queen solution. (CO1, 03)

**N-Queen Problem:** Place N queens on an N×N chessboard such that no two queens attack each other (no shared row, column, or diagonal).

**4-Queen Solutions using backtracking:**

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

---

## Q.7(c) Two applications of priority queue. (CO1, 02)

1. **Dijkstra's Algorithm** — uses a min-priority queue to always process the vertex with the smallest tentative distance next.

2. **CPU Scheduling** — operating systems use priority queues to schedule processes; higher-priority processes are executed before lower-priority ones.

---

## Q.8(a) Rotten Oranges BFS. (CO3, 05)

```
Procedure MIN_MINUTES_ROTTEN(GRID, M, N)
    Create empty Queue Q
    Set FRESH = 0, TIME = 0

    // Find all rotten oranges and count fresh ones
    For I = 1 to M do
        For J = 1 to N do
            If GRID[I][J] = 2 Then
                Enqueue (I, J) into Q
            Else If GRID[I][J] = 1 Then
                Set FRESH = FRESH + 1
            End If
        End For
    End For

    If FRESH = 0 Then Return 0          // no fresh oranges

    Set DIRECTIONS = {(0,1), (0,-1), (1,0), (-1,0)}

    While Q is not empty AND FRESH > 0 do
        Set SIZE = length of Q
        For K = 1 to SIZE do
            Set (R, C) = Dequeue from Q
            For each (DR, DC) in DIRECTIONS do
                Set NR = R + DR, NC = C + DC
                If NR, NC are valid AND GRID[NR][NC] = 1 Then
                    Set GRID[NR][NC] = 2
                    Set FRESH = FRESH - 1
                    Enqueue (NR, NC) into Q
                End If
            End For
        End For
        Set TIME = TIME + 1
    End While

    If FRESH > 0 Then
        Return -1                        // impossible
    Else
        Return TIME
    End If
End Procedure
```

---

## Q.8(b) Subset sum: m=31, W=(11,13,24,7). State space tree. (CO2, 03)

**Problem:** Find subsets of {11, 13, 24, 7} that sum to 31.

**State Space Tree (include/exclude each weight):**
```
                        []  (sum=0, remaining=55)
                       / \
               [11]       []
             (s=11,r=44)  (s=0,r=44)
              / \           / \
        [11,13] [11]    [13]   []
        (s=24)  (s=11)  (s=13) (s=0)
         / \     / \     / \    / \
    [+24] [11,13] [11,24] [11] [13,24] [13] [24] []
    s=48  s=24   s=35   s=11  s=37   s=13  s=24 s=0
    ✗     / \    ✗      / \   ✗      / \   / \  / \
      [+7] [no7]     [+7] [no]    [+7][no][+7][]
      s=31  s=24     s=18 s=11    s=20 s=13 s=31 s=0
      ✓✓    ✗        ✗    ✗       ✗    ✗   ✗   ✗
```

**Solutions found:**
1. **{11, 13, 7} = 31** ✓
2. **{24, 7} = 31** ✓

---

## Q.8(c) Define graph. Why linked representation is better. (CO1, 02)

**Graph:** A non-linear data structure consisting of a set of **vertices (V)** and **edges (E)** that connect pairs of vertices. G = (V, E).

**Why linked (adjacency list) representation is better than array (adjacency matrix):**

1. **Space:** Adjacency list uses O(V+E) space vs O(V²) for matrix — much better for sparse graphs
2. **Adding vertices:** Easy in list (add node), expensive in matrix (resize entire 2D array)
3. **Iterating neighbors:** O(degree) in list vs O(V) in matrix
4. **Real-world graphs** are usually sparse, making adjacency list the preferred choice

<br>

---
[⬅️ Previous](./2021_answer.md) | [🏠 Home](./README.md) | [Next ➡️](./2023_answer.md)
