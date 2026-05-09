[🏠 Home](./README.md) | [Next ➡️](./02_arrays_and_matrices.md)

---

# 📘 Chapter 1: Data Structures — Fundamentals

> **Exam Frequency:** 7/8 years | **Typical Marks:** 03–04 | **Section:** A
> **Course Outcome:** CO1 — Understand basic concepts of data structures

---

## 1. What is a Data Structure?

A **data structure** is a systematic way of organizing, storing, and managing data in a computer's memory so that it can be accessed and modified efficiently.

### Intuition
Think of a library. Books can be thrown randomly into a pile (unstructured), or they can be organized on shelves by subject, author, or ISBN (structured). The way you organize the books determines how fast you can find one, add a new one, or remove an old one. That "way of organizing" is the data structure.

### Formal Definition
> A data structure is a particular way of storing and organizing data in a computer so that it can be used efficiently. It defines:
> 1. The **logical arrangement** of data elements
> 2. The **operations** that can be performed on them
> 3. The **rules** governing those operations

### Why Do We Need Data Structures?

Without proper data structures, even a fast computer becomes slow:

| Scenario | Without Proper DS | With Proper DS |
|---|---|---|
| Search 1 million records | Linear scan: 1,000,000 comparisons | BST: ~20 comparisons |
| Insert into sorted collection | Shift all elements: O(n) | Linked List: O(1) after position found |
| Check if item exists | Scan entire list: O(n) | Hash Table: O(1) average |
| Find shortest path | Try all paths: exponential | Dijkstra: O(V²) |

**Bottom line:** The right data structure can turn an impossible computation into a trivial one.

---

## 2. Types of Data Structures

Data structures are broadly classified into two categories: **Linear** and **Non-Linear**.

```
                    Data Structures
                    /            \
               Linear          Non-Linear
              /  |  \  \        /       \
          Array  LL Stack Queue Tree    Graph
```

### 2.1 Linear Data Structures

**Definition:** A data structure in which elements are arranged in a **sequential manner**, where each element has a **unique predecessor** and a **unique successor** (except the first and last elements).

**Key Property:** Elements are stored/accessed in a linear (one-after-another) order.

**Examples:**

| DS | How it's Linear | Access Pattern |
|---|---|---|
| **Array** | Elements stored in contiguous memory locations, accessed by index | Random access — A[0], A[1], ... |
| **Linked List** | Each node points to the next node in sequence | Sequential access — follow pointers |
| **Stack** | Elements added/removed from one end only (LIFO) | Top element only |
| **Queue** | Elements added at rear, removed from front (FIFO) | Front and rear only |

**Intuition:** Imagine people standing in a single line. Person 1 is in front of Person 2, Person 2 is in front of Person 3, and so on. There's only one "direction" — forward. That's linear.

### 2.2 Non-Linear Data Structures

**Definition:** A data structure in which elements are **NOT arranged sequentially**. Each element can connect to **multiple other elements**, forming hierarchical or network relationships.

**Key Property:** There is no single sequence — elements can branch out in multiple directions.

**Examples:**

| DS | Structure | Relationship |
|---|---|---|
| **Tree** | Hierarchical — parent-child relationships | One parent, multiple children |
| **Graph** | Network — arbitrary connections | Any node can connect to any other |

**Intuition:** Think of a family tree — a parent has multiple children, each child can have their own children. Or think of a road map — every city connects to multiple other cities in a network. There's no single "line" to follow.

### 2.3 Comparison Table

| Criterion | Linear DS | Non-Linear DS |
|---|---|---|
| Arrangement | Sequential | Hierarchical / Network |
| Levels | Single level | Multiple levels |
| Traversal | Single pass (one run) | Multiple methods needed |
| Memory | May waste (arrays) or efficient (LL) | Generally efficient |
| Complexity | Simpler to implement | More complex |
| Examples | Array, LL, Stack, Queue | Tree, Graph |

---

## 3. Abstract Data Type (ADT)

An **Abstract Data Type (ADT)** is a mathematical model for a data type that defines:
1. **What** data is stored
2. **What** operations are supported
3. **What** are the rules for those operations

It does **NOT** define **how** these operations are implemented — that's the data structure's job.

### Intuition
Think of a TV remote. You know:
- Press "Volume Up" → volume increases
- Press "Channel" → channel changes

You don't know (or need to know) the circuits inside. The remote is an ADT — it specifies **what** happens, not **how**.

### Example: Stack ADT

| Component | Specification |
|---|---|
| **Data** | Collection of elements |
| **Operations** | push(x), pop(), peek(), isEmpty(), isFull() |
| **Rules** | LIFO — last element pushed is first to be popped |

The **implementation** could be an array or a linked list — the ADT doesn't care.

### Example: Queue ADT

| Component | Specification |
|---|---|
| **Data** | Collection of elements |
| **Operations** | enqueue(x), dequeue(), front(), isEmpty() |
| **Rules** | FIFO — first element enqueued is first to be dequeued |

---

## 4. Major Operations on Data Structures

Every data structure supports some or all of these **six fundamental operations**:

### 4.1 Traversing
**What:** Visiting (accessing) each element of the data structure exactly once in a systematic manner.

**Example — Array Traversal:**
**C++ Style:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

// Traverse vector A
void traverse(const vector<int>& A) {
    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";    // process each element
    }
}
```

**OR, Textbook Style:**
```
Procedure TRAVERSE(A, N)
    For I = 0 to N - 1 do
        Process(A[I])
    End For
End Procedure
```
**Time:** O(n) — must visit every element once.

### 4.2 Searching
**What:** Finding the location (index or address) of a specific element in the data structure.

**Two main types:**
- **Linear Search** — check every element one by one → O(n)
- **Binary Search** — divide sorted data in half each step → O(log n)

**C++ Style:**
```cpp
#include <vector>

// Linear search for ITEM in vector A
int linearSearch(const vector<int>& A, int ITEM) {
    for (int i = 0; i < A.size(); i++) {
        if (A[i] == ITEM)
            return i;           // found at index i
    }
    return -1;                  // not found
}
```

**OR, Textbook Style:**
```
Procedure LINEAR_SEARCH(A, N, ITEM)
    For I = 0 to N - 1 do
        If A[I] == ITEM Then
            Return I
        End If
    End For
    Return -1
End Procedure
```

### 4.3 Inserting
**What:** Adding a new element to the data structure at a specified position.

**Example — Insert 25 at position 3 in array [10, 20, 30, 40, 50]:**
```
Before: [10, 20, 30, 40, 50]
Step 1: Shift elements right from position 3 onward
        [10, 20, 30, __, 40, 50]   → shifted 40, 50
        [10, 20, __, 30, 40, 50]   → shifted 30
Step 2: Place 25 at position 3 (index 2)
After:  [10, 20, 25, 30, 40, 50]
```
**Time:** O(n) for arrays (due to shifting), O(1) for linked lists (after reaching position).

### 4.4 Deleting
**What:** Removing an existing element from the data structure.

**Example — Delete 30 from [10, 20, 30, 40, 50]:**
```
Before: [10, 20, 30, 40, 50]
Step 1: Remove element at index 2 (value 30)
Step 2: Shift elements left to fill gap
        [10, 20, 40, 50, __]
After:  [10, 20, 40, 50]   (size reduced by 1)
```
**Time:** O(n) for arrays (due to shifting), O(1) for linked lists (pointer update).

### 4.5 Sorting
**What:** Arranging elements in a specific order — ascending or descending — based on a key value.

**Example:** Sort [5, 2, 8, 1, 9] in ascending order → [1, 2, 5, 8, 9]

Common algorithms and their complexities:

| Algorithm | Best | Average | Worst |
|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

### 4.6 Merging
**What:** Combining two **sorted** data structures into a single **sorted** data structure.

**Example:**
```
List A: [1, 3, 5, 7]
List B: [2, 4, 6, 8]
Merged: [1, 2, 3, 4, 5, 6, 7, 8]
```

**Pseudocode:**
**C++ Style:**
```cpp
#include <vector>
using namespace std;

// Merge two sorted vectors A and B into C
void merge(const vector<int>& A, const vector<int>& B, vector<int>& C) {
    int i = 0, j = 0;
    while (i < A.size() && j < B.size()) {
        if (A[i] <= B[j])
            C.push_back(A[i++]);       // take from A
        else
            C.push_back(B[j++]);       // take from B
    }
    while (i < A.size()) C.push_back(A[i++]); // remaining from A
    while (j < B.size()) C.push_back(B[j++]); // remaining from B
}
```

**OR, Textbook Style:**
```
Procedure MERGE(A, M, B, N, C)
    Set I = 0, J = 0, K = 0
    While I < M AND J < N do
        If A[I] <= B[J] Then
            Set C[K] = A[I]
            Set I = I + 1
        Else
            Set C[K] = B[J]
            Set J = J + 1
        End If
        Set K = K + 1
    End While
    
    While I < M do
        Set C[K] = A[I]
        Set I = I + 1, K = K + 1
    End While
    
    While J < N do
        Set C[K] = B[J]
        Set J = J + 1, K = K + 1
    End While
End Procedure
```
**Time:** O(m + n)

---

## 5. Time-Space Trade Off

### Definition
The **time-space trade off** is a situation in algorithm design where we can:
- **Reduce execution time** by **using more memory space**, or
- **Reduce memory usage** by **allowing more execution time**

We "trade" one resource for the other to optimize the aspect that matters more for our application.

### Intuition
Imagine you're cooking for 100 guests:
- **More space, less time:** Use 10 stoves (needs a bigger kitchen) and cook everything in 1 hour
- **Less space, more time:** Use 1 stove (small kitchen) but take 10 hours

You trade kitchen space for cooking time, or vice versa.

### Example 1: Hash Table vs Linear Search

| Approach | Time | Space |
|---|---|---|
| Linear Search (no extra space) | O(n) | O(1) extra |
| Hash Table (extra hash array) | O(1) average | O(n) extra |

The hash table uses **extra space** to store the hash array, but in return gives **O(1) lookup time** instead of O(n). We traded space for time.

### Example 2: Compressed vs Uncompressed Data

| Approach | Space | Time |
|---|---|---|
| Uncompressed (store raw) | Large (e.g., 100 MB) | O(1) — instant access |
| Compressed (store zip) | Small (e.g., 20 MB) | O(k) — decompression time needed |

### Example 3: Sorted Array vs Linked List

| Operation | Sorted Array | Linked List |
|---|---|---|
| Search | O(log n) — binary search possible | O(n) — only linear search |
| Insert | O(n) — shifting required | O(1) — just update pointers |
| Extra Space | None | Extra pointer per node |

**Trade-off:** Sorted array gives faster search (less time) but harder insertion. Linked list gives easy insertion but slower search.

### Example 4: Sparse Matrix

A 1000×1000 matrix with only 50 non-zero elements:
- **2D Array approach:** 1,000,000 memory cells. Access time O(1). Wastes space.
- **Linked List of triplets (row, col, value):** Only 50 × 3 = 150 cells. Saves space but access time O(n).

---

## 6. Algorithm

### Definition
An **algorithm** is a finite, step-by-step, well-defined procedure for solving a computational problem. It takes some input, processes it through a sequence of unambiguous steps, and produces an output.

### Properties of an Algorithm

1. **Finiteness** — Must terminate after a finite number of steps
2. **Definiteness** — Each step must be precisely and unambiguously defined
3. **Input** — Takes zero or more inputs
4. **Output** — Produces at least one output
5. **Effectiveness** — Every step must be basic enough to be carried out (in principle) by a person using pencil and paper

### Algorithm vs Program

| Algorithm | Program |
|---|---|
| Written in pseudocode / natural language | Written in a programming language (C, Java) |
| Language independent | Language dependent |
| Design phase | Implementation phase |
| Must be finite | May run infinitely (e.g., OS kernel) |
| Analyzed for correctness & complexity | Tested for bugs & performance |

---

## 7. Performance Analysis vs Performance Measurement

### Performance Analysis (A Priori Analysis)
**What:** Estimating the performance of an algorithm **before** implementing it, using mathematical analysis.

**Focuses on:**
- **Time Complexity** — how many operations as a function of input size
- **Space Complexity** — how much memory as a function of input size

**Advantage:** Machine-independent. Results are universal.

**Example:** Analyzing that bubble sort is O(n²) — this is true regardless of which computer you run it on.

### Performance Measurement (A Posteriori Testing)
**What:** Measuring the **actual** performance of an implemented program by running it on a real machine and recording execution time and memory usage.

**Focuses on:**
- Wall-clock time (seconds, milliseconds)
- Actual memory consumed (KB, MB)

**Disadvantage:** Machine-dependent. Results vary by hardware, OS, compiler, and load.

### Comparison

| Criterion | Performance Analysis | Performance Measurement |
|---|---|---|
| When | Before implementation | After implementation |
| Method | Mathematical / theoretical | Experimental / empirical |
| Dependence | Machine-independent | Machine-dependent |
| Result | Big-O notation | Actual time in seconds |
| Usefulness | Comparing algorithms | Tuning a specific program |
| Tools | Pen and paper, math | Profilers, timers, benchmarks |

---

## 8. Garbage Collection

### Definition
**Garbage collection** is the process of automatically identifying and reclaiming memory that is no longer being used (referenced) by any part of the program, and returning it to the pool of available memory (the **AVAIL list** or **free space list**).

### Intuition
Think of a parking lot. When a car leaves a spot, that spot becomes "garbage" — unused but still occupied in the system. The parking attendant (garbage collector) periodically checks all spots, marks the empty ones, and updates the "available spots" board.

### How It Works in Linked Lists

When nodes are deleted from a linked list, the memory they occupied doesn't automatically become available for reuse. The system must:

1. **Mark Phase:** Go through all accessible nodes (starting from all START pointers) and mark them as "in use"
2. **Sweep Phase:** Scan through all memory cells. Any unmarked cell is "garbage" — add it back to the AVAIL list

```
Before Garbage Collection:
  START → [10] → [20] → [30] → NULL
  
  Memory: [10][20][xx][30][xx][xx]    (xx = inaccessible nodes)
  
After Garbage Collection:
  AVAIL → [xx] → [xx] → [xx] → NULL  (freed nodes returned to AVAIL)
```

### When Does Garbage Collection Happen?
- When `AVAIL = NULL` (no free space left) — the system runs garbage collection to reclaim space
- If garbage collection fails to free space → **OVERFLOW** error

---

## 9. Basic C Concepts Review (Instructor Notes)

Since the course implementation language is C, the instructor emphasized several core language concepts:

### 9.1 The `+=` vs `=+` Operators
- `+=` (Compound Assignment): Increments the value. Example: `x += 1` adds 1 to `x` (equivalent to `x = x + 1`).
- `=+` (Assignment with Unary Plus): Assigns a positive value. Example: `x = +y` or `x =+ y` simply assigns the positive value of `y` to `x`.

### 9.2 Difference Between `struct`, `union`, and `enum` (Important Viva Question)
| Feature | `struct` (Structure) | `union` | `enum` (Enumeration) |
|---|---|---|---|
| **Purpose** | Groups variables of different data types | Groups variables of different data types | Assigns names to integer constants |
| **Memory Allocation** | Allocates memory for **all** members separately | Allocates memory only for the **largest** member | Allocates memory for an integer |
| **Memory Size** | Sum of sizes of all members (plus padding) | Size of the largest member | Size of an `int` |
| **Access** | All members can be accessed at any time | Only one member can be accessed at a time | Members act as constant values |

### 9.3 Pointers Overview
A **pointer** is a variable that stores the memory address of another variable. There is a direct connection between the CPU and the memory unit via pointers.

**Important Pointer Types:**
1. **Void Pointer (`void *`):** A generic pointer that has no associated data type. It can hold the address of any type of variable and can be typecasted to any type.
   ```c
   int n = 10;
   void *ptr = &n;
   printf("%d", *(int*)ptr); // Must typecast before dereferencing
   ```
2. **NULL Pointer:** A pointer that points to nothing. Its value is 0 or `NULL`. It is a good practice to initialize pointers as NULL if they don't immediately point to a valid location.
3. **Dangling Pointer:** A pointer pointing to a memory location that has been deleted (or freed). Using a dangling pointer leads to undefined behavior.

---

## 10. Exam-Ready Summary

### Quick Revision Points
1. **Data Structure** = way of organizing data for efficient access
2. **Linear DS** = sequential (Array, LL, Stack, Queue)
3. **Non-Linear DS** = hierarchical/network (Tree, Graph)
4. **6 operations** = Traverse, Search, Insert, Delete, Sort, Merge
5. **ADT** = defines WHAT (interface), DS = defines HOW (implementation)
6. **Time-Space tradeoff** = more memory ↔ less time (and vice versa)
7. **Performance Analysis** = theoretical (Big-O, machine-independent)
8. **Performance Measurement** = experimental (actual time, machine-dependent)
9. **Garbage Collection** = reclaim unused memory → return to AVAIL list
10. **Pointers:** Void (no type), NULL (points to 0), Dangling (points to freed memory)

### Common Exam Question Patterns
- "Define linear and non-linear DS with examples" (02–04 marks) — appears almost every year
- "What are the major operations on DS?" (03–04 marks)
- "What is time-space tradeoff? Give an example." (03–04 marks)
- "Performance analysis vs measurement" (02–03 marks)
- "Why do we need data structures?" (02–03 marks)
- "DS can reduce time and space complexity — justify" (03 marks)
- "Differentiate between struct, union, and enum" (Viva/Short Q)

---

## 11. Practice Problems (From Past Exams)

### Problem 1 [2017, 04 marks]
**Q:** Define linear and non-linear data structure. Discuss major operations in data structures.

**Approach:** Define both with 2 examples each → list 6 operations with one-line description + tiny example for each.

### Problem 2 [2021, 03 marks]
**Q:** "Data structure can reduce time and space complexity" — justify with examples.

**Approach:** Give one time example (hash table O(1) vs linear search O(n)) + one space example (sparse matrix: 2D array vs triplet LL).

### Problem 3 [2024, 04 marks]
**Q:** Define linear and non-linear DS. Discuss major operations. (CO1)

**Approach:** Same as 2017 — this question was recycled almost identically. Definition + 6 operations.

---

*Next Chapter: [02 — Arrays and Matrices →](02_arrays_and_matrices.md)*

<br>

---
[🏠 Home](./README.md) | [Next ➡️](./02_arrays_and_matrices.md)
