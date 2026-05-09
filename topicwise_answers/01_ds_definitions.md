[🏠 Home](./README.md) | [Next ➡️](./02_linked_list.md)

---

# DS Definitions — Linear & Non-linear, Operations, Fundamentals


---

## [2017] 1(a) Define linear and non-linear data structure. Discuss major operations. (04)

**Linear Data Structure:** A data structure where elements are arranged in a sequential manner and each element has a unique predecessor and successor (except first and last).
*Examples:* Array, Linked List, Stack, Queue.

**Non-linear Data Structure:** A data structure where elements are not arranged sequentially. Each element can connect to multiple elements, forming hierarchical or network relationships.
*Examples:* Tree, Graph.

**Major Operations in Data Structure:**

1. **Traversing** — Accessing/visiting each element exactly once (e.g., printing all array elements)
2. **Searching** — Finding the location of an element (e.g., binary search)
3. **Inserting** — Adding a new element to the structure
4. **Deleting** — Removing an existing element from the structure
5. **Sorting** — Arranging elements in a specific order (ascending/descending)
6. **Merging** — Combining two sorted structures into a single sorted structure

---


---

## [2017] 1(b) What is time-space trade off? Give an example. (04)

**Time-Space Trade Off:** It is a situation where we can reduce the time required by an algorithm by using more memory space, or reduce memory usage by allowing the algorithm to take more time. We trade one resource for another to optimize performance.

**Example — Sorted Array vs Linked List:**

| Criterion | Sorted Array | Linked List |
|---|---|---|
| Search Time | O(log n) — binary search | O(n) — linear only |
| Space | No extra pointers | Extra pointer per node |
| Insertion | O(n) — shifting needed | O(1) — pointer update |

Another example: **Hash Table** uses extra space (hash array) to reduce search time from O(n) to O(1) average. Here, we trade space for faster time.

**Compressed vs Uncompressed data:** Storing data in compressed form saves space but requires extra time to decompress. Uncompressed data uses more space but is accessed instantly.

---


---

## [2018] Q1(a) Define (i) Data structure (ii) Linear DS (iii) Non-linear DS. (4.5)

**(i) Data Structure:** A systematic way of organizing, storing, and managing data in a computer so that it can be accessed and modified efficiently.

**(ii) Linear Data Structure:** Elements are arranged sequentially where each element has a unique predecessor and successor (except first and last).
- *Examples:* Array, Linked List, Stack, Queue

**(iii) Non-linear Data Structure:** Elements are not arranged sequentially. Each element can connect to multiple elements forming hierarchical or network structures.
- *Examples:* Tree, Graph

---


---

## [2018] Q1(b) Major operations in data structure. (04)

1. **Traversing** — Visiting each element exactly once (e.g., printing array elements)
2. **Searching** — Finding the location of a given element (e.g., binary search in sorted array)
3. **Inserting** — Adding a new element at a specific position
4. **Deleting** — Removing an element from the structure
5. **Sorting** — Arranging elements in ascending or descending order
6. **Merging** — Combining two sorted data structures into one sorted structure

---


---

## [2019] Q.1(a) Describe (i) Traversing (ii) Sorting (iii) Searching. (06)

**(i) Traversing:** The process of visiting and accessing each element of a data structure exactly once, in a systematic manner, to process or display the data.

**Example:** Printing all elements of an array A of size N:
```
Procedure TRAVERSE(A, N)
    For I = 1 to N do
        Print A[I]
    End For
End Procedure
```
Time: O(n)

**(ii) Sorting:** The process of arranging elements of a data structure in a specific order — either ascending or descending — based on a key value.

**Example:** Sorting [5, 2, 8, 1] in ascending order → [1, 2, 5, 8]
- Common algorithms: Bubble Sort O(n²), Quick Sort O(n log n), Merge Sort O(n log n)

**(iii) Searching:** The process of finding the location of a specific element (ITEM) within a data structure.

**Example:** Finding element 25 in array [10, 25, 30, 45]:
- **Linear Search:** Check each element sequentially → O(n)
- **Binary Search:** Divide sorted array in half each step → O(log n)

---


---

## [2020] Q.1(a) Why do we need DS? Explain linear and non-linear DS. (03)

**Why we need data structure:**
Data structures organize and manage data efficiently, enabling faster access, insertion, deletion, and searching. Without proper data structures, programs would be slow and consume excessive memory.

**Linear Data Structure:** Elements arranged sequentially with unique predecessor and successor.
- *Examples:* Array (indices), Linked List (pointers), Stack (LIFO), Queue (FIFO)

**Non-linear Data Structure:** Elements arranged hierarchically or in a network — each element may connect to multiple elements.
- *Examples:* Tree (parent-child hierarchy), Graph (nodes and edges)

---


---

## [2021] Q.1(c) "DS can reduce time and space complexity" — justify. (03)

**Example 1 — Time reduction:**
Searching 1,000,000 items:
- Using unsorted array (linear search): O(n) = 1,000,000 comparisons
- Using BST: O(log n) = ~20 comparisons
- Using Hash Table: O(1) = 1 comparison average

Choosing the right data structure reduces time drastically.

**Example 2 — Space reduction:**
Storing a sparse matrix (1000×1000 with only 50 non-zero elements):
- Using 2D array: 1,000,000 memory cells (wasteful)
- Using linked list of triplets (row, col, value): only 50 × 3 = 150 cells

Proper data structure choice saves both time and space.

---


---

## [2024] Q.1(a) Define linear/non-linear DS. Major operations. (CO1, 04)

**Linear Data Structure:** Elements arranged sequentially where each element has a unique predecessor and successor (except first and last).
- *Examples:* Array, Linked List, Stack, Queue

**Non-linear Data Structure:** Elements arranged hierarchically or in a network; each element can connect to multiple elements.
- *Examples:* Tree, Graph

**Major Operations:**
1. **Traversing** — Visiting each element exactly once
2. **Searching** — Finding the location of a specific element
3. **Inserting** — Adding a new element
4. **Deleting** — Removing an existing element
5. **Sorting** — Arranging elements in order
6. **Merging** — Combining two sorted structures into one

---


---

## 📊 Exam Priority
**Priority: 1/5** (Must Prepare)
**Appeared in:** 7/8 years
**Typical marks:** 03–04 per question

<br>

---
[🏠 Home](./README.md) | [Next ➡️](./02_linked_list.md)
