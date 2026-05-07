# Recurrence Relations — Substitution Method, Master Theorem


---

## [2022] Q.6(c) Recurrence: T(n) = 2T(n/2) + n, T(1)=2. (CO2, 03)

**Substitution method:**

T(n) = 2T(n/2) + n
     = 2[2T(n/4) + n/2] + n = 4T(n/4) + 2n
     = 4[2T(n/8) + n/4] + 2n = 8T(n/8) + 3n
     ...
     = 2^k · T(n/2^k) + k·n

When n/2^k = 1 → k = log₂n:
T(n) = n · T(1) + n·log₂n = 2n + n·log₂n

> **T(n) = n log n + 2n = O(n log n)**

---


---

## [2023] Q.6(a) T(n) = 2T(n/2) + Θ(n) using Master method. (CLO2, 03)

**Master Theorem:** T(n) = aT(n/b) + f(n)

Here: a = 2, b = 2, f(n) = Θ(n)

Compute: n^(log_b a) = n^(log₂ 2) = n¹ = n

Compare f(n) = Θ(n) with n^(log_b a) = n → they are **equal**.

This is **Case 2:** f(n) = Θ(n^(log_b a))

> **T(n) = Θ(n log n)**

---


---

## 📊 Exam Priority
**Priority: 2/5** (Should Prepare)
**Appeared in:** 4/8 years
**Typical marks:** 03–04 per question
