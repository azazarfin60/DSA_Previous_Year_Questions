# 📋 DSA Cheatsheet — Quick Reference

---

## Time Complexity Summary

| Algorithm | Best | Average | Worst | Space |
|---|---|---|---|---|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1)/O(log n) |
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) |
| **BST Search** | O(log n) | O(log n) | O(n) | O(1) |
| **Hash Search** | O(1) | O(1) | O(n) | O(n) |
| **BFS / DFS** | O(V+E) | O(V+E) | O(V+E) | O(V) |
| **Dijkstra** | — | O(V²) | O(V²) | O(V) |
| **Bellman-Ford** | — | O(VE) | O(VE) | O(V) |
| **Prim's** | — | O(V²) | O(V²) | O(V) |
| **Kruskal's** | — | O(E log E) | O(E log E) | O(V) |

---

## Key Formulas

| Formula | For |
|---|---|
| `B + i × w` | 1D Array address |
| `B + (i×N + j) × w` | 2D Row-Major address |
| `B + (j×M + i) × w` | 2D Column-Major address |
| `2^(h+1) − 1` | Max nodes in binary tree of height h |
| `⌊log₂(n)⌋` | Min height of binary tree with n nodes |
| `n + 1` | External nodes in 2-tree with n internal nodes |
| `2ⁿ − 1` | Tower of Hanoi moves for n disks |
| `h(k) = k mod m` | Hash function (division method) |
| Parent: `(i-1)/2` | Heap parent index |
| Children: `2i+1, 2i+2` | Heap children indices |

---

## Traversal Order Mnemonics

| Traversal | Order | Mnemonic |
|---|---|---|
| **Pre**order | **Root** → Left → Right | Root comes **PRE** (before) |
| **In**order | Left → **Root** → Right | Root is **IN** the middle |
| **Post**order | Left → Right → **Root** | Root comes **POST** (after) |

> **Inorder of BST = Sorted Order** (most important property!)

---

## Stack Rules for Infix→Postfix

1. **Operand** → output directly
2. **`(`** → push
3. **`)`** → pop until `(`
4. **Operator** → pop ≥ precedence, then push
5. **End** → pop all remaining

**Precedence:** `↑` (3) > `*,/` (2) > `+,-` (1)

---

## Dijkstra Steps

1. Set all distances to ∞, source = 0
2. Pick unvisited vertex with **minimum distance**
3. **Relax** all its neighbors: `if dist[u] + w < dist[v] → update`
4. Mark vertex as visited
5. Repeat until all visited

---

## MST Quick Rules

| Prim's | Kruskal's |
|---|---|
| Start from a vertex | Sort all edges |
| Add cheapest crossing edge | Add cheapest non-cycle edge |
| Grow one tree | Merge forests |
| Dense graphs (O(V²)) | Sparse graphs (O(E log E)) |

---

## Heap Operations

| Insert | Delete (root) |
|---|---|
| Add at end → **Bubble UP** | Replace root with last → **Sift DOWN** |
| Compare with parent | Compare with larger child (max-heap) |
| Swap if violates | Swap if violates |
| O(log n) | O(log n) |

---

## Knapsack Quick Reference

| 0/1 (DP) | Fractional (Greedy) |
|---|---|
| Item taken or not | Fractions allowed |
| DP table V[i][w] | Sort by value/weight ratio |
| O(nW) | O(n log n) |

---

## Graph Representation

| | Matrix | List |
|---|---|---|
| Space | O(V²) | O(V+E) |
| Edge check | O(1) | O(degree) |
| Dense graphs | ✅ | ❌ |
| Sparse graphs | ❌ | ✅ |
