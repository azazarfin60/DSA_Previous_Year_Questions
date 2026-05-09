[⬅️ Previous](./15_dijkstra.md) | [🏠 Home](./README.md) | [Next ➡️](./17_mst.md)

---

# Bellman-Ford Algorithm — Negative Edges, Cycle Detection


---

## [2020] Q.8(c) Shortest path with negative cycle. (03)

**Bellman-Ford algorithm** should be used when there are negative edge weights. However, if a **negative cycle** exists (a cycle whose total weight is negative), then:

- No shortest path exists — we can keep going around the negative cycle to reduce the distance infinitely
- **Bellman-Ford can detect negative cycles:** After V-1 relaxation iterations, perform one more iteration. If any distance still decreases, a negative cycle exists.

```
Procedure DETECT_NEGATIVE_CYCLE(G)
    Run Bellman-Ford for V-1 iterations
    For each edge (U, V, W) do
        If dist[U] + W < dist[V] Then
            Print "Negative cycle detected"
            Return TRUE
        End If
    End For
    Return FALSE
End Procedure
```

> **Answer: Use Bellman-Ford to detect the negative cycle. If detected, no finite shortest path exists.**

---

## [2022] Q.7(a) Bellman-Ford: node 4 to 1. Discuss result. (CO3, 04)

**Graph:** 1→3(5), 2→1(4), 2→4(7), 3→4(-15), 4→1(7)

**Source = 4:**

**Initialization:** dist[4]=0, dist[1]=∞, dist[2]=∞, dist[3]=∞

**Iteration 1 (relax all edges):**
- 4→1: 0+7=7 → dist[1]=7
- 1→3: 7+5=12 → dist[3]=12
- 3→4: 12+(-15)=-3 → dist[4]=-3
- 2→1: ∞ (skip), 2→4: ∞ (skip)

**Iteration 2:**
- 4→1: -3+7=4 < 7 → dist[1]=4
- 1→3: 4+5=9 < 12 → dist[3]=9
- 3→4: 9+(-15)=-6 < -3 → dist[4]=-6

**Iteration 3 (V-1 = 3):**
- 4→1: -6+7=1 < 4 → dist[1]=1
- 1→3: 1+5=6 < 9 → dist[3]=6
- 3→4: 6+(-15)=-9 < -6 → dist[4]=-9

**Negative Cycle Check (one more iteration):**
- Distances still decrease → **Negative cycle detected!**

> **Result: A negative cycle exists (4→1→3→4 with total weight 7+5-15 = -3). No finite shortest path exists from 4 to 1.**

---


---

## [2023] Q.7(c) Bellman-Ford shortest paths from A. (CLO3, 03)

**Graph:** A→B(5), A→C(1), A→D(2), B→D(2), B→E(-2), C→D(4), D→C(-1), D→E(4), E→C(3)

**Source = A, V=5 → V-1=4 iterations**

**Init:** dist = [A:0, B:∞, C:∞, D:∞, E:∞]

**Iteration 1:**
- A→B: 0+5=5, A→C: 0+1=1, A→D: 0+2=2
- B→D: 5+2=7 > 2, B→E: 5+(-2)=3
- C→D: 1+4=5 > 2
- D→C: 2+(-1)=1 = 1 (no change), D→E: 2+4=6 > 3
- E→C: 3+3=6 > 1

dist = [A:0, B:5, C:1, D:2, E:3]

**Iteration 2:**
- B→E: 5+(-2)=3 = 3 (no change)
- D→C: 2+(-1)=1 = 1 (no change)
- All others: no improvement

dist = [A:0, B:5, C:1, D:2, E:3] — **converged**

**Final Shortest Paths from A:**

| Node | Distance | Path |
|---|---|---|
| A → B | 5 | A → B |
| A → C | 1 | A → C |
| A → D | 2 | A → D |
| A → E | 3 | A → B → E |

No negative cycle detected. ✓

---


---

## 📊 Exam Priority
**Priority: 2/5** (Should Prepare)
**Appeared in:** 4/8 years
**Typical marks:** 03–04 per question

<br>

---
[⬅️ Previous](./15_dijkstra.md) | [🏠 Home](./README.md) | [Next ➡️](./17_mst.md)
