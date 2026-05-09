[⬅️ Previous](./06_searching_algorithms.md) | [🏠 Home](./README.md) | [Next ➡️](./08_recursion.md)

---

# 📘 Chapter 7: Sorting Algorithms

> **Exam Frequency:** 4–8/8 years combined | **Typical Marks:** 03–06 | **Section:** A
> **Key Topics:** Bubble, Selection, Insertion, Merge, Quick Sort — traces, pseudocode, comparisons

---

## 1. What is Sorting?

**Sorting** is the process of arranging elements of a data structure in a specific order — ascending or descending — based on a key value.

### Why Sorting Matters
- Enables **binary search** (O(log n) instead of O(n))
- Makes **duplicate detection** trivial
- Enables efficient **merging** of datasets
- Required for many algorithms (greedy, divide & conquer)

### Classification

| Criterion | Types |
|---|---|
| **By approach** | Comparison-based (Bubble, Quick) vs Non-comparison (Radix, Counting) |
| **By space** | In-place (no extra array) vs Not-in-place (needs extra space) |
| **By stability** | Stable (preserves order of equal elements) vs Unstable |
| **By method** | Incremental (Insertion) vs Divide & Conquer (Merge, Quick) |

---

## 2. Bubble Sort

### Concept
Repeatedly **compare adjacent elements** and **swap** them if they are in the wrong order. After each pass, the largest unsorted element "bubbles up" to its correct position.

### Intuition
Think of bubbles in water — the largest bubble rises to the top first. Similarly, the largest element moves to the end after each pass.

### Algorithm
```c
void bubbleSort(int A[], int N) {
    int i, j, temp;
    for (i = 0; i < N - 1; i++) {           // N-1 passes
        for (j = 0; j < N - 1 - i; j++) {   // compare adjacent
            if (A[j] > A[j + 1]) {           // wrong order?
                temp = A[j];                  // swap
                A[j] = A[j + 1];
                A[j + 1] = temp;
            }
        }
    }
}
```

### Trace: Sort [5, 3, 8, 1, 2]

**Pass 1:** (compare positions 0-1, 1-2, 2-3, 3-4)
```
[5, 3, 8, 1, 2] → 5>3, swap → [3, 5, 8, 1, 2]
[3, 5, 8, 1, 2] → 5<8, no swap
[3, 5, 8, 1, 2] → 8>1, swap → [3, 5, 1, 8, 2]
[3, 5, 1, 8, 2] → 8>2, swap → [3, 5, 1, 2, 8]  ← 8 is in place
```

**Pass 2:**
```
[3, 5, 1, 2, 8] → 3<5, no swap
[3, 5, 1, 2, 8] → 5>1, swap → [3, 1, 5, 2, 8]
[3, 1, 5, 2, 8] → 5>2, swap → [3, 1, 2, 5, 8]  ← 5 is in place
```

**Pass 3:**
```
[3, 1, 2, 5, 8] → 3>1, swap → [1, 3, 2, 5, 8]
[1, 3, 2, 5, 8] → 3>2, swap → [1, 2, 3, 5, 8]  ← 3 is in place
```

**Pass 4:**
```
[1, 2, 3, 5, 8] → 1<2, no swap → already sorted!
```

> **Result: [1, 2, 3, 5, 8]** ✅

### Complexity

| Case | Time | When |
|---|---|---|
| Best | O(n) | Already sorted (with optimized flag) |
| Average | O(n²) | Random order |
| Worst | O(n²) | Reverse sorted |
| Space | O(1) | In-place |
| Stable? | **Yes** | Equal elements maintain relative order |

---

## 3. Selection Sort

### Concept
Find the **minimum** element in the unsorted portion, and **swap** it with the first unsorted element. Repeat.

### Intuition
Like selecting the shortest person from a crowd and placing them first, then the next shortest, and so on.

### Algorithm
```c
void selectionSort(int A[], int N) {
    int i, j, minIdx, temp;
    for (i = 0; i < N - 1; i++) {
        minIdx = i;                          // assume current is min
        for (j = i + 1; j < N; j++) {
            if (A[j] < A[minIdx])
                minIdx = j;                  // found smaller
        }
        // Swap A[i] and A[minIdx]
        temp = A[i];
        A[i] = A[minIdx];
        A[minIdx] = temp;
    }
}
```

### Trace: Sort [29, 10, 14, 37, 13]

| Pass | Array | Min Found | Swap |
|---|---|---|---|
| 1 | [**29**, 10, 14, 37, 13] | min=10 at idx 1 | swap(0,1) → [10, 29, 14, 37, 13] |
| 2 | [10, **29**, 14, 37, 13] | min=13 at idx 4 | swap(1,4) → [10, 13, 14, 37, 29] |
| 3 | [10, 13, **14**, 37, 29] | min=14 at idx 2 | no swap needed |
| 4 | [10, 13, 14, **37**, 29] | min=29 at idx 4 | swap(3,4) → [10, 13, 14, 29, 37] |

> **Result: [10, 13, 14, 29, 37]** ✅

### Complexity
| Case | Time |
|---|---|
| All cases | **O(n²)** — always scans for minimum |
| Space | O(1), In-place |
| Stable? | **No** |

---

## 4. Insertion Sort

### Concept
Build the sorted array one element at a time. Take each element and **insert** it into its correct position in the already-sorted portion (shifting larger elements right).

### Intuition
Like **sorting playing cards** in your hand — you pick up one card at a time and slide it into the correct position among the cards you've already sorted.

### Algorithm
```c
void insertionSort(int A[], int N) {
    int i, j, key;
    for (i = 1; i < N; i++) {          // start from 2nd element
        key = A[i];                     // element to insert
        j = i - 1;
        // Shift elements greater than key to the right
        while (j >= 0 && A[j] > key) {
            A[j + 1] = A[j];           // shift right
            j--;
        }
        A[j + 1] = key;                // insert key
    }
}
```

### Trace: Sort [5, 2, 4, 6, 1, 3]

| Pass | Key | Sorted Portion | Shifting | Result |
|---|---|---|---|---|
| i=1 | 2 | [5] | 5 > 2, shift 5 right | [**2, 5**, 4, 6, 1, 3] |
| i=2 | 4 | [2, 5] | 5 > 4, shift 5; 2 < 4, stop | [**2, 4, 5**, 6, 1, 3] |
| i=3 | 6 | [2, 4, 5] | 5 < 6, no shift | [**2, 4, 5, 6**, 1, 3] |
| i=4 | 1 | [2, 4, 5, 6] | shift all (6,5,4,2) | [**1, 2, 4, 5, 6**, 3] |
| i=5 | 3 | [1, 2, 4, 5, 6] | shift 6,5,4; 2<3, stop | [**1, 2, 3, 4, 5, 6**] |

> **Result: [1, 2, 3, 4, 5, 6]** ✅

### Complexity

| Case | Time | When |
|---|---|---|
| Best | **O(n)** | Already sorted (no shifts needed) |
| Average | O(n²) | Random order |
| Worst | O(n²) | Reverse sorted (max shifts each step) |
| Space | O(1) | In-place |
| Stable? | **Yes** |

### Why Insertion Sort is Preferred for Small/Nearly-Sorted Data
- O(n) for already sorted data — **best among simple sorts**
- Low overhead — no recursion, no extra arrays
- Stable — preserves order of equal elements
- Many real-world datasets are "nearly sorted"

---

## 5. Merge Sort

### Concept
**Divide and Conquer** approach:
1. **Divide** the array into two halves
2. **Conquer** — recursively sort each half
3. **Combine** — merge the two sorted halves into one sorted array

### Intuition
Think of sorting a deck of cards:
1. Split the deck into two halves
2. Sort each half separately
3. Merge the two sorted halves by comparing top cards and placing the smaller one first

### Algorithm

```c
void mergeSort(int A[], int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;
        mergeSort(A, left, mid);          // sort left half
        mergeSort(A, mid + 1, right);     // sort right half
        merge(A, left, mid, right);       // merge both halves
    }
}

void merge(int A[], int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;             // size of left half
    int n2 = right - mid;                 // size of right half
    int L[n1], R[n2];                     // temp arrays
    
    // Copy data to temp arrays
    for (i = 0; i < n1; i++) L[i] = A[left + i];
    for (j = 0; j < n2; j++) R[j] = A[mid + 1 + j];
    
    // Merge back
    i = 0; j = 0; k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j])
            A[k++] = L[i++];
        else
            A[k++] = R[j++];
    }
    while (i < n1) A[k++] = L[i++];      // remaining from L
    while (j < n2) A[k++] = R[j++];      // remaining from R
}
```

### Trace: Sort [38, 27, 43, 3, 9, 82, 10]

```
                    [38, 27, 43, 3, 9, 82, 10]
                   /                            \
          [38, 27, 43, 3]                [9, 82, 10]
          /              \               /          \
     [38, 27]        [43, 3]        [9, 82]        [10]
     /      \        /      \       /      \          |
   [38]    [27]    [43]    [3]    [9]     [82]      [10]
     \      /        \      /       \      /
     [27, 38]        [3, 43]        [9, 82]
          \              /               \
      [3, 27, 38, 43]              [9, 10, 82]
                   \                    /
            [3, 9, 10, 27, 38, 43, 82]
```

**Merge step example — merging [27, 38] and [3, 43]:**
```
L = [27, 38], R = [3, 43]
Compare 27 vs 3: 3 < 27 → take 3     Result: [3]
Compare 27 vs 43: 27 < 43 → take 27  Result: [3, 27]
Compare 38 vs 43: 38 < 43 → take 38  Result: [3, 27, 38]
R remaining: 43                        Result: [3, 27, 38, 43]
```

### Complexity

| Case | Time | Why |
|---|---|---|
| Best | O(n log n) | Always divides in half |
| Average | O(n log n) | Same |
| Worst | **O(n log n)** | Same — guaranteed! |
| Space | **O(n)** | Needs temp arrays for merging |
| Stable? | **Yes** |

### Recurrence Relation
```
T(n) = 2T(n/2) + O(n)
     = O(n log n)    (by Master Theorem: a=2, b=2, f(n)=n → Case 2)
```

---

## 6. Quick Sort

### Concept
**Divide and Conquer** approach:
1. Choose a **pivot** element
2. **Partition** — rearrange so all elements ≤ pivot are on the left, all elements > pivot are on the right
3. **Recursively** sort left and right sub-arrays

### Intuition
Like organizing a group by height — pick one person (pivot), everyone shorter goes left, everyone taller goes right. Repeat for each group.

### Algorithm

```c
void quickSort(int A[], int low, int high) {
    if (low < high) {
        int pi = partition(A, low, high);    // partition and get pivot index
        quickSort(A, low, pi - 1);           // sort left of pivot
        quickSort(A, pi + 1, high);          // sort right of pivot
    }
}

int partition(int A[], int low, int high) {
    int pivot = A[high];                     // choose last element as pivot
    int i = low - 1;                         // index of smaller element boundary
    int j, temp;
    
    for (j = low; j < high; j++) {
        if (A[j] <= pivot) {
            i++;                             // expand boundary
            temp = A[i]; A[i] = A[j]; A[j] = temp;  // swap
        }
    }
    // Place pivot in correct position
    temp = A[i + 1]; A[i + 1] = A[high]; A[high] = temp;
    return i + 1;                            // pivot's final position
}
```

### Detailed Trace: Sort [10, 80, 30, 90, 40, 50, 70]

**Partition 1:** pivot = 70 (last element)

```
Array: [10, 80, 30, 90, 40, 50, 70]    pivot=70, i=-1

j=0: A[0]=10 ≤ 70 → i=0, swap(0,0) → [10, 80, 30, 90, 40, 50, 70]
j=1: A[1]=80 > 70 → skip
j=2: A[2]=30 ≤ 70 → i=1, swap(1,2) → [10, 30, 80, 90, 40, 50, 70]
j=3: A[3]=90 > 70 → skip
j=4: A[4]=40 ≤ 70 → i=2, swap(2,4) → [10, 30, 40, 90, 80, 50, 70]
j=5: A[5]=50 ≤ 70 → i=3, swap(3,5) → [10, 30, 40, 50, 80, 90, 70]

Place pivot: swap(i+1=4, high=6) → [10, 30, 40, 50, 70, 90, 80]
                                              pivot at index 4 ✓
```

**Left sub-array:** [10, 30, 40, 50] — already sorted
**Right sub-array:** [90, 80] — partition with pivot=80 → [80, 90]

> **Result: [10, 30, 40, 50, 70, 80, 90]** ✅

### Complexity

| Case | Time | When |
|---|---|---|
| Best | O(n log n) | Pivot always divides evenly |
| Average | **O(n log n)** | Random data |
| Worst | **O(n²)** | Already sorted + always pick min/max as pivot |
| Space | O(log n) | Call stack depth |
| Stable? | **No** |

### Recurrence
```
Best/Average: T(n) = 2T(n/2) + O(n) = O(n log n)
Worst:        T(n) = T(n-1) + O(n) = O(n²)
```

---

## 7. Quick Sort vs Bubble Sort — "Why Quick Sort is Better"

This exact question appeared in **2017 and 2018**.

| Criterion | Quick Sort | Bubble Sort |
|---|---|---|
| **Average time** | O(n log n) | O(n²) |
| **Best time** | O(n log n) | O(n) |
| **Worst time** | O(n²) | O(n²) |
| **Approach** | Divide & Conquer | Brute force (adjacent swaps) |
| **Practical speed** | Very fast (cache-friendly partitioning) | Very slow for large data |
| **For n=10,000** | ~133,000 operations | ~100,000,000 operations |
| **In-place?** | Yes (O(log n) stack) | Yes (O(1)) |
| **Stable?** | No | Yes |

> **Conclusion:** Quick sort is better than bubble sort for virtually all practical purposes because O(n log n) is dramatically faster than O(n²) for large datasets. Bubble sort's only advantage is simplicity and stability, but these rarely matter in practice.

---

## 8. Grand Comparison of All Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable | Method |
|---|---|---|---|---|---|---|
| **Bubble** | O(n) | O(n²) | O(n²) | O(1) | ✅ | Comparison |
| **Selection** | O(n²) | O(n²) | O(n²) | O(1) | ❌ | Comparison |
| **Insertion** | O(n) | O(n²) | O(n²) | O(1) | ✅ | Comparison |
| **Merge** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | Divide & Conquer |
| **Quick** | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | Divide & Conquer |
| **Heap** | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | Comparison |
| **Radix** | O(nk) | O(nk) | O(nk) | O(n+k) | ✅ | Non-comparison |

### When to Use Which?

| Situation | Best Choice | Why |
|---|---|---|
| Small data (n < 50) | Insertion Sort | Low overhead, O(n) if nearly sorted |
| Nearly sorted data | Insertion Sort | O(n) best case |
| Guaranteed O(n log n) | Merge Sort | Never degrades to O(n²) |
| General purpose, fast | Quick Sort | Best average-case constant factors |
| Memory constrained | Heap Sort | O(1) space, O(n log n) guaranteed |
| Stability required | Merge Sort | Stable + O(n log n) |
| Integer keys, known range | Radix Sort | O(nk) can beat O(n log n) |

---

## 9. Exam-Ready Summary

### Quick Revision Points
1. **Bubble:** Adjacent swaps, largest bubbles to end. O(n²). Stable.
2. **Selection:** Find min, swap to front. O(n²) always. Unstable.
3. **Insertion:** Insert each element into sorted portion. O(n) best. Stable.
4. **Merge:** Divide → sort halves → merge. O(n log n) always. Needs O(n) space. Stable.
5. **Quick:** Partition around pivot. O(n log n) average, O(n²) worst. Unstable.
6. Quick sort vs Bubble sort — asked in 2017, 2018.
7. **Memorize the comparison table** — appears frequently.

---

## 10. Practice Problems (From Past Exams)

### Problem 1 [2017 & 2018, 03 marks]
**Q:** Why is Quick Sort better than Bubble Sort?

**Answer:** See Section 7 — comparison table + conclusion about O(n log n) vs O(n²).

### Problem 2 [2017, 06 marks]
**Q:** Trace merge sort call tree for array [10, 4, 6, 3, 8, 2, 5, 7].

**Approach:** Draw the divide tree (split into halves recursively) then merge back up showing sorted results at each level.

### Problem 3 [2024, 03 marks]
**Q:** Trace quick sort on [3, 7, 1, 8, 2, 5, 4] with last element as pivot.

**Approach:** Show partition step (pivot=4), then recursive calls on sub-arrays.

---

*← [06 — Searching Algorithms](06_searching_algorithms.md) | Next: [08 — Recursion →](08_recursion.md)*

<br>

---
[⬅️ Previous](./06_searching_algorithms.md) | [🏠 Home](./README.md) | [Next ➡️](./08_recursion.md)
