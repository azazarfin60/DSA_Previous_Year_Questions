[⬅️ Previous](./01_data_structures_fundamentals.md) | [🏠 Home](./README.md) | [Next ➡️](./03_linked_lists.md)

---

# 📘 Chapter 2: Arrays and Matrices

> **Exam Frequency:** 2/8 years (Sparse Matrix), address calculation appears indirectly
> **Typical Marks:** 03–04 | **Section:** A
> **Key Topics:** Multi-dimensional arrays, Row/Column Major, Address formulas, Sparse Matrix

---

## 1. What is an Array?

An **array** is a linear data structure that stores a fixed-size collection of elements of the **same data type** in **contiguous memory locations**, where each element is identified by an **index** (or subscript).

### Intuition
Think of a row of numbered mailboxes in an apartment building. Each mailbox:
- Has a **fixed position** (index)
- Holds **one item** (data)
- Is **right next to** the others (contiguous memory)
- You can go directly to mailbox #47 without checking 1–46 (random access)

### Declaration in C
```c
int A[5];           // 1D array of 5 integers
float B[3][4];      // 2D array of 3 rows × 4 columns
int C[2][3][4];     // 3D array
```

### Key Properties

| Property | Description |
|---|---|
| **Fixed size** | Size declared at compile time (static allocation) |
| **Homogeneous** | All elements must be of the same data type |
| **Contiguous** | Elements stored in adjacent memory cells |
| **Random access** | Any element accessed in O(1) using index |
| **Zero-indexed** | In C, indexing starts from 0 (A[0], A[1], ...) |

### Time Complexity of Array Operations

| Operation | Time | Why |
|---|---|---|
| Access (by index) | O(1) | Direct address calculation |
| Search (unsorted) | O(n) | Must scan linearly |
| Search (sorted) | O(log n) | Binary search |
| Insert (at end) | O(1) | No shifting needed |
| Insert (at position) | O(n) | Must shift elements right |
| Delete (at position) | O(n) | Must shift elements left |
| Traverse | O(n) | Visit each element once |

---

## 2. One-Dimensional Arrays

### Memory Representation

A 1D array `A[0..n-1]` is stored sequentially starting from a **base address** `B`:

```
Memory:
  B     B+w   B+2w  B+3w  B+4w
  ┌─────┬─────┬─────┬─────┬─────┐
  │ A[0]│ A[1]│ A[2]│ A[3]│ A[4]│
  └─────┴─────┴─────┴─────┴─────┘
```

where `w` = size of each element in bytes (e.g., `int` = 4 bytes).

### Address Formula

The address of element `A[i]` is:

> **Address(A[i]) = B + i × w**

Where:
- `B` = base address (address of A[0])
- `i` = index of the element
- `w` = size of one element in bytes

**Example:** If `B = 1000`, `w = 4` (integer), find address of `A[3]`:
```
Address(A[3]) = 1000 + 3 × 4 = 1000 + 12 = 1012
```

### For arrays with lower bound `LB` (not starting from 0):

> **Address(A[i]) = B + (i − LB) × w**

**Example:** Array `A[5..10]`, base address = 2000, each element = 2 bytes.
Address of `A[7]`:
```
Address(A[7]) = 2000 + (7 − 5) × 2 = 2000 + 4 = 2004
```

---

## 3. Multi-Dimensional Arrays (2D Arrays)

A 2D array is essentially a **matrix** — a table of rows and columns.

### Declaration
```c
int A[M][N];    // M rows, N columns
```

### Logical View
```
         Col 0  Col 1  Col 2  Col 3
Row 0  [  10     20     30     40  ]
Row 1  [  50     60     70     80  ]
Row 2  [  90    100    110    120  ]
```

This is a 3×4 matrix (3 rows, 4 columns).

### The Key Question: How Is a 2D Array Stored in 1D Memory?

Computer memory is **linear** (1D), but arrays can be 2D, 3D, etc. So we must **flatten** the multi-dimensional array into a linear sequence. There are **two ways** to do this:

---

### 3.1 Row-Major Order

**Rule:** Store elements **row by row** — complete one row, then move to the next.

```
Logical View:                Stored in Memory:
  [10  20  30  40]           [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
  [50  60  70  80]            ←── Row 0 ───→ ←── Row 1 ──→ ←─── Row 2 ───→
  [90 100 110 120]
```

### Intuition
Think of reading a book — you read **left to right, then move to the next line**. Row-major reads each row completely before moving to the next row.

### Address Formula (Row-Major)

For array `A[M][N]` (M rows, N columns), base address `B`, element size `w`:

> **Address(A[i][j]) = B + (i × N + j) × w**

**Breaking it down:**
- `i × N` = skip `i` complete rows (each has N elements)
- `+ j` = then move `j` positions into the current row
- `× w` = multiply by element size for byte address

**Example:** Array `A[3][4]`, B = 1000, w = 4. Find address of `A[2][1]`:
```
Address(A[2][1]) = 1000 + (2 × 4 + 1) × 4
                 = 1000 + (8 + 1) × 4
                 = 1000 + 9 × 4
                 = 1000 + 36
                 = 1036
```

**Verification by listing all addresses:**
```
A[0][0] = 1000    A[0][1] = 1004    A[0][2] = 1008    A[0][3] = 1012
A[1][0] = 1016    A[1][1] = 1020    A[1][2] = 1024    A[1][3] = 1028
A[2][0] = 1032    A[2][1] = 1036 ✓  A[2][2] = 1040    A[2][3] = 1044
```

### Generalized Formula (with lower bounds)

For array `A[LR..UR][LC..UC]`:

> **Address(A[i][j]) = B + [(i − LR) × (UC − LC + 1) + (j − LC)] × w**

Where:
- `LR, UR` = lower and upper row bounds
- `LC, UC` = lower and upper column bounds
- `(UC − LC + 1)` = number of columns

---

### 3.2 Column-Major Order

**Rule:** Store elements **column by column** — complete one column, then move to the next.

```
Logical View:                Stored in Memory:
  [10  20  30  40]           [10, 50, 90, 20, 60, 100, 30, 70, 110, 40, 80, 120]
  [50  60  70  80]            ←─ Col 0 ─→ ←─ Col 1 ──→ ←── Col 2 ──→ ←─ Col 3─→
  [90 100 110 120]
```

### Intuition
Think of reading a newspaper column — you read **top to bottom, then move to the next column**. Column-major reads each column completely before moving to the next.

### Address Formula (Column-Major)

For array `A[M][N]`:

> **Address(A[i][j]) = B + (j × M + i) × w**

**Breaking it down:**
- `j × M` = skip `j` complete columns (each has M elements)
- `+ i` = then move `i` positions into the current column
- `× w` = multiply by element size

**Example:** Array `A[3][4]`, B = 1000, w = 4. Find address of `A[2][1]`:
```
Address(A[2][1]) = 1000 + (1 × 3 + 2) × 4
                 = 1000 + (3 + 2) × 4
                 = 1000 + 5 × 4
                 = 1000 + 20
                 = 1020
```

### Generalized Formula (with lower bounds)

For array `A[LR..UR][LC..UC]`:

> **Address(A[i][j]) = B + [(j − LC) × (UR − LR + 1) + (i − LR)] × w**

---

### 3.3 Row-Major vs Column-Major — Comparison

| Criterion | Row-Major | Column-Major |
|---|---|---|
| Storage order | Row by row | Column by column |
| Used by | **C**, C++, Java, Python | **Fortran**, MATLAB, R |
| Formula | B + (i×N + j) × w | B + (j×M + i) × w |
| Cache-friendly when | Accessing elements across columns (same row) | Accessing elements down rows (same column) |

### Quick Memory Trick
- **R**ow-Major: **R**ight first (go across the row, then down)
- **C**olumn-Major: **C**olumn first (go down the column, then right)

---

### 3.4 Worked Example — Complete Address Calculation

**Problem:** Given array `A[2..5][3..7]` stored in **row-major order** with base address 100 and element size 2 bytes, find the address of `A[4][5]`.

**Step 1:** Identify parameters.
- LR = 2, UR = 5, LC = 3, UC = 7
- Number of columns = UC − LC + 1 = 7 − 3 + 1 = 5
- B = 100, w = 2

**Step 2:** Apply row-major formula.
```
Address(A[4][5]) = B + [(i − LR) × (UC − LC + 1) + (j − LC)] × w
                 = 100 + [(4 − 2) × 5 + (5 − 3)] × 2
                 = 100 + [2 × 5 + 2] × 2
                 = 100 + [10 + 2] × 2
                 = 100 + 12 × 2
                 = 100 + 24
                 = 124
```

> **Address(A[4][5]) = 124** ✅

**Cross-check with column-major:**
```
Address(A[4][5]) = B + [(j − LC) × (UR − LR + 1) + (i − LR)] × w
                 = 100 + [(5 − 3) × (5 − 2 + 1) + (4 − 2)] × 2
                 = 100 + [2 × 4 + 2] × 2
                 = 100 + [8 + 2] × 2
                 = 100 + 10 × 2
                 = 100 + 20
                 = 120    (different because storage order is different!)
```

---

## 4. Sparse Matrix

### 4.1 What is a Sparse Matrix?

A **sparse matrix** is a matrix in which **most of the elements are zero** (or a default value). Storing such a matrix as a regular 2D array wastes enormous amounts of memory.

### Definition
> A matrix is called **sparse** if the number of non-zero elements is **significantly less** than the total number of elements.

### Intuition
Imagine a 1000-seat auditorium where only 10 seats are occupied. Recording the status of all 1000 seats is wasteful. Instead, just record: "Seat 23: John, Seat 47: Sarah, Seat 156: Ali, ..." — only the occupied seats.

### Example
```
Original 5×5 Matrix:
  0  0  3  0  0
  0  0  0  0  0
  7  0  0  0  0
  0  0  0  0  2
  0  0  0  9  0

Total elements: 25
Non-zero elements: 4
Zero elements: 21 (84% are zeros — this is sparse!)
```

### 4.2 Why Not Use a Regular 2D Array?

| Metric | Regular 2D Array | Sparse Representation |
|---|---|---|
| Memory for 1000×1000 matrix, 50 non-zeros | 1,000,000 cells | 50 × 3 = 150 cells |
| Wasted memory | 999,950 cells (99.995%) | 0 |
| Access time | O(1) random access | O(n) where n = non-zero count |

### 4.3 Sparse Matrix Representation — Triplet Method

Store only the non-zero elements as triplets: **(row, column, value)**

Also store the matrix dimensions in the first row of the triplet array.

**Example:**
```
Original Matrix (4×5):
  0  0  3  0  4
  0  0  0  0  0
  5  0  0  0  0
  0  6  0  0  0

Triplet Representation:
  Row  Col  Value
  ─────────────────
   4    5    4       ← header: 4 rows, 5 cols, 4 non-zero elements
   0    2    3
   0    4    4
   2    0    5
   3    1    6
```

**Memory saved:**
- Regular: 4 × 5 = 20 cells
- Sparse: 4 triplet rows (3 non-zero + 1 header) × 3 columns = 12 cells.

**Class Example Calculation (7×4 Matrix):**
Consider a 7×4 matrix with only 3 non-zero elements. Assuming each element takes 2 bytes:
- **Original Array Storage:** $7 \times 4 \times 2 = 56$ Bytes
- **Triplet Storage:** 4 triplet rows (3 non-zeros + 1 header) $\times$ 3 columns (row, col, val) $\times$ 2 bytes = $4 \times 3 \times 2 = 24$ Bytes
- **Improvement:** $\frac{56 - 24}{56} \times 100 = \mathbf{57.14\%}$ memory savings.

### 4.4 Sparse Matrix — Linked List Representation

Each non-zero element is stored as a node with fields: `(row, col, value, next)`

```
HEAD → (0,2,3) → (0,4,4) → (2,0,5) → (3,1,6) → NULL
```

**Advantages of LL representation:**
- Easy to insert/delete non-zero elements
- No pre-defined size limit
- Dynamic memory allocation

**Disadvantages:**
- Extra memory for pointers
- No random access — must traverse sequentially

### 4.5 Operations on Sparse Matrices

**Transpose of Sparse Matrix (Triplet):**
```
Original:              Transpose:
Row  Col  Value        Row  Col  Value
 4    5    4            5    4    4      ← header: rows↔cols
 0    2    3            2    0    3      ← swap row & col
 0    4    4            4    0    4
 2    0    5            0    2    5
 3    1    6            1    3    6
```

Then sort by row (and within same row, by column) for proper sparse representation.

**Algorithm — Fast Transpose:**
**C++ Style:**
```cpp
#include <vector>
using namespace std;

const int MAX_COL = 100; // Arbitrary maximum for illustration

struct Term {
    int row;
    int col;
    int value;
};

struct SparseMatrix {
    int rows;
    int cols;
    int terms;
    vector<Term> data;
};

void fastTranspose(const SparseMatrix& a, SparseMatrix& b) {
    vector<int> rowTerms(a.cols, 0);
    vector<int> startingPos(a.cols, 0);
    
    b.rows = a.cols;       // swap dimensions
    b.cols = a.rows;
    b.terms = a.terms;
    b.data.resize(a.terms);
    
    // Count elements in each column of 'a' (= row of 'b')
    for (int i = 0; i < a.terms; i++) {
        rowTerms[a.data[i].col]++;
    }
    
    // Starting position of each row in 'b'
    startingPos[0] = 0;
    for (int i = 1; i < a.cols; i++) {
        startingPos[i] = startingPos[i - 1] + rowTerms[i - 1];
    }
    
    // Place each element in correct position
    for (int i = 0; i < a.terms; i++) {
        int j = startingPos[a.data[i].col]++;
        b.data[j].row = a.data[i].col;
        b.data[j].col = a.data[i].row;
        b.data[j].value = a.data[i].value;
    }
}
```

**OR, Textbook Style:**
```
Procedure FAST_TRANSPOSE(A, B)
    Set B.rows = A.cols
    Set B.cols = A.rows
    Set B.terms = A.terms
    
    // Count elements in each column of A
    For I = 0 to A.cols - 1 do
        Set ROW_TERMS[I] = 0
    End For
    
    For I = 0 to A.terms - 1 do
        Set ROW_TERMS[A.data[I].col] = ROW_TERMS[A.data[I].col] + 1
    End For
    
    // Calculate starting position of each row in B
    Set STARTING_POS[0] = 0
    For I = 1 to A.cols - 1 do
        Set STARTING_POS[I] = STARTING_POS[I-1] + ROW_TERMS[I-1]
    End For
    
    // Transpose
    For I = 0 to A.terms - 1 do
        Set J = STARTING_POS[A.data[I].col]
        Set B.data[J].row = A.data[I].col
        Set B.data[J].col = A.data[I].row
        Set B.data[J].value = A.data[I].value
        Set STARTING_POS[A.data[I].col] = STARTING_POS[A.data[I].col] + 1
    End For
End Procedure
```
**Time Complexity:** O(columns + non-zero terms) = O(n + t)

---

## 5. Array vs Linked List — Detailed Comparison

This is an **extremely frequently asked** comparison question in the exam.

| Criterion | Array | Linked List |
|---|---|---|
| **Memory allocation** | Static (compile time) | Dynamic (runtime) |
| **Memory layout** | Contiguous | Non-contiguous |
| **Size** | Fixed — must declare in advance | Flexible — grows/shrinks as needed |
| **Access** | Random access O(1) | Sequential access O(n) |
| **Insertion** | O(n) — shifting needed | O(1) — pointer change (after position found) |
| **Deletion** | O(n) — shifting needed | O(1) — pointer change |
| **Memory waste** | May waste (unused allocated slots) | No waste (allocate per node) |
| **Extra memory** | None | Pointer per node (4–8 bytes) |
| **Cache performance** | Excellent (contiguous → cache-friendly) | Poor (scattered in memory) |
| **Binary search** | Possible (O(log n)) | Not possible (no random access) |

**When to use Array:** When size is known, random access is needed, cache performance matters.
**When to use Linked List:** When size varies, frequent insertions/deletions, no need for random access.

---

## 6. Exam-Ready Summary

### Key Formulas to Memorize

| Formula | For |
|---|---|
| `B + i × w` | 1D array address |
| `B + (i×N + j) × w` | 2D Row-Major |
| `B + (j×M + i) × w` | 2D Column-Major |
| With bounds: `(i−LR)×(UC−LC+1) + (j−LC)` | Row-Major generalized |
| With bounds: `(j−LC)×(UR−LR+1) + (i−LR)` | Column-Major generalized |

### Quick Revision Points
1. **Row-Major** = row by row (C, C++, Java use this)
2. **Column-Major** = column by column (Fortran, MATLAB use this)
3. **Sparse Matrix** = mostly zeros → store only non-zeros as triplets
4. **Triplet** = (row, col, value) — saves memory for sparse data
5. Array vs LL comparison — prepare a 6-row table

---

## 7. Practice Problems (From Past Exams)

### Problem 1 [2019, indirect, 03 marks]
**Q:** Represent the following sparse matrix efficiently and find its transpose.
```
  0  0  5  0
  0  0  0  0
  3  0  0  0
  0  7  0  0
```

**Approach:** Write triplet representation → swap row/col in each triplet → reorder.

### Problem 2 [Address Calculation — common in theory]
**Q:** Array `A[1..8][1..5]` is stored in row-major order. Base address = 200, element size = 4 bytes. Find address of `A[5][3]`.

**Solution:**
```
Address = 200 + [(5−1) × (5−1+1) + (3−1)] × 4
        = 200 + [4 × 5 + 2] × 4
        = 200 + 22 × 4
        = 200 + 88
        = 288
```

### Problem 3 [Memory calculation — from topic list emphasis]
**Q:** How much memory is needed for an array `int A[100][200]` if each integer is 4 bytes? If the matrix is sparse with only 300 non-zero values, how much memory does triplet representation save?

**Solution:**
```
Regular 2D array: 100 × 200 × 4 = 80,000 bytes = 78.1 KB
Triplet: 300 × 3 × 4 = 3,600 bytes = 3.5 KB
Savings: 80,000 − 3,600 = 76,400 bytes = 74.6 KB saved (95.5% reduction)
```

---

*← [01 — Data Structures Fundamentals](01_data_structures_fundamentals.md) | Next: [03 — Linked Lists →](03_linked_lists.md)*

<br>

---
[⬅️ Previous](./01_data_structures_fundamentals.md) | [🏠 Home](./README.md) | [Next ➡️](./03_linked_lists.md)
