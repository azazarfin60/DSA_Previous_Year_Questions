[⬅️ Previous](./pagecontext14.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext16.md)

---

# DSA Class Notes - Page Context 15 (Pages 071-075)

## Page 071
**Bellman-Ford and Negative Cycles**

- **Key Concept:** Bellman-Ford algorithm will **fail** to converge if the graph contains a **Negative Weight Cycle**.
- **Observation:** In a negative weight cycle, the path cost can be reduced infinitely by repeatedly traversing the cycle.
- **Bengali Note:** "কখনোই Converge করবে না" (Will never converge) if such a loop exists.

---

## Page 072
**Date:** 06 Apr, 2026  
**Instructor:** Foysal Sir  

**Bellman-Ford Algorithm Trace (Continued)**
- Shows a graph with negative edges and the step-by-step relaxation process across three iterations.
- Demonstrates how the algorithm handles negative weights that do not form a cycle, successfully updating node distances.

---

## Page 073
**Job Sequencing with Deadlines (Greedy Approach)**

**Objective:** Maximize total profit by executing jobs within their respective deadlines.

**Given Data:**
- **Jobs:** $J_1, J_2, J_3, J_4, J_5$
- **Profits:** $10, 5, 20, 1, 15$
- **Deadlines:** $1, 3, 2, 3, 2$

**Step 1: Sort by Profit (Descending)**
1. $J_3$ (Profit: 20, Deadline: 2)
2. $J_5$ (Profit: 15, Deadline: 2)
3. $J_1$ (Profit: 10, Deadline: 1)
4. $J_2$ (Profit: 5, Deadline: 3)
5. $J_4$ (Profit: 1, Deadline: 3)

**Step 2: Allocate Time Slots (Max Limit = 3)**
- **Slot (0-1):** $J_3$ (Deadline 2 allows this slot)
- **Slot (1-2):** $J_5$ (Deadline 2 allows this slot)
- **Slot (2-3):** $J_2$ (Deadline 3 allows this slot)
- **Rejected Jobs:** $J_1$ (Deadline was 1, no slot left) and $J_4$.



## Page 075
**Date:** 12 Apr, 2026  
**Instructor:** Foysal Sir  

### 0/1 Knapsack Problem (Dynamic Programming)

**Given Data:**
- **Max Weight (W):** 5
- **Number of Items (n):** 4
- **Items (Weight, Profit):**
  - Item 1: (3, 4)
  - Item 2: (2, 3)
  - Item 3: (5, 6)
  - Item 4: (4, 5)

**DP Table Construction (i = items, w = capacity):**
- The table is filled using the formula:
  $$V[i, w] = \max(V[i-1, w], \text{profit}_i + V[i-1, w - \text{weight}_i])$$
- **Result:** The value at $V[4, 5]$ is **7**, which is the maximum profit.
- **Backtracking:** Used to find the items included in the optimal set. In this case, Items 1 and 2 (total weight $3+2=5$, total profit $4+3=7$).

<br>

---
[⬅️ Previous](./pagecontext14.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext16.md)
