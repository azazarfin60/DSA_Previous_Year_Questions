[⬅️ Previous](./08_searching.md) | [🏠 Home](./README.md) | [Next ➡️](./10_recursion.md)

---

# Hashing — Hash Functions, Collision Resolution, Chaining, Probing


---

## [2017] 6(a) Discuss: Hashing, Collision Resolution, Chaining. (03)

**(i) Hashing:** A technique to map data (keys) to fixed-size values (hash codes) using a **hash function** h(k). This allows O(1) average-time search, insert, and delete operations. Example: h(k) = k mod 10.

**(ii) Collision Resolution:** When two different keys map to the same hash index, a **collision** occurs. Collision resolution is the method used to handle this. Two main methods:
- Open Addressing (Linear Probing, Quadratic Probing)
- Separate Chaining

**(iii) Chaining:** A collision resolution method where each slot of the hash table contains a **linked list**. All keys that hash to the same index are stored in that slot's linked list.

```
Index 0: → NULL
Index 1: → 11 → 21 → NULL
Index 2: → 42 → NULL
Index 3: → 23 → 33 → NULL
```

---


---

## [2018] Q5(a) How is Hash function used for better searching? (03)

A **hash function** h(k) maps a key k directly to an array index, allowing **O(1) average-time** searching instead of O(n) linear search.

**How it works:**
1. Given key k, compute index = h(k) (e.g., h(k) = k mod 10)
2. Go directly to that index in the hash table
3. If key is there, search is done in O(1)

**Example:** Keys: 25, 42, 33. Hash function: h(k) = k mod 10.
- h(25) = 5, h(42) = 2, h(33) = 3
- To find 42: compute h(42) = 2, go to index 2 → found in **1 step**

Without hashing, searching 42 in an unsorted list would take up to O(n) comparisons.

---


---

## [2020] Q.6(c) Collision in hashing. One method to solve. (03)

**Collision:** When two different keys map to the same index using the hash function.
Example: h(k) = k mod 7. Both h(14)=0 and h(21)=0 → collision at index 0.

**Method: Separate Chaining**
Each slot stores a linked list. All colliding keys are chained together.

Example: h(k) = k mod 7, insert: 14, 21, 7, 35
```
Index 0: → 14 → 21 → 7 → 35 → NULL
Index 1: → NULL
...
```
All four keys hash to 0 and are stored in the chain at index 0.

---


---

## [2022] Q.2(c) Why is a good hash function important? (CO1, 02)

A good hash function is important because:

1. **Minimizes collisions** — distributes keys uniformly across the table, reducing the chance of multiple keys mapping to the same index.
2. **Ensures O(1) performance** — poor hash functions cause clustering, degrading search/insert from O(1) to O(n).
3. **Uniform distribution** — every slot has equal probability of being filled, maximizing table utilization.

A bad hash function (e.g., h(k) = 1 for all k) makes the hash table degenerate into a linked list with O(n) operations.

---


---

## [2022] Q.4(a) Hash table h(k) = k mod 7 for 19,26,13,48,17. (CO2, 04)

**(i) Separate Chaining:**

| Index | Chain |
|---|---|
| 0 | → 48 → NULL |
| 1 | → 43... |

Let me compute: h(19)=19%7=5, h(26)=26%7=5, h(13)=13%7=6, h(48)=48%7=6, h(17)=17%7=3

| Index | Chain |
|---|---|
| 0 | NULL |
| 1 | NULL |
| 2 | NULL |
| 3 | → 17 → NULL |
| 4 | NULL |
| 5 | → 19 → 26 → NULL |
| 6 | → 13 → 48 → NULL |

**(ii) Linear Probing:**

| Insert | h(k) | Probe | Final Index |
|---|---|---|---|
| 19 | 5 | — | 5 |
| 26 | 5 | 5 occupied → 6 | 6 |
| 13 | 6 | 6 occupied → 0 | 0 |
| 48 | 6 | 6 occupied → 0 occupied → 1 | 1 |
| 17 | 3 | — | 3 |

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| Value | 13 | 48 | — | 17 | — | 19 | 26 |

---


---

## 📊 Exam Priority
**Priority: 2/5** (Should Prepare)
**Appeared in:** 5/8 years
**Typical marks:** 02–06 per question

<br>

---
[⬅️ Previous](./08_searching.md) | [🏠 Home](./README.md) | [Next ➡️](./10_recursion.md)
