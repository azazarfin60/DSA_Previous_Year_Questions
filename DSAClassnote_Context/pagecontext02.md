[⬅️ Previous](./pagecontext01.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext03.md)

---

# DSA Class Notes - Page Context 02 (Pages 006-010)



## Page 007
**Date:** 19 Nov, 2025  
**Instructor:** Foysal Sir  
**Course:** DSA (ECE-2103)

### Multi-Dimensional Array Memory Calculation

**Array Representations:**
- **1D Array (`a[i]`):** Linear sequential memory boxes.
- **2D Array (`a[i][j]`):** Matrix representation (Rows x Columns).

**Memory Storage Methods:**
1. **Row Major Order**
2. **Column Major Order**

**Example Problem:**
- **Matrix:** 10x12 ($m=10, n=12$)
- **Base Address (B):** 200
- **Storage Size (w):** 2 bits (Wait, classnote mentions 'size is 2 bit', usually 2 bytes/words, but we follow the note).
- **Target Element:** A(6, 7) ($i=6, j=7$)
- **Bounds:** $LBR=0, LBC=0$ (default)

**1. Row Major Order Formula:**
$$Address(A[i,j]) = B + w \times \{ n(i - LBR) + (j - LBC) \}$$
Calculation: $200 + 2 \times \{ 12(6-0) + (7-0) \} = 200 + 2 \times (72 + 7) = 200 + 158 = \mathbf{358}$

**2. Column Major Order Formula:**
$$Address(A[i,j]) = B + w \times \{ m(j - LBC) + (i - LBR) \}$$
Calculation: $200 + 2 \times \{ 10(7-0) + (6-0) \} = 200 + 2 \times (70 + 6) = 200 + 152 = \mathbf{352}$

---

## Page 008
**Sparse Matrix**

**Definition:** A matrix where most of the elements are zero.

**Representations:**
1. **Array (Triplet Representation / Coordinate List):** Only non-zero elements are stored as `(Row, Column, Value)`.
2. **Linked List.**

**Example & Memory Analysis:**
- A matrix with most values = 0.
- **Coordinate List Table:**
| Row | Col | Val |
| :--- | :--- | :--- |
| 2 | 2 | 5 |
| 2 | 4 | 2 |
| 4 | 2 | 3 |
| ... | ... | ... |

**Memory Savings Calculation:**
- Original Matrix (e.g., 7x4): $7 \times 4 \times 2 = 56$ Bytes.
- Triplet storage: $(3 \text{ rows stored}) \times (4 \text{ items}) \times 2 = 24$ Bytes (Note: Note says 3x4, likely referring to the metadata or specific non-zero count).
- **Improvement:** $\frac{56 - 24}{56} \times 100 = \mathbf{57.14\%}$

---

## Page 009
**Date:** 23 Nov, 2025  
**Instructor:** Foysal Sir  

### Linear Search

**Definition:**  
Linear searching is an operation where a value of an element can be found by checking all the elements from a given array.

**Time Complexity:** $O(N)$

**Algorithm (C Syntax):**
```c
int num[n] = { ... };
int val, position = -1;

// Searching loop
for (int i = 0; i < n; i++) {
    if (val == num[i]) {
        position = i + 1; // 1-based position
        break;
    }
}

if (position == -1) 
    printf("Not found");
else 
    printf("Found at position %d", position);
```

---

## Page 010
**Linear Search: Simulation and Analysis**

**Tracing Example:**
- **Array:** `[10, 20, 30, 40]`
- **Target (val):** 30
- **Trace:**
  - **Loop 1 (i=0):** `10 == 30`? No. `pos = -1`.
  - **Loop 2 (i=1):** `20 == 30`? No.
  - **Loop 3 (i=2):** `30 == 30`? **Yes**. `pos = 3`. Break.

**Complexity Analysis:**
- **Best Case:** $O(1)$ (Element is at the first position).
- **Average Case:** $O(N)$
- **Worst Case:** $O(N)$ (Element is at the last position or not present).

**Why Linear Search is "Worst":**
1. It has **$O(N)$ time complexity** in the worst case.
2. It must visit every single element for a search in an unsorted array.
3. **Inefficiency:** For a size 100 array, linear search might take 100 operations, whereas Binary Search would only take approx 7 ($\log_2 100$).
4. It makes **no assumptions** about data sorting, checking every element one by one and wasting processing power.

<br>

---
[⬅️ Previous](./pagecontext01.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext03.md)
