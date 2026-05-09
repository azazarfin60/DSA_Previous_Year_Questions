[⬅️ Previous](./pagecontext09.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext11.md)

---

# DSA Class Notes - Page Context 10 (Pages 046-050)

## Page 046
**Binary Tree: Node Calculations**

**Binary Tree Basics:**
- **Max children:** 2
- **Min children:** 0

**Maximum number of nodes for a given Height (H):**
- **H=0:** $N = 2^0 = 1$
- **H=1:** $N = 2^1 = 2$
- **H=2:** $N = 2^2 = 4$
- **H=3:** $N = 2^3 = 8$
- **Total nodes for Height H:** $1 + 2 + 4 + ... + 2^H = 2^{H+1} - 1$

**Example:**
- For level 2, total nodes = $1 + 2 + 4 = 7 = (2^{2+1} - 1)$.
- If height $H = 59$, total nodes can be up to $5.76 \times 10^{17}$.

---

## Page 047
**Height and Node Relation Formulas**

**Formula Derivations:**
1. **Minimum Height for $n$ nodes:**
   - $n = 2^{H+1} - 1$
   - $n + 1 = 2^{H+1}$
   - $\log_2(n+1) = H + 1$
   - $H = \log_2(n+1) - 1$

2. **Minimum nodes for Height H:**
   - $n = H + 1$

**Summary Table:**
- **Max nodes for H height:** $n = 2^{H+1} - 1$
- **Min nodes for H height:** $n = H + 1$
- **Max height for $n$ nodes:** $H = n - 1$ (Skewed tree)
- **Min height for $n$ nodes:** $H = \log_2(n+1) - 1$

---

## Page 048
**Date:** 13 Jan, 2026  
**Instructor:** Foysal Sir  

### Full Binary Tree
- A binary tree in which every node has either 0 or 2 children.
- No node has only one child.
- **Rule:** The number of leaf nodes is $L = I + 1$ (where $I$ is the number of internal nodes).
- Visual examples provided for valid and invalid Full Binary Trees.

---

## Page 049
**Minimum Nodes and Maximum Height**

**Minimum nodes for a specific height (H):**
- In a skewed binary tree, each level has only one node.
- **Formula:** $n = H + 1$

**Maximum height for $n$ nodes:**
- **Formula:** $H = n - 1$

**Comparison Summary:**
- **Min node for H height:** $n = H + 1$
- **Max height for $n$ nodes:** $H = n - 1$
- **Min height for $n$ nodes:** $H = \log_2(n+1) - 1$

---

## Page 050
**Complete and Perfect Binary Trees**

### Complete Binary Tree
- Every level, except possibly the last, is completely filled.
- All nodes in the last level are as far **left** as possible.
- **Rule:** Filling must happen from **left to right**.

### Perfect Binary Tree
- A binary tree in which all interior nodes have two children and all leaves are at the same level.
- It is a specific type of complete binary tree where the last level is also completely filled.
- Visual diagrams showing the structural differences between Complete and Perfect Binary Trees.

<br>

---
[⬅️ Previous](./pagecontext09.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext11.md)
