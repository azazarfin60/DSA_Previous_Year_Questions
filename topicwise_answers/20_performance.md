# Performance Analysis vs Measurement, Garbage Collection


---

## [2021] Q.6(a) "Performance analysis is far better than performance measurement." (03)

**Performance Analysis (a priori):** Determines algorithm efficiency **before** implementation using mathematical analysis (Big-O, recurrence). It is machine-independent and gives a general measure.

**Performance Measurement (a posteriori):** Measures actual running time **after** implementation on a specific machine. Depends on hardware, compiler, OS, and load.

**Why analysis is better:**
1. **Machine-independent** — results valid across all computers
2. **Done early** — before spending time coding; helps choose the best algorithm upfront
3. **Predicts scalability** — shows how performance changes with larger inputs
4. **Objective comparison** — two algorithms can be compared without implementation bias

Measurement is useful for fine-tuning but cannot replace theoretical analysis.

---


---

## [2021] Q.7(d) What is garbage collection? (01)

**Garbage Collection:** The automatic process of identifying and reclaiming memory cells (nodes) that are no longer referenced by any pointer in the program, returning them to the AVAIL (free space) list for reuse.

---


---

## [2023] Q.7(b) Performance analysis vs performance measurement. (CLO1, 02)

| Criterion | Performance Analysis | Performance Measurement |
|---|---|---|
| When | Before implementation (a priori) | After implementation (a posteriori) |
| Method | Mathematical (Big-O, recurrence) | Actual timing on hardware |
| Dependency | Machine-independent | Machine-dependent |
| Input | Theoretical input size n | Actual test data |
| Use | Compare algorithms abstractly | Fine-tune implementation |

---


---

## [2023] Q.8(c) Define algorithm. (CLO1, 01)

**Algorithm:** A finite, well-defined sequence of instructions or steps designed to solve a specific problem or perform a computation. It takes input, processes it through defined steps, and produces output in finite time.

---

## [2024] Q.6(c) "Performance analysis is far better than performance measurement." (CO2, 03)

**Performance Analysis (a priori):** Uses mathematical tools (Big-O, recurrence) to evaluate algorithm efficiency **before** coding. Machine-independent.

**Performance Measurement (a posteriori):** Measures actual execution time **after** implementation. Machine-dependent.

**Why analysis is better:**
1. **Machine-independent** — valid across all hardware configurations
2. **Done early** — choose the best algorithm before investing coding effort
3. **Predicts scalability** — shows behavior for any input size n
4. **Fair comparison** — two algorithms compared on equal theoretical footing

Measurement is useful for fine-tuning but cannot replace theoretical analysis for algorithm selection.

---


---

## 📊 Exam Priority
**Priority: 3/5** (Good to Know)
**Appeared in:** 3/8 years
**Typical marks:** 01–03 per question
