[⬅️ Previous](./pagecontext15.md) | [🏠 Home](./README.md)

---

# DSA Class Notes - Page Context 16 (Pages 076-079)

## Page 076
**0/1 Knapsack Trace (Final Steps)**

- **Recurrence Formula:** $B(i, w) = \max[B(i-1, w), B(i-1, w-w_i) + P_i]$
- **Specific Calculation Example:**
  - $B(4, 4) = \max[B(3, 4), B(3, 4-4) + 5] = \max[4, 0+5] = 5$
  - Final value: $B(4, 5) = \max[7, 7] = 7$.
- The result confirms that the maximum profit for a capacity of 5 is **7**.

---

## Page 077
**Date:** 13 Apr, 2026  
**Instructor:** Foysal Sir  

### Greedy Knapsack (Fractional Knapsack)
Unlike 0/1 Knapsack, the Greedy method is typically used for cases where items can be broken into fractions.

**Given Data (7 Objects):**
- **Profits:** $12, 5, 16, 7, 9, 11, 6$
- **Weights:** $3, 1, 4, 2, 9, 4, 3$

**Step 1: Calculate Profit/Weight (P/W) Ratio:**
- $O_1: 4.0$
- $O_2: 5.0$ (Highest)
- $O_3: 4.0$
- $O_4: 3.5$
- $O_5: 1.0$
- $O_6: 2.75$
- $O_7: 2.0$

**Step 2: Selection Strategy:**
- Sort objects in descending order of P/W ratio.
- Fill the knapsack with objects with the highest ratio first.

---

## Page 078
**Final Exam Preparation - Section A Focus**

1. **Algorithm Mastery:** Be prepared to write pseudocode and provide worked examples for all covered algorithms.
2. **Linked List (High Priority):**
   - Memory calculation for array-based implementations.
   - Understanding differences between Singly, Doubly, and Circular Linked Lists.
3. **Stack & Queue:**
   - Step-by-step logic for operations (Push/Pop, Enqueue/Dequeue).
   - Pseudocode for both.
4. **Sorting Algorithms:**
   - Focus on **Merge Sort** and **Quick Sort** (most frequent).
   - Know Bubble Sort and Binary Search logic.
   - Comparative analysis: Which algorithm is best for specific data sets?

---

## Page 079
**Final Exam Preparation - Section B Focus**

1. **Trees:**
   - Calculations for Height and Level.
   - Mastery of Traversals: Inorder, Preorder, and Postorder.
2. **Graphs (Likely 2 Full Question Sets):**
   - **Traversals:** BFS and DFS.
   - **Shortest Path:** Dijkstra's and Bellman-Ford.
   - **Minimum Spanning Tree:** Prim's and Kruskal's.
   - **Representation:** Adjacency Matrix and Adjoint Matrix.
3. **Hashing:** Assignment topics and potential exam questions.
4. **Recursion & Backtracking:** Core concepts and state-space tree construction.

**Final Note:** Focus on writing clean, C-style pseudocode as emphasized throughout the course.

<br>

---
[⬅️ Previous](./pagecontext15.md) | [🏠 Home](./README.md)
