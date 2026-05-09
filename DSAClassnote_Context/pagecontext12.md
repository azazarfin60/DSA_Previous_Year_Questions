[⬅️ Previous](./pagecontext11.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext13.md)

---

# DSA Class Notes - Page Context 12 (Pages 056-060)

## Page 056
**Date:** 25 Jan, 2026  
**Instructor:** Foysal Sir  

### AVL Tree (Adelson-Velsky and Landis)
1. It is a self-balancing **Binary Search Tree (BST)**.
2. **Balance Property:** For every node, the height difference between the left and right subtrees (Balance Factor) must be **0, 1, or -1**.
3. **Constraint:** $\text{Left Subtree} < \text{Root} < \text{Right Subtree}$.

**Balance Factor (BF) Formula:**
$$BF = \text{Height}(\text{Left Subtree}) - \text{Height}(\text{Right Subtree})$$

**Balancing Methods (Rotations):**
- **Left Rotation (L):** Used for RR imbalance.
- **Right Rotation (R):** Used for LL imbalance.
- **Left-Right Rotation (LR):** Double rotation for LR imbalance.
- **Right-Left Rotation (RL):** Double rotation for RL imbalance.

---

## Page 057
**AVL Rotations - Detailed Scenarios**

1. **LL Problem → Right Rotation:**
   - Case: A new node is inserted into the left subtree of the left child.
   - Action: Perform a single **Right Rotation** on the parent node.
2. **RR Problem → Left Rotation:**
   - Case: A new node is inserted into the right subtree of the right child.
   - Action: Perform a single **Left Rotation** on the parent node.
3. **RL Problem → RL Rotation:**
   - Case: A new node is inserted into the left subtree of the right child.
   - Action: First, a **Right Rotation** on the right child, then a **Left Rotation** on the root.

---

## Page 058
**AVL Tree Construction Example**

**Data Sequence:** `14, 17, 11, 7, 53, 4, 13, 12`

**Step-by-Step Construction:**
- Insert 14, 17, 11: Tree is balanced.
- Insert 7, 53: Tree is balanced.
- Insert 4: Node 11 becomes imbalanced ($BF=2$). Perform **Right Rotation** at 11.
- Insert 13: Imbalance occurs.
- Insert 12: Complex imbalance occurs requiring **R-L Rotation**.

**Rule:** Always keep the tree balanced after every insertion.

---

## Page 059 & 060
**Date:** 28 Jan, 2026  
**Instructor:** Foysal Sir  

### Binary Search Tree (BST) & Exam Prep
- **BST Property:** $\text{Left Child} < \text{Root} < \text{Right Child}$.
- **Construction Example:** `10, 5, 14, 4, 6, 4.5`
- Shows the resulting BST structure where 4.5 is the right child of 4.

**CT-3 (Class Test) Syllabus/Important Topics:**
1. **BST:** Insertion and Deletion algorithms.
2. **AVL Tree:** Construction and Rotations.
3. **Traversals:** Inorder, Preorder, Postorder.
4. **Mathematics:** Calculating Height and Depth of trees/nodes.
5. **B-Tree:** (Note: Marked as "Need to see").

**Special Note:** In case of same values, the left side is preferred (as per course convention).

<br>

---
[⬅️ Previous](./pagecontext11.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext13.md)
