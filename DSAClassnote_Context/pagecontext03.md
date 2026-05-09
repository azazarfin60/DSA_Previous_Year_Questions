[⬅️ Previous](./pagecontext02.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext04.md)

---

# DSA Class Notes - Page Context 03 (Pages 011-015)

## Page 011
**Binary Search**

**Concept:** Similar to linear search, but the search space is halved in each step ("divided by 2").

**Recursive Algorithm (C Style):**
```c
int bin_s(int arr[], int x, int start, int end) {
    int mid = (start + end) / 2;
    
    // Case 1: Element found at mid
    if (arr[mid] == x) 
        return mid;
        
    // Case 2: Element not in array (base case)
    if (start == end) 
        return -1;
        
    // Case 3: Target is in the left half
    if (arr[mid] > x) 
        return bin_s(arr, x, start, mid - 1);
        
    // Case 4: Target is in the right half
    if (arr[mid] < x) 
        return bin_s(arr, x, mid + 1, end);
}
```

**Complexity:** $O(\log N)$

---

## Page 012
**Date:** 24 Nov, 2025  
**Instructor:** Foysal Sir  
**Course:** DSA (ECE-2103)

### Sorting Methods
1. Bubble Sort
2. Insertion Sort
3. Selection Sort
4. Quick Sort
5. Merge Sort
6. Heap Sort

**Exam Note:** Lab final will likely require Example, Simulation Steps, Algorithm, and Code.

**Bubble Sort Simulation (Ascending):**
- **Unsorted Array:** `[20, 10, 5, 11, 17]`
- **Pass 1:**
  1. `(20, 10)` -> Swap -> `[10, 20, 5, 11, 17]`
  2. `(20, 5)` -> Swap -> `[10, 5, 20, 11, 17]`
  3. `(20, 11)` -> Swap -> `[10, 5, 11, 20, 17]`
  4. `(20, 17)` -> Swap -> `[10, 5, 11, 17, 20]`
  - Result after Pass 1: `[10, 5, 11, 17, 20]`

---

## Page 013
**Bubble Sort: Continuation and Implementation**

**Pass 2 Simulation:**
1. `(10, 5)` -> Swap -> `[5, 10, 11, 17, 20]`
2. Subsequent comparisons in this pass do not result in swaps as the array is already sorted.
- **Final Sorted Array:** `[5, 10, 11, 17, 20]`

**Algorithm Code (C):**
```c
for (i = 0; i < n; i++) {
    for (j = 0; j < n - i - 1; j++) {
        if (a[j] > a[j + 1]) {
            // Swap logic
            temp = a[j];
            a[j] = a[j + 1];
            a[j + 1] = temp;
        }
    }
}
```

**Time Complexity:**
- **Best Case:** $O(N)$ (if array is already sorted and optimized)
- **Worst Case:** $O(N^2)$
- **Average Case:** $O(N^2)$

---

## Page 014
**Large Scale Simulation of Sorting**

**Input Array:** `[15, 12, 11, 25, 35, 17, 4, 10, 3, 30, 10, 14, 7, 8, 36]`

**Pass 1 Tracing (Partial):**
- `(15, 12)` -> `12, 15`
- `(15, 11)` -> `11, 15`
- `(15, 25)` -> No swap
- `(25, 35)` -> No swap
- `(35, 17)` -> `17, 35`
- `(35, 4)` -> `4, 35`
- `(35, 10)` -> `10, 35`
- ... (Multiple swaps leading to 36 being at the end)

**Pass 2 Tracing (Partial):**
- Swapping smaller elements towards the front (e.g., 3, 4 moving left).

---

## Page 015
**Sorting Simulation (Continued)**

**Detailed Tracing of later passes:**
- **Pass 2, 3, 4, 5, 6:** Shows the step-by-step movement of elements.
- The trace shows the bubbling up of larger values and the "sinking" of smaller values to their correct positions.
- **Final Result:** Shows the fully sorted array.
- Tracing confirms that with each pass, the next largest element is placed in its final correct position at the end of the array.

<br>

---
[⬅️ Previous](./pagecontext02.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext04.md)
