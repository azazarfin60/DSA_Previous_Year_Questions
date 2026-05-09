[⬅️ Previous](./05_bst.md) | [🏠 Home](./README.md) | [Next ➡️](./07_sorting.md)

---

# Heap — Min/Max Heap Build, Insert, Delete


---

## [2017] 6(c) Insert 80, 75 into Max Heap. (03)

**Initial Heap:**
```
       100
      /   \
    50     70
   / \    /
  40  45  60
```

**Step 1: Insert 80** — Place at next position (right child of 70), then bubble up.
- 80 > 70 → swap 80 and 70

```
       100
      /   \
    50     80
   / \    / \
  40  45 60  70
```

**Step 2: Insert 75** — Place at next position (left child of 40), then bubble up.
- 75 > 40 → swap
- 75 > 50 → swap

```
        100
       /    \
     75      80
    / \     / \
   50  45  60  70
  /
 40
```

---


---

## [2018] Q4(a) Insert 80, 75 into Max Heap. (04)

**Initial Heap:**
```
       100
      /   \
    50     70
   / \    /
  40  45  60
```

**Insert 80:** Place at next available position (right of 70), bubble up.
- 80 > 70 → swap

```
       100
      /   \
    50     80
   / \    / \
  40  45 60  70
```

**Insert 75:** Place at next position (left child of 40), bubble up.
- 75 > 40 → swap
- 75 > 50 → swap

```
        100
       /    \
     75      80
    / \     / \
   50  45  60  70
  /
 40
```

---


---

## [2019] Q.3(b) Build minheap from: 44, 30, 50, 22, 60, 55, 77, 55. (04)

**Insert elements one by one, bubble up after each:**

**Insert 44:** Root = 44
**Insert 30:** 30 < 44 → swap
```
    30
   /
  44
```
**Insert 50:** 50 > 30 → no swap
```
    30
   /  \
  44   50
```
**Insert 22:** 22 < 44 → swap, 22 < 30 → swap
```
      22
     /  \
    30   50
   /
  44
```
**Insert 60:** 60 > 30 → no swap
```
      22
     /  \
    30   50
   / \
  44  60
```
**Insert 55:** 55 > 50 → no swap
```
      22
     /  \
    30   50
   / \  /
  44 60 55
```
**Insert 77:** 77 > 50 → no swap
```
       22
      /  \
    30    50
   / \   / \
  44 60 55  77
```
**Insert 55:** 55 > 44 → no swap (placed as left child of 44... wait, 55 > 44 so stays)
Actually: next position is left child of 44. 55 > 44 → no swap needed.
```
         22
        /  \
      30    50
     / \   / \
    44  60 55  77
   /
  55
```

> **Final Min-Heap: [22, 30, 50, 44, 60, 55, 77, 55]**

---


---

## [2021] Q.5(a) Insert 11 into min heap. (03)

**Initial Min Heap:** [8, 22, 33, 25, 44, 40, 55, 55, 33]

```
          8
        /   \
      22     33
     / \    /  \
    25  44 40  55
   / \
  55  33
```

**Insert 11:** Place at next position (left child of 44, index 10), then bubble up.

- 11 < 44 → swap with 44
- 11 < 22 → swap with 22

```
          8
        /   \
      11     33
     / \    /  \
    25  22 40  55
   / \  /
  55 33 44
```

> **Result: [8, 11, 33, 25, 22, 40, 55, 55, 33, 44]**

---


---

## [2021] Q.8(c) Insert 90 into two heaps. (04)

**(i) Max Heap — Insert 90:**

Initial:
```
        910
       /   \
     77     66
    / \    / \
   68  1  33  11
```

Insert 90 at next position (left child of 68). Bubble up:
- 90 > 68 → swap
- 90 > 77 → swap... wait, 90 < 910 → stop

Actually: 90 > 68 → swap. Now 90 is at 77's left child. 90 > 77 → swap.

```
        910
       /   \
     90     66
    / \    / \
   77  1  33  11
  /
 68
```

**(ii) Min Heap — Insert 90:**

Initial:
```
      70
     /  \
    60   40
   / \   /
  50  55 20
```

Insert 90 at next position (right child of 40). Bubble up:
- 90 > 40 → no swap needed (min heap — parent must be smaller)

```
      70
     /  \
    60   40
   / \  / \
  50 55 20 90
```

> 90 stays at position since it is larger than its parent (40). No bubbling needed.

---

## [2022] Q.2(a) Max-Heap from: 34,30,40,22,50,2,55,77,55. Insert 70, Delete 22. (CO1, 05)

**Building Max-Heap (insert one by one, bubble up):**

Insert 34: [34]
Insert 30: [34, 30]
Insert 40: 40 > 34 → swap → [40, 30, 34]
Insert 22: [40, 30, 34, 22]
Insert 50: 50 > 30 → swap, 50 > 40 → swap → [50, 40, 34, 22, 30]
Insert 2: [50, 40, 34, 22, 30, 2]
Insert 55: 55 > 34 → swap, 55 > 50 → swap → [55, 40, 50, 22, 30, 2, 34]
Insert 77: 77 > 22 → swap, 77 > 40 → swap, 77 > 55 → swap → [77, 55, 50, 40, 30, 2, 34, 22]
Insert 55: 55 > 30 → swap, 55 > 55 → no swap → [77, 55, 50, 40, 55, 2, 34, 22, 30]

**Final Max-Heap:**
```
            77
          /    \
        55      50
       / \     / \
      40  55  2   34
     / \
    22  30
```

**(i) Insert 70:**
Place at index 10 (left child of 55). Bubble up:
- 70 > 55 → swap
- 70 > 55 → swap (now at level 2)
- 70 < 77 → stop

```
            77
          /    \
        70      50
       / \     / \
      40  55  2   34
     / \  /
    22 30 55
```

**(ii) Delete 22:**
Find 22 (index 8). Replace with last element (55 at index 10). Remove last. Bubble up/down:
- 55 replaces 22 at position. 55 > 40 → swap with parent.

```
            77
          /    \
        70      50
       / \     / \
      55  55  2   34
     / \
    40  30
```

---


---

## [2023] Q.8(b) Max Heap: array, delete max, insert Q. (CLO3, 05)

**Given Max Heap:** W, M, O, J, L, D, K, A, G, I, E, B, C

**(i) Array representation:**

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value | W | M | O | J | L | D | K | A | G | I | E | B | C |

**(ii) Delete maximum (W):**
Replace root with last element (C). Remove last. Heapify down.
- C vs M, O → O is larger → swap C and O
- C vs D, K → K is larger → swap C and K

```
         O
        / \
       M    K
      /\   / \
     J  L D   C
    /\ /\  /
   A G I E B
```
Array: [O, M, K, J, L, D, C, A, G, I, E, B]

**(iii) Insert Q:**
Place Q at next position (index 13). Bubble up.
- Q > C → swap
- Q > K → swap (actually Q > O? Q < O alphabetically, so stop... wait, Q > O alphabetically)

Actually alphabetically: A<B<C<D<E<...O<P<Q<...W
So Q > O → swap. Q > ... Q < W (but W was deleted). Now root is O. Q > O → swap.

After insert Q at index 13, bubble up:
- Q at index 13, parent = index 6 (D). Q > D → swap
- Q now at index 6, parent = index 3 (K). Q > K → swap
- Q now at index 3, parent = index 1 (O). Q > O → swap
- Q is now root.

```
         Q
        / \
       M    O
      /\   / \
     J  L D   C
    /\ /\  /
   A G I E B
```
Hmm, but K was at index 3 before. Let me redo from the post-deletion state:

Post-deletion array: [O, M, K, J, L, D, C, A, G, I, E, B]

Insert Q at index 13: [O, M, K, J, L, D, C, A, G, I, E, B, Q]
- Index 13, parent = 6 (D). Q > D → swap → [O, M, K, J, L, Q, C, A, G, I, E, B, D]
- Index 6, parent = 3 (K). Q > K → swap → [O, M, Q, J, L, K, C, A, G, I, E, B, D]
- Index 3, parent = 1 (O). Q > O → swap → [Q, M, O, J, L, K, C, A, G, I, E, B, D]

> **Final Array: [Q, M, O, J, L, K, C, A, G, I, E, B, D]**

---


---

## [2024] Q.4(b) Min-Heap from: 34,30,40,22,50,2,55,77,55. Insert 60, Delete 22. (CO2, 05)

**Building Min-Heap (insert one by one, bubble up):**

Insert 34: [34]
Insert 30: 30<34 → swap → [30, 34]
Insert 40: 40>30 → [30, 34, 40]
Insert 22: 22<34 → swap, 22<30 → swap → [22, 30, 40, 34]
Insert 50: 50>30 → [22, 30, 40, 34, 50]
Insert 2: 2<40 → swap, 2<22 → swap → [2, 30, 22, 34, 50, 40]
Insert 55: 55>22 → [2, 30, 22, 34, 50, 40, 55]
Insert 77: 77>34 → [2, 30, 22, 34, 50, 40, 55, 77]
Insert 55: 55>30 → [2, 30, 22, 34, 50, 40, 55, 77, 55]

**Final Min-Heap:**
```
            2
          /   \
        30     22
       / \    /  \
      34  50 40   55
     / \
    77  55
```

**(i) Insert 60:**
Place at index 10. Parent = index 5 (50). 60 > 50 → no swap.

```
            2
          /   \
        30     22
       / \    /  \
      34  50 40   55
     / \  /
    77 55 60
```

**(ii) Delete 22:**
Replace 22 with last element (60). Remove last. Heapify down.
- 60 at index 3. Children: 40(6), 55(7). Min child = 40.
- 60 > 40 → swap.

```
            2
          /   \
        30     40
       / \    /  \
      34  50 60   55
     / \
    77  55
```

---

# Section B

---


---

## 📊 Exam Priority
**Priority: 1/5** (Must Prepare)
**Appeared in:** 7/8 years
**Typical marks:** 03–05 per question

<br>

---
[⬅️ Previous](./05_bst.md) | [🏠 Home](./README.md) | [Next ➡️](./07_sorting.md)
