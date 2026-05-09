[⬅️ Previous](./10_bst_and_avl.md) | [🏠 Home](./README.md) | [Next ➡️](./12_hashing.md)

---

# 📘 Chapter 11: Heap

> **Exam Frequency:** 7/8 years | **Typical Marks:** 03–05 | **Section:** A
> **Key Topics:** Min-Heap, Max-Heap, Build-Heap, Insert, Delete, Heapsort

---

## 1. What is a Heap?

A **heap** is a **complete binary tree** that satisfies the **heap property**:

- **Max-Heap:** Every parent is **greater than or equal to** its children → root is the **maximum**
- **Min-Heap:** Every parent is **less than or equal to** its children → root is the **minimum**

```
Max-Heap:               Min-Heap:
       90                      5
      /  \                   /   \
    70    80               10     15
   / \   /                / \   /
  50 60 40               20 30 25
```

### Key Properties
1. **Complete binary tree** — all levels filled except possibly the last (filled left to right)
2. **Heap-ordered** — parent ≥ children (max) or parent ≤ children (min)
3. **NOT a BST** — there's no left-right ordering between siblings
4. **Root is always the extreme value** — max (max-heap) or min (min-heap)

### Array Representation
Since a heap is a complete binary tree, it can be stored efficiently in an **array** (no pointers needed):

For node at index `i` (0-indexed):
- **Parent:** `(i - 1) / 2`
- **Left child:** `2i + 1`
- **Right child:** `2i + 2`

```
Max-Heap:        90
                /  \
              70    80
             / \   /
            50 60 40

Array: [90, 70, 80, 50, 60, 40]
Index:   0   1   2   3   4   5

Parent of index 4 (60): (4-1)/2 = 1 → 70 ✓
Children of index 1 (70): 2(1)+1=3 → 50, 2(1)+2=4 → 60 ✓
```

---

## 2. Heap Operations

### 2.1 Insert (Push Up / Sift Up / Heapify Up)

**Steps:**
1. Add the new element at the **end** of the array (next available position in complete tree)
2. **Bubble up:** Compare with parent — if heap property is violated, swap with parent
3. Repeat until heap property is restored or root is reached

**Example: Insert 95 into Max-Heap [90, 70, 80, 50, 60, 40]**

```
Step 1: Add 95 at end
  [90, 70, 80, 50, 60, 40, 95]
  
         90
        /  \
      70    80
     / \   / \
    50 60 40  95

Step 2: 95 > parent 80 → swap
  [90, 70, 95, 50, 60, 40, 80]
  
         90
        /  \
      70    95
     / \   / \
    50 60 40  80

Step 3: 95 > parent 90 → swap
  [95, 70, 90, 50, 60, 40, 80]
  
         95          ← new root (maximum)
        /  \
      70    90
     / \   / \
    50 60 40  80
```

**Time:** O(log n) — at most traverse the height of the tree.

### 2.2 Delete (Extract Max/Min — Sift Down / Heapify Down)

**Steps:**
1. Replace the root with the **last element**
2. Remove the last position
3. **Sift down:** Compare with children — swap with the larger child (max-heap) or smaller child (min-heap)
4. Repeat until heap property is restored or a leaf is reached

**Example: Delete max from Max-Heap [95, 70, 90, 50, 60, 40, 80]**

```
Step 1: Replace root with last element (80)
  [80, 70, 90, 50, 60, 40]
  
         80
        /  \
      70    90
     / \   /
    50 60 40

Step 2: 80 < larger child 90 → swap with 90
  [90, 70, 80, 50, 60, 40]
  
         90
        /  \
      70    80
     / \   /
    50 60 40

Step 3: 80 > child 40 → stop (heap property restored)

Extracted value: 95
```

**Time:** O(log n)

---

## 3. Building a Heap (Heapify)

### 3.1 Build Min-Heap from: 34, 30, 40, 22, 50, 2, 55, 77, 55

This exact problem appeared in **2022 and 2024**.

**Method:** Start from the last non-leaf node and sift down each node.

**Step 1:** Place all elements as a complete binary tree:
```
Array: [34, 30, 40, 22, 50, 2, 55, 77, 55]
Index:   0   1   2   3   4  5   6   7   8

             34
           /    \
         30      40
        /  \    /  \
      22   50  2   55
     / \
    77  55
```

**Step 2:** Last non-leaf = index (9/2)-1 = 3. Start heapifying from index 3 down to 0.

**Heapify index 3 (22):**
Children: 77(idx 7), 55(idx 8). 22 < both → no swap needed. ✓

**Heapify index 2 (40):**
Children: 2(idx 5), 55(idx 6). Min child = 2. 40 > 2 → swap.
```
             34
           /    \
         30       2
        /  \    /  \
      22   50 40   55
     / \
    77  55
```

**Heapify index 1 (30):**
Children: 22(idx 3), 50(idx 4). Min child = 22. 30 > 22 → swap.
```
             34
           /    \
         22       2
        /  \    /  \
      30   50 40   55
     / \
    77  55
```
Continue sifting 30 down: Children 77, 55. 30 < both → stop. ✓

**Heapify index 0 (34):**
Children: 22(idx 1), 2(idx 2). Min child = 2. 34 > 2 → swap.
```
              2
           /    \
         22      34
        /  \    /  \
      30   50 40   55
     / \
    77  55
```
Continue sifting 34 down: Children 40(idx 5), 55(idx 6). 34 < 40 → stop. ✓

**Final Min-Heap:**
```
              2
           /    \
         22      34
        /  \    /  \
      30   50 40   55
     / \
    77  55

Array: [2, 22, 34, 30, 50, 40, 55, 77, 55]
```

### 3.2 Insert 80 and 75 into this Min-Heap

**Insert 80:**
```
Add at end: [2, 22, 34, 30, 50, 40, 55, 77, 55, 80]
Parent of 80 (idx 9) = idx 4 → 50. 80 > 50 → no swap needed. ✓
```

**Insert 75:**
```
Add at end: [2, 22, 34, 30, 50, 40, 55, 77, 55, 80, 75]
Parent of 75 (idx 10) = idx 4 → 50. 75 > 50 → no swap needed. ✓
```

**Time to build heap:** O(n) (not O(n log n) — mathematical proof exists)

---

## 4. Heapsort

### Algorithm
1. Build a max-heap from the array
2. Repeatedly extract the maximum (swap root with last element, reduce heap size, sift down)

**C++ Style:**
```cpp
void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);   // recursive sift down
    }
}

void heapSort(int arr[], int n) {
    // Build max-heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    
    // Extract elements one by one
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];              // swap root (max) with last
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);        // heapify reduced heap
    }
}
```

**OR, Textbook Style:**
```
Procedure HEAPIFY(A, N, I)
    Set LARGEST = I
    Set LEFT = 2 * I + 1
    Set RIGHT = 2 * I + 2
    
    If LEFT < N AND A[LEFT] > A[LARGEST] Then
        Set LARGEST = LEFT
    End If
    If RIGHT < N AND A[RIGHT] > A[LARGEST] Then
        Set LARGEST = RIGHT
    End If
    
    If LARGEST ≠ I Then
        Swap A[I] and A[LARGEST]
        Call HEAPIFY(A, N, LARGEST)
    End If
End Procedure

Procedure HEAPSORT(A, N)
    For I = (N / 2) - 1 down to 0 do
        Call HEAPIFY(A, N, I)
    End For
    
    For I = N - 1 down to 1 do
        Swap A[0] and A[I]
        Call HEAPIFY(A, I, 0)
    End For
End Procedure
```

### Complexity

| | Time |
|---|---|
| Build Heap | O(n) |
| n extractions × sift down | O(n log n) |
| **Total** | **O(n log n)** all cases |
| Space | O(1) — in-place |
| Stable? | No |

---

## 5. Min-Heap vs Max-Heap

| Criterion | Min-Heap | Max-Heap |
|---|---|---|
| Root | Minimum value | Maximum value |
| Parent vs children | Parent ≤ children | Parent ≥ children |
| Extract | Extract-min (O(log n)) | Extract-max (O(log n)) |
| Use | Priority queue (min priority first) | Priority queue (max priority first) |

---

## 6. B-Tree

### 6.1 Definition
A **B-tree of order m** is a self-balancing search tree designed for systems that read and write large blocks of data (disk-based storage). Every node can have **up to m children** and **up to m−1 keys**.

### 6.2 Properties of B-tree of order m:
1. Every node has **at most m children**
2. Every node (except root) has **at least ⌈m/2⌉ children**
3. The root has **at least 2 children** (if it's not a leaf)
4. All **leaves appear at the same level**
5. A non-leaf node with k children contains **k−1 keys**
6. Keys within a node are in **sorted order**

### 6.3 Example: B-tree of order 3 (2-3 tree)
Each node has at most 3 children and 2 keys.

```
              [20, 40]
             /   |    \
      [10,15] [25,30] [50,60]
```

### 6.4 Why B-trees?
- Designed for **disk-based storage** where reading a large block is efficient
- **Minimizes disk I/O** — each node read brings many keys
- Used in **databases** and **file systems**
- All operations are O(log n) with a very large branching factor

### 6.5 B-tree vs BST

| Criterion | BST | B-tree |
|---|---|---|
| Max children per node | 2 | m (can be thousands) |
| Height for n keys | O(log₂ n) | O(log_m n) — much shorter |
| Best for | In-memory data | Disk-based data |
| Balance | Not guaranteed (unless AVL/RB) | Always balanced |
| Keys per node | 1 | Up to m−1 |

---

## 7. Exam-Ready Summary

### Quick Revision Points
1. **Heap** = complete binary tree + heap property (max or min)
2. **Array storage:** Parent = (i-1)/2, Left = 2i+1, Right = 2i+2
3. **Insert:** Add at end → bubble UP → O(log n)
4. **Delete root:** Replace root with last → sift DOWN → O(log n)
5. **Build heap:** Start from last non-leaf → sift down each → **O(n)**
6. **Heapsort:** Build max-heap + n extractions → O(n log n) guaranteed
7. **Min-heap from [34,30,40,22,50,2,55,77,55]** → result: [2,22,34,30,50,40,55,77,55]
8. **B-tree order m:** up to m children, m−1 keys per node, all leaves same level

---

## 8. Practice Problems (From Past Exams)

### Problem 1 [2022 & 2024, 04–05 marks]
**Q:** Build min-heap from: 34, 30, 40, 22, 50, 2, 55, 77, 55. Insert 80 and 75.

**Answer:** See Section 3 above.

### Problem 2 [2017 & 2018, 03–04 marks]
**Q:** Insert 80 and 75 into an existing heap. Show each step.

**Approach:** Add at end → bubble up, showing array state after each swap.

### Problem 3 [Typical, 03 marks]
**Q:** Delete the root from max-heap [90, 70, 80, 50, 60, 40]. Show the resulting heap.

**Answer:** Replace root with 40 → sift down: 40↔80, then 40↔(no swap needed) → [80, 70, 40, 50, 60].

### Problem 4 [2024, 03 marks]
**Q:** Define B-tree. State its properties for order 5.

**Answer:** Each node: max 5 children, max 4 keys, min ⌈5/2⌉=3 children (non-root), all leaves same level.

---

*← [10 — BST and AVL](10_bst_and_avl.md) | Next: [12 — Hashing →](12_hashing.md)*

<br>

---
[⬅️ Previous](./10_bst_and_avl.md) | [🏠 Home](./README.md) | [Next ➡️](./12_hashing.md)
