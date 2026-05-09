[⬅️ Previous](./05_queues.md) | [🏠 Home](./README.md) | [Next ➡️](./07_sorting_algorithms.md)

---

# 📘 Chapter 6: Searching Algorithms

> **Exam Frequency:** 6/8 years (Binary Search) | **Typical Marks:** 03–06 | **Section:** A
> **Key Topics:** Linear Search, Binary Search (iterative & recursive), Complexity proof

---

## 1. What is Searching?

**Searching** is the process of finding the **location** (index or address) of a specific element (called the **key** or **ITEM**) within a data structure.

### Two Fundamental Approaches

| Algorithm | Requirement | Time | Idea |
|---|---|---|---|
| **Linear Search** | None (works on unsorted data) | O(n) | Check every element one by one |
| **Binary Search** | Data MUST be sorted | O(log n) | Divide the search space in half each step |

---

## 2. Linear Search (Sequential Search)

### 2.1 Concept

Start from the first element and compare each element with the key, one by one, until either:
- The key is **found** → return its position
- The end of the array is reached → key is **not found**

### Intuition
Looking for a specific book on an **unsorted bookshelf** — you must check every single book from left to right until you find it. In the worst case, the book is at the very end (or not there at all).

### 2.2 Algorithm

**C++ Style:**
```cpp
int linearSearch(int A[], int N, int ITEM) {
    for (int I = 0; I < N; I++) {
        if (A[I] == ITEM) {
            return I;                // found at index I
        }
    }
    return -1;                       // not found
}
```

**OR, Textbook Style:**
```
Procedure LINEAR_SEARCH(A, N, ITEM)
    Set LOC = -1                     // not found initially
    For I = 0 to N-1 do
        If A[I] = ITEM Then
            Set LOC = I              // found at index I
            Return LOC
        End If
    End For
    Return LOC                       // -1 means not found
End Procedure
```

### 2.3 C Code
```c
int linearSearch(int A[], int N, int item) {
    int i;
    for (i = 0; i < N; i++) {
        if (A[i] == item)
            return i;                // found at index i
    }
    return -1;                       // not found
}
```

### 2.4 Trace Example

Search for ITEM = 30 in A = [10, 40, 30, 20, 50]

| Step | i | A[i] | Comparison | Result |
|---|---|---|---|---|
| 1 | 0 | 10 | 10 = 30? | No |
| 2 | 1 | 40 | 40 = 30? | No |
| 3 | 2 | 30 | 30 = 30? | **Yes! Found at index 2** |

**Comparisons made: 3**

### 2.5 Complexity Analysis

| Case | When | Comparisons | Time |
|---|---|---|---|
| **Best case** | Key is the first element | 1 | **O(1)** |
| **Worst case** | Key is the last element or not present | n | **O(n)** |
| **Average case** | Key is in the middle (on average) | n/2 | **O(n)** |

**Space Complexity:** O(1) — no extra space needed.

---

## 3. Proof: Linear Search is One of the Worst Search Algorithms

This topic was **specifically highlighted** in the topic list as important.

### Argument

**Claim:** Linear search has O(n) time complexity, making it one of the least efficient search algorithms for large datasets.

**Proof:**

1. **Worst case analysis:** In linear search, we compare the key with each element sequentially. If the key is at the last position or is absent, we must check ALL `n` elements.
   - Number of comparisons = n
   - Therefore, **T(n) = O(n)**

2. **Comparison with better algorithms:**

   | Algorithm | Time | On 1,000,000 elements |
   |---|---|---|
   | Linear Search | O(n) | 1,000,000 comparisons |
   | Binary Search | O(log n) | ~20 comparisons |
   | Hash Table | O(1) average | ~1 comparison |

3. **Why is it "worst"?**
   - It does NOT exploit any structure in the data (sortedness, distribution)
   - It treats every position as equally likely
   - No information is gained from any comparison — each eliminates only 1 element
   - Binary search eliminates **half the remaining elements** per comparison

4. **When linear search IS acceptable:**
   - Data is **unsorted** and cannot be sorted (or sorting is too expensive)
   - Data is **very small** (n < 20, overhead of binary search not worth it)
   - Searching only **once** (sorting takes O(n log n), which is worse than O(n) for one search)

> **Conclusion:** Linear search is O(n) in worst and average case. For any sorted data or when multiple searches are performed, algorithms like binary search (O(log n)) or hash-based search (O(1)) are far superior.

---

## 4. Binary Search

### 4.1 Concept

**Prerequisite:** The array MUST be **sorted**.

**Idea:** Compare the key with the **middle element**:
- If key = middle → **found!**
- If key < middle → search the **left half**
- If key > middle → search the **right half**

Each comparison **eliminates half** of the remaining elements.

### Intuition
Think of guessing a number between 1 and 100:
- "Is it 50?" → "Too high" → now you know it's 1–49
- "Is it 25?" → "Too low" → now it's 26–49
- "Is it 37?" → "Correct!"

You **halve the search space** each time. For 100 numbers, you need at most log₂(100) ≈ 7 guesses!

---

### 4.2 Iterative Algorithm

**C++ Style:**
```cpp
int binarySearch(int A[], int N, int ITEM) {
    int LOW = 0;
    int HIGH = N - 1;
    
    while (LOW <= HIGH) {
        int MID = LOW + (HIGH - LOW) / 2; // prevents overflow
        
        if (A[MID] == ITEM) {
            return MID;                   // found at MID
        } else if (ITEM < A[MID]) {
            HIGH = MID - 1;               // search left half
        } else {
            LOW = MID + 1;                // search right half
        }
    }
    
    return -1;                            // not found
}
```

**OR, Textbook Style:**
```
Procedure BINARY_SEARCH(A, N, ITEM)
    Set LOW = 0
    Set HIGH = N - 1
    
    While LOW ≤ HIGH do
        Set MID = (LOW + HIGH) / 2       // integer division
        
        If A[MID] = ITEM Then
            Return MID                    // found at MID
        Else If ITEM < A[MID] Then
            Set HIGH = MID - 1            // search left half
        Else
            Set LOW = MID + 1             // search right half
        End If
    End While
    
    Return -1                             // not found
End Procedure
```

### 4.3 Iterative C Code
```c
int binarySearch(int A[], int N, int item) {
    int low = 0, high = N - 1, mid;
    
    while (low <= high) {
        mid = (low + high) / 2;
        if (A[mid] == item)
            return mid;              // found
        else if (item < A[mid])
            high = mid - 1;          // search left
        else
            low = mid + 1;           // search right
    }
    return -1;                       // not found
}
```

---

### 4.4 Recursive Algorithm

**C++ Style:**
```cpp
int binarySearchRec(int A[], int LOW, int HIGH, int ITEM) {
    if (LOW > HIGH) {
        return -1;                        // base case: not found
    }
    
    int MID = LOW + (HIGH - LOW) / 2;
    
    if (A[MID] == ITEM) {
        return MID;                       // found
    } else if (ITEM < A[MID]) {
        return binarySearchRec(A, LOW, MID - 1, ITEM);   // left half
    } else {
        return binarySearchRec(A, MID + 1, HIGH, ITEM);  // right half
    }
}
```

**OR, Textbook Style:**
```
Procedure BINARY_SEARCH_REC(A, LOW, HIGH, ITEM)
    If LOW > HIGH Then
        Return -1                         // base case: not found
    End If
    
    Set MID = (LOW + HIGH) / 2
    
    If A[MID] = ITEM Then
        Return MID                        // found
    Else If ITEM < A[MID] Then
        Return BINARY_SEARCH_REC(A, LOW, MID - 1, ITEM)    // left half
    Else
        Return BINARY_SEARCH_REC(A, MID + 1, HIGH, ITEM)   // right half
    End If
End Procedure
```

### 4.5 Recursive C Code
```c
int binarySearchRec(int A[], int low, int high, int item) {
    if (low > high)
        return -1;                   // not found
    
    int mid = (low + high) / 2;
    
    if (A[mid] == item)
        return mid;                  // found
    else if (item < A[mid])
        return binarySearchRec(A, low, mid - 1, item);     // left
    else
        return binarySearchRec(A, mid + 1, high, item);    // right
}

// Call: binarySearchRec(A, 0, N-1, item)
```

---

### 4.6 Detailed Trace Example

**Array:** A = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]  (N=10)
**Search for:** ITEM = 35

| Iteration | LOW | HIGH | MID | A[MID] | Comparison | Action |
|---|---|---|---|---|---|---|
| 1 | 0 | 9 | 4 | 25 | 35 > 25 | LOW = 5 |
| 2 | 5 | 9 | 7 | 40 | 35 < 40 | HIGH = 6 |
| 3 | 5 | 6 | 5 | 30 | 35 > 30 | LOW = 6 |
| 4 | 6 | 6 | 6 | 35 | 35 = 35 | **FOUND at index 6** ✅ |

**Comparisons made: 4** (vs. linear search would need 7 comparisons)

### Trace for Item NOT Present

**Search for:** ITEM = 22 in same array

| Iteration | LOW | HIGH | MID | A[MID] | Comparison | Action |
|---|---|---|---|---|---|---|
| 1 | 0 | 9 | 4 | 25 | 22 < 25 | HIGH = 3 |
| 2 | 0 | 3 | 1 | 10 | 22 > 10 | LOW = 2 |
| 3 | 2 | 3 | 2 | 15 | 22 > 15 | LOW = 3 |
| 4 | 3 | 3 | 3 | 20 | 22 > 20 | LOW = 4 |
| 5 | 4 | 3 | — | — | LOW > HIGH | **NOT FOUND** ❌ |

---

### 4.7 Complexity Analysis

**At each step**, binary search eliminates half the elements:
```
n → n/2 → n/4 → n/8 → ... → 1
```

The number of steps is how many times we can halve n until we reach 1:
```
n / 2^k = 1
n = 2^k
k = log₂(n)
```

| Case | Comparisons | Time |
|---|---|---|
| **Best case** | 1 (key is at the middle) | **O(1)** |
| **Worst case** | log₂(n) | **O(log n)** |
| **Average case** | log₂(n) | **O(log n)** |

**Space Complexity:**
- Iterative: O(1) — no extra space
- Recursive: O(log n) — call stack depth

### Why O(log n) is Powerful

| n | Linear O(n) | Binary O(log n) |
|---|---|---|
| 10 | 10 | 4 |
| 100 | 100 | 7 |
| 1,000 | 1,000 | 10 |
| 1,000,000 | 1,000,000 | 20 |
| 1,000,000,000 | 1,000,000,000 | 30 |

Binary search in a **billion elements** takes only **30 comparisons**!

---

## 5. Linear Search vs Binary Search — Comparison

| Criterion | Linear Search | Binary Search |
|---|---|---|
| **Data requirement** | Works on unsorted data | Requires **sorted** data |
| **Time (worst case)** | O(n) | O(log n) |
| **Time (best case)** | O(1) | O(1) |
| **Approach** | Sequential scan | Divide and conquer |
| **Comparisons for n=1000** | Up to 1000 | Up to 10 |
| **Implementation** | Very simple | Slightly more complex |
| **Data structure** | Array or Linked List | **Array only** (needs random access) |
| **Space (iterative)** | O(1) | O(1) |
| **Space (recursive)** | O(1) | O(log n) |
| **Use when** | Small/unsorted data, single search | Large sorted data, many searches |

> **When to use which:**
> - **Linear search** → data is unsorted, small dataset, or only searching once
> - **Binary search** → data is sorted, large dataset, or searching multiple times

---

## 6. Exam-Ready Summary

### Quick Revision Points
1. **Linear search** = check each element → O(n), works on any data
2. **Binary search** = halve the search space each step → O(log n), needs sorted array
3. **Binary search recursive:** base case `LOW > HIGH`, recursive call with halved range
4. **Key formula:** Comparisons = ⌊log₂(n)⌋ + 1
5. **Binary search CANNOT work on linked lists** (no random access for MID)
6. **Linear search is O(n)** because it gains no information from each comparison

### Most Common Exam Questions
- Binary search recursive code (2023, 06 marks)
- Binary search iterative trace (2019, 2022)
- "Compare linear and binary search" (02–03 marks)
- "Prove linear search is one of the worst algorithms" (03 marks — from topic list)

---

## 7. Practice Problems (From Past Exams)

### Problem 1 [2023, CLO2, 06 marks]
**Q:** Write a recursive function for binary search. Trace for array [2, 5, 8, 12, 16, 23, 38, 56, 72, 91] searching for 23.

**Trace:**
| Call | LOW | HIGH | MID | A[MID] | Action |
|---|---|---|---|---|---|
| 1 | 0 | 9 | 4 | 16 | 23 > 16 → search right |
| 2 | 5 | 9 | 7 | 56 | 23 < 56 → search left |
| 3 | 5 | 6 | 5 | 23 | 23 = 23 → **FOUND at index 5** ✅ |

### Problem 2 [2022, CO1, 03 marks]
**Q:** Apply binary search on [10, 20, 30, 40, 50, 60, 70] to search for 40.

**Trace:**
| Call | LOW | HIGH | MID | A[MID] | Action |
|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 40 | 40 = 40 → **FOUND at index 3** ✅ |

Found in **1 comparison** (best case!).

### Problem 3 [Typical 03 marks]
**Q:** Binary search on [3, 9, 14, 21, 28, 35, 42, 49] for ITEM = 21.

**Trace:**
| Call | LOW | HIGH | MID | A[MID] | Action |
|---|---|---|---|---|---|
| 1 | 0 | 7 | 3 | 21 | 21 = 21 → **FOUND at index 3** ✅ |

---

*← [05 — Queues](05_queues.md) | Next: [07 — Sorting Algorithms →](07_sorting_algorithms.md)*

<br>

---
[⬅️ Previous](./05_queues.md) | [🏠 Home](./README.md) | [Next ➡️](./07_sorting_algorithms.md)
