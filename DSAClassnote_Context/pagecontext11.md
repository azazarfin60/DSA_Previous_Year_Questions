[⬅️ Previous](./pagecontext10.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext12.md)

---

# DSA Class Notes - Page Context 11 (Pages 051-055)

## Page 051
**Tree Traversal Techniques**

**Three main types of Depth-First Traversal:**
1. **Preorder:** Root → Left → Right
2. **Inorder:** Left → Root → Right
3. **Postorder:** Left → Right → Root

**Example 1:**
- **Tree Structure:** Root(A), Left(B), Right(C). B has children D, E.
- **Preorder Result:** `A B D E C`

**Example 2 (Large Tree):**
- **Tree Structure:** Detailed hierarchical structure with nodes A to K.
- **Preorder Result:** `A B D L M N O E Q C F G H I J K`

---

## Page 052
**Tree Traversal: Inorder and Postorder (Example 2 Continued)**

- **Inorder Result:** (Based on the large tree from p.051)  
  `L D B E Q L N M O D B E Q A C G F J I K H` (Note: Labels in handwritten notes show multiple corrections).
- **Postorder Result:**  
  `N O M L D Q E B G J K I H F C A`

---

## Page 053
**Date:** 22 Jan, 2026  
**Instructor:** Foysal Sir  

### Tree Reconstruction from Traversals
To uniquely reconstruct a binary tree, we need:
- **Inorder** traversal AND
- Either **Preorder** OR **Postorder** traversal.

**Reconstruction Algorithm (Inorder + Preorder):**
1. If the traversal lists are empty, return `NULL`.
2. The **first element** of the Preorder list is the **Root** of the current (sub)tree.
3. Find the position of this Root in the Inorder list.
4. Elements to the **left** of the Root in the Inorder list belong to the **Left Subtree**.
5. Elements to the **right** of the Root in the Inorder list belong to the **Right Subtree**.
6. Recursively repeat steps 2-5 for the left and right subtrees.

**Example Traversals for Practice:**
- **Inorder:** `G E D H F I B A C`
- **Preorder:** `A B D E G F H I C`
- **Postorder:** `G E H I F D B C A`

---

## Page 054
**Tree Reconstruction Walkthrough**

**Example:**
- **Inorder:** `K G D L H M B A E C`
- **Preorder:** `A B D G K L H M C E`

**Step-by-Step Logic:**
1. **Root is A** (from Preorder).
2. In Inorder, `K G D L H M B` is on the left of `A`, and `E C` is on the right.
3. The next root for the left subtree is `B` (next in Preorder).
4. In the left part `K G D L H M B`, `K G D L H M` is on the left of `B`.
5. This continues recursively until the full tree is mapped.

---

## Page 055
**Reconstruction Example 2 and Postorder Calculation**

**Input:**
- **Inorder:** `I F B H A D C G E`
- **Preorder:** `A B F I H C D G E` (Corrected from visual)

**Reconstruction Process:**
- Shows the tree being built level by level based on identifying the root and splitting the inorder list.
- Final Tree is verified against the original diagram.

**Final Postorder Calculation for the Reconstructed Tree:**
- **Postorder:** `I F H B D G E C A`
- **Rule used:** Scan left subtree, then right subtree, then root.

<br>

---
[⬅️ Previous](./pagecontext10.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext12.md)
