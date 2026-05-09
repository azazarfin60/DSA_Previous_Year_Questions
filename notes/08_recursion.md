[⬅️ Previous](./07_sorting_algorithms.md) | [🏠 Home](./README.md) | [Next ➡️](./09_trees_fundamentals.md)

---

# 📘 Chapter 8: Recursion & Recurrence Relations

> **Exam Frequency:** 5/8 years (Recursion), 4/8 (Recurrence) | **Typical Marks:** 02–04 | **Section:** A/B
> **Key Topics:** Properties, Tower of Hanoi, Recurrence Relations, Master Theorem, Tracing

---

## 1. What is Recursion?

**Recursion** is a technique where a function calls **itself** to solve a smaller instance of the same problem. Each recursive call works on a simpler sub-problem until a **base case** is reached that can be solved directly.

### Intuition
Think of Russian nesting dolls (Matryoshka). To find the smallest doll:
1. Open the current doll → find a smaller doll inside
2. Open that one → find an even smaller doll
3. Repeat until you reach the smallest doll (base case)
4. Then you work your way back out

---

## 2. Properties of Recursion (Important — asked in 2017, 2019, 2024)

Every recursive procedure must satisfy these properties:

1. **Base case (Stopping condition):** There must be at least one case that can be solved WITHOUT recursion. Without this, the function would call itself infinitely.

2. **Recursive case (Progress):** Each recursive call must make progress toward the base case — the problem must become smaller/simpler.

3. **Design rule:** Assume the recursive call works correctly, and build your solution using that assumption.

### Example: Factorial

**C++ Style:**
```cpp
int factorial(int n) {
    if (n == 0 || n == 1)       // Base case
        return 1;
    return n * factorial(n - 1); // Recursive case (n gets smaller)
}
```

**OR, Textbook Style:**
```
Procedure FACTORIAL(N)
    If N = 0 OR N = 1 Then
        Return 1
    End If
    Return N * FACTORIAL(N - 1)
End Procedure
```

**Trace: factorial(4)**
```
factorial(4) = 4 × factorial(3)
             = 4 × 3 × factorial(2)
             = 4 × 3 × 2 × factorial(1)
             = 4 × 3 × 2 × 1    ← base case reached
             = 24
```

---

## 3. Tower of Hanoi

### Problem Statement
Move `n` disks from peg **A** (source) to peg **C** (destination) using peg **B** (auxiliary), following these rules:
1. Move only **one disk** at a time
2. A larger disk can **never** be placed on a smaller disk
3. Only the **top disk** of any peg can be moved

### Algorithm
**C++ Style:**
```cpp
#include <iostream>
using namespace std;

void towerOfHanoi(int n, char from, char to, char aux) {
    if (n == 1) {
        cout << "Move disk 1 from " << from << " to " << to << endl;
        return;
    }
    towerOfHanoi(n - 1, from, aux, to);     // move n-1 disks to aux
    cout << "Move disk " << n << " from " << from << " to " << to << endl;  // move largest
    towerOfHanoi(n - 1, aux, to, from);     // move n-1 disks to dest
}
```

**OR, Textbook Style:**
```
Procedure TOWER_OF_HANOI(N, FROM, TO, AUX)
    If N = 1 Then
        Print "Move disk 1 from " + FROM + " to " + TO
        Return
    End If
    Call TOWER_OF_HANOI(N - 1, FROM, AUX, TO)
    Print "Move disk " + N + " from " + FROM + " to " + TO
    Call TOWER_OF_HANOI(N - 1, AUX, TO, FROM)
End Procedure
```

### Trace: n = 3 (A → C, using B)

| Step | Move | Peg A | Peg B | Peg C |
|---|---|---|---|---|
| Start | — | [3,2,1] | [] | [] |
| 1 | Disk 1: A → C | [3,2] | [] | [1] |
| 2 | Disk 2: A → B | [3] | [2] | [1] |
| 3 | Disk 1: C → B | [3] | [2,1] | [] |
| 4 | Disk 3: A → C | [] | [2,1] | [3] |
| 5 | Disk 1: B → A | [1] | [2] | [3] |
| 6 | Disk 2: B → C | [1] | [] | [3,2] |
| 7 | Disk 1: A → C | [] | [] | [3,2,1] |

**Total moves: 7 = 2³ − 1**

### Formula
> **Minimum moves for n disks = 2ⁿ − 1**

| n | Moves |
|---|---|
| 1 | 1 |
| 2 | 3 |
| 3 | 7 |
| 4 | 15 |
| 10 | 1,023 |
| 64 | 1.8 × 10¹⁹ (would take ~585 billion years at 1 move/second!) |

### Recurrence Relation
```
T(n) = 2T(n-1) + 1,  T(1) = 1
Solution: T(n) = 2ⁿ - 1
```

---

## 4. Recurrence Relations

### 4.1 What is a Recurrence?

A **recurrence relation** defines a function in terms of itself with smaller inputs. It's how we express the time complexity of recursive algorithms.

**Common form:** `T(n) = aT(n/b) + f(n)`

Where:
- `a` = number of recursive calls
- `n/b` = size of each sub-problem
- `f(n)` = work done outside recursion (dividing + combining)

### 4.2 Examples from Algorithms

| Algorithm | Recurrence | Solution |
|---|---|---|
| Binary Search | T(n) = T(n/2) + O(1) | O(log n) |
| Merge Sort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick Sort (best) | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick Sort (worst) | T(n) = T(n-1) + O(n) | O(n²) |
| Tower of Hanoi | T(n) = 2T(n-1) + 1 | O(2ⁿ) |
| Fibonacci | T(n) = T(n-1) + T(n-2) + O(1) | O(2ⁿ) |

---

### 4.3 Solving by Substitution (Back Substitution)

**Method:** Repeatedly substitute the recurrence into itself until you see a pattern.

**Example:** Solve T(n) = 2T(n/2) + n, T(1) = 1

```
T(n) = 2T(n/2) + n

Substitute T(n/2) = 2T(n/4) + n/2:
T(n) = 2[2T(n/4) + n/2] + n
     = 4T(n/4) + n + n
     = 4T(n/4) + 2n

Substitute T(n/4) = 2T(n/8) + n/4:
T(n) = 4[2T(n/8) + n/4] + 2n
     = 8T(n/8) + n + 2n
     = 8T(n/8) + 3n

Pattern after k substitutions:
T(n) = 2ᵏ T(n/2ᵏ) + kn

Base case when n/2ᵏ = 1 → k = log₂(n):
T(n) = 2^(log n) × T(1) + n × log n
     = n × 1 + n log n
     = n + n log n
     = O(n log n) ✅
```

---

### 4.4 Master Theorem

The **Master Theorem** provides a direct formula for recurrences of the form:

> **T(n) = aT(n/b) + f(n)**

where a ≥ 1, b > 1.

Compute: **c_crit = log_b(a)**

| Case | Condition | Solution |
|---|---|---|
| **Case 1** | f(n) = O(n^c) where c < log_b(a) | T(n) = **Θ(n^(log_b(a)))** |
| **Case 2** | f(n) = Θ(n^(log_b(a))) | T(n) = **Θ(n^(log_b(a)) × log n)** |
| **Case 3** | f(n) = Ω(n^c) where c > log_b(a) | T(n) = **Θ(f(n))** |

### Worked Examples

**Example 1:** T(n) = 2T(n/2) + n (Merge Sort)
```
a=2, b=2, f(n)=n
log_b(a) = log₂(2) = 1
f(n) = n = n¹ = Θ(n^1) → matches Case 2
T(n) = Θ(n¹ × log n) = Θ(n log n) ✅
```

**Example 2:** T(n) = 4T(n/2) + n
```
a=4, b=2, f(n)=n
log_b(a) = log₂(4) = 2
f(n) = n = n¹, and 1 < 2 → Case 1
T(n) = Θ(n²) ✅
```

**Example 3:** T(n) = T(n/2) + 1 (Binary Search)
```
a=1, b=2, f(n)=1
log_b(a) = log₂(1) = 0
f(n) = 1 = n⁰ = Θ(n⁰) → Case 2
T(n) = Θ(n⁰ × log n) = Θ(log n) ✅
```

**Example 4:** T(n) = 3T(n/4) + n log n
```
a=3, b=4, f(n) = n log n
log_b(a) = log₄(3) ≈ 0.793
f(n) = n log n = Ω(n^c) where c=1 > 0.793 → Case 3
T(n) = Θ(n log n) ✅
```

---

## 5. Tracing Recursive Calls

### Fibonacci Trace: fib(5)

**C++ Style:**
```cpp
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
```

**OR, Textbook Style:**
```
Procedure FIBONACCI(N)
    If N <= 1 Then
        Return N
    End If
    Return FIBONACCI(N - 1) + FIBONACCI(N - 2)
End Procedure
```

```
                    fib(5)
                   /      \
              fib(4)       fib(3)
             /     \       /     \
         fib(3)   fib(2) fib(2) fib(1)
         /   \    /   \   /   \    |
     fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)  1
     /   \    |      |      |      |      |
  fib(1) fib(0) 1    1      0      1      0
    |      |
    1      0

Result: fib(5) = 5
```

Notice: fib(3) is computed **twice**, fib(2) is computed **three times**! This is why naive recursive Fibonacci is O(2ⁿ) — exponential waste.

---

## 6. Exam-Ready Summary

### Quick Revision Points
1. **Recursion needs:** Base case + progress toward base case
2. **Tower of Hanoi:** 2ⁿ − 1 moves, T(n) = 2T(n−1) + 1
3. **Master Theorem:** T(n) = aT(n/b) + f(n), compare f(n) with n^(log_b(a))
4. **Substitution:** Expand recurrence k times → find pattern → substitute base case
5. **Key recurrences:** Binary Search = O(log n), Merge Sort = O(n log n)

---

## 7. Practice Problems (From Past Exams)

### Problem 1 [2017, 2019, 2024, 02–03 marks]
**Q:** What are the properties of a recursive procedure?

**Answer:** Base case (stopping condition), recursive case (progress toward base case), design rule (assume recursive call works).

### Problem 2 [2019, 2022, 03–04 marks]
**Q:** Solve T(n) = 2T(n/2) + n using substitution method.

**Answer:** See Section 4.3 — expand k times, substitute k = log n → O(n log n).

### Problem 3 [Typical, 03 marks]
**Q:** Solve T(n) = 9T(n/3) + n using Master Theorem.

**Solution:** a=9, b=3, log₃(9)=2, f(n)=n=n¹, 1<2 → Case 1, T(n) = Θ(n²).

---

*← [07 — Sorting Algorithms](07_sorting_algorithms.md) | Next: [09 — Trees Fundamentals →](09_trees_fundamentals.md)*

<br>

---
[⬅️ Previous](./07_sorting_algorithms.md) | [🏠 Home](./README.md) | [Next ➡️](./09_trees_fundamentals.md)
