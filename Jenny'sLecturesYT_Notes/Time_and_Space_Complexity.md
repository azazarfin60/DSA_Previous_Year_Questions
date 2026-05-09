[⬅️ Previous](./Introduction_to_Data_Structure_and_Algorithm.md) | [🏠 Home](./README.md)

---

# Time and Space Complexity

📺 [Watch on YouTube](https://www.youtube.com/watch?v=IzGac_ZANqg)

---

## 📌 Executive Summary

This lecture covers complexity analysis — specifically **time complexity** and **space complexity**. It explains why we analyze algorithms, how to calculate Big-O notation, the rules for simplifying complexity expressions, and the difference between best/worst/average case analysis. Time complexity is NOT the actual execution time — it's a theoretical measure of how runtime scales with input size.

---

## 🔑 Core Concepts

### Analysis of Algorithm
- The process of determining the resources (time, space) required by an algorithm
- Factors: time, space, correctness, trade-offs, best/worst/average case
- **Complexity analysis** focuses specifically on **time** and **space** complexity

### Time Complexity ≠ Execution Time

| Aspect | Execution Time | Time Complexity |
|--------|---------------|-----------------|
| Unit | milliseconds, seconds | Big-O notation |
| Depends on | hardware, CPU, background processes | algorithm/logic only |
| Same algorithm, different machines | Different values | Same value |
| Purpose | Actual runtime | Growth rate relationship |

> **Key Definition:** Time complexity is the measure of time taken by an algorithm **as a function of input size (n)**. It shows the relationship between input size and number of operations.

### Big-O Notation (Worst Case)
- Describes the **upper bound** of an algorithm's time complexity
- Represents the **worst-case scenario**
- Provides a **guarantee** — algorithm won't take longer than this

### Why Worst Case?
- Provides performance guarantees
- Helps plan resources for the most demanding scenario
- Real-life analogy: planning for worst traffic conditions, not best ones

---

## 📊 Common Complexities Compared

| Complexity | Name | Example | Operations for n=1000 |
|-----------|------|---------|----------------------|
| **O(1)** | Constant | Direct array access | 1 |
| **O(log n)** | Logarithmic | Binary Search | ~10 |
| **O(n)** | Linear | Linear Search | 1000 |
| **O(n²)** | Quadratic | Nested loops (pairs) | 1,000,000 |
| **O(n³)** | Cubic | Triple nested loops | 1,000,000,000 |

### Linear Search vs Binary Search

```
Linear Search: O(n)         Binary Search: O(log n)
─────────────────           ──────────────────────
Compare one by one          Array must be sorted
Works on unsorted data      Divide array in half each step
n=1000 → 1000 comparisons   n=1000 → ~10 comparisons
```

---

## 📏 Rules for Calculating Time Complexity

### Rule 1: Always Consider Worst Case
```
Array: [10, 1, 5, 0, 20]
Searching for 20 (last element) → must check ALL n elements
Worst case = O(n)
```

### Rule 2: Focus on Frequently Executed Statements
- Focus on **loops**, **recursive calls**, **function calls**
- Ignore constant-time operations (assignments, single comparisons)

### Rule 3: Drop the Constants
```
O(2n) → O(n)
O(n + 100) → O(n)
O(n/2) → O(n)
```
Constants don't matter for large n because the **growth relationship** stays the same.

### Rule 4: Ignore Less Dominating Terms
```
O(n² + n) → O(n²)
O(n³ + n² + 100 + n/2) → O(n³)
```
Keep only the highest-order term.

### Rule 5: Different Inputs → Different Variables
```c
// If iterating over TWO different arrays:
for (i = 0; i < arr1.length; i++)    // O(n)
  for (j = 0; j < arr2.length; j++)  // O(m)

// Time Complexity = O(n × m), NOT O(n²)
// Only O(n²) if arr1 and arr2 are the same array
```

---

## 💻 Complexity of Common Patterns

```c
// Pattern 1: Single loop → O(n)
for (int i = 0; i < n; i++) { ... }

// Pattern 2: Nested loop → O(n²)
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) { ... }

// Pattern 3: Dividing by 2 each step → O(log n)
while (i > 1) { i = i / 2; ... }

// Pattern 4: Constant loop → O(1)
for (int i = 0; i < 100; i++) { ... }
```

---

## 🗄️ Space Complexity

**Space Complexity** = Fixed Space (input) + Auxiliary Space (extra/temporary)

| Component | Example | Space |
|-----------|---------|-------|
| Input array of size n | `int arr[n]` | O(n) |
| Few variables | `int i, sum, temp` | O(1) |
| Copy of input array | `int copy[n]` | O(n) |

- **In-place algorithms** (e.g., Bubble Sort): O(1) auxiliary space
- Interviews usually care about **auxiliary space** (extra space beyond input)

### Example
```c
int total = 0;           // O(1)
for (int i = 0; i < n; i++)
    total += arr[i];     // No extra array needed
// Space Complexity: O(1) (excluding input)
```

---

## 📐 Asymptotic Notations

| Notation | Name | Represents | Bound |
|----------|------|-----------|-------|
| **O** (Big-O) | Worst Case | Upper bound | Most commonly used |
| **Ω** (Omega) | Best Case | Lower bound | Rarely used alone |
| **Θ** (Theta) | Average Case | Tight bound | Exact growth rate |

---

## 💡 Key Takeaways

- Time complexity measures **scalability**, not actual speed
- Always analyze for **worst case** using **Big-O notation**
- **Drop constants** and **less dominating terms** in Big-O
- O(log n) < O(n) < O(n²) < O(n³) — prefer lower complexity
- For small data, algorithm choice doesn't matter much; for **large data**, it's critical
- Space complexity = input space + auxiliary space
- Scalability is the most important factor in software development

<br>

---
[⬅️ Previous](./Introduction_to_Data_Structure_and_Algorithm.md) | [🏠 Home](./README.md)
