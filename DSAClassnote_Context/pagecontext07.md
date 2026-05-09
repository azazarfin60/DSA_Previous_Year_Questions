[⬅️ Previous](./pagecontext06.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext08.md)

---

# DSA Class Notes - Page Context 07 (Pages 031-035)

## Page 031
**Selection Sort: Completion and Code**

**Simulation (Continued):**
- **Iteration 3:** Current unsorted `[25, 22, 64]`. Smallest is 22. Swap with 25.  
  Result: `[11, 12, 22 | 25, 64]`
- **Iteration 4:** Current unsorted `[25, 64]`. Smallest is 25. (No change).  
  Result: `[11, 12, 22, 25 | 64]`
- **Final Result:** `[11, 12, 22, 25, 64]`

**Selection Sort Algorithm (C Style):**
```c
for (i = 0; i < n - 1; i++) {
    minindex = i;
    for (j = i + 1; j < n; j++) {
        if (A[j] < A[minindex]) {
            minindex = j;
        }
    }
    // Swap the found minimum element with the first element
    temp = A[i];
    A[i] = A[minindex];
    A[minindex] = temp;
}
```

---

## Page 032
**Selection Sort Analysis & Merge Sort Revisit**

**Selection Sort Analysis:**
- **Advantages:**
  1. Easy to understand.
  2. No extra space ($O(1)$).
  3. Minimum number of swaps (Memory efficient for write operations).
- **Disadvantages:**
  1. Time Complexity is always $O(N^2)$ for Best, Average, and Worst cases.
  2. **Not Stable:** Does not preserve relative order of equal elements.

### Merge Sort Concept
- Efficient and stable sorting algorithm.
- Uses **Divide and Conquer** approach.
- Recursively divides the array into two halves until individual elements are reached.
- Subarrays are merged back together in sorted order.

---

## Page 033
**Merge Sort: Complexity and Simulation**

**Time Complexity:**
- **Best, Average, Worst Case:** $O(N \log N)$

**Space Complexity:**
- $O(N)$ (Requires additional memory).

**Simulation Example:**
- **Input:** `[70, 30, 50, 10]`
- **Divide:**
  - `[70, 30]` and `[50, 10]`
  - `[70]`, `[30]`, `[50]`, `[10]`
- **Conquer & Merge:**
  - `[30, 70]` and `[10, 50]`
  - `[10, 30, 50, 70]`

**Merge Sort Analysis:**
- **Advantages:** Stable, efficient for large datasets ($O(N \log N)$), simple implementation.
- **Disadvantages:** High space complexity ($O(N)$), requires additional memory.

---

## Page 034
**Expression Conversion: Infix to Postfix**

**Rules for Conversion:**
1. **Priority Levels:** `^` (3), `*, /` (2), `+, -` (1).
2. **Lower priority** cannot be pushed onto a **higher priority** operator in the stack. If a lower priority operator arrives, pop the higher priority one first.
3. **Left-Associativity:** Two operators of the same priority cannot stay together in the stack; the existing one must be popped.
4. **Operands:** Directly added to the Postfix expression.
5. **Brackets:** When a closing bracket `)` is encountered, pop all operators from the stack until the opening bracket `(` is found.

**Trace Example:** `(A + B / C * (D + E) - F)`
- Tracing involves columns for **Symbol**, **Stack**, and **Postfix String**.

---

## Page 035
**Expression Conversion: Postfix to Infix**

**Rules for Conversion:**
1. **Scan** the Postfix expression from left to right.
2. **Operands:** If the symbol is an operand, push it into the stack.
3. **Operators:** If the symbol is an operator:
   - Pop two operands from the stack (the first pop is the right operand, the second pop is the left operand).
   - Form a new equation by putting the operator between them: `(LeftOperand Operator RightOperand)`.
   - Push the resulting equation back onto the stack.
4. **Result:** After scanning the whole expression, the final result is at the top of the stack.

**Trace Example:** `ABC/DE+*+F-`
1. Push `A`, `B`, `C`.
2. Operator `/`: Pop `C`, `B`. Form `(B/C)`. Push it.
3. Push `D`, `E`.
4. Operator `+`: Pop `E`, `D`. Form `(D+E)`. Push it.
5. Operator `*`: Pop `(D+E)`, `(B/C)`. Form `((B/C)*(D+E))`. Push it.
6. Operator `+`: Pop result, `A`. Form `(A+((B/C)*(D+E)))`. Push it.
7. Push `F`.
8. Operator `-`: Pop `F`, result. Form `((A+((B/C)*(D+E)))-F)`.
- **Final Infix:** `((A+((B/C)*(D+E)))-F)`

<br>

---
[⬅️ Previous](./pagecontext06.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext08.md)
