[⬅️ Previous](./09_hashing.md) | [🏠 Home](./README.md) | [Next ➡️](./11_complexity_analysis.md)

---

# Recursion — Properties, Tower of Hanoi, Head/Tail Recursion


---

## [2017] 3(c) Properties of recursive procedure. (02)

A recursive procedure must satisfy two mandatory properties:

1. **Base Case (Stopping Condition):** There must be at least one condition where the function does not call itself, preventing infinite recursion.

2. **Progressive Approach:** Each recursive call must move closer to the base case. The problem must get smaller with each call so that the base case is eventually reached.

Example: Factorial
```
Procedure FACTORIAL(N)
    If N <= 1 Then
        Return 1                    // base case
    Else
        Return N × FACTORIAL(N - 1) // moves toward base case
    End If
End Procedure
```

---


---

## [2019] Q.4(a) Properties of recursive procedure. (02)

1. **Base Case:** At least one condition where the function stops calling itself, preventing infinite recursion.

2. **Progressive Approach:** Each recursive call must reduce the problem size, moving closer to the base case.

Example — Tower of Hanoi:
```
Procedure HANOI(N, SOURCE, DEST, AUX)
    If N = 1 Then                              // base case
        Print "Move disk 1 from", SOURCE, "to", DEST
        Return
    End If
    Call HANOI(N-1, SOURCE, AUX, DEST)         // smaller problem
    Print "Move disk", N, "from", SOURCE, "to", DEST
    Call HANOI(N-1, AUX, DEST, SOURCE)         // smaller problem
End Procedure
```

---


---

## [2021] Q.6(d) Head recursion and tail recursion. (02)

**Head Recursion:** The recursive call is the **first** statement in the function. Processing happens **after** the recursive call returns.
```
Procedure HEAD_EXAMPLE(N)
    If N > 0 Then
        Call HEAD_EXAMPLE(N - 1)    // recursive call first
        Print N                      // processing after
    End If
End Procedure
```
HEAD_EXAMPLE(3) prints: 1 2 3

**Tail Recursion:** The recursive call is the **last** statement in the function. Processing happens **before** the recursive call.
```
Procedure TAIL_EXAMPLE(N)
    If N > 0 Then
        Print N                      // processing first
        Call TAIL_EXAMPLE(N - 1)    // recursive call last
    End If
End Procedure
```
TAIL_EXAMPLE(3) prints: 3 2 1

---


---

## [2022] Q.1(a) Define DS. Tower of Hanoi code. (CO1, 03)

**Data Structure:** A systematic way of organizing, storing, and managing data so that it can be accessed and modified efficiently.

**Tower of Hanoi — Recursive Pseudocode:**
```
Procedure TOWER_OF_HANOI(N, SOURCE, DEST, AUX)
    If N = 1 Then
        Print "Move disk 1 from", SOURCE, "to", DEST
        Return
    End If
    Call TOWER_OF_HANOI(N-1, SOURCE, AUX, DEST)
    Print "Move disk", N, "from", SOURCE, "to", DEST
    Call TOWER_OF_HANOI(N-1, AUX, DEST, SOURCE)
End Procedure
```

For N=3, SOURCE=A, DEST=C, AUX=B:
1. Move disk 1 from A to C
2. Move disk 2 from A to B
3. Move disk 1 from C to B
4. Move disk 3 from A to C
5. Move disk 1 from B to A
6. Move disk 2 from B to C
7. Move disk 1 from A to C

**Total moves = 2ⁿ − 1 = 7**

---


---

## 📊 Exam Priority
**Priority: 2/5** (Should Prepare)
**Appeared in:** 5/8 years
**Typical marks:** 02–03 per question

<br>

---
[⬅️ Previous](./09_hashing.md) | [🏠 Home](./README.md) | [Next ➡️](./11_complexity_analysis.md)
