# 📘 Chapter 4: Stacks

> **Exam Frequency:** 5/8 years | **Typical Marks:** 04 | **Section:** A
> **Key Topics:** Stack ADT, PUSH/POP, Infix/Postfix/Prefix, Conversions, Evaluation

---

## 1. What is a Stack?

A **stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle — the element that is inserted last is the first one to be removed.

### Intuition
Think of a **stack of plates** in a cafeteria:
- You can only **add (push)** a plate on **top**
- You can only **remove (pop)** the plate from the **top**
- You can't pull a plate from the middle or bottom without removing everything above it

```
        ┌─────┐
        │  40 │  ← TOP (last added, first to be removed)
        ├─────┤
        │  30 │
        ├─────┤
        │  20 │
        ├─────┤
        │  10 │  ← BOTTOM (first added, last to be removed)
        └─────┘
```

### Real-World Analogies
- **Browser back button** — pages are stacked; back takes you to the most recent
- **Undo/Redo** — operations stored in a stack
- **Function call stack** — most recently called function returns first
- **Reversal** — push all elements, then pop → reversed order

---

## 2. Stack ADT

| Component | Specification |
|---|---|
| **Data** | Ordered collection of elements with a TOP pointer |
| **Operations** | PUSH, POP, PEEK (TOP), isEmpty, isFull |
| **Rules** | LIFO — only the top element is accessible |
| **Implementation** | Array-based or Linked-list-based |

---

## 3. Stack Operations

### 3.1 PUSH — Insert Element

```
Procedure PUSH(STACK, TOP, MAXSIZE, ITEM)
    If TOP = MAXSIZE - 1 Then
        Print "OVERFLOW — Stack is full"
        Return
    End If
    Set TOP = TOP + 1
    Set STACK[TOP] = ITEM
End Procedure
```

### 3.2 POP — Remove Element

```
Procedure POP(STACK, TOP)
    If TOP = -1 Then
        Print "UNDERFLOW — Stack is empty"
        Return
    End If
    Set ITEM = STACK[TOP]
    Set TOP = TOP - 1
    Return ITEM
End Procedure
```

### 3.3 PEEK — View Top Element (without removing)

```
Procedure PEEK(STACK, TOP)
    If TOP = -1 Then
        Print "Stack is empty"
        Return
    End If
    Return STACK[TOP]
End Procedure
```

### 3.4 Complete C Implementation

```c
#define MAX 100

int stack[MAX];
int top = -1;

void push(int item) {
    if (top == MAX - 1) {
        printf("Stack Overflow\n");
        return;
    }
    stack[++top] = item;          // increment top, then store
}

int pop() {
    if (top == -1) {
        printf("Stack Underflow\n");
        return -1;
    }
    return stack[top--];          // return top, then decrement
}

int peek() {
    if (top == -1) return -1;
    return stack[top];            // just look, don't remove
}

int isEmpty() {
    return (top == -1);
}
```

### Time Complexity
All stack operations are **O(1)** — constant time. No traversal or shifting needed.

---

## 4. Infix, Postfix, and Prefix Notation

This is one of the **most important stack application topics** for the exam. Let's understand all three notations deeply.

### 4.1 What Are These Notations?

| Notation | Operator Position | Example | Full Name |
|---|---|---|---|
| **Infix** | Between operands | `A + B` | Normal mathematical notation |
| **Postfix** | After operands | `A B +` | Reverse Polish Notation (RPN) |
| **Prefix** | Before operands | `+ A B` | Polish Notation (PN) |

### 4.2 Why Do We Need Postfix/Prefix?

**Problem with Infix:** It requires **parentheses** and **precedence rules** to be unambiguous.

Consider: `A + B * C`
- Does this mean `(A + B) * C` or `A + (B * C)`?
- We need precedence rules (× before +) to decide → `A + (B * C)`

**Postfix and Prefix eliminate this ambiguity entirely** — no parentheses needed, and the order of operations is built into the notation itself.

| Expression | Infix | Postfix | Prefix |
|---|---|---|---|
| A + B | A + B | A B + | + A B |
| A + B × C | A + B * C | A B C * + | + A * B C |
| (A + B) × C | (A + B) * C | A B + C * | * + A B C |
| A + B × C − D | A + B * C - D | A B C * + D - | - + A * B C D |

### 4.3 Operator Precedence and Associativity

| Operator | Precedence | Associativity |
|---|---|---|
| `↑` (exponentiation) | Highest (3) | Right to Left |
| `*`, `/` | Medium (2) | Left to Right |
| `+`, `-` | Lowest (1) | Left to Right |

**Key:** Higher precedence operators bind tighter. Parentheses override all precedence.

---

## 5. Infix → Postfix Conversion (Using Stack)

This is the **most commonly asked** stack question in exams.

### Algorithm

```
Procedure INFIX_TO_POSTFIX(infix)
    Create empty STACK
    Create empty OUTPUT string
    
    For each symbol S in infix (left to right) do
        Case 1: S is an OPERAND (A, B, C, ...)
            Append S to OUTPUT
            
        Case 2: S is '('
            PUSH '(' onto STACK
            
        Case 3: S is ')'
            While STACK top ≠ '(' do
                POP from STACK and append to OUTPUT
            End While
            POP '(' from STACK (discard it)
            
        Case 4: S is an OPERATOR (+, -, *, /, ↑)
            While STACK is not empty 
                  AND top of STACK ≠ '('
                  AND precedence(STACK top) ≥ precedence(S) do
                POP from STACK and append to OUTPUT
            End While
            PUSH S onto STACK
    End For
    
    // Pop remaining operators
    While STACK is not empty do
        POP from STACK and append to OUTPUT
    End While
    
    Return OUTPUT
End Procedure
```

### Important Rules Summary
1. **Operand** → directly to output
2. **`(`** → push onto stack
3. **`)`** → pop and output until `(` is found, discard `(`
4. **Operator** → pop and output all operators with ≥ precedence from stack, then push current operator
5. **End of expression** → pop all remaining operators to output

### Note on Exponentiation
`↑` is **right-associative**, so when comparing precedences in Step 4:
- For `↑` vs `↑` on stack: do NOT pop (use `>` instead of `≥`)
- For all other operators: use `≥`

---

### 5.1 Worked Example 1: `A + B * C - D`

| Step | Symbol | Stack | Output | Action |
|---|---|---|---|---|
| 1 | A | (empty) | A | Operand → output |
| 2 | + | + | A | Push + |
| 3 | B | + | A B | Operand → output |
| 4 | * | + * | A B | Prec(*) > Prec(+), push * |
| 5 | C | + * | A B C | Operand → output |
| 6 | - | + - | A B C * + | Prec(-) ≤ Prec(*), pop * → output; Prec(-) ≤ Prec(+), pop + → output; push - |
| 7 | D | + - | A B C * + D | Operand → output |
| End | — | (empty) | A B C * + D - | Pop remaining: - |

> **Postfix: `A B C * + D -`** ✅

---

### 5.2 Worked Example 2: `A + (B * C - (D / E ↑ F) * G) * H`

This is the **exact expression** that appeared in **2021 and 2024 exams**.

| Step | Symbol | Stack | Output | Action |
|---|---|---|---|---|
| 1 | A | | A | Operand |
| 2 | + | + | A | Push + |
| 3 | ( | + ( | A | Push ( |
| 4 | B | + ( | A B | Operand |
| 5 | * | + ( * | A B | Push * |
| 6 | C | + ( * | A B C | Operand |
| 7 | - | + ( - | A B C * | Pop * (prec≥), push - |
| 8 | ( | + ( - ( | A B C * | Push ( |
| 9 | D | + ( - ( | A B C * D | Operand |
| 10 | / | + ( - ( / | A B C * D | Push / |
| 11 | E | + ( - ( / | A B C * D E | Operand |
| 12 | ↑ | + ( - ( / ↑ | A B C * D E | Push ↑ (prec > /) |
| 13 | F | + ( - ( / ↑ | A B C * D E F | Operand |
| 14 | ) | + ( - | A B C * D E F ↑ / | Pop until (: pop ↑, pop / |
| 15 | * | + ( - * | A B C * D E F ↑ / | Push * (prec > -) |
| 16 | G | + ( - * | A B C * D E F ↑ / G | Operand |
| 17 | ) | + | A B C * D E F ↑ / G * - | Pop until (: pop *, pop - |
| 18 | * | + * | A B C * D E F ↑ / G * - | Push * (prec > +) |
| 19 | H | + * | A B C * D E F ↑ / G * - H | Operand |
| End | — | | A B C * D E F ↑ / G * - H * + | Pop: *, + |

> **Postfix: `A B C * D E F ↑ / G * - H * +`** ✅

---

## 6. Postfix Expression Evaluation (Using Stack)

### Algorithm

```
Procedure EVALUATE_POSTFIX(postfix)
    Create empty STACK
    
    For each symbol S in postfix (left to right) do
        If S is an OPERAND Then
            PUSH S onto STACK
        Else (S is an OPERATOR)
            Set OP2 = POP(STACK)       // second operand (popped first!)
            Set OP1 = POP(STACK)       // first operand
            Set RESULT = OP1 (S) OP2   // apply operator
            PUSH RESULT onto STACK
        End If
    End For
    
    Return POP(STACK)                  // final result
End Procedure
```

### ⚠️ Important: Order of Operands
When you pop two operands, the **first popped** is the **second operand** (right side):
- POP → OP2 (right operand)
- POP → OP1 (left operand)
- Result = OP1 operator OP2

This matters for **subtraction**, **division**, and **exponentiation**!

### Worked Example: Evaluate `6 3 2 * + 4 -`

| Step | Symbol | Stack | Action |
|---|---|---|---|
| 1 | 6 | 6 | Push 6 |
| 2 | 3 | 6, 3 | Push 3 |
| 3 | 2 | 6, 3, 2 | Push 2 |
| 4 | * | 6, 6 | Pop 2, Pop 3 → 3*2=6, Push 6 |
| 5 | + | 12 | Pop 6, Pop 6 → 6+6=12, Push 12 |
| 6 | 4 | 12, 4 | Push 4 |
| 7 | - | 8 | Pop 4, Pop 12 → 12-4=8, Push 8 |

> **Result: 8** ✅

### Another Example: Evaluate `5 3 + 8 2 - *`

| Step | Symbol | Stack | Action |
|---|---|---|---|
| 1 | 5 | 5 | Push |
| 2 | 3 | 5, 3 | Push |
| 3 | + | 8 | 5+3=8 |
| 4 | 8 | 8, 8 | Push |
| 5 | 2 | 8, 8, 2 | Push |
| 6 | - | 8, 6 | 8-2=6 |
| 7 | * | 48 | 8*6=48 |

> **Result: 48** ✅

---

## 7. Postfix → Infix Conversion

### Algorithm
```
Procedure POSTFIX_TO_INFIX(postfix)
    Create empty STACK (stores string expressions)
    
    For each symbol S in postfix do
        If S is OPERAND Then
            PUSH S as a string
        Else (S is OPERATOR)
            Set OP2 = POP(STACK)
            Set OP1 = POP(STACK)
            Set EXPR = "(" + OP1 + S + OP2 + ")"
            PUSH EXPR onto STACK
        End If
    End For
    
    Return POP(STACK)
End Procedure
```

### Example: Convert `A B C * + D -` to Infix

| Step | Symbol | Stack | Action |
|---|---|---|---|
| 1 | A | "A" | Push |
| 2 | B | "A", "B" | Push |
| 3 | C | "A", "B", "C" | Push |
| 4 | * | "A", "(B*C)" | Pop C, B → "(B*C)" |
| 5 | + | "(A+(B*C))" | Pop (B*C), A → "(A+(B*C))" |
| 6 | D | "(A+(B*C))", "D" | Push |
| 7 | - | "((A+(B*C))-D)" | Pop D, (A+(B*C)) → result |

> **Infix: ((A+(B*C))-D)** ✅

---

## 8. Prefix (Polish Notation)

### Infix → Prefix Conversion

**Method:** Modified version of Infix→Postfix:
1. **Reverse** the infix expression
2. Replace `(` with `)` and `)` with `(`
3. Apply Infix→Postfix algorithm
4. **Reverse** the result

### Example: Convert `A + B * C` to Prefix

```
Step 1: Reverse → "C * B + A"
Step 2: Swap parens → "C * B + A" (no parens here)
Step 3: Apply Infix→Postfix on "C * B + A":
    C → output: C
    * → push *
    B → output: C B
    + → pop * (prec≥), push +: output: C B *
    A → output: C B * A
    End → pop +: output: C B * A +
Step 4: Reverse → "+ A * B C"
```

> **Prefix: `+ A * B C`** ✅

---

## 9. Implementing Stack Using Queues

This is a **tricky concept** that has appeared in exams (2020, 2022).

### Method: Using Two Queues

**Idea:** Use two queues Q1 and Q2. Make the **PUSH operation expensive** by always keeping elements in reverse order.

```
PUSH(x):
    1. Enqueue x into Q2
    2. Dequeue all elements from Q1 and enqueue into Q2
    3. Swap names of Q1 and Q2

POP():
    1. Dequeue from Q1
```

### Trace: PUSH 1, PUSH 2, PUSH 3, POP

```
PUSH 1:
  Q2: [1] → Dequeue all from Q1 (empty) → Swap
  Q1: [1], Q2: []

PUSH 2:
  Q2: [2] → Dequeue 1 from Q1 to Q2 → Q2: [2, 1] → Swap
  Q1: [2, 1], Q2: []

PUSH 3:
  Q2: [3] → Dequeue 2,1 from Q1 to Q2 → Q2: [3, 2, 1] → Swap
  Q1: [3, 2, 1], Q2: []

POP:
  Dequeue from Q1 → returns 3 (LIFO order!) ✓
  Q1: [2, 1]
```

---

## 10. Exam-Ready Summary

### Quick Revision Points
1. **Stack** = LIFO, TOP pointer, PUSH/POP/PEEK all O(1)
2. **Infix→Postfix:** Operand→output, `(`→push, `)`→pop until `(`, Operator→pop higher/equal precedence then push
3. **Postfix evaluation:** Operand→push, Operator→pop two (OP2 first, OP1 second), compute, push result
4. **Precedence:** ↑(3) > */÷(2) > +−(1)
5. **↑ is right-associative** — don't pop ↑ when current is also ↑
6. The expression `A+(B*C-(D/E↑F)*G)*H` has appeared in 2021 AND 2024

### Most Common Exam Questions
- Infix → Postfix conversion with full stack trace (04 marks, 5/8 years)
- Postfix evaluation with stack trace (03–04 marks)
- Define stack, PUSH/POP pseudocode (02–03 marks)

---

## 11. Practice Problems (From Past Exams)

### Problem 1 [2021 & 2024, 04 marks]
**Q:** Convert `A + (B * C - (D / E ↑ F) * G) * H` to postfix. Show stack at each step.

**Answer:** See Section 5.2 above. Result: `A B C * D E F ↑ / G * - H * +`

### Problem 2 [Typical 03 marks]
**Q:** Evaluate the postfix expression: `2 3 4 * + 5 -`

**Solution:**
| Step | Symbol | Stack |
|---|---|---|
| 1 | 2 | 2 |
| 2 | 3 | 2, 3 |
| 3 | 4 | 2, 3, 4 |
| 4 | * | 2, 12 |
| 5 | + | 14 |
| 6 | 5 | 14, 5 |
| 7 | - | 9 |

**Result: 9**

### Problem 3 [Typical 03 marks]
**Q:** Convert Infix `(A + B) * (C - D)` to Postfix.

**Solution:** `A B + C D - *`

---

*← [03 — Linked Lists](03_linked_lists.md) | Next: [05 — Queues →](05_queues.md)*
