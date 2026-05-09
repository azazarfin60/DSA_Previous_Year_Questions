[⬅️ Previous](./06_heap.md) | [🏠 Home](./README.md) | [Next ➡️](./08_searching.md)

---

# Sorting Algorithms — Quick, Merge, Bubble, Insertion, Radix


---

## [2017] 1(c) "Quick sort is better than bubble sort." Explain. (04)

**Bubble Sort:**
- Compares adjacent elements and swaps if out of order
- Time: Best O(n), Worst O(n²), Average O(n²)
- Very slow for large datasets

**Quick Sort:**
- Uses divide-and-conquer with a pivot element
- Time: Best O(n log n), Worst O(n²), Average O(n log n)
- Much faster in practice

| Criterion | Quick Sort | Bubble Sort |
|---|---|---|
| Avg Time | O(n log n) | O(n²) |
| Approach | Divide & Conquer | Brute force comparison |
| Swaps | Fewer (distant swaps) | Many (adjacent only) |
| In-place | Yes | Yes |
| Practical speed | Very fast | Very slow |

**Example:** For array [5, 3, 8, 1, 9]:
- Bubble Sort needs ~10 comparisons and many swaps
- Quick Sort with pivot=5: partition into [3,1] [5] [8,9], then recurse — far fewer operations

Quick sort is better because its average case O(n log n) is significantly faster than bubble sort's O(n²). For n=1000, quick sort does ~10,000 operations vs bubble sort's ~1,000,000.

---


---

## [2017] 5(b) When is insertion sort more efficient? (02)

Insertion sort is more efficient than other algorithms in these cases:

1. **Nearly sorted data** — When the array is almost sorted, insertion sort runs in **O(n)** time because very few shifts are needed.
2. **Small input size** — For small arrays (n < 20), insertion sort outperforms quick sort and merge sort due to low overhead (no recursion, no extra space).
3. **Online sorting** — When data arrives one element at a time, insertion sort can sort incrementally.

---


---

## [2017] 5(c) MergeSort call tree for D: 50, 100, 30, 10, 200, 150 (06)

**MergeSort Partition Tree (splitting):**

```
              [50,100,30,10,200,150]
              /                    \
      [50,100,30]              [10,200,150]
       /       \                /         \
   [50,100]   [30]        [10,200]      [150]
    /    \                  /    \
  [50]  [100]            [10]  [200]
```

**Merge Tree (combining back):**

```
  [50] [100]            [10] [200]
    \   /                 \   /
  [50,100]  [30]       [10,200]  [150]
      \     /              \      /
   [30,50,100]          [10,150,200]
         \                   /
      [10,30,50,100,150,200]
```

**Final sorted array: [10, 30, 50, 100, 150, 200]**

**Time Complexity:** O(n log n) for all cases.
- Splitting: log₂(6) ≈ 3 levels
- Each level does O(n) merge work
- Total: O(n log n)

---


---

## [2018] Q2(b) "Quick sort is better than bubble sort." Explain. (04)

| Criterion | Quick Sort | Bubble Sort |
|---|---|---|
| Average Time | O(n log n) | O(n²) |
| Approach | Divide & Conquer | Adjacent comparison |
| Swaps | Fewer (distant) | Many (adjacent only) |
| Practical Speed | Very fast | Very slow |
| In-place | Yes | Yes |

**Example:** Sorting [5, 1, 4, 2, 8]:
- Bubble sort: ~10 comparisons, ~4 swaps per pass, multiple passes
- Quick sort: pivot=5, partition [1,4,2] [5] [8], recurse — far fewer operations

For n=1000: Quick sort ≈ 10,000 ops vs Bubble sort ≈ 1,000,000 ops.

Quick sort is better because its **average O(n log n)** significantly outperforms bubble sort's **O(n²)** for all practical input sizes.

---


---

## [2019] Q.1(b) Merge Sort on Budget[] = {30, 20, 100, 50, 10, 15}. (06)

**Step-by-step splitting (divide):**

```
Level 0: [30, 20, 100, 50, 10, 15]
Level 1: [30, 20, 100]        [50, 10, 15]
Level 2: [30, 20]  [100]      [50, 10]  [15]
Level 3: [30] [20]            [50] [10]
```

**Merging (conquer) — bottom up:**

**Merge [30] and [20]:** Compare 30 vs 20 → [20, 30]
**Merge [20, 30] and [100]:** Compare 20<100, 30<100 → [20, 30, 100]

**Merge [50] and [10]:** Compare 50 vs 10 → [10, 50]
**Merge [10, 50] and [15]:** Compare 10<15, then 15<50 → [10, 15, 50]

**Final Merge [20, 30, 100] and [10, 15, 50]:**

| Compare | Left | Right | Result so far |
|---|---|---|---|
| 20 vs 10 | 20 | **10** | [10] |
| 20 vs 15 | 20 | **15** | [10, 15] |
| **20** vs 50 | 20 | 50 | [10, 15, 20] |
| **30** vs 50 | 30 | 50 | [10, 15, 20, 30] |
| **100** vs 50 | 100 | **50** | [10, 15, 20, 30, 50] |
| Copy 100 | | | [10, 15, 20, 30, 50, 100] |

> **Sorted: [10, 15, 20, 30, 50, 100]**

**Time Complexity:**
- n = 6, levels = ⌈log₂(6)⌉ = 3
- Each level does O(n) merge work
- **Total: O(n log n)** for all cases (best, worst, average)
- Space: O(n) for temporary merge arrays

---


---

## [2019] Q.3(a) Bubble sort: Find comparisons and interchanges for PEOPLE. (04)

**Array:** P, E, O, P, L, E → indices 1 to 6

**Pass 1:** (compare adjacent, swap if needed)
- P vs E → swap → **E**, **P**, O, P, L, E (interchange 1)
- P vs O → swap → E, **O**, **P**, P, L, E (interchange 2)
- P vs P → no swap
- P vs L → swap → E, O, P, **L**, **P**, E (interchange 3)
- P vs E → swap → E, O, P, L, **E**, **P** (interchange 4)
After Pass 1: E, O, P, L, E, **P** | Comparisons: 5, Swaps: 4

**Pass 2:**
- E vs O → no swap
- O vs P → no swap
- P vs L → swap → E, O, **L**, **P**, E, P (interchange 5)
- P vs E → swap → E, O, L, **E**, **P**, P (interchange 6)
After Pass 2: E, O, L, E, **P**, P | Comparisons: 4, Swaps: 2

**Pass 3:**
- E vs O → no swap
- O vs L → swap → E, **L**, **O**, E, P, P (interchange 7)
- O vs E → swap → E, L, **E**, **O**, P, P (interchange 8)
After Pass 3: E, L, E, **O**, P, P | Comparisons: 3, Swaps: 2

**Pass 4:**
- E vs L → no swap
- L vs E → swap → E, **E**, **L**, O, P, P (interchange 9)
After Pass 4: E, E, **L**, O, P, P | Comparisons: 2, Swaps: 1

**Pass 5:**
- E vs E → no swap
After Pass 5: **E, E, L, O, P, P** ✓ | Comparisons: 1, Swaps: 0

> **Total Comparisons = 5+4+3+2+1 = 15**
> **Total Interchanges = 4+2+2+1+0 = 9**

---


---

## [2020] Q.1(c) Bubble sort pseudocode with example. (05)

```
Procedure BUBBLE_SORT(A, N)
    For I = 1 to N-1 do
        For J = 1 to N-I do
            If A[J] > A[J+1] Then
                Swap A[J] and A[J+1]
            End If
        End For
    End For
End Procedure
```

**Example:** A = [5, 3, 8, 1]

**Pass 1:** Compare adjacent pairs:
- 5>3 → swap → [3, 5, 8, 1]
- 5<8 → no swap
- 8>1 → swap → [3, 5, 1, **8**]

**Pass 2:**
- 3<5 → no swap
- 5>1 → swap → [3, 1, **5**, 8]

**Pass 3:**
- 3>1 → swap → [**1**, **3**, 5, 8] ✓

> **Sorted: [1, 3, 5, 8]**
> **Time: O(n²) worst/avg, O(n) best (with optimization)**

---


---

## [2020] Q.5(b) Insertion sort pseudocode + time complexity. (04)

```
Procedure INSERTION_SORT(A, N)
    For I = 2 to N do
        Set KEY = A[I]
        Set J = I - 1
        While J >= 1 AND A[J] > KEY do
            Set A[J+1] = A[J]        // shift right
            Set J = J - 1
        End While
        Set A[J+1] = KEY              // place KEY
    End For
End Procedure
```

**Best Case (sorted):** Inner while never executes → **O(n)**
**Worst Case (reverse sorted):** Inner while shifts all → 1+2+...+(n-1) = **O(n²)**
**Average Case:** **O(n²)**

---


---

## [2021] Q.7(c) Merge sort pseudocode + time complexity. (04)

```
Procedure MERGE_SORT(A, LOW, HIGH)
    If LOW < HIGH Then
        Set MID = FLOOR((LOW + HIGH) / 2)
        Call MERGE_SORT(A, LOW, MID)         // sort left half
        Call MERGE_SORT(A, MID+1, HIGH)      // sort right half
        Call MERGE(A, LOW, MID, HIGH)        // merge two halves
    End If
End Procedure

Procedure MERGE(A, LOW, MID, HIGH)
    Create temporary arrays L and R
    Copy A[LOW..MID] into L, A[MID+1..HIGH] into R
    Set I = 1, J = 1, K = LOW
    While I <= size(L) AND J <= size(R) do
        If L[I] <= R[J] Then
            Set A[K] = L[I], I = I + 1
        Else
            Set A[K] = R[J], J = J + 1
        End If
        Set K = K + 1
    End While
    Copy remaining elements of L or R into A
End Procedure
```

**Time Complexity:**
- T(n) = 2T(n/2) + O(n)
- By Master Theorem: a=2, b=2, f(n)=n, n^(log₂2) = n = f(n) → Case 2
- **Best Case: O(n log n)**
- **Worst Case: O(n log n)**
- Space: O(n) for temporary arrays

---


---

## [2022] Q.3(b) Quicksort time complexity when all elements are same. (CO2, 03)

When all elements have the **same value**, quicksort's pivot selection results in the **worst possible partitioning**.

**Analysis:**
- Pivot = any element (all are equal)
- Partition: one side has n-1 elements, other side has 0
- Recurrence: T(n) = T(n-1) + T(0) + O(n) = T(n-1) + O(n)
- Expanding: T(n) = O(n) + O(n-1) + ... + O(1) = O(n²)

> **Time Complexity: O(n²)** — worst case, same as reverse-sorted input.

This can be avoided using **3-way partitioning** (Dutch National Flag), which handles duplicates in O(n).

---


---

## 📊 Exam Priority
**Priority: 1/5** (Must Prepare)
**Appeared in:** 7/8 years (at least one sorting topic)
**Typical marks:** 03–06 per question

<br>

---
[⬅️ Previous](./06_heap.md) | [🏠 Home](./README.md) | [Next ➡️](./08_searching.md)
