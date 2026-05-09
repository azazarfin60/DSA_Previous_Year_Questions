[⬅️ Previous](./pagecontext03.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext05.md)

---

# DSA Class Notes - Page Context 04 (Pages 016-020)

## Page 016
**Date:** 26 Nov, 2025  
**Instructor:** Foysal Sir  

### Insertion Sort

**Logic:**  
The array is conceptually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

**Simulation:**
- **Input Array:** `[8, 5, 3, 4, 7]`
- **Iteration 1 (key=5):** Compare 8 and 5. Swap -> `[5, 8, 3, 4, 7]`
- **Iteration 2 (key=3):** 
  - Compare 8 and 3 -> `[5, 3, 8, 4, 7]`
  - Compare 5 and 3 -> `[3, 5, 8, 4, 7]`
- **Iteration 3 (key=4):**
  - Compare 8 and 4 -> `[3, 5, 4, 8, 7]`
  - Compare 5 and 4 -> `[3, 4, 5, 8, 7]`
- **Final Result:** `[3, 4, 5, 7, 8]`

---

## Page 017
**Insertion Sort Algorithm & Selection Sort Intro**

**Insertion Sort Algorithm (C Style):**
```c
for (i = 1; i < n; i++) {
    key = A[i];
    j = i - 1;
    
    // Move elements of A[0..i-1] that are greater than key
    // to one position ahead of their current position
    while (j >= 0 && A[j] > key) {
        A[j + 1] = A[j];
        j = j - 1;
    }
    A[j + 1] = key;
}
```

### Selection Sort

**Algorithm Steps:**
1. Divide the array into a sorted and an unsorted region.
2. Find the minimum element in the unsorted region.
3. Swap it with the first element of the unsorted region (expanding the sorted area).
4. Repeat for the remaining unsorted elements.

---

## Page 018
**Selection Sort: Simulation & Exam Tips**

**Simulation:**
- **Input Array:** `[5, 3, 2, 7]`
- **Pass 1:** Min is 2. Swap with 5. Result: `[2 | 3, 5, 7]`
- **Pass 2:** Min in `[3, 5, 7]` is 3. (Already in place). Result: `[2, 3 | 5, 7]`
- **Final Sorted Array:** `[2, 3, 5, 7]`

**Exam Tips (CT-1):**
- **Code:** Not required for this specific test.
- **Requirements:** 
  - Algorithm steps.
  - Technical analysis (Comparison of algorithms with examples).
  - Tracing/Simulation.

---

## Page 019
**Date:** 30 Nov, 2025  
**Instructor:** Foysal Sir  

### Merge Sort

**Conceptual Overview:**
- Based on **Divide and Conquer** paradigm.
- Uses **Recursion**.
- **Efficiency:**
  - **Space Complexity:** High (requires extra space for merging).
  - **Time Complexity:** Low (Very efficient).

**Merge Sort Algorithm (Pseudocode):**
```c
MergeSort(l, h) {
    if (l < h) {
        mid = (l + h) / 2;
        MergeSort(l, mid);       // Divide left half
        MergeSort(mid + 1, h);   // Divide right half
        Merge(l, mid, h);        // Conquer/Merge
    }
}
```

**Division Diagram:**
Shows an 8-element array `[5, 6, 7, 2, 4, 9, 8, 3]` being recursively split into individual units.

---

## Page 020
**Merge Sort: Detailed Simulation**

**Simulation Example:**
- **Initial Array:** `[10, 7, 9, 2, 3, 4, 8]`

**Divide Phase:**
- `[10, 7, 9, 2]` | `[3, 4, 8]`
- `([10, 7], [9, 2])` | `([3, 4], [8])`
- `(10, 7, 9, 2, 3, 4, 8)` (Individual elements)

**Conquer (Merge) Phase:**
1. Merge `(10, 7)` -> `[7, 10]`
2. Merge `(9, 2)` -> `[2, 9]`
3. Merge `[7, 10]` and `[2, 9]` -> `[2, 7, 9, 10]`
4. Merge `(3, 4)` -> `[3, 4]`
5. Merge `[3, 4]` and `[8]` -> `[3, 4, 8]`
6. Merge `[2, 7, 9, 10]` and `[3, 4, 8]` -> `[2, 3, 4, 7, 8, 9, 10]`

**Final Result:** `[2, 3, 4, 7, 8, 9, 10]`
**Note:** This topic is flagged for Class Test (CT).

<br>

---
[⬅️ Previous](./pagecontext03.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext05.md)
