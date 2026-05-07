# Complexity Analysis — Big-O, Time Complexity, Frequency Counts


---

## [2017] 5(a) What is complexity? Discuss O(n²). (04)

**Algorithm Complexity:** A measure of the amount of resources (time and space) required by an algorithm as a function of input size n. It helps us evaluate how efficiently an algorithm performs.

**Two types:**
- **Time Complexity** — how execution time grows with input size
- **Space Complexity** — how memory usage grows with input size

**O(n²) Complexity — Quadratic:**
An algorithm is O(n²) when its running time grows proportional to the square of the input size. This typically occurs with **nested loops** where both iterate over n elements.

**Example — Bubble Sort:**
```
Procedure BUBBLE_SORT(A, N)
    For I = 1 to N-1 do               // runs N-1 times
        For J = 1 to N-I do           // runs N-I times
            If A[J] > A[J+1] Then
                Swap A[J] and A[J+1]
            End If
        End For
    End For
End Procedure
```
Total comparisons = (n-1) + (n-2) + ... + 1 = **n(n-1)/2 = O(n²)**

For n=10: ~45 operations. For n=100: ~4,950. For n=1000: ~499,500.
The time grows quadratically — doubling n quadruples the time.

---


---

## [2018] Q2(a) "Complexity analysis is a vital issue" — Explain. (04)

Complexity analysis is vital because it allows us to predict an algorithm's performance **before** running it, enabling us to choose the best algorithm for a given problem.

**Example:** Searching in a sorted array of 1,000,000 elements:
- **Linear Search:** O(n) = 1,000,000 comparisons in worst case
- **Binary Search:** O(log n) = ~20 comparisons in worst case

Without complexity analysis, we might implement linear search, wasting enormous time. Complexity analysis tells us binary search is exponentially better.

**Why it matters:**
1. Helps compare algorithms objectively
2. Predicts scalability — will it work for large inputs?
3. Identifies bottlenecks in the algorithm
4. Guides algorithm selection based on problem constraints

---


---

## [2019] Q.5(a) Criterions for best fit algorithm. Why better algorithm needed? (04)

**Criterions for selecting a best fit algorithm:**

1. **Time Complexity** — How fast does it run? Compare best/worst/average cases.
2. **Space Complexity** — How much extra memory does it require?
3. **Input characteristics** — Is data nearly sorted? Random? Size?
4. **Stability** — Does it preserve relative order of equal elements?
5. **Simplicity** — How easy is it to implement and maintain?

**Why a better algorithm is needed:**
A better algorithm can solve the same problem significantly faster. For example, sorting 1 million items:
- Bubble Sort O(n²) → ~10¹² operations → takes hours
- Merge Sort O(n log n) → ~2×10⁷ operations → takes seconds

Choosing the right algorithm can mean the difference between a solution that runs in seconds vs one that takes days. As data sizes grow, algorithm efficiency becomes critical.

---


---

## [2019] Q.5(b) Rate of growth. Technique to find complexity. (04)

**Rate of Growth:** The rate at which the running time of an algorithm increases as the input size n increases. It describes the asymptotic behavior of the function.

Common growth rates (slowest to fastest):
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ)

**Technique — Counting Method:**
Count the number of basic operations as a function of input size n.

**Example:**
```
Sum = 0                    // 1 operation
For I = 1 to N do          // loop runs N times
    For J = 1 to N do      // loop runs N times
        Sum = Sum + 1      // 1 operation
    End For
End For
```
Total operations = 1 + N × N × 1 = N² + 1

**Rate of growth = O(n²)**

We drop constants and lower-order terms, keeping only the dominant term.

---


---

## [2020] Q.5(a) Frequency counts. (04)

**(i) Triple nested loop:**
```
for i:=1 to n do
    for j:=1 to i do
        for k:=1 to j do
            x:=x+1;
```

The innermost statement executes: Σ(i=1 to n) Σ(j=1 to i) j = Σ(i=1 to n) i(i+1)/2

= (1/2) Σ(i=1 to n) (i² + i) = (1/2)[n(n+1)(2n+1)/6 + n(n+1)/2]

> **Frequency ≈ n³/6 = O(n³)**

**(ii) While loop:**
```
i:=1;                   // 1 time
while (i <= n) do       // n+1 times (n true + 1 false)
    x:=x+1;            // n times
    i:=i+1;            // n times
```

> **Frequency = 1 + (n+1) + n + n = 3n + 2 = O(n)**

---


---

## [2020] Q.8(b) Big-O notation. Methods to calculate complexity. (04)

**Big-O Notation:** Describes the upper bound of an algorithm's growth rate. f(n) = O(g(n)) means there exist constants c and n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀.

**Methods to calculate complexity:**
1. **Counting method:** Count basic operations as function of n
2. **Recurrence method:** Express T(n) recursively, solve using substitution or Master Theorem
3. **Amortized analysis:** Average cost over sequence of operations

**Example (Counting):**
```
For I = 1 to N do        // N times
    For J = 1 to N do    // N times
        x = x + 1        // 1 operation
```
Total = N × N = N² → **O(n²)**

---


---

## [2022] Q.1(b) Merge two sorted arrays. Time complexity. (CO2, 04)

```
Procedure MERGE_SORTED(A, N, B, M, C)
    // A = sorted array of size N, B = sorted array of size M
    // C = output merged sorted array
    Set I = 1, J = 1, K = 1
    While I <= N AND J <= M do
        If A[I] <= B[J] Then
            Set C[K] = A[I]
            Set I = I + 1
        Else
            Set C[K] = B[J]
            Set J = J + 1
        End If
        Set K = K + 1
    End While
    // Copy remaining elements
    While I <= N do
        Set C[K] = A[I]
        Set I = I + 1, K = K + 1
    End While
    While J <= M do
        Set C[K] = B[J]
        Set J = J + 1, K = K + 1
    End While
End Procedure
```

**Time Complexity: O(N + M)** — each element is compared and copied exactly once. We traverse both arrays once linearly.

**Space Complexity: O(N + M)** — for the output array C.

---


---

## [2023] Q.6 Memory space for complexity analysis. (CLO2, 03)

Memory space must be considered because:

1. **Limited resources** — RAM is finite. An algorithm using O(n²) space may crash for large inputs even if it's time-efficient.
2. **Cache performance** — algorithms using less memory have better cache utilization, running faster in practice.
3. **Trade-offs** — some algorithms trade space for time (e.g., hash tables use extra space for O(1) access). We must evaluate whether the space cost is justified.

**Example:** Merge sort uses O(n) extra space vs Quick sort's O(log n). For memory-constrained systems, quick sort is preferred despite similar time complexity.

---


---

## [2024] Q.3(b) Time complexity of nested loop. (CO2, 03)

```
for i = 1 to n:
    for j = 1 to n:
        print(i, j)
```

- Outer loop runs **n** times
- Inner loop runs **n** times for each iteration of outer loop
- `print(i,j)` executes n × n = **n²** times

> **Time Complexity: O(n²)**

---


---

## 📊 Exam Priority
**Priority: 1/5** (Must Prepare — appeared EVERY year)
**Appeared in:** 8/8 years
**Typical marks:** 03–05 per question
