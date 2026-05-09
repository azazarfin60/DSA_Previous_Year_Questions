[⬅️ Previous](./01_ds_definitions.md) | [🏠 Home](./README.md) | [Next ➡️](./03_stack_applications.md)

---

# Linked List — Operations, Types, vs Array


---

## [2017] 2(a) What is garbage collection? Memory representation of linked list. Difference from array. (04)

**Garbage Collection:** The process of automatically collecting and reclaiming unused memory cells (nodes that are no longer referenced by any pointer) and returning them to the AVAIL (free space) list for future use.

**Memory Representation of Linked List:**
A linked list is stored using two parallel arrays:
- **INFO[ ]** — stores the actual data
- **LINK[ ]** — stores the index of the next node

Two special pointers:
- **START** — points to the first node
- **AVAIL** — points to the first free (available) node

```
Index:  1    2    3    4    5
INFO:  [40] [30] [ ] [10] [20]
LINK:  [ 5] [ 1] [—] [ 2] [ 0]
START = 4,  AVAIL = 3
```
Traversal: 4→10, 2→30, 1→40, 5→20, 0(end)

**Differences from Array:**

| Criterion | Linked List | Array |
|---|---|---|
| Memory | Dynamic, non-contiguous | Static, contiguous |
| Size | Can grow/shrink | Fixed at declaration |
| Access | Sequential O(n) | Random access O(1) |
| Insert/Delete | O(1) pointer change | O(n) shifting needed |

---


---

## [2017] 2(b) Linked List CGPA ordering and insertion. (04)

**Given:** INFO = {3.80, 3.95, _, 3.90, _}, START and AVAIL pointers.

**i) Linking in descending order of CGPA (3.95 → 3.90 → 3.80):**

| Index | INFO | LINK |
|---|---|---|
| 1 | 3.80 | 0 (end) |
| 2 | 3.95 | 4 |
| 3 | — | 5 |
| 4 | 3.90 | 1 |
| 5 | — | 0 |

**START = 2**, AVAIL = 3

Traversal: 2(3.95) → 4(3.90) → 1(3.80) → end ✓

**ii) Insert 4.00 (should become the first element since 4.00 > 3.95):**

Take node from AVAIL: index 3. New AVAIL = 5.

| Index | INFO | LINK |
|---|---|---|
| 1 | 3.80 | 0 |
| 2 | 3.95 | 4 |
| 3 | **4.00** | **2** |
| 4 | 3.90 | 1 |
| 5 | — | 0 |

**START = 3**, AVAIL = 5

Traversal: 3(4.00) → 2(3.95) → 4(3.90) → 1(3.80) → end ✓

---


---

## [2017] 8(c) Advantages of Header node in Header linked list. (04)

A **Header Linked List** is a linked list that has a special node at the beginning called the **header node**. This node does not store actual data but serves as a permanent first node.

**Advantages:**

1. **Simplified Insertion/Deletion:** The header node ensures the list is never truly empty (START always points to header). This eliminates special-case handling for inserting/deleting the first element.

2. **Storing Metadata:** The header node can store useful information like the total number of nodes, making operations like counting O(1) instead of O(n).

3. **Uniform Operations:** Without a header, inserting at the beginning requires updating the START pointer. With a header, all insertions happen after some node, making the algorithm uniform.

4. **Circular List Support:** In a grounded header list, the last node's LINK = NULL. In a circular header list, the last node's LINK points back to the header, making circular traversal easy.

**Example:**
```
Header → [count=3] → [10] → [20] → [30] → NULL
```
Without header: inserting before 10 requires changing START.
With header: insert after header — no pointer change needed for START.

---

## [2023] Q.4(a) C function to split linked list at point loc. (CLO4, 04)

**C++ Style:**
```cpp
void splitList(Node* inList, int loc, Node*& outList1, Node*& outList2) {
    outList1 = inList;
    Node* PTR = inList;
    int COUNT = 1;

    // Traverse to the loc-th node
    while (COUNT < loc && PTR != nullptr) {
        PTR = PTR->link;
        COUNT++;
    }

    if (PTR != nullptr) {
        outList2 = PTR->link;       // second list starts after loc
        PTR->link = nullptr;        // terminate first list
    } else {
        outList2 = nullptr;
    }
}
```

**OR, Textbook Style:**
```
Procedure SPLIT_LIST(inList, loc, outList1, outList2)
    // Split inList into outList1 (first loc nodes) and outList2 (rest)
    Set outList1 = inList
    Set PTR = inList
    Set COUNT = 1

    // Traverse to the loc-th node
    While COUNT < loc AND PTR ≠ NULL do
        Set PREV = PTR
        Set PTR = NEXT[PTR]
        Set COUNT = COUNT + 1
    End While

    // PTR is now at loc-th node
    Set outList2 = NEXT[PTR]       // second list starts after loc
    Set NEXT[PTR] = NULL            // terminate first list
End Procedure
```

**Example:** inList = (10→20→30→40→50), loc=3
- Traverse to 3rd node (30)
- outList1 = 10→20→30→NULL
- outList2 = 40→50→NULL ✓

---


---

## [2024] Q.2(a) Define linked list. Benefits over array. (CO2, 03)

**Linked List:** A linear data structure where elements (nodes) are stored in non-contiguous memory locations. Each node contains DATA and a LINK (pointer) to the next node.

**Benefits over Array:**
1. **Dynamic size** — grows/shrinks at runtime, no fixed size declaration
2. **Efficient insert/delete** — O(1) pointer update after reaching position, vs O(n) shifting in arrays
3. **No wasted memory** — allocates exactly what is needed
4. **No overflow** — can add nodes as long as memory exists

---


---

## [2024] Q.2(c) Insert into linked list after LOC. (CO2, 03)

**C++ Style:**
```cpp
void insertAfter(Node* START, Node* LOC, int ITEM) {
    if (LOC == nullptr) {
        cout << "Location cannot be NULL" << endl;
        return;
    }
    Node* NEW = new Node;              // dynamically allocate new node
    NEW->data = ITEM;                  // store data
    NEW->link = LOC->link;             // new node points to LOC's next
    LOC->link = NEW;                   // LOC now points to new node
}
```

**OR, Textbook Style:**
```
Procedure INSERT_AFTER(START, LOC, ITEM, AVAIL)
    If AVAIL = NULL Then
        Print "Overflow"
        Return
    End If
    Set NEW = AVAIL                    // get free node
    Set AVAIL = LINK[AVAIL]            // update free list
    Set INFO[NEW] = ITEM               // store data
    Set LINK[NEW] = LINK[LOC]          // point to LOC's next
    Set LINK[LOC] = NEW                // LOC now points to NEW
End Procedure
```

**Example:** Insert 25 after node containing 20:
```
Before: [10] → [20] → [30] → NULL
After:  [10] → [20] → [25] → [30] → NULL
```

---


---

## [2024] Q.6(b) Reverse a singly linked list. (CO1, 04)

**C++ Style:**
```cpp
Node* reverseList(Node* HEAD) {
    Node* PREV = nullptr;
    Node* CURR = HEAD;
    while (CURR != nullptr) {
        Node* NEXT_NODE = CURR->link;  // save next
        CURR->link = PREV;             // reverse pointer
        PREV = CURR;                   // advance PREV
        CURR = NEXT_NODE;              // advance CURR
    }
    HEAD = PREV;                       // new head
    return HEAD;
}
```

**OR, Textbook Style:**
```
Procedure REVERSE_LIST(HEAD)
    Set PREV = NULL
    Set CURR = HEAD
    While CURR ≠ NULL do
        Set NEXT_NODE = LINK[CURR]     // save next
        Set LINK[CURR] = PREV          // reverse pointer
        Set PREV = CURR                // advance PREV
        Set CURR = NEXT_NODE           // advance CURR
    End While
    Set HEAD = PREV                    // new head
    Return HEAD
End Procedure
```

**Trace:** 1 → 2 → 3 → 4 → NULL

| Step | PREV | CURR | NEXT | List State |
|---|---|---|---|---|
| 1 | NULL | 1 | 2 | NULL ← 1, 2→3→4 |
| 2 | 1 | 2 | 3 | NULL ← 1 ← 2, 3→4 |
| 3 | 2 | 3 | 4 | NULL ← 1 ← 2 ← 3, 4 |
| 4 | 3 | 4 | NULL | NULL ← 1 ← 2 ← 3 ← 4 |
| End | 4 | NULL | — | HEAD = 4 |

> **Output: 4 → 3 → 2 → 1 → NULL** ✓
> **Time: O(n), Space: O(1)**

---


---

## [2024] Q.7(c) Advantages of Header linked list. (CO2, 03)

A **Header Linked List** has a special node at the beginning (header node) that doesn't store actual data.

**Advantages:**

1. **Simplified operations** — list is never empty (START always points to header). No special case for inserting/deleting the first element.

2. **Metadata storage** — header can store count of nodes, making length queries O(1).

3. **Uniform algorithms** — all insertions happen after some node, no need to update START pointer.

**Example:**
```
Header → [count=3] → [10] → [20] → [30] → NULL
```
Insert 5 at beginning: just insert after header node — no START pointer change.

---


---

## [2024] Q.8(b) Two-way vs singly linked list. (CO3, 03)

| Criterion | Singly Linked List | Doubly Linked List |
|---|---|---|
| Pointers per node | 1 (NEXT only) | 2 (NEXT + PREV) |
| Traversal | Forward only | Both directions |
| Delete given node | O(n) — need predecessor | **O(1)** — PREV available |
| Memory | Less per node | More per node |
| Insertion before node | O(n) | **O(1)** |
| Complexity | Simpler | More complex |

**Example:**
```
Singly: [10|→] → [20|→] → [30|NULL]

Doubly: [NULL←|10|→] ↔ [←|20|→] ↔ [←|30|NULL→]
```

In doubly linked list, deleting node 20 requires only updating 10's NEXT and 30's PREV — O(1).

---


---

## 📊 Exam Priority
**Priority: 1/5** (Must Prepare)
**Appeared in:** 5/8 years
**Typical marks:** 02–04 per question

<br>

---
[⬅️ Previous](./01_ds_definitions.md) | [🏠 Home](./README.md) | [Next ➡️](./03_stack_applications.md)
