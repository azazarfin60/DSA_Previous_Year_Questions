[⬅️ Previous](./14_bfs_dfs.md) | [🏠 Home](./README.md) | [Next ➡️](./16_bellman_ford.md)

---

# Dijkstra's Algorithm — Shortest Path


---

## [2017] 6(b) Dijkstra's Algorithm from A. (06)

**Graph:** A→B(6), A→C(10), A→D(5), B→D(2), B→E(9), C→E(5), D→B(7), D→E(5)

**Initialization:**
| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | 0 | ∞ | ∞ | ∞ | ∞ |

**Iteration 1: Visit A (dist=0)**
- A→B: 0+6=6 < ∞ → update B=6
- A→C: 0+10=10 < ∞ → update C=10
- A→D: 0+5=5 < ∞ → update D=5

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | 6 | 10 | 5 | ∞ |

**Iteration 2: Visit D (dist=5, smallest unvisited)**
- D→B: 5+7=12 > 6 → no update
- D→E: 5+5=10 < ∞ → update E=10

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | 6 | 10 | **5** | 10 |

**Iteration 3: Visit B (dist=6)**
- B→D: 6+2=8 > 5 → no update
- B→E: 6+9=15 > 10 → no update

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | **6** | 10 | **5** | 10 |

**Iteration 4: Visit C (dist=10)**
- C→E: 10+5=15 > 10 → no update

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | **6** | **10** | **5** | 10 |

**Iteration 5: Visit E (dist=10)** — no outgoing edges to update.

**Final Shortest Paths from A:**

| Destination | Distance | Path |
|---|---|---|
| A → A | 0 | A |
| A → B | 6 | A → B |
| A → C | 10 | A → C |
| A → D | 5 | A → D |
| A → E | 10 | A → D → E |

---


---

## [2021] Q.8(a) Dijkstra's from S. (04)

**Graph:** S→t(3), S→y(5), t→x(6), t→y(1), x→z(7), y→t(4), y→x(2), y→z(6)

**Initialization:**

| Node | S | t | x | y | z |
|---|---|---|---|---|---|
| Dist | 0 | ∞ | ∞ | ∞ | ∞ |

**Visit S (dist=0):** S→t(3), S→y(5)

| Node | S | t | x | y | z |
|---|---|---|---|---|---|
| Dist | **0** | 3 | ∞ | 5 | ∞ |

**Visit t (dist=3):** t→x(3+6=9), t→y(3+1=4 < 5)

| Node | S | t | x | y | z |
|---|---|---|---|---|---|
| Dist | **0** | **3** | 9 | 4 | ∞ |

**Visit y (dist=4):** y→t(4+4=8 > 3), y→x(4+2=6 < 9), y→z(4+6=10)

| Node | S | t | x | y | z |
|---|---|---|---|---|---|
| Dist | **0** | **3** | 6 | **4** | 10 |

**Visit x (dist=6):** x→z(6+7=13 > 10)

| Node | S | t | x | y | z |
|---|---|---|---|---|---|
| Dist | **0** | **3** | **6** | **4** | 10 |

**Visit z (dist=10):** No outgoing edges to update.

**Final Shortest Paths from S:**

| Destination | Distance | Path |
|---|---|---|
| S → t | 3 | S → t |
| S → y | 4 | S → t → y |
| S → x | 6 | S → t → y → x |
| S → z | 10 | S → t → y → z |

---


---

## [2022] Q.5(a) Dijkstra's: shortest path 1 to 8. (CO3, 04)

**Graph:** 1→2(1), 1→4(1), 2→3(2), 2→5(1), 3→5(2), 3→8(10), 4→1(3), 4→6(4), 5→7(3), 6→7(7), 7→8(7)

| Step | Visit | Dist 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Init | — | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | 1 | **0** | 1 | ∞ | 1 | ∞ | ∞ | ∞ | ∞ |
| 2 | 2 (d=1) | 0 | **1** | 3 | 1 | 2 | ∞ | ∞ | ∞ |
| 3 | 4 (d=1) | 0 | 1 | 3 | **1** | 2 | 5 | ∞ | ∞ |
| 4 | 5 (d=2) | 0 | 1 | 3 | 1 | **2** | 5 | 5 | ∞ |
| 5 | 3 (d=3) | 0 | 1 | **3** | 1 | 2 | 5 | 5 | 13 |
| 6 | 6 (d=5) | 0 | 1 | 3 | 1 | 2 | **5** | 5 | 13 |
| 7 | 7 (d=5) | 0 | 1 | 3 | 1 | 2 | 5 | **5** | 12 |
| 8 | 8 (d=12) | 0 | 1 | 3 | 1 | 2 | 5 | 5 | **12** |

> **Shortest path from 1 to 8 = 12**
> **Path: 1 → 2 → 5 → 7 → 8**

---


---

## [2023] Q.2(c) Dijkstra's: node 1 to node 8. (CLO3, 04)

**Graph:** 1→2(2), 1→3(1), 1→4(1), 2→5(5), 3→2(1), 3→5(2), 4→3(1), 4→6(4), 5→7(2), 5→8(10), 6→7(7), 7→8(6)

| Step | Visit | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Init | — | 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | 1 | **0** | 2 | 1 | 1 | ∞ | ∞ | ∞ | ∞ |
| 2 | 3(d=1) | 0 | 2 | **1** | 1 | 3 | ∞ | ∞ | ∞ |
| 3 | 4(d=1) | 0 | 2 | 1 | **1** | 3 | 5 | ∞ | ∞ |
| 4 | 2(d=2) | 0 | **2** | 1 | 1 | 3 | 5 | ∞ | ∞ |
| 5 | 5(d=3) | 0 | 2 | 1 | 1 | **3** | 5 | 5 | 13 |
| 6 | 6(d=5) | 0 | 2 | 1 | 1 | 3 | **5** | 5 | 13 |
| 7 | 7(d=5) | 0 | 2 | 1 | 1 | 3 | 5 | **5** | 11 |
| 8 | 8(d=11) | 0 | 2 | 1 | 1 | 3 | 5 | 5 | **11** |

> **Shortest path from 1 to 8 = 11**
> **Path: 1 → 3 → 5 → 7 → 8** (or 1 → 4 → 3 → 5 → 7 → 8, same cost)

---


---

## [2024] Q.5(b) Dijkstra's from A. (CO3, 06)

**Graph:** A→B(6), A→D(10), A→C(12), B→D(3), C→E(5), D→B(7), D→E(5), D→C(4)

**Initialization:**

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | 0 | ∞ | ∞ | ∞ | ∞ |

**Iteration 1: Visit A (dist=0)**
- A→B: 6, A→D: 10, A→C: 12

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | 6 | 12 | 10 | ∞ |

**Iteration 2: Visit B (dist=6)**
- B→D: 6+3=9 < 10 → update D=9

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | **6** | 12 | 9 | ∞ |

**Iteration 3: Visit D (dist=9)**
- D→B: 9+7=16 > 6
- D→E: 9+5=14
- D→C: 9+4=13 > 12

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | **6** | 12 | **9** | 14 |

**Iteration 4: Visit C (dist=12)**
- C→E: 12+5=17 > 14

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | **6** | **12** | **9** | 14 |

**Iteration 5: Visit E (dist=14)** — no outgoing updates.

**Final Shortest Paths from A:**

| Destination | Distance | Path |
|---|---|---|
| A → B | 6 | A → B |
| A → D | 9 | A → B → D |
| A → C | 12 | A → C |
| A → E | 14 | A → B → D → E |

---


---

## 📊 Exam Priority
**Priority: 1/5** (Must Prepare)
**Appeared in:** 7/8 years
**Typical marks:** 04–06 per question

<br>

---
[⬅️ Previous](./14_bfs_dfs.md) | [🏠 Home](./README.md) | [Next ➡️](./16_bellman_ford.md)
