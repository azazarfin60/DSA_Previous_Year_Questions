[⬅️ Previous](./pagecontext07.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext09.md)

---

# DSA Class Notes - Page Context 08 (Pages 036-040)

## Page 036
**Code: Infix to Postfix Conversion**

**Precedence Function:**
```c
int precedence(char ch) {
    if (ch == '^') return 3;
    else if (ch == '*' || ch == '/') return 2;
    else if (ch == '+' || ch == '-') return 1;
    else return -1;
}
```

**Main Logic (Partial):**
```c
for (ch : eqn) {
    if (precedence(ch) == -1 && ch != '(' && ch != ')') {
        // Operand: Add to postfix output string
        post += ch;
    }
    else if (ch == '(') {
        st.push(ch);
    }
    else if (ch == ')') {
        while (!st.empty() && st.top() != '(') {
            post += st.top();
            st.pop();
        }
        st.pop(); // Pop the '('
    }
    // Operator logic continues...
}
```

---

## Page 037
**Code: Infix to Postfix (Continued)**

**Operator Logic & Completion:**
```c
    else { // Symbol is an operator
        while (!st.empty() && precedence(st.top()) >= precedence(ch)) {
            post += st.top();
            st.pop();
        }
        st.push(ch);
    }
}

// After scanning the whole equation, pop remaining operators
while (!st.empty()) {
    post += st.top();
    st.pop();
}

cout << post;
```

---

## Page 038
**Date:** 03 Jan, 2026  
**Instructor:** Foysal Sir  

### Infix to Postfix Trace Example 1

**Input Expression:** `A + B * (D - E)`

| Input Symbol | Stack | Postfix Output |
| :--- | :--- | :--- |
| A | | A |
| + | + | A |
| B | + | AB |
| * | + * | AB |
| ( | + * ( | AB |
| D | + * ( | ABD |
| - | + * ( - | ABD |
| E | + * ( - | ABDE |
| ) | + * | ABDE - |
| (End) | | ABDE - * + |

---

## Page 039
**Infix to Postfix Trace Example 2**

**Input Expression:** `A * B / (D + E * F) + H ^ K`

**Tracing Process:**
- This trace meticulously shows how the stack handles the multiplication/division sequence and the nested addition/multiplication within parentheses.
- It also demonstrates how the exponentiation operator (`^`) with the highest priority interacts with the final addition.
- **Key Observation:** Operators with equal precedence (like `*` and `/`) result in the first one being popped before the second is pushed due to left-associativity.

---

## Page 040
**Date:** 04 Jan, 2026  
**Instructor:** Foysal Sir  

### Infix to Prefix Conversion

**Algorithm Steps:**
1. **Reverse** the original Infix expression string.
2. **Swap Brackets:** Change all `(` to `)` and all `)` to `(`.
3. **Postfix Conversion:** Convert this modified expression to Postfix using the standard Infix-to-Postfix algorithm.
4. **Reverse Again:** Reverse the resulting Postfix expression to obtain the final Prefix string.

**Example Trace:**
- **Original Infix:** `A * B + (C - D)`
- **Step 1 (Reverse):** `) D - C ( + B * A`
- **Step 2 (Swap Brackets):** `( D - C ) + B * A`
- **Step 3 (Postfix of Rev):** `D C - B A * +`
- **Step 4 (Final Prefix):** `+ * A B - C D`
- **Final Result:** `+ * A B - C D`

<br>

---
[⬅️ Previous](./pagecontext07.md) | [🏠 Home](./README.md) | [Next ➡️](./pagecontext09.md)
