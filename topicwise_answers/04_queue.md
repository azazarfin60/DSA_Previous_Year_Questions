[⬅️ Previous](./03_stack_applications.md) | [🏠 Home](./README.md) | [Next ➡️](./05_bst.md)

---

# Queue — Queue, Priority Queue, Dequeue, Circular Queue


---

## [2017] 3(b) Priority Queue operations. (06)

**Initial State:**
- Queue 1: empty (F=0, R=0)
- Queue 2: DD, UU, GG (F=2, R=4)
- Queue 3: FF (F=1, R=1)
- Queue 4: RR, SS, CC, _, XX, EE (F=5, R=3, wraps around)
- Queue 5: TT (F=4, R=4)

**(i) Delete two elements (deletion is by priority — lowest queue number first):**

Delete 1: Queue 1 is empty → Queue 2: delete DD (Front 2→3)
Delete 2: Queue 2: delete UU (Front 3→4)

After deletion:

| Queue | Front | Rear | Elements |
|---|---|---|---|
| 1 | 0 | 0 | (empty) |
| 2 | 4 | 4 | GG |
| 3 | 1 | 1 | FF |
| 4 | 5 | 3 | XX, EE, RR, SS, CC |
| 5 | 4 | 4 | TT |

**(ii) Insert (AA,3), (BB,1), (LL,4), (MM,5):**

- AA → Queue 3: add after FF → R becomes 2
- BB → Queue 1: first element → F=1, R=1
- LL → Queue 4: add after CC → R becomes 4
- MM → Queue 5: add after TT → R becomes 5

| Queue | Front | Rear | Elements |
|---|---|---|---|
| 1 | 1 | 1 | BB |
| 2 | 4 | 4 | GG |
| 3 | 1 | 2 | FF, AA |
| 4 | 5 | 4 | XX, EE, RR, SS, CC, LL |
| 5 | 4 | 5 | TT, MM |

**(iii) Delete five elements (by priority):**

1. Delete BB from Queue 1 (now empty, F=0, R=0)
2. Delete GG from Queue 2 (now empty, F=0, R=0)
3. Delete FF from Queue 3 (F becomes 2)
4. Delete AA from Queue 3 (now empty, F=0, R=0)
5. Delete XX from Queue 4 (F becomes 6)

| Queue | Front | Rear | Elements |
|---|---|---|---|
| 1 | 0 | 0 | (empty) |
| 2 | 0 | 0 | (empty) |
| 3 | 0 | 0 | (empty) |
| 4 | 6 | 4 | EE, RR, SS, CC, LL |
| 5 | 4 | 5 | TT, MM |

---


---

## [2018] Q6(a) Define (i) Queue (ii) Priority Queue (iii) Circular Queue. (03)

**(i) Queue:** A linear data structure following **FIFO** (First In First Out) principle. Elements are inserted at REAR and deleted from FRONT.
Example: Queue = [A, B, C] → Delete returns A, Insert D gives [B, C, D]

**(ii) Priority Queue:** A queue where each element has a **priority**. Element with the highest priority is dequeued first, regardless of insertion order.
Example: Emergency room — critical patients served before minor cases.

**(iii) Circular Queue:** A queue where the last position connects back to the first position, forming a circle. This prevents the "false overflow" problem of linear queues.
Example: FRONT=4, REAR=1 in a 5-element array — wraps around.

---


---

## [2018] Q6(c) How does queue differ from array? (02)

| Criterion | Queue | Array |
|---|---|---|
| Access | FIFO — only front and rear | Random access by index |
| Operations | Enqueue (rear), Dequeue (front) | Insert/delete anywhere |
| Flexibility | Restricted access | Unrestricted access |
| Use case | Scheduling, BFS | General storage |

A queue is a **restricted** data structure — elements can only be added at one end and removed from the other. An array allows access to any element at any index.

---


---

## [2019] Q.2(c) Circular Queue with example and advantages. (04)

**Circular Queue:** A linear queue where the last position connects back to the first position, forming a circle. When REAR reaches the end, it wraps around to the beginning if space is available.

**Example:** Circular queue of size 5:
```
Initial:    FRONT = -1, REAR = -1
Insert A:   [A, _, _, _, _]   F=0, R=0
Insert B:   [A, B, _, _, _]   F=0, R=1
Insert C:   [A, B, C, _, _]   F=0, R=2
Delete:     [_, B, C, _, _]   F=1, R=2
Insert D:   [_, B, C, D, _]   F=1, R=3
Insert E:   [_, B, C, D, E]   F=1, R=4
Insert F:   [F, B, C, D, E]   F=1, R=0  ← wraps around!
```

**Formula:** REAR = (REAR + 1) mod SIZE

**Advantages:**
1. **No wasted space** — linear queue wastes space after deletions (FRONT moves forward). Circular queue reuses freed positions.
2. **Efficient memory utilization** — eliminates "false overflow" where queue appears full but has empty slots at the beginning.
3. **Constant time** operations — O(1) for both enqueue and dequeue.

---


---

## [2020] Q.3(c) Queue operations: 3 dequeue + 2 enqueue. (04)

**Initial Queue:** [10, 5, 7, 8, 9, 11, 12] (FRONT=10, REAR=12)

**Dequeue 3 times:**
1. Remove 10 → [5, 7, 8, 9, 11, 12]
2. Remove 5 → [7, 8, 9, 11, 12]
3. Remove 7 → [8, 9, 11, 12]

**Enqueue 11, 12:**
4. Add 11 → [8, 9, 11, 12, 11]
5. Add 12 → [8, 9, 11, 12, 11, 12]

> **Final Queue: [8, 9, 11, 12, 11, 12]** (FRONT=8, REAR=12)

---


---

## [2021] Q.3(b) Queue operations. (04)

**Initial Queue:** [10, 20, 30, 40] (FRONT=10, REAR=40)

**Dequeue 2 times:**
1. Remove 10 → [20, 30, 40]
2. Remove 20 → [30, 40]

**Enqueue 5, 15, 25:**
3. Add 5 → [30, 40, 5]
4. Add 15 → [30, 40, 5, 15]
5. Add 25 → [30, 40, 5, 15, 25]

**Dequeue 4 times:**
6. Remove 30 → [40, 5, 15, 25]
7. Remove 40 → [5, 15, 25]
8. Remove 5 → [15, 25]
9. Remove 15 → [25]

> **Final Queue: [25]**

---


---

## [2021] Q.3(c) Priority Queue — array and heap representation. (04)

**Given:** AAA|1, BBB|2, CCC|2, DDD|4, EEE|4, FFF|4, GGG|5

**Array Representation (one array per priority level):**
```
Priority 1: [AAA]
Priority 2: [BBB, CCC]
Priority 3: (empty)
Priority 4: [DDD, EEE, FFF]
Priority 5: [GGG]
```

**Disadvantages of array:**
1. Wasted space for empty priority levels
2. Fixed size — cannot dynamically add elements
3. Deletion from front requires shifting elements O(n)

**Heap Representation (Min-Heap by priority):**
```
         AAA|1
        /     \
    BBB|2     CCC|2
    /   \     /   \
 DDD|4 EEE|4 FFF|4 GGG|5
```

**Advantages of heap:**
1. Insert: O(log n) — add at end, bubble up
2. Delete-min: O(log n) — remove root, heapify down
3. No wasted space — compact array representation
4. Much faster than array's O(n) for deletions

---


---

## [2022] Q.2(b) Dequeue operations. (CO1, 03)

**Initial:** Dequeue: [_, A, C, D, _, _], left=2, right=4, size=6

**(i) F added to right:**
right = (4+1) mod 6 = 5 → Dequeue[5] = F
→ [_, A, C, D, F, _], left=2, right=5

**(ii) Two letters deleted from right:**
Delete Dequeue[5] = F, right = 4
Delete Dequeue[4] = D, right = 3
→ [_, A, C, _, _, _], left=2, right=3

**(iii) K, L, M added to left:**
Add K: left = (2-1) mod 6 = 1 → Dequeue[1] = K
→ [_, K, A, C, _, _], left=1, right=3... 

Actually left moves backward: left = left - 1.
Add K: left = 2-1 = 1 → Dequeue[1] = K, left=1
Add L: left = 1-1 = 0 → Dequeue[0] = L, left=0
Add M: left = 0-1 = 5 (wrap) → Dequeue[5] = M, left=5

→ **[L, K, A, C, _, M]**, left=5, right=3

---


---

## [2022] Q.3(c) Implement stack using two queues. (CO2, 04)

**Approach: Make PUSH costly**

```
// Use two queues: Q1 (main), Q2 (helper)

Procedure PUSH(ITEM)
    Enqueue ITEM into Q2
    While Q1 is not empty do
        Enqueue DEQUEUE(Q1) into Q2
    End While
    Swap Q1 and Q2              // Q1 now has newest on front
End Procedure

Procedure POP()
    If Q1 is empty Then
        Print "Stack Underflow"
        Return
    End If
    Return DEQUEUE(Q1)
End Procedure
```

**Example:** Push 1, 2, 3:
- Push 1: Q2=[1], Q1=[] → swap → Q1=[1]
- Push 2: Q2=[2], move Q1→Q2: Q2=[2,1] → swap → Q1=[2,1]
- Push 3: Q2=[3], move Q1→Q2: Q2=[3,2,1] → swap → Q1=[3,2,1]
- Pop: returns 3 ✓ (LIFO)

**Time:** PUSH = O(n), POP = O(1)

---


---

## [2022] Q.7(c) Two applications of priority queue. (CO1, 02)

1. **Dijkstra's Algorithm** — uses a min-priority queue to always process the vertex with the smallest tentative distance next.

2. **CPU Scheduling** — operating systems use priority queues to schedule processes; higher-priority processes are executed before lower-priority ones.

---


---

## [2023] Q.3(a) Deque operations. LEFT=7, RIGHT=2, size=8. (CLO3, 03)

**Initial:** [ _ | _ | yy | zz | _ | _ | ww | xx ] (indices 0–7), LEFT=7, RIGHT=2

Occupied: index 7=ww, 0=xx, 1=yy, 2=zz. Wait — LEFT=7 means leftmost is at 7.
Reading left to right (circular): ww(7), xx(0), yy(1), zz(2)

**(i) Add "FF" to right:** RIGHT = (2+1) mod 8 = 3
→ [ xx | yy | zz | FF | _ | _ | _ | ww ], LEFT=7, RIGHT=3

**(ii) Add "KK" and "LL" to left:**
KK: LEFT = (7-1) mod 8 = 6 → index 6 = KK, LEFT=6
LL: LEFT = (6-1) mod 8 = 5 → index 5 = LL, LEFT=5
→ [ xx | yy | zz | FF | _ | LL | KK | ww ], LEFT=5, RIGHT=3

**(iii) Delete one from left:**
Remove index 5 (LL), LEFT = (5+1) mod 8 = 6
→ [ xx | yy | zz | FF | _ | _ | KK | ww ], LEFT=6, RIGHT=3

---


---

## 📊 Exam Priority
**Priority: 2/5** (Should Prepare)
**Appeared in:** 7/8 years
**Typical marks:** 02–07 per question

<br>

---
[⬅️ Previous](./03_stack_applications.md) | [🏠 Home](./README.md) | [Next ➡️](./05_bst.md)
