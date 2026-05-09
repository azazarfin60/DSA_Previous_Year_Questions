[⬅️ Previous](./17_mst.md) | [🏠 Home](./README.md) | [Next ➡️](./19_tree_concepts.md)

---

# Backtracking — N-Queens, NP-Hard, NP-Complete


---

## [2022] Q.7(b) N-Queen + 4-Queen solution. (CO1, 03)

**N-Queen Problem:** Place N queens on an N×N chessboard such that no two queens attack each other (no shared row, column, or diagonal).

**4-Queen Solutions using backtracking:**

**Solution 1: [2, 4, 1, 3]**
```
  1 2 3 4
1 . Q . .
2 . . . Q
3 Q . . .
4 . . Q .
```

**Solution 2: [3, 1, 4, 2]**
```
  1 2 3 4
1 . . Q .
2 Q . . .
3 . . . Q
4 . Q . .
```

---


---

## [2022] Q.8(b) Subset sum: m=31, W=(11,13,24,7). State space tree. (CO2, 03)

**Problem:** Find subsets of {11, 13, 24, 7} that sum to 31.

**State Space Tree (include/exclude each weight):**
```
                        []  (sum=0, remaining=55)
                       / \
               [11]       []
             (s=11,r=44)  (s=0,r=44)
              / \           / \
        [11,13] [11]    [13]   []
        (s=24)  (s=11)  (s=13) (s=0)
         / \     / \     / \    / \
    [+24] [11,13] [11,24] [11] [13,24] [13] [24] []
    s=48  s=24   s=35   s=11  s=37   s=13  s=24 s=0
    ✗     / \    ✗      / \   ✗      / \   / \  / \
      [+7] [no7]     [+7] [no]    [+7][no][+7][]
      s=31  s=24     s=18 s=11    s=20 s=13 s=31 s=0
      ✓✓    ✗        ✗    ✗       ✗    ✗   ✗   ✗
```

**Solutions found:**
1. **{11, 13, 7} = 31** ✓
2. **{24, 7} = 31** ✓

---


---

## [2024] Q.8(a) NP-Hard, NP-Complete, and backtracking. (CO3, 03)

**NP-Hard:** Problems at least as hard as any NP problem. No known polynomial-time algorithm exists. May not have polynomial-time verification.

**NP-Complete:** Problems that are both in NP (verifiable in polynomial time) and NP-Hard. If any NP-Complete problem is solved in polynomial time, all NP problems can be.

**Relation to Backtracking:**
Since NP-Hard/NP-Complete problems have no known efficient solution, **backtracking** is used as a practical approach. It systematically explores all possible solutions, pruning branches that violate constraints. Examples:
- **N-Queens** (NP) — backtracking tries all placements, prunes conflicts
- **Subset Sum** (NP-Complete) — backtracking explores include/exclude for each element
- **TSP** (NP-Hard) — backtracking explores all permutations of cities

---


---

## 📊 Exam Priority
**Priority: 2/5** (Should Prepare)
**Appeared in:** 4/8 years (N-Queens), 3/8 (NP)
**Typical marks:** 03–04 per question

<br>

---
[⬅️ Previous](./17_mst.md) | [🏠 Home](./README.md) | [Next ➡️](./19_tree_concepts.md)
