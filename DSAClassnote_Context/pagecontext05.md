[⬅️ Previous](./pagecontext04.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext06.md)

---

# DSA Class Notes - Page Context 05 (Pages 021-025)

## Page 021
**Date:** 07 Dec, 2025  
**Instructor:** Foysal Sir  

### Stack Applications: Expression Handling

**Purpose:**  
1. Storing equations containing operators (`+`, `-`, `*`, `/`) and brackets (`()`, `{}`, `[]`).
2. **Equation Validity Check:** Ensuring brackets are balanced.
3. **Operation Performance:** Evaluating the expression.

**Bracket Validity Concept:**
- Brackets are stored in the stack memory in "left order" (opening brackets are pushed).
- Example logic: `{(2+3)*5}`.

---

## Page 022
**Validity Checking Algorithm & Operator Priority**

**Algorithm: Bracket Validity Checking:**
1. **Initialize** an empty stack.
2. **Scan** the expression symbols from left to right.
3. **If** the symbol is a **Left Bracket** (`(`, `{`, `[`): Push it into the stack.
4. **If** the symbol is a **Right Bracket** (`)`, `}`, `]`):
   - **If** the stack is empty: Print "Invalid".
   - **Else:** Pop the top element. If the popped left bracket does not match the current right bracket: Print "Invalid".
5. **After scanning all symbols:**
   - **If** the stack is empty: Print "Valid Expression".
   - **Else:** Print "Invalid".

**Operator Priority (Precedence):**
1. `^` (Exponential) - **High**
2. `*`, `/` (Multiplication, Division) - **Medium**
3. `+`, `-` (Addition, Subtraction) - **Low**

**Expression Notations:**
- **Infix (Normal):** `(2+3)+7`
- **Postfix (Reverse Polish):** `(23+)7+` (Commonly used by computers).
- **Prefix (Polish):** `(+23)+7`

---

## Page 023
**Infix to Postfix Conversion Using Stack**

**Core Rules:**
1. A higher priority operator cannot stay on top of a lower priority operator in the stack (it must be popped first).
2. When a **closing bracket** is encountered, pop and output everything from the stack until the corresponding opening bracket is found.
3. Every operator must be popped exactly once to appear in the output.

**Examples Traced:**
- `3 + 5 * (5 / 5)`
- `(5 + 5 * 4 + 3)`

---

## Page 024
**Topic: Bubble Sort (Class Test CT-1 Prep)**

**Efficiency Analysis:**
- Not efficient for large datasets because average and worst-case time complexities are high.
- **Complexity:**
  - **Best Case:** $O(N)$
  - **Average Case:** $O(N^2)$
  - **Worst Case:** $O(N^2)$

**Algorithm Steps:**
1. Uses multiple passes to sort the array.
2. After the **first pass**, the maximum element "bubbles up" to its correct final position at the end.
3. In every subsequent pass, the next largest remaining element is placed in its correct position.
4. After **k passes**, the largest k elements are correctly positioned at the end.
5. Adjacent elements are compared and swapped if they are in the wrong order.

---

## Page 025
**Bubble Sort: Detailed Simulation**

**Tracing Example:**
- **Input Array:** `[5, 6, 1, 3]`

**Pass 1:**
1. `(5, 6)`: No swap.
2. `(6, 1)`: Swap -> `[5, 1, 6, 3]`
3. `(6, 3)`: Swap -> `[5, 1, 3 | 6]` (6 is now in its final position).

**Pass 2:**
1. `(5, 1)`: Swap -> `[1, 5, 3 | 6]`
2. `(5, 3)`: Swap -> `[1, 3 | 5, 6]` (5 is now in its final position).

**Pass 3:**
1. `(1, 3)`: No swap.
- **Final Result:** `[1, 3, 5, 6]` (Array fully sorted).

<br>

---
[⬅️ Previous](./pagecontext04.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext06.md)
