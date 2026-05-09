[⬅️ Previous](./09_trees_fundamentals.md) | [🏠 Home](./README.md) | [Next ➡️](./11_heap_and_btree.md)

---

# 📘 Chapter 10: Binary Search Tree (BST) & Tree Traversals

> **Exam Frequency:** 8/8 years | **Typical Marks:** 04–06 | **Section:** A
> **Key Topics:** BST construction, search, insert, delete, Inorder/Preorder/Postorder traversal

---

## 1. What is a Binary Search Tree?

A **BST** is a binary tree where for every node:
- All values in the **left subtree** are **less than** the node's value
- All values in the **right subtree** are **greater than** the node's value

This property holds **recursively** for every subtree.

```
        50
       /  \
     30    70
    / \   / \
   20 40 60  80

For node 50: Left(30,20,40) < 50 < Right(70,60,80) ✓
For node 30: Left(20) < 30 < Right(40) ✓
For node 70: Left(60) < 70 < Right(80) ✓
```

### Why BST?
| Operation | Array (unsorted) | Array (sorted) | Linked List | **BST (balanced)** |
|---|---|---|---|---|
| Search | O(n) | O(log n) | O(n) | **O(log n)** |
| Insert | O(1) | O(n) | O(1) | **O(log n)** |
| Delete | O(n) | O(n) | O(n) | **O(log n)** |

BST provides O(log n) for ALL three operations — the best of both worlds.

---

## 2. BST Construction

### Algorithm
To insert a value into a BST:
1. Start at the root
2. If value < current node → go left
3. If value > current node → go right
4. When you reach NULL → insert here

### Example: Construct BST from [50, 30, 70, 20, 40, 60, 80, 10, 35]

```
Insert 50:     50

Insert 30:     50
              /
            30

Insert 70:     50
              / \
            30   70

Insert 20:     50
              / \
            30   70
           /
         20

Insert 40:     50
              / \
            30   70
           / \
         20   40

Insert 60:     50
              / \
            30   70
           / \  /
         20  40 60

Insert 80:     50
              / \
            30   70
           / \  / \
         20  40 60  80

Insert 10:     50
              / \
            30   70
           / \  / \
         20  40 60  80
        /
       10

Insert 35:     50
              / \
            30   70
           / \  / \
         20  40 60  80
        /   /
       10  35
```

### Pseudocode
```c
struct Node* insert(struct Node* root, int key) {
    if (root == NULL) {                // base case: found position
        struct Node* newNode = createNode(key);
        return newNode;
    }
    if (key < root->data)
        root->left = insert(root->left, key);    // go left
    else if (key > root->data)
        root->right = insert(root->right, key);  // go right
    // if key == root->data, duplicate — ignore
    return root;
}
```

---

## 3. BST Search

```c
struct Node* search(struct Node* root, int key) {
    if (root == NULL || root->data == key)
        return root;                   // not found or found
    if (key < root->data)
        return search(root->left, key);    // search left
    else
        return search(root->right, key);   // search right
}
```

**Trace: Search for 40 in the BST above**
```
At 50: 40 < 50 → go left
At 30: 40 > 30 → go right
At 40: 40 = 40 → FOUND! ✓
Comparisons: 3
```

**Complexity:** O(h) where h = height. Best: O(log n), Worst: O(n) (skewed tree).

---

## 4. Tree Traversals

Traversal means visiting every node in the tree exactly once. There are three depth-first traversals and one level-order traversal.

### 4.1 Inorder Traversal (Left → Root → Right)

**C++ Style:**
```cpp
void inorder(Node* root) {
    if (root != nullptr) {
        inorder(root->left);       // visit left subtree
        cout << root->data << " "; // visit root
        inorder(root->right);      // visit right subtree
    }
}
```

**OR, Textbook Style:**
```
Procedure INORDER(node)
    If node ≠ NULL Then
        INORDER(node.left)         // visit left subtree
        Process(node.data)         // visit root
        INORDER(node.right)        // visit right subtree
    End If
End Procedure
```

**Key Property:** Inorder traversal of a BST gives elements in **sorted (ascending) order**.

**Example on our BST:**
```
        50
       / \
     30   70
    / \  / \
   20 40 60 80
  /  /
 10 35

Inorder: 10, 20, 30, 35, 40, 50, 60, 70, 80  ← sorted! ✓
```

**Detailed trace:**
```
INORDER(50)
  INORDER(30)
    INORDER(20)
      INORDER(10)
        INORDER(NULL) → return
        Print 10
        INORDER(NULL) → return
      Print 20
      INORDER(NULL) → return
    Print 30
    INORDER(40)
      INORDER(35)
        INORDER(NULL) → return
        Print 35
        INORDER(NULL) → return
      Print 40
      INORDER(NULL) → return
  Print 50
  INORDER(70)
    INORDER(60)
      INORDER(NULL) → return
      Print 60
      INORDER(NULL) → return
    Print 70
    INORDER(80)
      INORDER(NULL) → return
      Print 80
      INORDER(NULL) → return

Output: 10 20 30 35 40 50 60 70 80
```

### 4.2 Preorder Traversal (Root → Left → Right)

**C++ Style:**
```cpp
void preorder(Node* root) {
    if (root != nullptr) {
        cout << root->data << " "; // visit root FIRST
        preorder(root->left);      // visit left subtree
        preorder(root->right);     // visit right subtree
    }
}
```

**OR, Textbook Style:**
```
Procedure PREORDER(node)
    If node ≠ NULL Then
        Process(node.data)         // visit root FIRST
        PREORDER(node.left)        // visit left subtree
        PREORDER(node.right)       // visit right subtree
    End If
End Procedure
```

**Example:** `50, 30, 20, 10, 40, 35, 70, 60, 80`

**Use:** Creates a copy of the tree. Used to serialize/reconstruct a tree.

### 4.3 Postorder Traversal (Left → Right → Root)

**C++ Style:**
```cpp
void postorder(Node* root) {
    if (root != nullptr) {
        postorder(root->left);     // visit left subtree
        postorder(root->right);    // visit right subtree
        cout << root->data << " "; // visit root LAST
    }
}
```

**OR, Textbook Style:**
```
Procedure POSTORDER(node)
    If node ≠ NULL Then
        POSTORDER(node.left)       // visit left subtree
        POSTORDER(node.right)      // visit right subtree
        Process(node.data)         // visit root LAST
    End If
End Procedure
```

**Example:** `10, 20, 35, 40, 30, 60, 80, 70, 50`

**Use:** Used to delete/free a tree (delete children before parent).

### 4.4 Level-Order Traversal (BFS on Tree)

Visit nodes level by level, left to right. Uses a **queue**.

**C++ Style:**
```cpp
#include <queue>

void levelOrder(Node* root) {
    if (root == nullptr) return;
    
    queue<Node*> q;
    q.push(root);
    
    while (!q.empty()) {
        Node* curr = q.front();
        q.pop();
        
        cout << curr->data << " ";
        
        if (curr->left != nullptr) q.push(curr->left);
        if (curr->right != nullptr) q.push(curr->right);
    }
}
```

**OR, Textbook Style:**
```
Procedure LEVEL_ORDER(root)
    Create empty Queue Q
    ENQUEUE(Q, root)
    While Q is not empty do
        node = DEQUEUE(Q)
        Process(node.data)
        If node.left ≠ NULL Then ENQUEUE(Q, node.left)
        If node.right ≠ NULL Then ENQUEUE(Q, node.right)
    End While
End Procedure
```

**Example:** `50, 30, 70, 20, 40, 60, 80, 10, 35`

### 4.5 Traversal Summary

| Traversal | Order | Mnemonic | BST gives | Use |
|---|---|---|---|---|
| **Inorder** | L → Root → R | "Left, Root, Right" | **Sorted order** | Sorting, validation |
| **Preorder** | Root → L → R | "Root, Left, Right" | Tree copy/serialization | |
| **Postorder** | L → R → Root | "Left, Right, Root" | Delete order | Freeing memory |
| **Level-order** | Level by level | "BFS" | Breadth-first | Printing level-wise |

### Memory Trick
- In**order** → root in the **middle** (L **Root** R)
- **Pre**order → root comes **first** (**Root** L R)
- **Post**order → root comes **last** (L R **Root**)

---

## 5. BST Deletion

Three cases when deleting a node:

### Case 1: Node is a Leaf (no children)
Simply remove it.
```
Delete 10:       50              50
                / \            / \
              30   70   →    30   70
             / \              \
            20  40             40
           /
          10
```

### Case 2: Node has One Child
Replace the node with its child.
```
Delete 20:       50              50
                / \            / \
              30   70   →    30   70
             / \            / \
            20  40         10  40
           /
          10
```

### Case 3: Node has Two Children
Replace with **inorder successor** (smallest value in right subtree) or **inorder predecessor** (largest value in left subtree). Then delete that successor/predecessor.

```
Delete 30:       50
                / \
              30   70          Inorder successor of 30 = 35
             / \  / \          (smallest in right subtree of 30)
            20  40 60  80
               /
              35

Replace 30 with 35, then delete 35 from its original position:

                 50
                / \
              35   70
             / \  / \
            20  40 60  80
```

### Deletion Algorithm
```c
struct Node* deleteNode(struct Node* root, int key) {
    if (root == NULL) return root;
    
    if (key < root->data)
        root->left = deleteNode(root->left, key);
    else if (key > root->data)
        root->right = deleteNode(root->right, key);
    else {
        // Found the node to delete
        // Case 1 & 2: No child or one child
        if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        }
        if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }
        // Case 3: Two children
        struct Node* succ = findMin(root->right);  // inorder successor
        root->data = succ->data;                   // copy successor's value
        root->right = deleteNode(root->right, succ->data); // delete successor
    }
    return root;
}

struct Node* findMin(struct Node* node) {
    while (node->left != NULL)
        node = node->left;
    return node;
}
```

---

## 6. BST Construction from Exam Data

### Example (2021, 2023): Insert J, R, D, G, T, E, M, H, P, A, F, Q

```
Insert J:      J

Insert R:      J
                \
                 R

Insert D:      J
              / \
             D   R

Insert G:      J
              / \
             D   R
              \
               G

Insert T:      J
              / \
             D   R
              \    \
               G    T

Insert E:      J
              / \
             D   R
              \    \
               G    T
              /
             E

Insert M:      J
              / \
             D   R
              \  / \
               G M   T
              /
             E

Insert H:      J
              / \
             D     R
              \   / \
               G  M   T
              / \
             E   H

Insert P:      J
              / \
             D     R
              \   / \
               G  M   T
              / \ /
             E  H P

Wait — P goes: J→R(P<R, go left)→M(P>M, go right)
Actually:
               J
              / \
             D     R
              \   / \
               G  M   T
              / \  \
             E  H   P

Insert A:      J
              / \
             D     R
            / \   / \
           A   G  M   T
              / \  \
             E  H   P

Insert F:      J
              / \
             D     R
            / \   / \
           A   G  M   T
              / \  \
             E  H   P
              \
               F

Insert Q:      J
              / \
             D     R
            / \   / \
           A   G  M   T
              / \  \
             E  H   P
              \    /
               F  Q

Wait — Q: J→R→M→P→Q(Q>P, right of P)
               J
              / \
             D     R
            / \   / \
           A   G  M   T
              / \  \
             E  H   P
              \   / \
               F Q   (nothing)

Actually Q > P, so right of P:
              ... P
                   \
                    Q
```

**Traversals of this BST:**
- **Inorder:** A, D, E, F, G, H, J, M, P, Q, R, T (sorted ✓)
- **Preorder:** J, D, A, G, E, F, H, R, M, P, Q, T
- **Postorder:** A, F, E, H, G, D, Q, P, M, T, R, J

---

## 7. Tree Construction from Traversals

### Given Inorder + Preorder → Construct Tree

**Rule:** First element of Preorder is always the root. Find it in Inorder — everything left of it is the left subtree, everything right is the right subtree.

**Example:** Inorder: D B E A F C, Preorder: A B D E C F

```
Step 1: Root = A (first of preorder)
  Inorder: [D B E] A [F C]
  Left subtree: D B E,  Right subtree: F C

Step 2: Left subtree root = B (next in preorder)
  Inorder of left: [D] B [E]
  B's left = D, B's right = E

Step 3: Right subtree root = C (next unused in preorder)
  Inorder of right: [F] C
  C's left = F

Result:
        A
       / \
      B   C
     / \ /
    D  E F
```

### Given Inorder + Postorder → Construct Tree

**Rule:** Last element of Postorder is the root. Process from right to left.

---

## 8. AVL Tree (Adelson-Velsky and Landis)

### 8.1 Definition
An **AVL tree** is a **self-balancing Binary Search Tree** where the difference between the heights of the left and right subtrees of every node is at most 1.

> **Balance Factor (BF) = Height(Left Subtree) − Height(Right Subtree)**
> 
> For every node in an AVL tree: **BF ∈ {-1, 0, +1}**

### Intuition
A regular BST can become skewed (like a linked list) with bad insertion order, making operations O(n). AVL trees prevent this by **rebalancing** after every insertion/deletion, guaranteeing O(log n) operations.

### 8.2 Why AVL Trees?

| Tree Type | Search | Insert | Delete |
|---|---|---|---|
| BST (balanced) | O(log n) | O(log n) | O(log n) |
| BST (skewed) | O(n) | O(n) | O(n) |
| **AVL Tree** | **O(log n) guaranteed** | **O(log n) guaranteed** | **O(log n) guaranteed** |

### 8.3 Rotations

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

### 8.4 AVL Insertion Example

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

## 9. BST Advantages Over Array and Linked List

This is asked in **2017, 2021, 2024**.

| Criterion | Array | Linked List | BST (balanced) |
|---|---|---|---|
| Search | O(n) unsorted / O(log n) sorted | O(n) | **O(log n)** |
| Insert | O(1) end / O(n) sorted | O(1) at head | **O(log n)** |
| Delete | O(n) | O(n) find + O(1) remove | **O(log n)** |
| Sorted traversal | O(n log n) to sort first | O(n log n) | **O(n)** — just inorder |
| Memory | Contiguous, fixed | Dynamic, extra pointers | Dynamic, extra pointers |

> **BST advantage:** It provides O(log n) for search, insert, AND delete simultaneously — neither array nor linked list can do this.

---

## 10. Exam-Ready Summary

### Quick Revision Points
1. **BST property:** Left < Root < Right (recursively)
2. **Inorder traversal of BST = sorted order** — most important property
3. **Construction:** Compare with current → go left/right → insert at NULL
4. **Deletion 3 cases:** leaf (remove), one child (bypass), two children (replace with inorder successor)
5. **Inorder successor:** smallest node in right subtree (go right once, then keep going left)
6. **Traversal mnemonics:** Pre=Root first, In=Root middle, Post=Root last
7. **AVL:** Self-balancing BST, BF ∈ {-1,0,+1}, 4 rotation cases (LL, RR, LR, RL)

### Most Common Exam Questions
- BST construction + all 3 traversals (2017–2024, every year, 04–06 marks)
- BST deletion (2023, 2024, 04 marks)
- BST advantages over array and LL (2017, 2021, 2024, 02–03 marks)
- Tree construction from given traversals (03–04 marks)

---

## 11. Practice Problems (From Past Exams)

### Problem 1 [2023, CLO4, 06 marks]
**Q:** Construct BST from J, R, D, G, T, E, M, H, P, A, F, Q. Show inorder, preorder, postorder. Delete G.

**Approach:** See Section 6 above. For deletion of G (has 2 children E and H): inorder successor = H, replace G with H.

### Problem 2 [2017, 2021, 02–03 marks]
**Q:** What are the advantages of BST over array and linked list?

**Approach:** 4-row comparison table showing BST gives O(log n) for all operations.

### Problem 3 [Typical, 04 marks]
**Q:** Construct a tree given: Inorder: D B E A F C G, Preorder: A B D E C F G

**Solution:** Root=A, left subtree inorder=[D B E], right=[F C G]. Continue recursively.

---

*← [09 — Trees Fundamentals](09_trees_fundamentals.md) | Next: [11 — Heap and B-Tree →](11_heap_and_btree.md)*

<br>

---
[⬅️ Previous](./09_trees_fundamentals.md) | [🏠 Home](./README.md) | [Next ➡️](./11_heap_and_btree.md)
