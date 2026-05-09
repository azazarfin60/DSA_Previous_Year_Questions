[⬅️ Previous](./pagecontext08.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext10.md)

---

# DSA Class Notes - Page Context 09 (Pages 041-045)

## Page 041
**Prefix to Postfix Conversion**

**Algorithm Steps:**
1. Create an empty stack.
2. **Scan** the Prefix expression from **right to left**.
3. For each symbol:
   - **If operand:** Push it into the stack.
   - **If operator:**
     - Pop two operands from the stack (`op1` then `op2`).
     - Form a string: `operand1 + operand2 + operator`.
     - Push this new string back into the stack.
4. After scanning all symbols, the final result is in the stack.

**Trace Example:** `+ * AB - CD`
- Scan `D` -> Push `D`
- Scan `C` -> Push `C`
- Scan `-` -> Pop `C`, `D`. Form `CD-`. Push `CD-`.
- Scan `B` -> Push `B`
- Scan `A` -> Push `A`
- Scan `*` -> Pop `A`, `B`. Form `AB*`. Push `AB*`.
- Scan `+` -> Pop `AB*`, `CD-`. Form `AB*CD-+`. Push `AB*CD-+`.

---

## Page 042
**Expression Conversion & Introduction to Trees**

- Visual tracing of a complex Prefix to Postfix conversion: `- + A * BC / D ^ EF`
- Final result formed: `ABC*+DEF^/-`

### Tree (Non-Linear Data Structure)
- A tree consists of a set of nodes connected by edges.
- One node is designated as the **Root**.
- Remaining nodes form **subtrees**.

---

## Page 043
**Date:** 10 Jan, 2026  
**Instructor:** Foysal Sir  

### Tree Definition & Basic Terminology
- **Tree:** A non-linear, hierarchical data structure consisting of nodes.
- **Root:** The top node of a tree.
- **Child:** A node that has a parent.
- **Parent:** A node that has children.
- **Leaf Node:** A node with no children (terminal node).

**Key Properties:**
1. **Degree:** Number of children a node has.
2. **Degree of Tree:** The maximum degree among all nodes in the tree.
3. **Depth of Node:** The length of the path from the root to that specific node.
4. **Height of Node:** The length of the path from that specific node to the deepest leaf.

---

## Page 044
**Advanced Tree Terminology**

- **Ancestor:** All nodes on the path from the root to a specific node (excluding the node itself).
- **Descendant:** All nodes reachable from a specific node moving towards the leaves.
- **Predecessor / Successor:** Immediate neighbors in a hierarchy (Parent/Child).

**Tree Example Diagram (A to M):**
- **Root:** `A`
- **Ancestors of H:** `A`
- **Descendants of H:** `I, J, K, L, M`
- **Leaves:** `D, F, G, J, K, L, M` (Nodes with no children).

---

## Page 045
**Date:** 11 Jan, 2026  
**Instructor:** Foysal Sir  

### Tree Terminology with Visual Examples

**Levels:**
- **Level 0:** `A` (Root)
- **Level 1:** `B, C`
- **Level 2:** `D, E, F, G, J`
- **Level 3:** `H, I`

**Specific Definitions & Examples:**
1. **Degree:**
   - Degree of `C` is 3 (it has children `F, G, J`).
   - Degree of `A` is 2.
2. **Degree of Tree:** 3 (Maximum degree present).
3. **Depth of Node:**
   - Depth of `C` = 1.
   - Depth of `D` = 2.
4. **Height of Node:**
   - Height of `E` = 0 (Leaf).
   - Height of `A` = 3 (Max path to leaf `H` or `I`).
5. **Level of Node:** Length of path from root. `A` is level 0.
6. **Level of Tree:** Max level reached (here 3).

<br>

---
[⬅️ Previous](./pagecontext08.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext10.md)
