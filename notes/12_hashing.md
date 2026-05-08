# 📘 Chapter 12: Hashing

> **Exam Frequency:** 5/8 years | **Typical Marks:** 02–06 | **Section:** A/B
> **Key Topics:** Hash functions, Collision resolution (Chaining, Linear Probing, Quadratic Probing)

---

## 1. What is Hashing?

**Hashing** is a technique to map data (keys) to fixed-size indices in a table (called a **hash table**) using a mathematical function (called a **hash function**). This enables **O(1) average-case** search, insert, and delete.

### Intuition
Think of a **library card catalog** — given a book title, you compute which drawer to look in using a formula (e.g., first letter → drawer A, B, C...). You don't search all drawers — you go directly to the right one.

### Components

| Component | Description |
|---|---|
| **Hash Table** | Array of fixed size to store data |
| **Hash Function** | Maps key → index (position in table) |
| **Collision** | When two different keys map to the same index |
| **Collision Resolution** | Strategy to handle collisions |

---

## 2. Hash Functions

### 2.1 Division Method (Most Common in Exams)

> **h(k) = k mod m**

Where `k` = key, `m` = table size (usually a prime number).

**Example:** Table size m = 10, keys: 23, 45, 12, 67, 89
```
h(23) = 23 mod 10 = 3
h(45) = 45 mod 10 = 5
h(12) = 12 mod 10 = 2
h(67) = 67 mod 10 = 7
h(89) = 89 mod 10 = 9
```

### 2.2 Properties of a Good Hash Function
1. **Uniform distribution** — keys spread evenly across the table
2. **Deterministic** — same key always produces the same hash
3. **Fast to compute** — O(1)
4. **Minimizes collisions** — different keys should map to different indices

### 2.3 Why Use Prime Numbers for Table Size?
Prime numbers distribute keys more uniformly. Composite numbers create patterns — e.g., with m=10, all keys ending in 0 go to slot 0.

---

## 3. Collisions

A **collision** occurs when two different keys hash to the **same index**.

**Example:** m = 10
```
h(23) = 3
h(33) = 3    ← COLLISION! Both map to index 3
```

Collisions are **inevitable** if the number of possible keys exceeds the table size (pigeonhole principle). We need strategies to handle them.

---

## 4. Collision Resolution — Chaining (Separate Chaining)

### Concept
Each slot in the hash table is a **linked list**. All keys that hash to the same index are stored in that slot's linked list.

### Example
Insert 23, 45, 12, 33, 67, 53, 89 into table of size 10 using h(k) = k mod 10:

```
h(23)=3, h(45)=5, h(12)=2, h(33)=3, h(67)=7, h(53)=3, h(89)=9

Hash Table:
Index  Chain
  0    → NULL
  1    → NULL
  2    → [12] → NULL
  3    → [23] → [33] → [53] → NULL     ← 3 elements chained!
  4    → NULL
  5    → [45] → NULL
  6    → NULL
  7    → [67] → NULL
  8    → NULL
  9    → [89] → NULL
```

### Searching in Chaining
To search for key 33:
1. Compute h(33) = 3
2. Go to index 3
3. Search the linked list: 23≠33, 33=33 → **FOUND!**

### Performance

| Operation | Average | Worst |
|---|---|---|
| Search | O(1 + α) | O(n) |
| Insert | O(1) | O(1) |
| Delete | O(1 + α) | O(n) |

Where **α = n/m** is the **load factor** (n = number of keys, m = table size).

### Advantages & Disadvantages

| Pros | Cons |
|---|---|
| Simple to implement | Extra memory for linked list pointers |
| Table never "full" | Cache-unfriendly (pointer chasing) |
| Deletion is easy | Worst case O(n) if all keys hash to same slot |

---

## 5. Collision Resolution — Open Addressing

In open addressing, all elements are stored **directly in the table** (no linked lists). When a collision occurs, we **probe** for the next available slot.

### 5.1 Linear Probing

**Probe sequence:** h(k, i) = (h(k) + i) mod m, for i = 0, 1, 2, ...

If slot h(k) is occupied, try h(k)+1, then h(k)+2, and so on (wrapping around).

### Example
Insert 23, 45, 12, 33, 67, 53, 89 into table of size 10, h(k) = k mod 10:

```
Insert 23: h(23)=3, slot 3 empty → place at 3
  [ _, _, _, 23, _, _, _, _, _, _ ]

Insert 45: h(45)=5, slot 5 empty → place at 5
  [ _, _, _, 23, _, 45, _, _, _, _ ]

Insert 12: h(12)=2, slot 2 empty → place at 2
  [ _, _, 12, 23, _, 45, _, _, _, _ ]

Insert 33: h(33)=3, slot 3 OCCUPIED → try 4, empty → place at 4
  [ _, _, 12, 23, 33, 45, _, _, _, _ ]

Insert 67: h(67)=7, slot 7 empty → place at 7
  [ _, _, 12, 23, 33, 45, _, 67, _, _ ]

Insert 53: h(53)=3, slot 3 OCCUPIED → try 4 OCCUPIED → try 5 OCCUPIED → try 6, empty → place at 6
  [ _, _, 12, 23, 33, 45, 53, 67, _, _ ]

Insert 89: h(89)=9, slot 9 empty → place at 9
  [ _, _, 12, 23, 33, 45, 53, 67, _, 89 ]
```

**Final table:**
```
Index: 0    1    2    3    4    5    6    7    8    9
Value: _    _    12   23   33   45   53   67   _    89
```

### Problem: Primary Clustering
Linear probing creates **clusters** — long runs of occupied slots. Once a cluster forms, it grows faster because any key hashing into the cluster must traverse the entire cluster to find an empty slot.

In the example above, slots 2–7 form a cluster.

---

### 5.2 Quadratic Probing

**Probe sequence:** h(k, i) = (h(k) + i²) mod m, for i = 0, 1, 2, ...

If slot h(k) is occupied, try h(k)+1, then h(k)+4, then h(k)+9, ...

This reduces primary clustering because probes spread out more.

### Example
Same keys, table size 10:

```
Insert 23: h=3, i=0: 3 → place at 3
Insert 45: h=5, i=0: 5 → place at 5
Insert 12: h=2, i=0: 2 → place at 2
Insert 33: h=3, i=0: 3 OCCUPIED
           i=1: (3+1)%10 = 4 → place at 4
Insert 67: h=7, i=0: 7 → place at 7
Insert 53: h=3, i=0: 3 OCCUPIED
           i=1: (3+1)%10 = 4 OCCUPIED
           i=2: (3+4)%10 = 7 OCCUPIED
           i=3: (3+9)%10 = 2 OCCUPIED
           i=4: (3+16)%10 = 9 → place at 9
Insert 89: h=9, i=0: 9 OCCUPIED
           i=1: (9+1)%10 = 0 → place at 0
```

**Final table:**
```
Index: 0    1    2    3    4    5    6    7    8    9
Value: 89   _    12   23   33   45   _    67   _    53
```

Notice: different from linear probing! Keys are more spread out.

---

## 6. Chaining vs Open Addressing

| Criterion | Chaining | Linear Probing | Quadratic Probing |
|---|---|---|---|
| Storage | Linked lists per slot | Directly in table | Directly in table |
| Load factor > 1 | ✅ Possible | ❌ Not possible | ❌ Not possible |
| Clustering | No clustering | Primary clustering | Reduced clustering |
| Deletion | Easy (delete from LL) | Complex (lazy deletion) | Complex |
| Cache performance | Poor | Good (sequential memory) | Moderate |
| Extra memory | Pointers | None | None |

---

## 7. Load Factor & Rehashing

### Load Factor
> **α = n / m** (number of elements / table size)

| α | Meaning |
|---|---|
| < 0.5 | Table mostly empty — fast operations |
| 0.5–0.7 | Good range for open addressing |
| > 0.7 | Performance degrades — collisions increase |
| > 1.0 | Only possible with chaining |

### Rehashing
When α exceeds a threshold, **double the table size** and re-insert all elements using the new hash function.

---

## 8. Exam-Ready Summary

### Quick Revision Points
1. **Hash function:** h(k) = k mod m (division method)
2. **Chaining:** Each slot is a linked list; no limit on load factor
3. **Linear probing:** h(k,i) = (h(k)+i) mod m; causes primary clustering
4. **Quadratic probing:** h(k,i) = (h(k)+i²) mod m; reduces clustering
5. **Average case:** O(1) for search/insert/delete
6. **Load factor** α = n/m; keep below 0.7 for open addressing
7. Use **prime number** for table size

### Most Common Exam Questions
- Insert keys using chaining / linear probing (03–04 marks)
- Search for a key and count comparisons (02–03 marks)
- Compare chaining vs probing (02–03 marks)

---

## 9. Practice Problems (From Past Exams)

### Problem 1 [2017, 2020, 2022, 03–04 marks]
**Q:** Insert keys 25, 42, 96, 101, 53, 87 into a hash table of size 7 using h(k) = k mod 7 with linear probing.

**Solution:**
```
h(25)=4, h(42)=0, h(96)=5, h(101)=3, h(53)=4→5→6, h(87)=3→4→5→6→0→1
Index: 0    1    2    3    4    5    6
Value: 42   87   _    101  25   96   53
```

### Problem 2 [Typical, 03 marks]
**Q:** Same keys as above, using separate chaining.

**Solution:**
```
0: [42] → NULL
3: [101] → NULL
4: [25] → [53] → NULL
5: [96] → [87] → NULL
```
No probing needed — just append to linked list!

---

*← [11 — Heap](11_heap_and_btree.md) | Next: [13 — Graphs →](13_graphs.md)*
