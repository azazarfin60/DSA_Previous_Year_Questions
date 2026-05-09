[⬅️ Previous](./16_bellman_ford.md) | [🏠 Home](./README.md) | [Next ➡️](./18_backtracking.md)

---

# Minimum Spanning Tree — Prim's & Kruskal's Algorithm


---

## [2017] 8(b) All spanning trees and MST. (05)

**Graph:** ECE—CSE(2), CSE—CE(8), ECE—EEE(4), CE—ME(5), EEE—ME(5), CSE—ME(7), CSE—EEE(3)

5 nodes → spanning tree needs exactly 4 edges.

**Some possible spanning trees (of many):**

**ST1:** ECE—CSE(2), CSE—EEE(3), CSE—CE(8), CE—ME(5) → Total = 18
**ST2:** ECE—CSE(2), CSE—EEE(3), EEE—ME(5), CSE—CE(8) → Total = 18
**ST3:** ECE—CSE(2), CSE—EEE(3), EEE—ME(5), CE—ME(5) — ✗ (cycle via ME)
**ST4:** ECE—CSE(2), CSE—EEE(3), CE—ME(5), CSE—ME(7) — ✗ (cycle via ME)
**ST5:** ECE—CSE(2), CSE—EEE(3), EEE—ME(5), CSE—ME(7) — ✗ (cycle)
**ST6:** ECE—EEE(4), ECE—CSE(2), CSE—CE(8), CE—ME(5) → Total = 19

**MST using Kruskal's (sort edges, pick smallest without cycle):**

| Edge | Weight | Action |
|---|---|---|
| ECE—CSE | 2 | ✅ Add |
| CSE—EEE | 3 | ✅ Add |
| ECE—EEE | 4 | ✗ Cycle (ECE-CSE-EEE) |
| CE—ME | 5 | ✅ Add |
| EEE—ME | 5 | ✗ Cycle |
| CSE—ME | 7 | ✗ Cycle |
| CSE—CE | 8 | ✅ Add (connects CE) |

**MST:** ECE—CSE(2), CSE—EEE(3), CE—ME(5), CSE—CE(8)
> **MST Total Weight = 2 + 3 + 5 + 8 = 18**

This is the MST because at each step we chose the minimum weight edge that doesn't form a cycle, guaranteeing the minimum total cost by Kruskal's greedy property.

---


---

## [2018] Q8(a) MST for broadband network. (06)

**Using Kruskal's Algorithm** (sort edges, pick smallest without forming cycle):

**Sorted edges:**
| Edge | Weight |
|---|---|
| H3—H7 | 0.5K |
| H4—H5 | 0.5K |
| H1—H3 | 1K |
| H5—H6 | 1K |
| H1—H2 | 2K |
| H4—H6 | 2K |
| H6—H7 | 2K |
| H1—H7 | 3K |
| H2—H3 | 3K |
| H2—H5 | 3K |
| H3—H6 | 5K |

**Selection (7 nodes → need 6 edges):**

| Step | Edge | Weight | Action |
|---|---|---|---|
| 1 | H3—H7 | 0.5K | ✅ Add |
| 2 | H4—H5 | 0.5K | ✅ Add |
| 3 | H1—H3 | 1K | ✅ Add (connects H1) |
| 4 | H5—H6 | 1K | ✅ Add (connects H6) |
| 5 | H1—H2 | 2K | ✅ Add (connects H2) |
| 6 | H4—H6 | 2K | ✗ Cycle (H4-H5-H6) |
| 7 | H6—H7 | 2K | ✗ Cycle (H6-H5-H4... wait) |

Let me recheck: After step 5, connected = {H1,H2,H3,H7}, {H4,H5,H6}. Need 1 more edge to connect the two components.

| 6 | H4—H6 | 2K | ✗ Cycle (H4,H5,H6 same component) |
| 7 | H6—H7 | 2K | ✅ Add (connects the two components) |

**MST Edges:** H3—H7(0.5K), H4—H5(0.5K), H1—H3(1K), H5—H6(1K), H1—H2(2K), H6—H7(2K)

> **Minimum Cost = 0.5 + 0.5 + 1 + 1 + 2 + 2 = 7K (7,000 Taka)**

---


---

## [2020] Q.4(c) MST using Kruskal's. (03)

**Sorted edges:**

| Edge | Weight |
|---|---|
| B—D | 2 |
| D—T | 2 |
| A—C | 3 |
| C—D | 4 |
| B—T | 5 |
| A—B | 6 |
| S—A | 7 |
| S—C | 8 |
| S—B | 9 |

**Selection (6 nodes → 5 edges):**

| Step | Edge | Weight | Action |
|---|---|---|---|
| 1 | B—D | 2 | ✅ Add |
| 2 | D—T | 2 | ✅ Add |
| 3 | A—C | 3 | ✅ Add |
| 4 | C—D | 4 | ✅ Add (connects {A,C} with {B,D,T}) |
| 5 | B—T | 5 | ✗ Cycle |
| 6 | A—B | 6 | ✗ Cycle |
| 7 | S—A | 7 | ✅ Add (connects S) |

> **MST: {B—D(2), D—T(2), A—C(3), C—D(4), S—A(7)} = 18**

---


---

## [2021] Q.5(d) MST of graph G. (03)

**Edges sorted:** D—E(1), D—G(1), A—D(2), A—B(2), B—E(2), B—D(2), A—G(2), F—G(2), G—H(2), C—F(3), E—H(3)

**Kruskal's (8 nodes → 7 edges):**

| Step | Edge | Weight | Action |
|---|---|---|---|
| 1 | D—E | 1 | ✅ Add |
| 2 | D—G | 1 | ✅ Add |
| 3 | A—D | 2 | ✅ Add (connects A) |
| 4 | A—B | 2 | ✅ Add (connects B) |
| 5 | B—E | 2 | ✗ Cycle (A-B, A-D-E) |
| 6 | B—D | 2 | ✗ Cycle |
| 7 | A—G | 2 | ✗ Cycle |
| 8 | F—G | 2 | ✅ Add (connects F) |
| 9 | G—H | 2 | ✅ Add (connects H) |
| 10 | C—F | 3 | ✅ Add (connects C) |

> **MST: {D—E(1), D—G(1), A—D(2), A—B(2), F—G(2), G—H(2), C—F(3)} = 13**

---


---

## [2022] Q.6(b) Prim's MST. (CO2, 03)

**Graph:** (1,2)=10, (1,4)=30, (2,3)=50, (2,5)=40, (2,4)=45, (3,4)=35, (3,5)=25, (4,5)=15, (4,6)=20, (5,6)=55

**Starting from node 1:**

| Step | Add Node | Edge Added | Cost | MST Nodes |
|---|---|---|---|---|
| 1 | 1 | — | — | {1} |
| 2 | 2 | (1,2) | 10 | {1,2} |
| 3 | 4 | (1,4) | 30 | {1,2,4} |
| 4 | 5 | (4,5) | 15 | {1,2,4,5} |
| 5 | 6 | (4,6) | 20 | {1,2,4,5,6} |
| 6 | 3 | (5,3) | 25 | {1,2,3,4,5,6} |

> **MST: {(1,2)=10, (1,4)=30, (4,5)=15, (4,6)=20, (5,3)=25} = 100**

---


---

## [2023] Q.5(c) Kruskal's MST. (CLO3, 04)

**Sorted edges:**

| Edge | Weight |
|---|---|
| (1,6) | 10 |
| (3,4) | 12 |
| (2,7) | 14 |
| (2,3) | 16 |
| (4,7) | 18 |
| (4,5) | 22 |
| (5,7) | 24 |
| (5,6) | 25 |
| (1,2) | 28 |

**Selection (7 nodes → 6 edges):**

| Step | Edge | Weight | Action | Components |
|---|---|---|---|---|
| 1 | (1,6) | 10 | ✅ Add | {1,6} |
| 2 | (3,4) | 12 | ✅ Add | {1,6}, {3,4} |
| 3 | (2,7) | 14 | ✅ Add | {1,6}, {3,4}, {2,7} |
| 4 | (2,3) | 16 | ✅ Add | {1,6}, {2,3,4,7} |
| 5 | (4,7) | 18 | ✗ Cycle | — |
| 6 | (4,5) | 22 | ✅ Add | {1,6}, {2,3,4,5,7} |
| 7 | (5,7) | 24 | ✗ Cycle | — |
| 8 | (5,6) | 25 | ✅ Add | {1,2,3,4,5,6,7} |

> **MST: {(1,6)=10, (3,4)=12, (2,7)=14, (2,3)=16, (4,5)=22, (5,6)=25} = 99**

---


---

## [2024] Q.3(c) Define 2-tree. Kruskal's MST. (CO2, 04)

**2-tree (Extended Binary Tree):** A binary tree where every node has either **0 or 2 children** — no node has exactly one child. Internal nodes have 2 children; leaf nodes (external) have 0.

**Kruskal's MST:**

**Sorted edges:**

| Edge | Weight |
|---|---|
| (3,4) | 1 |
| (0,1) | 2 |
| (2,4) | 2 |
| (1,2) | 3 |
| (2,3) | 5 |
| (1,4) | 6 |
| (0,4) | 7 |

**Selection (5 nodes → 4 edges):**

| Step | Edge | Weight | Action |
|---|---|---|---|
| 1 | (3,4) | 1 | ✅ Add |
| 2 | (0,1) | 2 | ✅ Add |
| 3 | (2,4) | 2 | ✅ Add |
| 4 | (1,2) | 3 | ✅ Add (connects {0,1} with {2,3,4}) |
| 5 | (2,3) | 5 | ✗ Cycle |

> **MST: {(3,4)=1, (0,1)=2, (2,4)=2, (1,2)=3} = 8**

---


---

## [2024] Q.7(a) Define spanning tree. Prim's MST. (CO3, 03)

**Spanning Tree:** A subgraph of a connected graph that includes **all vertices**, is connected, has no cycles, and contains exactly **V-1 edges**.

**Prim's MST (starting from node 1):**

| Step | Add Node | Edge | Cost | MST Nodes |
|---|---|---|---|---|
| 1 | 1 | — | — | {1} |
| 2 | 2 | (1,2) | 10 | {1,2} |
| 3 | 6 | (6,1) | 30 | {1,2,6} |
| 4 | 4 | (4,6) | 15 | {1,2,4,6} |
| 5 | 7 | (6,7) | 20 | {1,2,4,6,7} |
| 6 | 5 | (4,5) | 25 | {1,2,4,5,6,7} |
| 7 | 3 | (3,4) | 35 | {1,2,3,4,5,6,7} |

> **MST: {(1,2)=10, (6,1)=30, (4,6)=15, (6,7)=20, (4,5)=25, (3,4)=35} = 135**

---


---

## 📊 Exam Priority
**Priority: 1/5** (Must Prepare)
**Appeared in:** 7/8 years
**Typical marks:** 03–06 per question

<br>

---
[⬅️ Previous](./16_bellman_ford.md) | [🏠 Home](./README.md) | [Next ➡️](./18_backtracking.md)
