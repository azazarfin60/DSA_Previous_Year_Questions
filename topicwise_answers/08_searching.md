[⬅️ Previous](./07_sorting.md) | [🏠 Home](./README.md) | [Next ➡️](./09_hashing.md)

---

# Searching — Linear Search, Binary Search


---

## [2017] 2(c) Binary Search for item 18 in DATA. (04)

**DATA:** 10 18 23 25 30 35 45 50 60 70 (indices 1 to 10)

**Pass 1:**
- BEG = 1, END = 10
- MID = ⌊(1+10)/2⌋ = 5
- DATA[5] = 30 > 18 → search left half
- Set END = MID - 1 = 4

**Pass 2:**
- BEG = 1, END = 4
- MID = ⌊(1+4)/2⌋ = 2
- DATA[2] = 18 = 18 → **ITEM FOUND at position 2** ✓

| Pass | BEG | END | MID | DATA[MID] | Action |
|---|---|---|---|---|---|
| 1 | 1 | 10 | 5 | 30 | 30 > 18, END = 4 |
| 2 | 1 | 4 | 2 | 18 | **Found!** |

> **Result: Item 18 found at index 2 in 2 passes.**

---


---

## [2018] Q1(c) Complexity of algorithm. Time complexity of linear search. (3.5)

**Complexity of an Algorithm:** A measure of the amount of time and/or space an algorithm requires as a function of the input size n. It tells us how the algorithm's performance scales as input grows.

**Linear Search Algorithm:**
```
Procedure LINEAR_SEARCH(A, N, ITEM)
    Set I = 1
    While I <= N do
        If A[I] = ITEM Then
            Print "Found at position", I
            Return I
        End If
        Set I = I + 1
    End While
    Print "Not Found"
    Return -1
End Procedure
```

**Time Complexity:**
- **Best Case:** O(1) — element found at first position
- **Worst Case:** O(n) — element at last position or not present
- **Average Case:** O(n) — on average, checks n/2 elements

---


---

## [2019] Q.2(b) Algorithm of binary search. (04)

```
Procedure BINARY_SEARCH(A, N, ITEM)
    // A = sorted array, N = size, ITEM = element to find
    Set BEG = 1
    Set END = N
    While BEG <= END do
        Set MID = FLOOR((BEG + END) / 2)
        If A[MID] = ITEM Then
            Print "Found at position", MID
            Return MID
        Else If ITEM < A[MID] Then
            Set END = MID - 1          // search left half
        Else
            Set BEG = MID + 1          // search right half
        End If
    End While
    Print "Item not found"
    Return -1
End Procedure
```

**Time Complexity:**
- Best: O(1) — found at middle
- Worst/Average: O(log n) — halves search space each step
- **Prerequisite:** Array must be sorted

---


---

## [2019] Q.5(c) Binary search better than linear search in time complexity. (04)

| Criterion | Linear Search | Binary Search |
|---|---|---|
| Best Case | O(1) | O(1) |
| Worst Case | **O(n)** | **O(log n)** |
| Average Case | O(n) | O(log n) |
| Prerequisite | None | Array must be sorted |
| Approach | Check every element | Halve search space |

**Why Binary Search is better:**

For a sorted array of n = 1,000,000 elements:
- Linear Search: up to **1,000,000** comparisons
- Binary Search: up to **log₂(1,000,000) ≈ 20** comparisons

Binary search eliminates half the remaining elements at each step. After k comparisons, only n/2ᵏ elements remain. So it needs at most ⌈log₂ n⌉ comparisons.

**However:** Binary search requires the array to be **sorted first** (which costs O(n log n)). If searching only once in an unsorted array, linear search may be better overall. Binary search excels when the array is already sorted or when many searches are performed.

---


---

## [2020] Q.1(b) Which searching technique for 10 search queries? (04)

**Given:** Array = [1, 2, 7, 5, 1, 2, 10, 8, 11, 12] — **unsorted**.

**Analysis:**
- **Linear Search:** Works on unsorted data, O(n) per query → 10 queries = O(10n)
- **Binary Search:** Requires sorted array first. Sort cost = O(n log n), then O(log n) per query → Total = O(n log n + 10 log n)

**For 10 queries:**
- Linear: 10 × 10 = 100 comparisons (worst case)
- Binary: Sort once (~33 operations) + 10 × 4 = 73 comparisons

**Recommendation:** Since we need **at least 10 queries**, it is better to **sort the array first** using an O(n log n) algorithm and then use **Binary Search**. The one-time sorting cost is amortized over multiple queries.

> **Answer: Sort first, then use Binary Search.**

---


---

## [2020] Q.4(d) Linear vs Binary search. When each is better. (03)

**Linear Search:** Checks each element one by one from beginning to end. Works on both sorted and unsorted data. Time: O(n).

**Binary Search:** Repeatedly divides sorted array in half, eliminating half the elements each step. Requires sorted data. Time: O(log n).

**When each is better:**
- **Linear** is better for: unsorted data, small arrays (n < 20), single search on unsorted data
- **Binary** is better for: sorted data, large arrays, repeated search queries

---


---

## [2020] Q.8(a) Best, worst, average of linear and binary search. (05)

| Case | Linear Search | Binary Search |
|---|---|---|
| **Best** | O(1) — element at first position | O(1) — element at middle |
| **Worst** | O(n) — element at last or absent | O(log n) — element at deepest level |
| **Average** | O(n) — checks n/2 on average | O(log n) — halves each step |

**Linear Search:** Scans sequentially. For n=1024: worst = 1024 comparisons.

**Binary Search:** Divides sorted array in half. For n=1024: worst = log₂(1024) = 10 comparisons.

Binary search is **exponentially faster** but requires sorted data.

---


---

## [2021] Q.1(b) Binary search recursive pseudocode + time complexity. (05)

```
Procedure BINARY_SEARCH(A, BEG, END, ITEM)
    If BEG > END Then
        Print "Item not found"
        Return -1
    End If
    Set MID = FLOOR((BEG + END) / 2)
    If A[MID] = ITEM Then
        Return MID                              // found
    Else If ITEM < A[MID] Then
        Return BINARY_SEARCH(A, BEG, MID-1, ITEM)  // left half
    Else
        Return BINARY_SEARCH(A, MID+1, END, ITEM)  // right half
    End If
End Procedure
```

**Time Complexity Analysis:**
- Each call halves the search space: T(n) = T(n/2) + O(1)
- **Best Case: O(1)** — element found at middle on first check
- **Worst Case: O(log n)** — element at deepest level or absent. After k calls, n/2^k = 1 → k = log₂n
- **Average Case: O(log n)** — on average, searches log₂n levels

**Space Complexity:** O(log n) due to recursion stack.

---


---

## [2022] Q.3(a) Complete Binary Search recursive code. (CO3, 03)

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


---

## [2023] Q.1(b) Complete BinarySearch recursive function + time complexity. (CLO3, 06)

```
Procedure BinarySearch(A, l, h, x)
    If l > h Then
        Return -1                              // not found
    End If
    Set mid = FLOOR((l + h) / 2)
    If A[mid] = x Then
        Return mid                             // found at mid
    Else If x < A[mid] Then
        Return BinarySearch(A, l, mid - 1, x)  // search left
    Else
        Return BinarySearch(A, mid + 1, h, x)  // search right
    End If
End Procedure
```

**Time Complexity:**
- Each call halves the problem: T(n) = T(n/2) + O(1)
- By Master Theorem: a=1, b=2, f(n)=O(1), n^(log₂1) = n⁰ = 1 = f(n) → Case 2
- **T(n) = O(log n)**
- Best: O(1), Worst: O(log n), Average: O(log n)
- Space: O(log n) for recursion stack

---


---

## [2023] Q.7(a) Why binary search not applicable for sorted linked list? (CLO1, 02)

Binary search requires **O(1) random access** to the middle element. Linked lists only support **sequential access** — finding the middle requires traversing n/2 nodes (O(n)). This makes each "halving" step O(n) instead of O(1), giving total O(n log n) — worse than simple linear search O(n).

---


---

## [2024] Q.1(b) Time complexity of linear search. (CO1, 03)

**Time Complexity:** A measure of how the running time of an algorithm grows as the input size n increases. Expressed using asymptotic notation (Big-O).

**Linear Search:** Scans each element one by one until the target is found or the array ends.

```
Procedure LINEAR_SEARCH(A, N, ITEM)
    For I = 1 to N do
        If A[I] = ITEM Then
            Return I
        End If
    End For
    Return -1
End Procedure
```

- **Best Case: O(1)** — element found at first position
- **Worst Case: O(n)** — element at last position or absent
- **Average Case: O(n)** — on average checks n/2 elements

---


---

## 📊 Exam Priority
**Priority: 1/5** (Must Prepare)
**Appeared in:** 6/8 years
**Typical marks:** 03–06 per question

<br>

---
[⬅️ Previous](./07_sorting.md) | [🏠 Home](./README.md) | [Next ➡️](./09_hashing.md)
