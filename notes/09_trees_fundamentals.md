[⬅️ Previous](./08_recursion.md) | [🏠 Home](./README.md) | [Next ➡️](./10_bst_and_avl.md)

---

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

## 6. AVL Tree

> **Note:** The comprehensive section on AVL Trees, including definitions, rotations, and detailed step-by-step insertions, has been moved to **[Chapter 10: BST and AVL](10_bst_and_avl.md)**.

---

## 7. B-Tree

> **Note:** The detailed section on B-Trees, including properties, order m, and comparisons with BST, has been moved to **[Chapter 11: Heap and B-Tree](11_heap_and_btree.md)**.

---

## 8. Exam-Ready Summary

### Quick Revision Points
1. **Tree terms:** Root, Leaf, Degree, Depth, Height, Level
2. **Binary tree types:** Full (0 or 2 children), Complete (left-filled), Perfect (all full)
3. **Max nodes height h:** 2^(h+1) − 1. **Min height for n nodes:** ⌊log₂(n)⌋
4. **2-tree:** Full binary tree. External nodes = Internal + 1
5. **Height calculation:** recursive — `1 + max(left_height, right_height)`

---

## 9. Practice Problems (From Past Exams)

### Problem 1 [2017, 2018, 2024, 02–04 marks]
**Q:** Define 2-tree. If a 2-tree has n internal nodes, prove it has n+1 external nodes.

**Approach:** Definition → property → inductive argument or direct proof.

### Problem 2 [Typical, 03 marks]
**Q:** Find the maximum number of nodes in a binary tree of height 5. What is the minimum height for a tree with 100 nodes?

**Answer:** Max nodes = 2⁶ − 1 = 63. Min height = ⌊log₂(100)⌋ = 6.

---

*← [08 — Recursion](08_recursion.md) | Next: [10 — BST and AVL →](10_bst_and_avl.md)*

<br>

---
[⬅️ Previous](./08_recursion.md) | [🏠 Home](./README.md) | [Next ➡️](./10_bst_and_avl.md)
