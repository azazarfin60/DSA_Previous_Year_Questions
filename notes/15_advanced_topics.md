[⬅️ Previous](./14_graph_algorithms.md) | [🏠 Home](./README.md) | [Next ➡️](./cheatsheet.md)

---

# 📘 Chapter 15: Advanced Topics

> **Key Topics:** 0/1 Knapsack (DP), Fractional Knapsack (Greedy), Job Sequencing, N-Queens, NP-Hard/NP-Complete, Huffman Coding

---

## 1. 0/1 Knapsack Problem (Dynamic Programming)

### Problem
Given `n` items, each with a **weight** and a **value**, and a knapsack of capacity `W`. Find the maximum value you can carry **without exceeding capacity**. Each item is either taken completely or not taken (0 or 1 — no fractions).

### Intuition
You're a burglar with a bag that holds W kg. Each item in the house has a weight and value. You want to maximize total value without the bag exceeding W kg.

### Algorithm (DP Table)
Create table `V[i][w]` where:
- `i` = considering first i items
- `w` = current capacity
- `V[i][w]` = maximum value achievable

**Recurrence:**
```
V[i][w] = V[i-1][w]                              if wt[i] > w  (can't take item i)
V[i][w] = max(V[i-1][w], val[i] + V[i-1][w-wt[i]])   otherwise (take or skip)
```

### Worked Example

**Items:** n=4, W=7

| Item | Weight | Value |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 3 | 4 |
| 3 | 4 | 5 |
| 4 | 5 | 7 |

**DP Table:**

| i\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 0 | 1 | 1 | 4 | 5 | 5 | 5 | 5 |
| 3 | 0 | 1 | 1 | 4 | 5 | 6 | 6 | 9 |
| 4 | 0 | 1 | 1 | 4 | 5 | 7 | 8 | 9 |

**V[4][7] = 9** → Maximum value = 9

**Tracing selected items:** V[4][7]=9 ≠ V[3][7]=9, so item 4 NOT taken.
V[3][7]=9 ≠ V[2][7]=5, so item 3 IS taken (remaining capacity = 7-4=3).
V[2][3]=4 ≠ V[1][3]=1, so item 2 IS taken (remaining = 3-3=0).
V[1][0]=0 = V[0][0]=0, so item 1 NOT taken.

**Selected items: 2 and 3** (weight=3+4=7, value=4+5=9) ✅

### Pseudocode
```c
int knapsack01(int W, int wt[], int val[], int n) {
    int V[n+1][W+1];
    int i, w;
    
    for (i = 0; i <= n; i++) {
        for (w = 0; w <= W; w++) {
            if (i == 0 || w == 0)
                V[i][w] = 0;
            else if (wt[i-1] <= w)
                V[i][w] = max(val[i-1] + V[i-1][w-wt[i-1]], V[i-1][w]);
            else
                V[i][w] = V[i-1][w];
        }
    }
    return V[n][W];
}
```

**Complexity:** Time O(nW), Space O(nW)

---

## 2. Fractional Knapsack (Greedy Method)

### Problem
Same as 0/1 but you CAN take **fractions** of items.

### Algorithm
1. Calculate **value/weight ratio** for each item
2. Sort by ratio (descending)
3. Greedily take items with highest ratio first
4. If an item doesn't fit entirely, take a fraction

### Example

| Item | Weight | Value | Ratio |
|---|---|---|---|
| A | 10 | 60 | 6.0 |
| B | 20 | 100 | 5.0 |
| C | 30 | 120 | 4.0 |

**Capacity W = 50**

**Sorted by ratio:** A(6.0), B(5.0), C(4.0)

```
Take A: weight=10, value=60. Remaining capacity = 50-10 = 40
Take B: weight=20, value=100. Remaining = 40-20 = 20
Take C: Only 20 kg fits out of 30 → take 20/30 = 2/3 of C
  Value = (2/3) × 120 = 80

Total value = 60 + 100 + 80 = 240
```

### 0/1 vs Fractional Knapsack

| Criterion | 0/1 Knapsack | Fractional Knapsack |
|---|---|---|
| Fractions allowed? | ❌ No | ✅ Yes |
| Approach | Dynamic Programming | Greedy |
| Time | O(nW) | O(n log n) — sorting |
| Optimal? | Yes (DP guarantees) | Yes (greedy works here) |

---

## 3. Job Sequencing with Deadlines

### Problem
Given `n` jobs with **deadlines** and **profits**. Each job takes 1 unit of time. Only one job at a time. Maximize total profit by scheduling jobs before their deadlines.

### Algorithm (Greedy)
1. Sort jobs by **profit (descending)**
2. For each job, schedule it in the **latest available slot** before its deadline
3. If no slot available, skip the job

### Example

| Job | Deadline | Profit |
|---|---|---|
| J1 | 2 | 100 |
| J2 | 1 | 19 |
| J3 | 2 | 27 |
| J4 | 1 | 25 |
| J5 | 3 | 15 |

**Sorted by profit:** J1(100), J3(27), J4(25), J2(19), J5(15)

**Available slots:** [_, _, _] (3 time slots)

```
J1 (deadline=2, profit=100): Latest slot ≤ 2 → slot 2 available → place at slot 2
  Slots: [_, J1, _]

J3 (deadline=2, profit=27): Latest slot ≤ 2 → slot 2 taken → slot 1 available → place at slot 1
  Slots: [J3, J1, _]

J4 (deadline=1, profit=25): Latest slot ≤ 1 → slot 1 taken → NO SLOT → skip

J2 (deadline=1, profit=19): Latest slot ≤ 1 → slot 1 taken → skip

J5 (deadline=3, profit=15): Latest slot ≤ 3 → slot 3 available → place at slot 3
  Slots: [J3, J1, J5]
```

**Schedule: J3, J1, J5 | Total Profit: 27 + 100 + 15 = 142** ✅

---

## 4. N-Queens Problem (Backtracking)

### Problem
Place N queens on an N×N chessboard such that **no two queens attack each other** (no two in the same row, column, or diagonal).

### 4-Queens Solution

```
Board:     . Q . .         Solution positions: (0,1), (1,3), (2,0), (3,2)
           . . . Q
           Q . . .
           . . Q .
```

### Backtracking Approach
Place queens row by row. For each row, try each column. If safe (no conflict), move to next row. If no column works, **backtrack** to the previous row.

### Algorithm
```c
int isSafe(int board[][N], int row, int col) {
    int i, j;
    // Check column above
    for (i = 0; i < row; i++)
        if (board[i][col]) return 0;
    
    // Check upper-left diagonal
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j]) return 0;
    
    // Check upper-right diagonal
    for (i = row, j = col; i >= 0 && j < N; i--, j++)
        if (board[i][j]) return 0;
    
    return 1;
}

int solveNQueens(int board[][N], int row) {
    if (row == N) return 1;              // all queens placed
    
    for (int col = 0; col < N; col++) {
        if (isSafe(board, row, col)) {
            board[row][col] = 1;         // place queen
            if (solveNQueens(board, row + 1))
                return 1;               // solved!
            board[row][col] = 0;         // backtrack
        }
    }
    return 0;                            // no solution in this config
}
```

### State Space Tree for 4-Queens (partial)
```
Row 0: Try col 0 → Q at (0,0)
  Row 1: Try col 0 ✗ (same col)
          Try col 1 ✗ (diagonal)
          Try col 2 → Q at (1,2)
    Row 2: All cols fail → BACKTRACK
  Row 1: Try col 3 → Q at (1,3)
    Row 2: Try col 0 ✗, col 1 → Q at (2,1)
      Row 3: All cols fail → BACKTRACK
    Row 2: col 2 ✗, col 3 ✗ → BACKTRACK
  ...Eventually finds: (0,1), (1,3), (2,0), (3,2) ✓
```

---

## 5. NP-Hard and NP-Complete

### Definitions

| Class | Definition |
|---|---|
| **P** | Problems solvable in **polynomial time** — O(n^k) for some constant k |
| **NP** | Problems whose solutions can be **verified** in polynomial time |
| **NP-Hard** | At least as hard as the hardest NP problems. May not be in NP. |
| **NP-Complete** | Both **NP** AND **NP-Hard** (hardest problems in NP) |

### Intuition
- **P:** Easy to solve AND verify (sorting, searching)
- **NP:** Maybe hard to solve, but easy to CHECK a given answer (Sudoku: hard to solve, easy to verify)
- **NP-Complete:** The hardest problems in NP. If ANY NP-Complete problem has a polynomial solution, ALL NP problems do (P = NP)
- **NP-Hard:** At least as hard as NP-Complete, but might not even be verifiable in polynomial time

### Relationship
```
    ┌─────────────────────────────┐
    │         NP-Hard             │
    │    ┌──────────────────┐     │
    │    │   NP-Complete    │     │
    │    │   ┌──────────┐   │     │
    │    │   │    P      │   │     │
    │    │   └──────────┘   │     │
    │    └──────────────────┘     │
    └─────────────────────────────┘
    
    (assuming P ≠ NP)
```

### Examples
| Class | Examples |
|---|---|
| **P** | Sorting, searching, shortest path, MST |
| **NP-Complete** | Travelling Salesman (decision), 3-SAT, Subset Sum, Graph Coloring, Hamiltonian Cycle |
| **NP-Hard** | Travelling Salesman (optimization), Halting Problem |

---

## 6. Huffman Coding

### Concept
A **lossless data compression** algorithm that assigns **variable-length codes** to characters based on frequency. More frequent characters get shorter codes.

### Algorithm
1. Create a leaf node for each character with its frequency
2. Build a min-heap from these nodes
3. Repeat until one node remains:
   - Extract the two minimum frequency nodes
   - Create a new node with their sum as frequency
   - Make the two nodes its children (left=0, right=1)
4. Read codes by traversing root to each leaf

### Example

| Character | Frequency |
|---|---|
| a | 5 |
| b | 9 |
| c | 12 |
| d | 13 |
| e | 16 |
| f | 45 |

**Step-by-step building:**
```
Combine a(5) + b(9) = 14
Combine c(12) + d(13) = 25
Combine 14 + e(16) = 30
Combine 25 + 30 = 55
Combine f(45) + 55 = 100

Huffman Tree:
              100
             /    \
           f(45)   55
                  /   \
                25     30
               / \    / \
             c(12) d(13) 14 e(16)
                        / \
                      a(5) b(9)
```

**Codes (left=0, right=1):**

| Character | Code | Bits |
|---|---|---|
| f | 0 | 1 |
| c | 100 | 3 |
| d | 101 | 3 |
| a | 1100 | 4 |
| b | 1101 | 4 |
| e | 111 | 3 |

Most frequent character (f: 45) gets shortest code (1 bit). Least frequent (a: 5) gets longest (4 bits).

---

## 7. Performance Analysis vs Performance Measurement

### 7.1 Definitions
| Criterion | Performance Analysis (A Priori) | Performance Measurement (A Posteriori) |
|---|---|---|
| **What is it?** | Theoretical estimation of resource usage (Time/Space Complexity). | Actual measurement of running time and memory usage. |
| **When is it done?** | Before implementation (during algorithm design). | After implementation and compilation. |
| **Dependency** | Independent of hardware, language, or compiler. | Highly dependent on CPU speed, RAM, OS, compiler, and language. |
| **Output Format** | Expressed in asymptotic notations (O, Ω, Θ). | Expressed in absolute time (seconds/milliseconds) or bytes. |

### 7.2 Why is Analysis preferred?
Measurement is hardware-dependent. An O(n²) algorithm might run faster than an O(n) algorithm on a supercomputer vs a phone for small inputs, giving a misleading conclusion. Analysis provides a universal, hardware-independent metric.

---

## 8. Garbage Collection

### 8.1 Definition
**Garbage Collection (GC)** is a form of automatic memory management. The garbage collector attempts to reclaim garbage, or memory occupied by objects that are no longer in use by the program.

### 8.2 Common Approaches
1. **Reference Counting:** Every object keeps a count of the number of references to it. When the count reaches zero, the object's memory is reclaimed. (Problem: Cannot handle cyclic references).
2. **Mark-and-Sweep:** 
   - **Mark phase:** Traverses from root objects and marks all reachable objects as "alive".
   - **Sweep phase:** Scans the heap and frees any memory that is not marked.

---

## 9. Exam-Ready Summary

### Quick Revision Points
1. **0/1 Knapsack (DP):** Build table V[i][w], each item taken or not. O(nW).
2. **Fractional Knapsack (Greedy):** Sort by value/weight ratio, take greedily. O(n log n).
3. **Job Sequencing:** Sort by profit, assign latest available slot. Greedy.
4. **N-Queens:** Backtracking — place row by row, check safety, backtrack on failure.
5. **NP-Complete:** Both in NP and NP-Hard. No known polynomial solution.
6. **Huffman:** Greedy, min-heap, frequent chars get shorter codes.
7. **Performance Analysis vs Measurement:** Analysis = theoretical (O notation), Measurement = actual time (seconds).
8. **Garbage Collection:** Automatic memory cleanup (Reference counting, Mark-and-sweep).

---

## 10. Practice Problems (From Past Exams)

### Problem 1 [2022, 2024, 04 marks]
**Q:** Solve 0/1 Knapsack for items with weights [2,3,4,5], values [3,4,5,6], capacity W=5.

**Approach:** Build 4×5 DP table, trace back selected items.

### Problem 2 [2021, 2023, 03–04 marks]
**Q:** Apply fractional knapsack on given items with capacity W.

**Approach:** Calculate ratios → sort → take greedily → show fraction for last item.

### Problem 3 [2019, 2020, 2022, 03–04 marks]
**Q:** Solve 4-Queens problem. Show the state space tree.

**Approach:** Draw partial state space tree showing placements and backtracks → give final board.

---

*← [14 — Graph Algorithms](14_graph_algorithms.md) | [Back to Index →](00_index.md)*

<br>

---
[⬅️ Previous](./14_graph_algorithms.md) | [🏠 Home](./README.md) | [Next ➡️](./cheatsheet.md)
