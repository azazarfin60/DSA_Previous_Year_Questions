[⬅️ Previous](./04_queue.md) | [🏠 Home](./README.md) | [Next ➡️](./06_heap.md)

---

# Binary Search Tree — Construction, Traversal, Deletion


---

## [2017] 4(a) Construct tree from Inorder and Preorder. (05)

**Inorder:**  M N O P Q R S T U
**Preorder:** Q N M P O S R U T

**Step 1:** First element of Preorder = **Q** → Root
In Inorder, Q splits into: Left = {M, N, O, P}, Right = {R, S, T, U}

**Step 2:** Next in Preorder = **N** → Root of left subtree
In left Inorder {M, N, O, P}, N splits: Left = {M}, Right = {O, P}

**Step 3:** Next = **M** → Left child of N (leaf node)

**Step 4:** Next = **P** → Root of {O, P} subtree
In {O, P}, P splits: Left = {O}, Right = {}

**Step 5:** Next = **O** → Left child of P (leaf)

**Step 6:** Next = **S** → Root of right subtree {R, S, T, U}
In {R, S, T, U}, S splits: Left = {R}, Right = {T, U}

**Step 7:** Next = **R** → Left child of S (leaf)

**Step 8:** Next = **U** → Root of {T, U}
In {T, U}, U splits: Left = {T}, Right = {}

**Step 9:** Next = **T** → Left child of U (leaf)

```
            Q
           / \
          N    S
         / \  / \
        M  P R   U
          /     /
         O     T
```

---


---

## [2017] 4(b) BST from: 20, 15, 10, 30, 20, 40, 10, 12, 50, 10 (05)

**Step-by-step insertion (duplicates ignored in standard BST):**

Insert 20 → root
Insert 15 → 15 < 20, go left
Insert 10 → 10 < 20 < 15, go left of 15
Insert 30 → 30 > 20, go right
Insert 20 → duplicate, skip
Insert 40 → 40 > 30, go right of 30
Insert 10 → duplicate, skip
Insert 12 → 12 > 10, go right of 10
Insert 50 → 50 > 40, go right of 40
Insert 10 → duplicate, skip

```
         20
        /  \
      15    30
      /       \
    10        40
      \         \
      12        50
```

---


---

## [2019] Q.4(b) BST from: 40, 60, 50, 33, 55, 11. (04)

- Insert 40 → root
- Insert 60 → right of 40
- Insert 50 → left of 60
- Insert 33 → left of 40
- Insert 55 → right of 50
- Insert 11 → left of 33

```
       40
      /  \
    33    60
    /    /
   11   50
          \
          55
```

**Traversals:**
- **Inorder (LNR):** 11, 33, 40, 50, 55, 60
- **Preorder (NLR):** 40, 33, 11, 60, 50, 55
- **Postorder (LRN):** 11, 33, 55, 50, 60, 40

---


---

## [2020] Q.3(a) BST from: 30, 50, 20, 40, 25, 15, 45, 60, 46. (04)

Insert step by step:
- 30 → root
- 50 → right of 30
- 20 → left of 30
- 40 → left of 50
- 25 → right of 20
- 15 → left of 20
- 45 → right of 40
- 60 → right of 50
- 46 → left of 45... wait, 46 > 45, so right of 45

```
          30
         /  \
       20    50
      / \   /  \
    15  25 40   60
            \
            45
             \
             46
```

---


---

## [2020] Q.3(b) Traversals and delete root. (04)

**From the BST above:**

**Preorder (NLR):** 30, 20, 15, 25, 50, 40, 45, 46, 60

**Inorder (LNR):** 15, 20, 25, 30, 40, 45, 46, 50, 60

**Postorder (LRN):** 15, 25, 20, 46, 45, 40, 60, 50, 30

**Deleting root (30):**
Root has two children → Replace with **inorder successor** (smallest in right subtree) = **40**.

```
          40
         /  \
       20    50
      / \   /  \
    15  25 45   60
            \
            46
```

---


---

## [2021] Q.4(c) BST: J,R,D,G,T,E,M,H,P,A,F,Q — build and delete D. (05)

**(i) Building the BST:**

- J → root
- R → right of J
- D → left of J
- G → right of D
- T → right of R
- E → left of G
- M → left of R
- H → right of G
- P → right of M
- A → left of D
- F → right of E
- Q → left of T... wait, Q > R but Q < T → left of T

```
            J
           / \
          D    R
         / \  / \
        A  G M   T
          /\ \  /
         E  H P Q
          \
           F
```

**(ii) Delete node D (has two children):**
Replace D with its **inorder successor** = E (smallest in D's right subtree).
Then delete E from its original position (E has one child F, so F takes E's place).

```
            J
           / \
          E    R
         / \  / \
        A  G M   T
          /\ \  /
         F  H P Q
```

---

# Section B

---


---

## [2022] Q.5(b) BST insertion code. (CO2, 03)

```
Procedure BST_INSERT(ROOT, ITEM)
    Create new node NEW with DATA = ITEM, LEFT = NULL, RIGHT = NULL
    If ROOT = NULL Then
        Set ROOT = NEW
        Return ROOT
    End If
    Set PTR = ROOT
    While TRUE do
        If ITEM < DATA[PTR] Then
            If LEFT[PTR] = NULL Then
                Set LEFT[PTR] = NEW
                Return ROOT
            Else
                Set PTR = LEFT[PTR]
            End If
        Else
            If RIGHT[PTR] = NULL Then
                Set RIGHT[PTR] = NEW
                Return ROOT
            Else
                Set PTR = RIGHT[PTR]
            End If
        End If
    End While
End Procedure
```

---


---

## [2022] Q.5(c) Binary tree height recursive. (CO2, 03)

```
Procedure HEIGHT(ROOT)
    If ROOT = NULL Then
        Return -1                    // empty tree has height -1
    End If
    Set LEFT_H = HEIGHT(LEFT[ROOT])
    Set RIGHT_H = HEIGHT(RIGHT[ROOT])
    Return MAX(LEFT_H, RIGHT_H) + 1
End Procedure
```

**Example:** For tree with root only → HEIGHT = MAX(-1,-1)+1 = 0.
For tree with depth 3 → returns 3.

---


---

## [2024] Q.4(a) BST from: 14,20,40,10,30,15,5,35,50,45. Traversals. Delete 20. (CO2, 05)

**(i) Build BST:**
```
           14
          /  \
        10    20
       /     /  \
      5    15    40
                /  \
              30    50
                \   /
                35 45
```

**(ii) Traversals:**

**Preorder (NLR):** 14, 10, 5, 20, 15, 40, 30, 35, 50, 45

**Inorder (LNR):** 5, 10, 14, 15, 20, 30, 35, 40, 45, 50

**Postorder (LRN):** 5, 10, 15, 35, 30, 45, 50, 40, 20, 14

**(iii) Delete 20 (two children):**
Inorder successor of 20 = **30** (smallest in right subtree).
Replace 20 with 30. Delete original 30 (30 has child 35 → 35 takes 30's place).

```
           14
          /  \
        10    30
       /     /  \
      5    15    40
                /  \
              35    50
                   /
                  45
```

---


---

## 📊 Exam Priority
**Priority: 1/5** (Must Prepare — appeared EVERY year)
**Appeared in:** 8/8 years
**Typical marks:** 04–06 per question

<br>

---
[⬅️ Previous](./04_queue.md) | [🏠 Home](./README.md) | [Next ➡️](./06_heap.md)
