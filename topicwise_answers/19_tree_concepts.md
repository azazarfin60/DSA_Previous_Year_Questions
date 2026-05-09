[⬅️ Previous](./18_backtracking.md) | [🏠 Home](./README.md) | [Next ➡️](./20_performance.md)

---

# Tree Concepts — Definitions, Representation, B-tree, Huffman


---

## [2017] 4(c) What is 2-tree? (02)

A **2-tree** (also called an **extended binary tree** or **strictly binary tree**) is a binary tree in which every node has either **0 children (leaf)** or exactly **2 children (internal node)**. No node has exactly one child.

**Properties:**
- If there are n internal nodes, there are (n+1) leaf nodes
- Leaf nodes are called **external nodes** (often shown as squares)
- Internal nodes are called **circular nodes**

```
       A          ← internal (2 children)
      / \
     B   C        ← B is internal, C is leaf (external)
    / \
   □   □          ← external nodes
```

---

# Section B

---


---

## [2017] 8(a) Advantages of BST over sorted array and linked list. (03)

| Operation | Sorted Array | Linked List | BST (balanced) |
|---|---|---|---|
| Search | O(log n) | O(n) | **O(log n)** |
| Insert | O(n) shifting | O(n) finding | **O(log n)** |
| Delete | O(n) shifting | O(n) finding | **O(log n)** |
| Space | Fixed size | Dynamic | Dynamic |

**Key Advantages:**
1. BST provides O(log n) search like sorted array, BUT also O(log n) insert/delete unlike sorted array which needs O(n) shifting.
2. BST allows dynamic size like linked list, BUT provides O(log n) search unlike linked list's O(n).
3. BST combines the best of both — fast search AND fast insert/delete.

---


---

## [2019] Q.4(d) What is sparse matrix? (02)

A **sparse matrix** is a matrix in which the majority of elements are **zero**. Only a small number of elements have non-zero values.

**Example:**
```
0  0  0  5
0  8  0  0
0  0  0  0
0  6  0  0
```
Out of 16 elements, only 3 are non-zero → sparse.

**Efficient storage:** Instead of storing all elements, store only non-zero values as triplets: (row, column, value).
```
(0, 3, 5)
(1, 1, 8)
(3, 1, 6)
```
This saves significant memory for large sparse matrices.

---


---

## [2020] Q.2(c) Store binary tree using array. (04)

**Array Representation Rules:**
- Root at index 1
- Left child of node at index i = **2i**
- Right child of node at index i = **2i + 1**

**Given tree:** A(root), B(left of A), C(right of A), D(left of B), E(right of C), F(left of D), G(right of D), H(left of G)

**Mapping:**

| Index | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Node | A | B | C | D | — | — | E | F | — | G | H |

**Explanation:**
- A at 1, B at 2 (left of 1), C at 3 (right of 1)
- D at 4 (left of 2), E at 7 (right of 3)
- F at 8 (left of 4), G at 10 (right of... wait)

The tree structure shows G as right child of D (index 4), so G at 2×4+1 = 9. H as left of G at 2×9 = 18... This requires a larger array but many positions are empty — showing the **disadvantage** of array representation for non-complete trees (wasted space).

---


---

## [2022] Q.8(c) Define graph. Why linked representation is better. (CO1, 02)

**Graph:** A non-linear data structure consisting of a set of **vertices (V)** and **edges (E)** that connect pairs of vertices. G = (V, E).

**Why linked (adjacency list) representation is better than array (adjacency matrix):**

1. **Space:** Adjacency list uses O(V+E) space vs O(V²) for matrix — much better for sparse graphs
2. **Adding vertices:** Easy in list (add node), expensive in matrix (resize entire 2D array)
3. **Iterating neighbors:** O(degree) in list vs O(V) in matrix
4. **Real-world graphs** are usually sparse, making adjacency list the preferred choice

---

## [2023] Q.2(b) Huffman Tree from weights: 4, 3, 8, 2, 15, 25, 40. (CLO2, 03)

**Step-by-step (combine two smallest each time):**

**Step 1:** Sort: 2, 3, 4, 8, 15, 25, 40
Combine 2+3 = 5 → {4, 5, 8, 15, 25, 40}

**Step 2:** Combine 4+5 = 9 → {8, 9, 15, 25, 40}

**Step 3:** Combine 8+9 = 17 → {15, 17, 25, 40}

**Step 4:** Combine 15+17 = 32 → {25, 32, 40}

**Step 5:** Combine 25+32 = 57 → {40, 57}

**Step 6:** Combine 40+57 = 97 (root)

**Huffman Tree:**
```
            97
          /    \
        57      40
       /  \
      32   25
     /  \
    15   17
        /  \
       8    9
           / \
          4   5
             / \
            2   3
```

---


---

## [2023] Q.3(c) Path vs Simple Path. (CLO1, 02)

**Path:** A sequence of vertices v₁, v₂, ..., vₖ where each consecutive pair (vᵢ, vᵢ₊₁) is connected by an edge. Vertices **may repeat**.

**Simple Path:** A path where **no vertex is repeated** (except possibly the first and last for a cycle).

**Example:** In graph A—B—C—D—B—E:
- A→B→C→D→B→E is a **path** (B repeats)
- A→B→C→D is a **simple path** (no repeat)

---


---

## [2023] Q.5(a) Define: Root, Child, Depth, Leaf, Parent. (CLO1, 03)

```
         A          ← Root, Parent of B and C
        / \
       B   C        ← B is Child of A, Parent of D,E
      / \    \
     D   E    F     ← D, E, F are Leaf nodes
```

1. **Root:** The topmost node with no parent. (A)
2. **Child Node:** A node directly connected below another node. (B, C are children of A)
3. **Depth:** The number of edges from the root to a node. (Depth of D = 2)
4. **Leaf:** A node with no children. (D, E, F)
5. **Parent Node:** A node directly above another node. (A is parent of B and C)

---


---

## 📊 Exam Priority
**Priority: 2/5** (Should Prepare)
**Appeared in:** 7/8 years (various tree topics)
**Typical marks:** 02–04 per question

<br>

---
[⬅️ Previous](./18_backtracking.md) | [🏠 Home](./README.md) | [Next ➡️](./20_performance.md)
