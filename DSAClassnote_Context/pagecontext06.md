[⬅️ Previous](./pagecontext05.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext07.md)

---

# DSA Class Notes - Page Context 06 (Pages 026-030)

## Page 026
**Optimized Bubble Sort Implementation**

**Algorithm (C Style):**
```c
Bubblesort(A, n) {
    for (i = 0; i < n - 1; i++) {
        swapped = false;
        for (j = 0; j < n - i - 1; j++) {
            if (A[j] > A[j + 1]) {
                // Swap logic
                temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
                swapped = true;
            }
        }
        // Optimization: If no two elements were swapped by inner loop, then break
        if (swapped == false) 
            break;
    }
}
```

**Advantages:**
1. Easy to understand and implement.
2. Does not require additional memory (In-place).
3. **Stable:** Preserves the relative order of equal elements.

**Disadvantages:**
1. Slow for large datasets ($O(N^2)$).

---

## Page 027
**Insertion Sort: Conceptual Steps**

**Logic:**
Iteratively inserting each element of an unsorted array into its correct position in a sorted portion of the same array.

**Steps:**
1. Divide the array into sorted and unsorted parts.
2. Assume the first element is already sorted.
3. Take the first element of the unsorted part as the **key**.
4. Compare the key with elements in the sorted part (from right to left).
5. If the key is smaller, shift the sorted elements to the right.
6. Insert the key at its correct position.
7. Repeat until the entire array is sorted.

---

## Page 028
**Insertion Sort: Complexity and Simulation**

**Time Complexity:**
- **Best Case:** $O(N)$ (When array is already sorted).
- **Average Case:** $O(N^2)$
- **Worst Case:** $O(N^2)$

**Simulation Tracing:**
- **Input:** `[12, 11, 13, 5, 6]`
- **Iteration 1 (key=11):** `[11, 12 | 13, 5, 6]`
- **Iteration 2 (key=13):** `[11, 12, 13 | 5, 6]` (No shift needed).
- **Iteration 3 (key=5):** `[5, 11, 12, 13 | 6]`
- **Iteration 4 (key=6):** `[5, 6, 11, 12, 13]`

---

## Page 029
**Insertion Sort: Characteristics and Implementation**

**Advantages:**
1. Simple to implement.
2. Stable.
3. Efficient for small datasets and "nearly sorted" lists.
4. **Space-efficient:** Requires $O(1)$ additional space.
5. **Adaptive:** Faster if the list is already partially sorted.

**Disadvantages:**
1. Inefficient for large datasets.

**C Code Snippet:**
```c
for (i = 1; i < n; i++) {
    key = A[i];
    j = i - 1;
    while (j >= 0 && A[j] > key) {
        A[j + 1] = A[j];
        j--;
    }
    A[j + 1] = key;
}
```

---

## Page 030
**Selection Sort: Detailed Process and Simulation**

**Core Steps:**
1. Divide array into sorted and unsorted regions.
2. Initially, the whole array is unsorted.
3. Find the minimum element from the unsorted part.
4. Swap it with the first element of the unsorted part.
5. Expand the sorted region and shrink the unsorted region.
6. Repeat.

**Simulation Tracing:**
- **Input:** `[64, 25, 12, 22, 11]`
- **Iteration 1:** Smallest is 11. Swap with 64.  
  Result: `[11 | 25, 12, 22, 64]`
- **Iteration 2:** Smallest in `[25, 12, 22, 64]` is 12. Swap with 25.  
  Result: `[11, 12 | 25, 22, 64]`
- **Iteration 3:** Smallest in `[25, 22, 64]` is 22. Swap with 25.  
  Result: `[11, 12, 22 | 25, 64]`
- **Final Result:** `[11, 12, 22, 25, 64]`

<br>

---
[⬅️ Previous](./pagecontext05.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext07.md)
