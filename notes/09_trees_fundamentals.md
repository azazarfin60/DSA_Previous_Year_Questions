# 📘 Chapter 9: Trees — Fundamentals

> **Exam Frequency:** 7–8/8 years (combined tree topics) | **Typical Marks:** 02–06 | **Section:** A/B
> **Key Topics:** Terminology, Binary Tree types, Height/Level, Max/Min nodes, 2-tree, AVL, B-tree

---

## 1. What is a Tree?

A **tree** is a non-linear, hierarchical data structure consisting of **nodes** connected by **edges**. It has one special node called the **root**, and every other node has exactly one parent.

### Intuition
Think of a **family tree** — one ancestor at the top (root), with children branching out below, each child can have their own children, and so on. Or a **file system** — root folder contains subfolders, which contain more subfolders and files.

```
            A           ← Root
          / | \
        B   C   D       ← Children of A
       / \     / \
      E   F   G   H     ← Children of B and D
         /
        I               ← Child of F
```

---

## 2. Tree Terminology (Important — asked frequently)

| Term | Definition | Example (above tree) |
|---|---|---|
| **Root** | Topmost node with no parent | A |
| **Parent** | Node with children below it | B is parent of E, F |
| **Child** | Node directly below a parent | E, F are children of B |
| **Sibling** | Nodes sharing the same parent | E and F are siblings |
| **Leaf** | Node with no children (terminal node) | E, I, G, H, C |
| **Internal node** | Node with at least one child | A, B, D, F |
| **Edge** | Connection between parent and child | A—B, B—E, etc. |
| **Path** | Sequence of nodes connected by edges | A → B → F → I |
| **Ancestor** | Any node on the path from root to that node | Ancestors of I: F, B, A |
| **Descendant** | Any node reachable going down from a node | Descendants of B: E, F, I |

### Degree, Depth, Height, Level

| Term | Definition | Example |
|---|---|---|
| **Degree of a node** | Number of children of that node | Degree(A)=3, Degree(B)=2, Degree(E)=0 |
| **Degree of tree** | Maximum degree among all nodes | Degree(tree)=3 (node A) |
| **Level of a node** | Root is level 0 (or 1). Level = distance from root | Level(A)=0, Level(B)=1, Level(E)=2 |
| **Depth of a node** | Number of edges from root to that node | Depth(I)=3, Depth(B)=1 |
| **Height of a node** | Number of edges on longest path from that node to a leaf | Height(A)=3, Height(B)=2, Height(E)=0 |
| **Height of tree** | Height of the root node = longest path from root to any leaf | Height=3 (A→B→F→I) |

### Visual Summary
```
  Level 0:        A          Height of tree = 3
                / | \
  Level 1:     B   C   D
              / \     / \
  Level 2:   E   F   G   H
                /
  Level 3:     I           ← deepest leaf
```

---

## 3. Binary Tree

### 3.1 Definition
A **binary tree** is a tree where each node has **at most 2 children** — called the **left child** and **right child**.

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

### 3.2 Types of Binary Trees

#### Full Binary Tree (Proper / Strictly Binary / 2-tree)
Every node has **exactly 0 or 2 children** (no node has only 1 child).

```
        A                    A
       / \                  / \
      B   C                B   C
     / \                  / \  / \
    D   E                D  E F   G
    
    Full ✓             Full ✓
```

```
        A
       / \
      B   C
     /
    D
    
    NOT Full ✗  (B has only 1 child)
```

#### Complete Binary Tree
All levels are completely filled **except possibly the last level**, which is filled from **left to right**.

```
        A                    A
       / \                  / \
      B   C                B   C
     / \  /               / \
    D   E F              D   E
    
    Complete ✓           Complete ✓
```

```
        A
       / \
      B   C
       \
        E
    
    NOT Complete ✗  (B's left child missing but right exists)
```

#### Perfect Binary Tree
ALL internal nodes have exactly 2 children AND all leaves are at the **same level**.

```
        A
       / \
      B   C
     / \ / \
    D  E F  G
    
    Perfect ✓  (all leaves at level 2, all internal nodes have 2 children)
```

#### Degenerate (Skewed) Binary Tree
Every node has at most **one child** — essentially becomes a linked list.

```
    A               A
     \             /
      B           B
       \         /
        C       C
         \     /
          D   D
    
  Right-skewed   Left-skewed
```

### 3.3 Comparison Table

| Type | Rule | Leaves at same level? | Every node 0 or 2 children? |
|---|---|---|---|
| **Full** | Each node has 0 or 2 children | Not necessarily | ✅ Yes |
| **Complete** | All levels full except last (left-filled) | Not necessarily | Not necessarily |
| **Perfect** | All levels completely full | ✅ Yes | ✅ Yes |
| **Degenerate** | Each node has 0 or 1 child | No | No |

**Relationship:** Every Perfect tree is both Full and Complete. Not every Full tree is Complete, and vice versa.

---

## 4. Binary Tree Properties — Max/Min Nodes & Height

### 4.1 Key Formulas

| Property | Formula |
|---|---|
| Max nodes at level L | **2^L** (if root is level 0) |
| Max total nodes in tree of height h | **2^(h+1) − 1** |
| Min height for n nodes | **⌊log₂(n)⌋** |
| Max height for n nodes | **n − 1** (degenerate/skewed tree) |
| Number of leaves in a Full binary tree with n internal nodes | **n + 1** |
| Total nodes in a Perfect tree of height h | **2^(h+1) − 1** |

### 4.2 Worked Examples

**Q: Maximum nodes in a binary tree of height 4?**
```
Max nodes = 2^(h+1) − 1 = 2^5 − 1 = 32 − 1 = 31
```

**Q: Minimum height of a binary tree with 15 nodes?**
```
Min height = ⌊log₂(15)⌋ = ⌊3.9⌋ = 3
(A perfect binary tree of height 3 has 2⁴−1 = 15 nodes ✓)
```

**Q: A full binary tree has 7 internal nodes. How many leaves?**
```
Leaves = internal nodes + 1 = 7 + 1 = 8
```

**Q: How many nodes at level 3?**
```
Max nodes at level 3 = 2³ = 8
```

### 4.3 Height Calculation Algorithm

```c
int height(struct Node* root) {
    if (root == NULL)
        return -1;                    // empty tree has height -1
    int leftH = height(root->left);
    int rightH = height(root->right);
    return 1 + max(leftH, rightH);    // 1 + taller subtree
}
```

**Trace:**
```
        A
       / \
      B   C
     /
    D

height(D) = -1+1 = 0  (leaf)
height(B) = 1 + max(height(D), height(NULL)) = 1 + max(0, -1) = 1
height(C) = 0  (leaf)
height(A) = 1 + max(height(B), height(C)) = 1 + max(1, 0) = 2

Height of tree = 2 ✓
```

---

## 5. 2-Tree (Extended Binary Tree)

### Definition
A **2-tree** (or **extended binary tree**) is a binary tree where every node has **exactly 0 or 2 children** (same as a Full Binary Tree).

Nodes with 2 children are called **internal nodes** (shown as circles).
Nodes with 0 children are called **external nodes** (shown as squares).

```
        ●
       / \
      ●   ●
     / \ / \
    □  □ □  □
    
    ● = internal node (circle)
    □ = external node (square)
```

### Properties of 2-Tree
1. If there are `n` internal nodes, there are exactly `n + 1` external nodes
2. Every path from root to an external node passes through only internal nodes
3. Used in **Huffman coding** and **weighted path length** calculations

### Weighted Path Length
- **Internal path length (I):** Sum of depths of all internal nodes
- **External path length (E):** Sum of depths of all external nodes
- **Relation:** E = I + 2n (where n = number of internal nodes)

---

## 6. AVL Tree (Adelson-Velsky and Landis)

### 6.1 Definition
An **AVL tree** is a **self-balancing Binary Search Tree** where the difference between the heights of the left and right subtrees of every node is at most 1.

> **Balance Factor (BF) = Height(Left Subtree) − Height(Right Subtree)**
> 
> For every node in an AVL tree: **BF ∈ {-1, 0, +1}**

### Intuition
A regular BST can become skewed (like a linked list) with bad insertion order, making operations O(n). AVL trees prevent this by **rebalancing** after every insertion/deletion, guaranteeing O(log n) operations.

### 6.2 Why AVL Trees?

| Tree Type | Search | Insert | Delete |
|---|---|---|---|
| BST (balanced) | O(log n) | O(log n) | O(log n) |
| BST (skewed) | O(n) | O(n) | O(n) |
| **AVL Tree** | **O(log n) guaranteed** | **O(log n) guaranteed** | **O(log n) guaranteed** |

### 6.3 Rotations

When an insertion/deletion causes a node's balance factor to become ±2, we perform **rotations** to rebalance.

#### Case 1: Left-Left (LL) → Right Rotation
```
Before (BF of A = +2):        After Right Rotation:
        A (+2)                       B (0)
       /                            / \
      B (+1)                       C   A
     /
    C

Right Rotate around A: B becomes root, A becomes B's right child.
```

#### Case 2: Right-Right (RR) → Left Rotation
```
Before (BF of A = -2):        After Left Rotation:
    A (-2)                         B (0)
     \                            / \
      B (-1)                     A   C
       \
        C

Left Rotate around A: B becomes root, A becomes B's left child.
```

#### Case 3: Left-Right (LR) → Left Rotation then Right Rotation
```
Before:                   After Left Rotate at B:    After Right Rotate at A:
    A (+2)                      A (+2)                      C (0)
   /                           /                           / \
  B (-1)                      C (+1)                      B   A
   \                         /
    C                       B

Step 1: Left rotate around B
Step 2: Right rotate around A
```

#### Case 4: Right-Left (RL) → Right Rotation then Left Rotation
```
Before:                   After Right Rotate at B:   After Left Rotate at A:
  A (-2)                    A (-2)                        C (0)
   \                         \                           / \
    B (+1)                    C (-1)                    A   B
   /                           \
  C                             B

Step 1: Right rotate around B
Step 2: Left rotate around A
```

### 6.4 AVL Insertion Example

Insert: 10, 20, 30, 25, 28

```
Insert 10:       10 (BF=0)

Insert 20:       10 (BF=-1)
                   \
                    20

Insert 30:       10 (BF=-2)  ← UNBALANCED! RR case
                   \
                    20 (BF=-1)
                      \
                       30

After Left Rotation at 10:
                 20 (BF=0)
                /  \
              10    30

Insert 25:       20 (BF=-1)
                /  \
              10    30 (BF=+1)
                   /
                  25

Insert 28:       20 (BF=-2)  ← UNBALANCED at 20!
                /  \
              10    30 (BF=+2) ← UNBALANCED at 30! (LR case at 30)
                   /
                  25 (BF=-1)
                    \
                     28

Fix at 30: LR case
Step 1: Left rotate at 25:    Step 2: Right rotate at 30:
        30                           28
       /                            / \
      28                           25  30
     /
    25

Result:
                 20
                /  \
              10    28
                   / \
                  25  30
All BFs ∈ {-1, 0, +1} ✓
```

---

## 7. B-Tree

### 7.1 Definition
A **B-tree of order m** is a self-balancing search tree designed for systems that read and write large blocks of data (disk-based storage). Every node can have **up to m children** and **up to m−1 keys**.

### 7.2 Properties of B-tree of order m:
1. Every node has **at most m children**
2. Every node (except root) has **at least ⌈m/2⌉ children**
3. The root has **at least 2 children** (if it's not a leaf)
4. All **leaves appear at the same level**
5. A non-leaf node with k children contains **k−1 keys**
6. Keys within a node are in **sorted order**

### 7.3 Example: B-tree of order 3 (2-3 tree)
Each node has at most 3 children and 2 keys.

```
              [20, 40]
             /   |    \
      [10,15] [25,30] [50,60]
```

### 7.4 Why B-trees?
- Designed for **disk-based storage** where reading a large block is efficient
- **Minimizes disk I/O** — each node read brings many keys
- Used in **databases** and **file systems**
- All operations are O(log n) with a very large branching factor

### 7.5 B-tree vs BST

| Criterion | BST | B-tree |
|---|---|---|
| Max children per node | 2 | m (can be thousands) |
| Height for n keys | O(log₂ n) | O(log_m n) — much shorter |
| Best for | In-memory data | Disk-based data |
| Balance | Not guaranteed (unless AVL/RB) | Always balanced |
| Keys per node | 1 | Up to m−1 |

---

## 8. Exam-Ready Summary

### Quick Revision Points
1. **Tree terms:** Root, Leaf, Degree, Depth, Height, Level
2. **Binary tree types:** Full (0 or 2 children), Complete (left-filled), Perfect (all full)
3. **Max nodes height h:** 2^(h+1) − 1. **Min height for n nodes:** ⌊log₂(n)⌋
4. **2-tree:** Full binary tree. External nodes = Internal + 1
5. **AVL:** Self-balancing BST, BF ∈ {-1,0,+1}, 4 rotation cases (LL, RR, LR, RL)
6. **B-tree order m:** up to m children, m−1 keys per node, all leaves same level
7. **Height calculation:** recursive — `1 + max(left_height, right_height)`

---

## 9. Practice Problems (From Past Exams)

### Problem 1 [2017, 2018, 2024, 02–04 marks]
**Q:** Define 2-tree. If a 2-tree has n internal nodes, prove it has n+1 external nodes.

**Approach:** Definition → property → inductive argument or direct proof.

### Problem 2 [Typical, 03 marks]
**Q:** Find the maximum number of nodes in a binary tree of height 5. What is the minimum height for a tree with 100 nodes?

**Answer:** Max nodes = 2⁶ − 1 = 63. Min height = ⌊log₂(100)⌋ = 6.

### Problem 3 [2024, 03 marks]
**Q:** Define B-tree. State its properties for order 5.

**Answer:** Each node: max 5 children, max 4 keys, min ⌈5/2⌉=3 children (non-root), all leaves same level.

---

*← [08 — Recursion](08_recursion.md) | Next: [10 — BST and AVL →](10_bst_and_avl.md)*
