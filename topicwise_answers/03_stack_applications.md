# Stack Applications — Postfix Evaluation, Infix→Postfix Conversion


---

## [2017] 3(a) Evaluate postfix: 15, 8, 3, -, 1, 4, 2, 6, +, *, + (04)

**Note:** The expression seems to have an issue with operands/operators count. Evaluating as given, processing left to right:

| Step | Symbol | Stack (top→) | Action |
|---|---|---|---|
| 1 | 15 | 15 | Push |
| 2 | 8 | 15, 8 | Push |
| 3 | 3 | 15, 8, 3 | Push |
| 4 | − | 15, 5 | 8-3=5 |
| 5 | 1 | 15, 5, 1 | Push |
| 6 | 4 | 15, 5, 1, 4 | Push |
| 7 | 2 | 15, 5, 1, 4, 2 | Push |
| 8 | 6 | 15, 5, 1, 4, 2, 6 | Push |
| 9 | + | 15, 5, 1, 4, 8 | 2+6=8 |
| 10 | * | 15, 5, 1, 32 | 4*8=32 |
| 11 | + | 15, 5, 33 | 1+32=33 |

Remaining stack: 15, 5, 33 — expression appears incomplete in the original paper. If we apply two more operations implicitly:

Assuming the full expression resolves, the intermediate result after all valid operations is **33** from the last sub-expression.

---


---

## [2019] Q.3(c) Postfix notation of (3+9)² − 4. (04)

**Infix Expression:** (3 + 9) ↑ 2 − 4

**Using stack-based Infix to Postfix conversion:**

| Symbol | Stack | Output |
|---|---|---|
| ( | ( | |
| 3 | ( | 3 |
| + | ( + | 3 |
| 9 | ( + | 3 9 |
| ) | (empty) | 3 9 + |
| ↑ | ↑ | 3 9 + |
| 2 | ↑ | 3 9 + 2 |
| − | − | 3 9 + 2 ↑ |
| 4 | − | 3 9 + 2 ↑ 4 |
| End | (empty) | 3 9 + 2 ↑ 4 − |

> **Postfix: 3 9 + 2 ↑ 4 −**

**Verification (evaluating the postfix):**
- 3 9 + → 12
- 12 2 ↑ → 144
- 144 4 − → **140** ✓

---


---

## [2021] Q.3(a) Infix→Postfix: A + (B * C − (D/E ↑ F) * G) * H (04)

| Step | Symbol | Stack | Output (P) |
|---|---|---|---|
| 1 | A | | A |
| 2 | + | + | A |
| 3 | ( | + ( | A |
| 4 | B | + ( | A B |
| 5 | * | + ( * | A B |
| 6 | C | + ( * | A B C |
| 7 | − | + ( − | A B C * |
| 8 | ( | + ( − ( | A B C * |
| 9 | D | + ( − ( | A B C * D |
| 10 | / | + ( − ( / | A B C * D |
| 11 | E | + ( − ( / | A B C * D E |
| 12 | ↑ | + ( − ( / ↑ | A B C * D E |
| 13 | F | + ( − ( / ↑ | A B C * D E F |
| 14 | ) | + ( − | A B C * D E F ↑ / |
| 15 | * | + ( − * | A B C * D E F ↑ / |
| 16 | G | + ( − * | A B C * D E F ↑ / G |
| 17 | ) | + | A B C * D E F ↑ / G * − |
| 18 | * | + * | A B C * D E F ↑ / G * − |
| 19 | H | + * | A B C * D E F ↑ / G * − H |
| 20 | End | | A B C * D E F ↑ / G * − H * + |

> **Postfix P: A B C * D E F ↑ / G * − H * +**

---


---

## [2022] Q.4(b) Evaluate postfix: 9 4 3 2 / 1 5 + * / * + (CO1, 04)

Processing left to right:

| Step | Symbol | Stack | Action |
|---|---|---|---|
| 1 | 9 | 9 | Push |
| 2 | 4 | 9, 4 | Push |
| 3 | 3 | 9, 4, 3 | Push |
| 4 | 2 | 9, 4, 3, 2 | Push |
| 5 | / | 9, 4, 1 | 3/2 = 1 (integer division) |
| 6 | 1 | 9, 4, 1, 1 | Push |
| 7 | 5 | 9, 4, 1, 1, 5 | Push |
| 8 | + | 9, 4, 1, 6 | 1+5 = 6 |
| 9 | * | 9, 4, 6 | 1×6 = 6 |
| 10 | / | 9, 0 | 4/6 = 0 (integer) |
| 11 | * | 0 | 9×0 = 0 |
| 12 | + | — | insufficient operands |

Assuming real division at step 5: 3/2 = 1.5

| 5 | / | 9, 4, 1.5 | 3/2=1.5 |
| 8 | + | 9, 4, 1.5, 6 | 1+5=6 |
| 9 | * | 9, 4, 9 | 1.5×6=9 |
| 10 | / | 9, 0.44 | 4/9=0.44 |
| 11 | * | 4 | 9×0.44=4 |

> **Result ≈ 4** (with real division)

---


---

## [2024] Q.2(b) Infix→Postfix: A + (B * C − (D / E ↑ F) * G) * H (CO2, 04)

| Step | Symbol | Stack | Output (P) |
|---|---|---|---|
| 1 | A | | A |
| 2 | + | + | A |
| 3 | ( | + ( | A |
| 4 | B | + ( | A B |
| 5 | * | + ( * | A B |
| 6 | C | + ( * | A B C |
| 7 | − | + ( − | A B C * |
| 8 | ( | + ( − ( | A B C * |
| 9 | D | + ( − ( | A B C * D |
| 10 | / | + ( − ( / | A B C * D |
| 11 | E | + ( − ( / | A B C * D E |
| 12 | ↑ | + ( − ( / ↑ | A B C * D E |
| 13 | F | + ( − ( / ↑ | A B C * D E F |
| 14 | ) | + ( − | A B C * D E F ↑ / |
| 15 | * | + ( − * | A B C * D E F ↑ / |
| 16 | G | + ( − * | A B C * D E F ↑ / G |
| 17 | ) | + | A B C * D E F ↑ / G * − |
| 18 | * | + * | A B C * D E F ↑ / G * − |
| 19 | H | + * | A B C * D E F ↑ / G * − H |
| 20 | End | | A B C * D E F ↑ / G * − H * + |

> **Postfix P: A B C * D E F ↑ / G * − H * +**

---


---

## 📊 Exam Priority
**Priority: 1/5** (Must Prepare)
**Appeared in:** 5/8 years
**Typical marks:** 04 per question
