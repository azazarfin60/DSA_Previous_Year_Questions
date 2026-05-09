[⬅️ Previous](./04_stacks.md) | [🏠 Home](./README.md) | [Next ➡️](./06_searching_algorithms.md)

---

# 📘 Chapter 5: Queues

> **Exam Frequency:** 7/8 years | **Typical Marks:** 02–07 | **Section:** A
> **Key Topics:** Queue, Circular Queue, Deque, Priority Queue

---

## 1. What is a Queue?

A **queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle — the element that is inserted first is the first one to be removed.

### Intuition
Think of a **line at a ticket counter**:
- People **join at the back** (REAR) of the line → **Enqueue**
- People **leave from the front** (FRONT) of the line → **Dequeue**
- The person who arrived first gets served first

```
  Enqueue →  ┌────┬────┬────┬────┬────┐  → Dequeue
  (REAR)     │ 50 │ 40 │ 30 │ 20 │ 10 │     (FRONT)
             └────┴────┴────┴────┴────┘
             REAR                 FRONT
```

### Queue vs Stack

| Queue (FIFO) | Stack (LIFO) |
|---|---|
| First in, first out | Last in, first out |
| Two ends (FRONT + REAR) | One end (TOP) |
| Enqueue at REAR, Dequeue at FRONT | Push/Pop at TOP |
| Like a ticket counter line | Like a stack of plates |

---

## 2. Queue ADT

| Component | Specification |
|---|---|
| **Data** | Ordered collection with FRONT and REAR pointers |
| **Operations** | Enqueue, Dequeue, Front/Peek, isEmpty, isFull |
| **Rules** | FIFO — first enqueued is first dequeued |

---

## 3. Queue Operations (Linear Queue)

### 3.1 Array Representation

```
Queue: QUEUE[0..MAXSIZE-1]
FRONT: index of the front element (initially -1)
REAR:  index of the rear element (initially -1)
```

### 3.2 Enqueue (Insert at Rear)

**C++ Style:**
```cpp
void enqueue(int QUEUE[], int& FRONT, int& REAR, int MAXSIZE, int ITEM) {
    if (REAR == MAXSIZE - 1) { // Assuming 0-indexed array
        cout << "OVERFLOW - Queue is full" << endl;
        return;
    }
    if (FRONT == -1) {
        FRONT = 0;
    }
    REAR = REAR + 1;
    QUEUE[REAR] = ITEM;
}
```

**OR, Textbook Style:**
```
Procedure ENQUEUE(QUEUE, FRONT, REAR, MAXSIZE, ITEM)
    // Step 1: Check overflow
    If REAR = MAXSIZE - 1 Then
        Print "OVERFLOW — Queue is full"
        Return
    End If
    
    // Step 2: Handle first insertion
    If FRONT = -1 Then
        Set FRONT = 0
    End If
    
    // Step 3: Insert
    Set REAR = REAR + 1
    Set QUEUE[REAR] = ITEM
End Procedure
```

### 3.3 Dequeue (Remove from Front)

**C++ Style:**
```cpp
int dequeue(int QUEUE[], int& FRONT, int& REAR) {
    if (FRONT == -1 || FRONT > REAR) {
        cout << "UNDERFLOW - Queue is empty" << endl;
        return -1;
    }
    
    int ITEM = QUEUE[FRONT];
    FRONT = FRONT + 1;
    
    // Reset if queue becomes empty
    if (FRONT > REAR) {
        FRONT = -1;
        REAR = -1;
    }
    
    return ITEM;
}
```

**OR, Textbook Style:**
```
Procedure DEQUEUE(QUEUE, FRONT, REAR)
    // Step 1: Check underflow
    If FRONT = -1 OR FRONT > REAR Then
        Print "UNDERFLOW — Queue is empty"
        Return
    End If
    
    // Step 2: Remove and advance
    Set ITEM = QUEUE[FRONT]
    Set FRONT = FRONT + 1
    
    // Step 3: Reset if queue becomes empty
    If FRONT > REAR Then
        Set FRONT = -1
        Set REAR = -1
    End If
    
    Return ITEM
End Procedure
```

### 3.4 Trace Example

```
Initial: FRONT = -1, REAR = -1, QUEUE = [_, _, _, _, _] (size 5)

ENQUEUE(10): FRONT=0, REAR=0   → [10, _, _, _, _]
ENQUEUE(20): FRONT=0, REAR=1   → [10, 20, _, _, _]
ENQUEUE(30): FRONT=0, REAR=2   → [10, 20, 30, _, _]
DEQUEUE():   Returns 10, FRONT=1 → [_, 20, 30, _, _]
DEQUEUE():   Returns 20, FRONT=2 → [_, _, 30, _, _]
ENQUEUE(40): FRONT=2, REAR=3   → [_, _, 30, 40, _]
ENQUEUE(50): FRONT=2, REAR=4   → [_, _, 30, 40, 50]
ENQUEUE(60): OVERFLOW! (REAR=4=MAXSIZE-1)

But wait — positions 0 and 1 are empty! This is wasted space!
```

### The Problem with Linear Queue
After several enqueue/dequeue operations, FRONT moves forward, leaving **wasted space** at the beginning. Even though there ARE empty slots, the queue reports "OVERFLOW" because REAR has reached the end. This is the **major drawback** of a linear queue.

**Solution:** Circular Queue.

---

## 4. Circular Queue

### 4.1 Concept

A **circular queue** treats the array as if it were **circular** — when REAR reaches the end of the array, it wraps around to the beginning (if there's space). Similarly, FRONT wraps around.

### Intuition
Think of people sitting around a **circular dining table**. When someone leaves, the next person doesn't have to shift — you just move the "front" marker around the circle. There's no "end" of the table — it wraps around.

```
          ┌────┐
       ┌──│ 40 │──┐
    ┌──┤  └────┘  ├──┐
    │  │          │  │
  ┌────┐        ┌────┐
  │ 30 │        │ 50 │
  └────┘        └────┘
    │  │          │  │
    └──┤  ┌────┐  ├──┘
       └──│ __ │──┘
          └────┘
    FRONT →  30         REAR → 50
```

### 4.2 Key Formula: Wrap-Around Using Modulo

```
REAR = (REAR + 1) % MAXSIZE
FRONT = (FRONT + 1) % MAXSIZE
```

The `%` (modulo) operator makes the index wrap around:
- If MAXSIZE = 5: after index 4, next is (4+1)%5 = 0 (wrap to beginning)

### 4.3 Circular Queue Operations

**Enqueue:**
**C++ Style:**
```cpp
void cqEnqueue(int QUEUE[], int& FRONT, int& REAR, int MAXSIZE, int ITEM) {
    // Check if full
    if ((REAR + 1) % MAXSIZE == FRONT) {
        cout << "OVERFLOW - Queue is full" << endl;
        return;
    }
    
    // First insertion
    if (FRONT == -1) {
        FRONT = 0;
        REAR = 0;
    } else {
        REAR = (REAR + 1) % MAXSIZE; // wrap around
    }
    
    QUEUE[REAR] = ITEM;
}
```

**OR, Textbook Style:**
```
Procedure CQ_ENQUEUE(QUEUE, FRONT, REAR, MAXSIZE, ITEM)
    // Check if full
    If (REAR + 1) % MAXSIZE = FRONT Then
        Print "OVERFLOW — Queue is full"
        Return
    End If
    
    // First insertion
    If FRONT = -1 Then
        Set FRONT = 0
        Set REAR = 0
    Else
        Set REAR = (REAR + 1) % MAXSIZE     // wrap around
    End If
    
    Set QUEUE[REAR] = ITEM
End Procedure
```

**Dequeue:**
**C++ Style:**
```cpp
int cqDequeue(int QUEUE[], int& FRONT, int& REAR, int MAXSIZE) {
    // Check if empty
    if (FRONT == -1) {
        cout << "UNDERFLOW - Queue is empty" << endl;
        return -1;
    }
    
    int ITEM = QUEUE[FRONT];
    
    // If only one element was left
    if (FRONT == REAR) {
        FRONT = -1;
        REAR = -1;
    } else {
        FRONT = (FRONT + 1) % MAXSIZE; // wrap around
    }
    
    return ITEM;
}
```

**OR, Textbook Style:**
```
Procedure CQ_DEQUEUE(QUEUE, FRONT, REAR, MAXSIZE)
    // Check if empty
    If FRONT = -1 Then
        Print "UNDERFLOW — Queue is empty"
        Return
    End If
    
    Set ITEM = QUEUE[FRONT]
    
    // If only one element was left
    If FRONT = REAR Then
        Set FRONT = -1
        Set REAR = -1
    Else
        Set FRONT = (FRONT + 1) % MAXSIZE   // wrap around
    End If
    
    Return ITEM
End Procedure
```

### 4.4 Trace Example (MAXSIZE = 5)

```
ENQUEUE(10): F=0, R=0  → [10,  _,  _,  _,  _]
ENQUEUE(20): F=0, R=1  → [10, 20,  _,  _,  _]
ENQUEUE(30): F=0, R=2  → [10, 20, 30,  _,  _]
ENQUEUE(40): F=0, R=3  → [10, 20, 30, 40,  _]
DEQUEUE():   F=1, R=3  → [ _, 20, 30, 40,  _]   Returns 10
DEQUEUE():   F=2, R=3  → [ _,  _, 30, 40,  _]   Returns 20
ENQUEUE(50): F=2, R=4  → [ _,  _, 30, 40, 50]
ENQUEUE(60): F=2, R=0  → [60,  _, 30, 40, 50]   ← WRAPPED AROUND!
ENQUEUE(70): F=2, R=1  → [60, 70, 30, 40, 50]
ENQUEUE(80): (R+1)%5 = 2 = FRONT → OVERFLOW!    (Queue truly full now)
```

Notice how element 60 was placed at index 0 (wrapped around) — this is the power of circular queue. No wasted space!

### 4.5 Linear vs Circular Queue

| Criterion | Linear Queue | Circular Queue |
|---|---|---|
| Memory usage | Wastes space after dequeues | Reuses freed space |
| Full condition | REAR = MAXSIZE - 1 | (REAR+1) % MAX = FRONT |
| Empty condition | FRONT > REAR or FRONT = -1 | FRONT = -1 |
| Wrap-around | No | Yes (using modulo) |
| Practical use | Rarely used (wasteful) | Standard implementation |

---

## 5. Deque (Double-Ended Queue)

### 5.1 Definition
A **deque** (pronounced "deck") is a generalized queue that allows insertion and deletion at **both ends** — front and rear.

```
  ← Insert/Delete    ┌────┬────┬────┬────┐    Insert/Delete →
     (FRONT)          │ 10 │ 20 │ 30 │ 40 │       (REAR)
                      └────┴────┴────┴────┘
```

### 5.2 Types of Deque

| Type | Operations Allowed |
|---|---|
| **Input-Restricted Deque** | Insert at REAR only; Delete from BOTH ends |
| **Output-Restricted Deque** | Insert at BOTH ends; Delete from FRONT only |
| **General Deque** | Insert and Delete from BOTH ends |

### 5.3 Operations

```
InsertFront(ITEM)     — Add ITEM at front
InsertRear(ITEM)      — Add ITEM at rear  
DeleteFront()         — Remove from front
DeleteRear()          — Remove from rear
```

### 5.4 Deque as a Superset
A deque can function as:
- **Stack** — if we only insert and delete from one end (say REAR)
- **Queue** — if we insert at REAR and delete from FRONT

---

## 6. Priority Queue

### 6.1 Definition
A **priority queue** is a queue where each element has a **priority** associated with it. Elements are dequeued based on **priority, not insertion order**.

- **Higher priority** elements are served before lower priority ones
- Among elements with **equal priority**, FIFO order is maintained

### Intuition
Think of an **emergency room**. A patient with a heart attack (high priority) gets treated before someone with a sprained ankle (low priority), even if the ankle patient arrived first.

### 6.2 Types

| Type | Rule |
|---|---|
| **Ascending Priority Queue** | Smallest value = highest priority (dequeue minimum) |
| **Descending Priority Queue** | Largest value = highest priority (dequeue maximum) |

### 6.3 Implementation Methods

| Method | Enqueue | Dequeue | Best For |
|---|---|---|---|
| **Unsorted Array** | O(1) | O(n) — scan for min/max | Few dequeues |
| **Sorted Array** | O(n) — insert in order | O(1) — front/rear | Few enqueues |
| **Heap** | O(log n) | O(log n) | **Best general case** |
| **Linked List** | O(n) — insert in order | O(1) | Small queues |

### 6.4 Array-Based Priority Queue

**Using sorted array (ascending — min at front):**

```
Insert 30: [30]
Insert 10: [10, 30]         ← inserted in sorted position
Insert 20: [10, 20, 30]     ← inserted in sorted position
Insert 5:  [5, 10, 20, 30]  ← inserted at front

Dequeue: Remove 5 (minimum priority value = highest priority)
        [10, 20, 30]
```

### 6.5 Priority Queue Using 2D Array

In exams (especially 2017, 2018), priority queues have been asked using a **2D array** representation where each row represents a different priority level.

```
Priority Queue with 3 priority levels (1=highest, 3=lowest):

Priority 1: [Job_A, Job_D]        ← served first
Priority 2: [Job_B]               ← served second
Priority 3: [Job_C, Job_E, Job_F] ← served last

2D Array:
  QUEUE[1] = [Job_A, Job_D]   FRONT[1]=0, REAR[1]=1
  QUEUE[2] = [Job_B]          FRONT[2]=0, REAR[2]=0
  QUEUE[3] = [Job_C, Job_E, Job_F]  FRONT[3]=0, REAR[3]=2
```

**Dequeue Logic:**
1. Check priority 1 queue first — if not empty, dequeue from it
2. If empty, check priority 2 queue
3. If empty, check priority 3 queue
4. If all empty → UNDERFLOW

**Enqueue Logic:**
Insert into the queue corresponding to the element's priority level.

### 6.6 C Pseudocode for 2D Priority Queue

```c
#define PRIORITIES 3
#define MAX_SIZE 10

int queue[PRIORITIES][MAX_SIZE];
int front[PRIORITIES], rear[PRIORITIES];

void enqueue(int item, int priority) {
    // priority: 0 = highest, PRIORITIES-1 = lowest
    if (rear[priority] == MAX_SIZE - 1) {
        printf("Overflow at priority %d\n", priority);
        return;
    }
    if (front[priority] == -1)
        front[priority] = 0;
    queue[priority][++rear[priority]] = item;
}

int dequeue() {
    int i;
    for (i = 0; i < PRIORITIES; i++) {        // check highest priority first
        if (front[i] != -1 && front[i] <= rear[i]) {
            int item = queue[i][front[i]++];
            if (front[i] > rear[i]) {         // queue at this level empty
                front[i] = -1;
                rear[i] = -1;
            }
            return item;
        }
    }
    printf("Underflow — all queues empty\n");
    return -1;
}
```

---

## 7. Applications of Queues

| Application | Queue Type | Why Queue? |
|---|---|---|
| **CPU scheduling** | Queue/Priority Queue | Processes served in order of arrival/priority |
| **Print spooling** | Queue | Documents printed in submission order |
| **BFS traversal** | Queue | Visit nodes level by level |
| **Keyboard buffer** | Queue | Keystrokes processed in order typed |
| **Call center** | Priority Queue | VIP customers served first |
| **Disk scheduling** | Circular Queue | Head cycles through requests |

---

## 8. Exam-Ready Summary

### Quick Revision Points
1. **Queue** = FIFO, FRONT (dequeue) + REAR (enqueue)
2. **Linear Queue** has wasted space problem → use **Circular Queue** with `(index + 1) % MAXSIZE`
3. **Circular Queue full:** `(REAR + 1) % MAX = FRONT`
4. **Deque** = insert/delete from both ends
5. **Priority Queue** = dequeue by priority, not arrival order
6. **Best PQ implementation** = Heap (O(log n) for both insert and delete)
7. **PQ with 2D array** = each row is a separate queue for that priority level

### Most Common Exam Questions
- Queue ENQUEUE/DEQUEUE operations with trace (02–04 marks)
- Priority Queue using 2D array (06–07 marks — 2017, 2018)
- Circular Queue concept and operations (03–04 marks)
- Deque definition and types (02–03 marks)

---

## 9. Practice Problems (From Past Exams)

### Problem 1 [2017, 06 marks]
**Q:** Implement a priority queue using a 2D array. Show insert and delete operations.

**Approach:** Define 2D array with rows = priority levels → show enqueue with priority → dequeue by checking highest priority row first.

### Problem 2 [2018, 07 marks]
**Q:** Priority Queue insert and delete operations.

**Approach:** Same as 2017 — draw the 2D array, trace insertions at different priority levels, show dequeue order.

### Problem 3 [Typical 03 marks]
**Q:** Differentiate between linear queue and circular queue.

**Approach:** 4–5 row comparison table covering memory usage, full condition, wrap-around, and practical use.

---

*← [04 — Stacks](04_stacks.md) | Next: [06 — Searching Algorithms →](06_searching_algorithms.md)*

<br>

---
[⬅️ Previous](./04_stacks.md) | [🏠 Home](./README.md) | [Next ➡️](./06_searching_algorithms.md)
