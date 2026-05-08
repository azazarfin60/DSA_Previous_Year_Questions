# 📘 Chapter 3: Linked Lists

> **Exam Frequency:** 5/8 years | **Typical Marks:** 02–04 | **Section:** A
> **Key Topics:** Singly, Doubly, Circular LL, all operations, Header LL, Memory representation

---

## 1. What is a Linked List?

A **linked list** is a linear data structure where elements (called **nodes**) are stored in **non-contiguous** (scattered) memory locations. Each node contains:
1. **DATA** — the actual value stored
2. **LINK (pointer/NEXT)** — the address of the next node in the sequence

The nodes are "linked" together through pointers, forming a chain.

### Intuition
Think of a **treasure hunt**. At each location, you find a clue (data) and directions to the next location (pointer). You don't know all locations in advance — you discover them one by one by following the clues. If one clue is lost, the chain is broken and remaining treasures are unreachable.

### Comparison with Array

```
Array (contiguous):
  ┌────┬────┬────┬────┬────┐
  │ 10 │ 20 │ 30 │ 40 │ 50 │    All in a row, like houses on a street
  └────┴────┴────┴────┴────┘
  
Linked List (non-contiguous):
  START
    │
    ▼
  ┌────┬───┐    ┌────┬───┐    ┌────┬───┐    ┌────┬──────┐
  │ 10 │ ──┼───→│ 20 │ ──┼───→│ 30 │ ──┼───→│ 40 │ NULL │
  └────┴───┘    └────┴───┘    └────┴───┘    └────┴──────┘
  (addr 200)    (addr 508)    (addr 112)    (addr 740)
```

---

## 2. Memory Representation of Linked Lists

In textbook/exam context, a linked list is stored using **two parallel arrays**:
- **INFO[ ]** — stores data values
- **LINK[ ]** — stores the index (address) of the next node

Two special pointers:
- **START** — points to the first node of the list
- **AVAIL** — points to the first node of the free space (available memory) list

> **Exam Note (Array Memory Calculation):** The syllabus explicitly mentions "Array memory calculation math" alongside Linked Lists. This refers to 1D/2D array address calculation formulas (Row-Major/Column-Major) which are often bundled with Linked List theory questions in exams. Please refer to **[Chapter 2: Arrays and Matrices](02_arrays_and_matrices.md)** for detailed mathematical formulas and worked examples.

### Example

```
Index:   1     2     3     4     5     6     7
INFO:  [ 40 ] [ _ ] [ 10 ] [ 30 ] [ _ ] [ 20 ] [ _ ]
LINK:  [  6 ] [  5 ] [  4 ] [  1 ] [  7 ] [  0 ] [  0 ]

START = 3        (list starts at index 3)
AVAIL = 2        (free space starts at index 2)
```

**Tracing the data list:**
```
START = 3 → INFO[3] = 10, LINK[3] = 4
         → INFO[4] = 30, LINK[4] = 1
         → INFO[1] = 40, LINK[1] = 6
         → INFO[6] = 20, LINK[6] = 0 (NULL = end)

Data List: 10 → 30 → 40 → 20 → NULL
```

**Tracing the free list:**
```
AVAIL = 2 → LINK[2] = 5
          → LINK[5] = 7
          → LINK[7] = 0 (NULL = end)

Free List: 2 → 5 → 7 → NULL   (3 free nodes available)
```

---

## 3. Types of Linked Lists

### 3.1 Singly Linked List (SLL)

Each node has **one pointer** (NEXT) — traversal is **one-direction only** (forward).

```
  START
    │
    ▼
  ┌────┬───┐    ┌────┬───┐    ┌────┬──────┐
  │ 10 │ ──┼───→│ 20 │ ──┼───→│ 30 │ NULL │
  └────┴───┘    └────┴───┘    └────┴──────┘
```

**Node Structure in C:**
```c
struct Node {
    int data;
    struct Node *next;    // pointer to next node
};
```

**Properties:**
- Can only traverse forward (left to right)
- Last node's NEXT = NULL
- Deleting a node requires knowing the previous node (O(n) to find)
- Uses less memory per node (one pointer only)

---

### 3.2 Doubly Linked List (DLL)

Each node has **two pointers**: PREV (previous) and NEXT (next) — traversal in **both directions**.

```
  NULL ←── PREV          NEXT ──→ NULL
            │                │
  ┌──────┬────┬───┐    ┌───┬────┬───┐    ┌───┬────┬──────┐
  │ NULL │ 10 │ ──┼───→│←──│ 20 │ ──┼───→│←──│ 30 │ NULL │
  └──────┴────┴───┘    └───┴────┴───┘    └───┴────┴──────┘
      PREV  DATA  NEXT
```

**Node Structure in C:**
```c
struct DNode {
    struct DNode *prev;   // pointer to previous node
    int data;
    struct DNode *next;   // pointer to next node
};
```

**Properties:**
- Can traverse both forward AND backward
- Each node uses more memory (two pointers instead of one)
- Deletion of a given node is O(1) — no need to find predecessor
- Insertion before a given node is O(1)

---

### 3.3 Circular Linked List (CLL)

The **last node points back to the first node** instead of NULL, forming a circle.

**Circular Singly Linked List:**
```
  START
    │
    ▼
  ┌────┬───┐    ┌────┬───┐    ┌────┬───┐
  │ 10 │ ──┼───→│ 20 │ ──┼───→│ 30 │ ──┼───┐
  └────┴───┘    └────┴───┘    └────┴───┘   │
    ▲                                       │
    └───────────────────────────────────────┘
```

**Properties:**
- No NULL pointer — last node points to START
- Can traverse the entire list starting from any node
- Useful for applications that require cycling (e.g., round-robin scheduling)
- Must be careful to detect when you've completed a full cycle (check if PTR == START again)

**Circular Doubly Linked List:**
```
  ┌──→ [10] ←→ [20] ←→ [30] ──┐
  │                              │
  └──────────────────────────────┘
```
Both first.PREV → last and last.NEXT → first.

---

### 3.4 Comparison of Types

| Criterion | Singly LL | Doubly LL | Circular LL |
|---|---|---|---|
| Pointers per node | 1 (NEXT) | 2 (PREV + NEXT) | 1 or 2 |
| Traversal | Forward only | Both directions | Circular (no end) |
| Memory per node | Less | More | Same as base type |
| Delete given node | O(n) — need predecessor | **O(1)** | O(n) or O(1) |
| Insert before node | O(n) | **O(1)** | O(n) or O(1) |
| Last node NEXT | NULL | NULL | Points to first |
| Use case | Simple lists | When backward traversal needed | Round-robin, cycling |

---

## 4. Operations on Singly Linked List

### 4.1 Traversal

**Goal:** Visit every node from START to the end (NULL).

```
Procedure TRAVERSE(START)
    Set PTR = START
    While PTR ≠ NULL do
        Process INFO[PTR]          // print, count, etc.
        Set PTR = LINK[PTR]        // move to next node
    End While
End Procedure
```

**Time:** O(n) — must visit every node.

**Trace Example:** START = 3, List: 10 → 30 → 40 → 20 → NULL
```
PTR = 3 → Process 10 → PTR = 4
PTR = 4 → Process 30 → PTR = 1
PTR = 1 → Process 40 → PTR = 6
PTR = 6 → Process 20 → PTR = 0 (NULL)
Stop.
```

---

### 4.2 Searching

**Goal:** Find the location (index) of a node containing a given ITEM.

```
Procedure SEARCH(START, ITEM)
    Set PTR = START
    While PTR ≠ NULL do
        If INFO[PTR] = ITEM Then
            Return PTR             // found! return location
        End If
        Set PTR = LINK[PTR]
    End While
    Return NULL                    // not found
End Procedure
```

**Time:** O(n) — worst case, ITEM is at the end or not present.

---

### 4.3 Insertion at Beginning

**Goal:** Add a new node with ITEM at the start of the list.

```
Procedure INSERT_BEGINNING(START, AVAIL, ITEM)
    // Step 1: Check overflow
    If AVAIL = NULL Then
        Print "OVERFLOW"
        Return
    End If
    
    // Step 2: Get a free node
    Set NEW = AVAIL
    Set AVAIL = LINK[AVAIL]
    
    // Step 3: Fill data and link
    Set INFO[NEW] = ITEM
    Set LINK[NEW] = START          // new node points to old first
    
    // Step 4: Update START
    Set START = NEW                // START now points to new node
End Procedure
```

**Diagram:**
```
Before: START → [10] → [20] → [30] → NULL
                                        AVAIL → [__] → ...

After INSERT_BEGINNING(5):
        START → [5] → [10] → [20] → [30] → NULL
```

**Time:** O(1) — no traversal needed.

---

### 4.4 Insertion After a Given Location (LOC)

**Goal:** Insert ITEM after the node at position LOC.

```
Procedure INSERT_AFTER(START, AVAIL, LOC, ITEM)
    // Step 1: Check overflow
    If AVAIL = NULL Then
        Print "OVERFLOW"
        Return
    End If
    
    // Step 2: Get a free node
    Set NEW = AVAIL
    Set AVAIL = LINK[AVAIL]
    
    // Step 3: Fill data
    Set INFO[NEW] = ITEM
    
    // Step 4: Link new node into the chain
    Set LINK[NEW] = LINK[LOC]     // new node points to LOC's next
    Set LINK[LOC] = NEW            // LOC now points to new node
End Procedure
```

**Diagram:**
```
Before: [10] → [20] → [30] → NULL
                 ↑ LOC

After INSERT_AFTER(LOC, 25):
        [10] → [20] → [25] → [30] → NULL
```

**Time:** O(1) — just pointer manipulation (assuming LOC is given).

---

### 4.5 Insertion Into a Sorted List

**Goal:** Insert ITEM into its correct position in a sorted linked list.

```
Procedure INSERT_SORTED(START, AVAIL, ITEM)
    // Step 1: Check overflow
    If AVAIL = NULL Then
        Print "OVERFLOW"
        Return
    End If
    
    // Step 2: Get a free node
    Set NEW = AVAIL
    Set AVAIL = LINK[AVAIL]
    Set INFO[NEW] = ITEM
    
    // Step 3: Find correct position
    Set PTR = START
    Set PREV = NULL
    While PTR ≠ NULL AND INFO[PTR] < ITEM do
        Set PREV = PTR
        Set PTR = LINK[PTR]
    End While
    
    // Step 4: Insert
    If PREV = NULL Then            // insert at beginning
        Set LINK[NEW] = START
        Set START = NEW
    Else                           // insert after PREV
        Set LINK[NEW] = LINK[PREV]
        Set LINK[PREV] = NEW
    End If
End Procedure
```

**Trace:** Insert 25 into sorted list: 10 → 20 → 30 → 40 → NULL
```
PTR=10, PREV=NULL: 10 < 25 → move
PTR=20, PREV=10:  20 < 25 → move
PTR=30, PREV=20:  30 < 25 → FALSE, stop
Insert after PREV(20): 10 → 20 → 25 → 30 → 40 → NULL ✓
```

---

### 4.6 Deletion from Beginning

```
Procedure DELETE_BEGINNING(START, AVAIL)
    // Step 1: Check underflow
    If START = NULL Then
        Print "UNDERFLOW — list is empty"
        Return
    End If
    
    // Step 2: Save and remove first node
    Set PTR = START
    Set START = LINK[START]        // START moves to second node
    
    // Step 3: Return freed node to AVAIL
    Set LINK[PTR] = AVAIL
    Set AVAIL = PTR
End Procedure
```

**Time:** O(1)

---

### 4.7 Deletion of a Specific Node (by value)

```
Procedure DELETE_NODE(START, AVAIL, ITEM)
    // Step 1: Check underflow
    If START = NULL Then
        Print "UNDERFLOW"
        Return
    End If
    
    // Step 2: Special case — deleting first node
    If INFO[START] = ITEM Then
        Set PTR = START
        Set START = LINK[START]
        Set LINK[PTR] = AVAIL
        Set AVAIL = PTR
        Return
    End If
    
    // Step 3: Find the node and its predecessor
    Set PTR = START
    While LINK[PTR] ≠ NULL do
        If INFO[LINK[PTR]] = ITEM Then
            // Found! LINK[PTR] is the node to delete
            Set TEMP = LINK[PTR]
            Set LINK[PTR] = LINK[TEMP]    // bypass the node
            Set LINK[TEMP] = AVAIL        // return to free list
            Set AVAIL = TEMP
            Return
        End If
        Set PTR = LINK[PTR]
    End While
    
    Print "ITEM not found"
End Procedure
```

**Trace:** Delete 30 from: 10 → 20 → 30 → 40 → NULL
```
START=10, INFO[10]=10 ≠ 30
PTR=10: LINK[10]=20, INFO[20]=20 ≠ 30 → PTR=20
PTR=20: LINK[20]=30, INFO[30]=30 = 30 → FOUND!
  TEMP = 30
  LINK[20] = LINK[30] = 40       (bypass 30)
  Return 30 to AVAIL
Result: 10 → 20 → 40 → NULL ✓
```

**Time:** O(n) — must search for the node.

---

### 4.8 Reversing a Singly Linked List

**Goal:** Reverse the direction of all pointers so the list goes backward.

```
Procedure REVERSE(HEAD)
    Set PREV = NULL
    Set CURR = HEAD
    While CURR ≠ NULL do
        Set NEXT_NODE = LINK[CURR]     // save next
        Set LINK[CURR] = PREV          // reverse the pointer
        Set PREV = CURR                // advance PREV
        Set CURR = NEXT_NODE           // advance CURR
    End While
    Set HEAD = PREV                    // new head is the last node
    Return HEAD
End Procedure
```

### Intuition
Imagine a conga line of people, each holding the shoulder of the person in front. To reverse it:
1. Take each person
2. Make them face the opposite direction (reverse their pointer)
3. The last person in the original line becomes the new leader

### Complete Trace

**Input:** 1 → 2 → 3 → 4 → NULL

| Step | PREV | CURR | NEXT | Action | List State |
|---|---|---|---|---|---|
| Init | NULL | 1 | — | — | 1→2→3→4→NULL |
| 1 | NULL | 1 | 2 | 1.next = NULL | NULL←1  2→3→4→NULL |
| 2 | 1 | 2 | 3 | 2.next = 1 | NULL←1←2  3→4→NULL |
| 3 | 2 | 3 | 4 | 3.next = 2 | NULL←1←2←3  4→NULL |
| 4 | 3 | 4 | NULL | 4.next = 3 | NULL←1←2←3←4 |
| End | 4 | NULL | — | HEAD = 4 | 4→3→2→1→NULL |

> **Result: 4 → 3 → 2 → 1 → NULL** ✅
> **Time: O(n), Space: O(1)**

### C Code
```c
struct Node* reverse(struct Node* head) {
    struct Node *prev = NULL, *curr = head, *next;
    while (curr != NULL) {
        next = curr->next;      // save next
        curr->next = prev;      // reverse link
        prev = curr;            // advance prev
        curr = next;            // advance curr
    }
    return prev;                // new head
}
```

---

## 5. Doubly Linked List — Operations

### 5.1 Node Structure
```c
struct DNode {
    struct DNode *prev;
    int data;
    struct DNode *next;
};
```

### 5.2 Insertion at Beginning
```
Procedure DLL_INSERT_BEGINNING(HEAD, ITEM)
    Create NEW node
    Set DATA[NEW] = ITEM
    Set NEXT[NEW] = HEAD
    Set PREV[NEW] = NULL
    
    If HEAD ≠ NULL Then
        Set PREV[HEAD] = NEW       // old head's PREV points to new node
    End If
    
    Set HEAD = NEW
End Procedure
```

### 5.3 Deletion of a Node (given the node pointer)

This is where DLL shines — **O(1) deletion** because we have access to both neighbors.

```
Procedure DLL_DELETE(HEAD, PTR)
    // Case 1: PTR is the first node
    If PREV[PTR] = NULL Then
        Set HEAD = NEXT[PTR]
    Else
        Set NEXT[PREV[PTR]] = NEXT[PTR]    // previous node skips PTR
    End If
    
    // Case 2: PTR is not the last node
    If NEXT[PTR] ≠ NULL Then
        Set PREV[NEXT[PTR]] = PREV[PTR]    // next node's PREV skips PTR
    End If
    
    Free PTR
End Procedure
```

**Trace:** Delete node 20 from: NULL←10↔20↔30→NULL
```
PREV[20] = 10 (not NULL) → NEXT[10] = NEXT[20] = 30
NEXT[20] = 30 (not NULL) → PREV[30] = PREV[20] = 10
Free node 20
Result: NULL←10↔30→NULL ✓
```

---

### 5.4 Doubly vs Singly Linked List — Detailed Comparison

| Criterion | Singly Linked List | Doubly Linked List |
|---|---|---|
| **Pointers per node** | 1 (NEXT only) | 2 (NEXT + PREV) |
| **Memory per node** | data + 1 pointer | data + 2 pointers |
| **Traversal** | Forward only | Both forward and backward |
| **Delete given node** | O(n) — need to find predecessor | **O(1)** — PREV pointer available |
| **Insert before given node** | O(n) — need to find predecessor | **O(1)** — PREV available |
| **Insert after given node** | O(1) | O(1) |
| **Implementation complexity** | Simpler | More complex |
| **Reverse traversal** | Not possible without reversing | Directly possible via PREV |

**When to use SLL:** Simple lists, forward-only traversal, memory-constrained.
**When to use DLL:** Need backward traversal, frequent deletions of specific nodes, implementing LRU cache.

---

## 6. Header Linked List

### Definition
A **Header Linked List** is a linked list that contains a special node at the very beginning called the **header node**. The header node does NOT store actual list data — it serves as a permanent sentinel/anchor.

### Types
1. **Grounded Header List:** Last node's LINK = NULL
2. **Circular Header List:** Last node's LINK points back to the header node

```
Grounded Header List:
  HEADER → [count=3] → [10] → [20] → [30] → NULL

Circular Header List:
  HEADER → [count=3] → [10] → [20] → [30] ──┐
    ▲                                          │
    └──────────────────────────────────────────┘
```

### Advantages (Important for Exam — asked in 2017 & 2024)

1. **List is never "empty"** — START always points to the header node. Eliminates special-case handling for empty list operations.

2. **Metadata storage** — The header node can store useful information like:
   - Total number of nodes → makes counting O(1) instead of O(n)
   - Pointer to the last node → makes insertion at end O(1)

3. **Uniform algorithms** — Without a header, inserting at the beginning requires updating START. With a header, ALL insertions happen "after some node" — the algorithm is the same for every position.

4. **Simplified deletion** — Every data node always has a predecessor (at minimum, the header). No special case for deleting the first data node.

**Example:**
```
Without header:
  Insert 5 at beginning: Must change START from [10] to [5]
  Delete first node: Must change START from [10] to [20]
  
With header:
  Insert 5 at beginning: Insert after HEADER — START never changes!
  Delete first node: Delete HEADER's next — START never changes!
```

---

## 7. Polynomial Representation Using Linked Lists

### Concept
A polynomial like `5x³ + 4x² + 2x + 1` can be represented as a linked list where each node stores:
- **Coefficient** (5, 4, 2, 1)
- **Exponent** (3, 2, 1, 0)
- **Pointer to next term**

```
POLY → [5|3|→] → [4|2|→] → [2|1|→] → [1|0|NULL]
        5x³        4x²        2x         1
```

### Polynomial Addition

To add: P(x) = 3x³ + 2x + 1 and Q(x) = 4x² + 2x + 5

**Algorithm:** Compare exponents, add coefficients when equal, otherwise copy the term with the larger exponent.

```
P: [3|3] → [2|1] → [1|0] → NULL
Q: [4|2] → [2|1] → [5|0] → NULL

Step 1: P.exp=3 > Q.exp=2 → Copy 3x³ to result
Step 2: P.exp=1 < Q.exp=2 → Copy 4x² to result
Step 3: P.exp=1 = Q.exp=1 → Add: (2+2)x¹ = 4x¹
Step 4: P.exp=0 = Q.exp=0 → Add: (1+5)x⁰ = 6

Result: 3x³ + 4x² + 4x + 6
```

---

## 8. Splitting a Linked List

**Goal:** Split one linked list into two at a given position LOC.

```
Procedure SPLIT_LIST(HEAD, LOC)
    Set PTR = HEAD
    Set COUNT = 1
    
    // Traverse to the LOC-th node
    While COUNT < LOC AND PTR ≠ NULL do
        Set PTR = LINK[PTR]
        Set COUNT = COUNT + 1
    End While
    
    // PTR is now at LOC-th node
    Set HEAD2 = LINK[PTR]         // second list starts here
    Set LINK[PTR] = NULL          // terminate first list
    
    // HEAD = first list, HEAD2 = second list
End Procedure
```

**Example:** Split [10→20→30→40→50] at position 3:
```
First list:  10 → 20 → 30 → NULL
Second list: 40 → 50 → NULL
```

---

## 9. Exam-Ready Summary

### Quick Revision Points
1. **Linked List** = non-contiguous nodes connected by pointers
2. **Memory representation** = INFO[] + LINK[] arrays, START, AVAIL
3. **3 types:** Singly (1 pointer), Doubly (2 pointers), Circular (no NULL end)
4. **Header LL** = sentinel node at beginning → simplifies operations, stores metadata
5. **Reversal** uses 3 pointers: PREV, CURR, NEXT → O(n) time, O(1) space
6. **Insert after LOC** = O(1), **Delete by value** = O(n) for SLL, **Delete given node** = O(1) for DLL

### Most Frequently Asked in Exams
- Define LL + benefits over array (2021, 2023, 2024) → 3 marks
- Insert after LOC pseudocode (2021, 2023, 2024) → 3 marks
- Header LL advantages (2017, 2024) → 3–4 marks
- DLL vs SLL comparison (2024) → 3 marks
- Reverse a linked list (2024) → 4 marks

---

## 10. Practice Problems (From Past Exams)

### Problem 1 [2024, CO2, 03 marks]
**Q:** Define linked list. Write benefits of linked list over array.

**Approach:** 1-line definition → 4 bullet points (dynamic size, efficient insert/delete, no waste, no overflow).

### Problem 2 [2024, CO1, 04 marks]
**Q:** Write pseudocode to reverse a singly linked list. Trace for list: 1 → 2 → 3 → 4.

**Approach:** Write the 3-pointer algorithm → trace table showing PREV, CURR, NEXT at each step.

### Problem 3 [2024, CO2, 03 marks]
**Q:** Discuss advantages of header linked list.

**Approach:** Define header LL → 3 advantages (never empty, metadata, uniform algorithms) → small diagram.

---

*← [02 — Arrays and Matrices](02_arrays_and_matrices.md) | Next: [04 — Stacks →](04_stacks.md)*
