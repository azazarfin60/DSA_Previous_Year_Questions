# 2017 — ECE 2103 Answer Key
# Section A

---

## 1(a) Define linear and non-linear data structure. Discuss major operations. (04)

**Linear Data Structure:** A data structure where elements are arranged in a sequential manner and each element has a unique predecessor and successor (except first and last).
*Examples:* Array, Linked List, Stack, Queue.

**Non-linear Data Structure:** A data structure where elements are not arranged sequentially. Each element can connect to multiple elements, forming hierarchical or network relationships.
*Examples:* Tree, Graph.

**Major Operations in Data Structure:**

1. **Traversing** — Accessing/visiting each element exactly once (e.g., printing all array elements)
2. **Searching** — Finding the location of an element (e.g., binary search)
3. **Inserting** — Adding a new element to the structure
4. **Deleting** — Removing an existing element from the structure
5. **Sorting** — Arranging elements in a specific order (ascending/descending)
6. **Merging** — Combining two sorted structures into a single sorted structure

---

## 1(b) What is time-space trade off? Give an example. (04)

**Time-Space Trade Off:** It is a situation where we can reduce the time required by an algorithm by using more memory space, or reduce memory usage by allowing the algorithm to take more time. We trade one resource for another to optimize performance.

**Example — Sorted Array vs Linked List:**

| Criterion | Sorted Array | Linked List |
|---|---|---|
| Search Time | O(log n) — binary search | O(n) — linear only |
| Space | No extra pointers | Extra pointer per node |
| Insertion | O(n) — shifting needed | O(1) — pointer update |

Another example: **Hash Table** uses extra space (hash array) to reduce search time from O(n) to O(1) average. Here, we trade space for faster time.

**Compressed vs Uncompressed data:** Storing data in compressed form saves space but requires extra time to decompress. Uncompressed data uses more space but is accessed instantly.

---

## 1(c) "Quick sort is better than bubble sort." Explain. (04)

**Bubble Sort:**
- Compares adjacent elements and swaps if out of order
- Time: Best O(n), Worst O(n²), Average O(n²)
- Very slow for large datasets

**Quick Sort:**
- Uses divide-and-conquer with a pivot element
- Time: Best O(n log n), Worst O(n²), Average O(n log n)
- Much faster in practice

| Criterion | Quick Sort | Bubble Sort |
|---|---|---|
| Avg Time | O(n log n) | O(n²) |
| Approach | Divide & Conquer | Brute force comparison |
| Swaps | Fewer (distant swaps) | Many (adjacent only) |
| In-place | Yes | Yes |
| Practical speed | Very fast | Very slow |

**Example:** For array [5, 3, 8, 1, 9]:
- Bubble Sort needs ~10 comparisons and many swaps
- Quick Sort with pivot=5: partition into [3,1] [5] [8,9], then recurse — far fewer operations

Quick sort is better because its average case O(n log n) is significantly faster than bubble sort's O(n²). For n=1000, quick sort does ~10,000 operations vs bubble sort's ~1,000,000.

---

## 2(a) What is garbage collection? Memory representation of linked list. Difference from array. (04)

**Garbage Collection:** The process of automatically collecting and reclaiming unused memory cells (nodes that are no longer referenced by any pointer) and returning them to the AVAIL (free space) list for future use.

**Memory Representation of Linked List:**
A linked list is stored using two parallel arrays:
- **INFO[ ]** — stores the actual data
- **LINK[ ]** — stores the index of the next node

Two special pointers:
- **START** — points to the first node
- **AVAIL** — points to the first free (available) node

```
Index:  1    2    3    4    5
INFO:  [40] [30] [ ] [10] [20]
LINK:  [ 5] [ 1] [—] [ 2] [ 0]
START = 4,  AVAIL = 3
```
Traversal: 4→10, 2→30, 1→40, 5→20, 0(end)

**Differences from Array:**

| Criterion | Linked List | Array |
|---|---|---|
| Memory | Dynamic, non-contiguous | Static, contiguous |
| Size | Can grow/shrink | Fixed at declaration |
| Access | Sequential O(n) | Random access O(1) |
| Insert/Delete | O(1) pointer change | O(n) shifting needed |

---

## 2(b) Linked List CGPA ordering and insertion. (04)

**Given:** INFO = {3.80, 3.95, _, 3.90, _}, START and AVAIL pointers.

**i) Linking in descending order of CGPA (3.95 → 3.90 → 3.80):**

| Index | INFO | LINK |
|---|---|---|
| 1 | 3.80 | 0 (end) |
| 2 | 3.95 | 4 |
| 3 | — | 5 |
| 4 | 3.90 | 1 |
| 5 | — | 0 |

**START = 2**, AVAIL = 3

Traversal: 2(3.95) → 4(3.90) → 1(3.80) → end ✓

**ii) Insert 4.00 (should become the first element since 4.00 > 3.95):**

Take node from AVAIL: index 3. New AVAIL = 5.

| Index | INFO | LINK |
|---|---|---|
| 1 | 3.80 | 0 |
| 2 | 3.95 | 4 |
| 3 | **4.00** | **2** |
| 4 | 3.90 | 1 |
| 5 | — | 0 |

**START = 3**, AVAIL = 5

Traversal: 3(4.00) → 2(3.95) → 4(3.90) → 1(3.80) → end ✓

---

## 2(c) Binary Search for item 18 in DATA. (04)

**DATA:** 10 18 23 25 30 35 45 50 60 70 (indices 1 to 10)

**Pass 1:**
- BEG = 1, END = 10
- MID = ⌊(1+10)/2⌋ = 5
- DATA[5] = 30 > 18 → search left half
- Set END = MID - 1 = 4

**Pass 2:**
- BEG = 1, END = 4
- MID = ⌊(1+4)/2⌋ = 2
- DATA[2] = 18 = 18 → **ITEM FOUND at position 2** ✓

| Pass | BEG | END | MID | DATA[MID] | Action |
|---|---|---|---|---|---|
| 1 | 1 | 10 | 5 | 30 | 30 > 18, END = 4 |
| 2 | 1 | 4 | 2 | 18 | **Found!** |

> **Result: Item 18 found at index 2 in 2 passes.**

---

## 3(a) Evaluate postfix: 15, 8, 3, -, 1, 4, 2, 6, +, *, + (04)

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

## 3(b) Priority Queue operations. (06)

**Initial State:**
- Queue 1: empty (F=0, R=0)
- Queue 2: DD, UU, GG (F=2, R=4)
- Queue 3: FF (F=1, R=1)
- Queue 4: RR, SS, CC, _, XX, EE (F=5, R=3, wraps around)
- Queue 5: TT (F=4, R=4)

**(i) Delete two elements (deletion is by priority — lowest queue number first):**

Delete 1: Queue 1 is empty → Queue 2: delete DD (Front 2→3)
Delete 2: Queue 2: delete UU (Front 3→4)

After deletion:

| Queue | Front | Rear | Elements |
|---|---|---|---|
| 1 | 0 | 0 | (empty) |
| 2 | 4 | 4 | GG |
| 3 | 1 | 1 | FF |
| 4 | 5 | 3 | XX, EE, RR, SS, CC |
| 5 | 4 | 4 | TT |

**(ii) Insert (AA,3), (BB,1), (LL,4), (MM,5):**

- AA → Queue 3: add after FF → R becomes 2
- BB → Queue 1: first element → F=1, R=1
- LL → Queue 4: add after CC → R becomes 4
- MM → Queue 5: add after TT → R becomes 5

| Queue | Front | Rear | Elements |
|---|---|---|---|
| 1 | 1 | 1 | BB |
| 2 | 4 | 4 | GG |
| 3 | 1 | 2 | FF, AA |
| 4 | 5 | 4 | XX, EE, RR, SS, CC, LL |
| 5 | 4 | 5 | TT, MM |

**(iii) Delete five elements (by priority):**

1. Delete BB from Queue 1 (now empty, F=0, R=0)
2. Delete GG from Queue 2 (now empty, F=0, R=0)
3. Delete FF from Queue 3 (F becomes 2)
4. Delete AA from Queue 3 (now empty, F=0, R=0)
5. Delete XX from Queue 4 (F becomes 6)

| Queue | Front | Rear | Elements |
|---|---|---|---|
| 1 | 0 | 0 | (empty) |
| 2 | 0 | 0 | (empty) |
| 3 | 0 | 0 | (empty) |
| 4 | 6 | 4 | EE, RR, SS, CC, LL |
| 5 | 4 | 5 | TT, MM |

---

## 3(c) Properties of recursive procedure. (02)

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

## 4(a) Construct tree from Inorder and Preorder. (05)

**Inorder:**  M N O P Q R S T U
**Preorder:** Q N M P O S R U T

**Step 1:** First element of Preorder = **Q** → Root
In Inorder, Q splits into: Left = {M, N, O, P}, Right = {R, S, T, U}

**Step 2:** Next in Preorder = **N** → Root of left subtree
In left Inorder {M, N, O, P}, N splits: Left = {M}, Right = {O, P}

**Step 3:** Next = **M** → Left child of N (leaf node)

**Step 4:** Next = **P** → Root of {O, P} subtree
In {O, P}, P splits: Left = {O}, Right = {}

**Step 5:** Next = **O** → Left child of P (leaf)

**Step 6:** Next = **S** → Root of right subtree {R, S, T, U}
In {R, S, T, U}, S splits: Left = {R}, Right = {T, U}

**Step 7:** Next = **R** → Left child of S (leaf)

**Step 8:** Next = **U** → Root of {T, U}
In {T, U}, U splits: Left = {T}, Right = {}

**Step 9:** Next = **T** → Left child of U (leaf)

```
            Q
           / \
          N    S
         / \  / \
        M  P R   U
          /     /
         O     T
```

---

## 4(b) BST from: 20, 15, 10, 30, 20, 40, 10, 12, 50, 10 (05)

**Step-by-step insertion (duplicates ignored in standard BST):**

Insert 20 → root
Insert 15 → 15 < 20, go left
Insert 10 → 10 < 20 < 15, go left of 15
Insert 30 → 30 > 20, go right
Insert 20 → duplicate, skip
Insert 40 → 40 > 30, go right of 30
Insert 10 → duplicate, skip
Insert 12 → 12 > 10, go right of 10
Insert 50 → 50 > 40, go right of 40
Insert 10 → duplicate, skip

```
         20
        /  \
      15    30
      /       \
    10        40
      \         \
      12        50
```

---

## 4(c) What is 2-tree? (02)

A **2-tree** (also called an **extended binary tree** or **strictly binary tree**) is a binary tree in which every node has either **0 children (leaf)** or exactly **2 children (internal node)**. No node has exactly one child.

**Properties:**
- If there are n internal nodes, there are (n+1) leaf nodes
- Leaf nodes are called **external nodes** (often shown as squares)
- Internal nodes are called **circular nodes**

```
       A          ← internal (2 children)
      / \
     B   C        ← B is internal, C is leaf (external)
    / \
   □   □          ← external nodes
```

---

# Section B

---

## 5(a) What is complexity? Discuss O(n²). (04)

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

## 5(b) When is insertion sort more efficient? (02)

Insertion sort is more efficient than other algorithms in these cases:

1. **Nearly sorted data** — When the array is almost sorted, insertion sort runs in **O(n)** time because very few shifts are needed.
2. **Small input size** — For small arrays (n < 20), insertion sort outperforms quick sort and merge sort due to low overhead (no recursion, no extra space).
3. **Online sorting** — When data arrives one element at a time, insertion sort can sort incrementally.

---

## 5(c) MergeSort call tree for D: 50, 100, 30, 10, 200, 150 (06)

**MergeSort Partition Tree (splitting):**

```
              [50,100,30,10,200,150]
              /                    \
      [50,100,30]              [10,200,150]
       /       \                /         \
   [50,100]   [30]        [10,200]      [150]
    /    \                  /    \
  [50]  [100]            [10]  [200]
```

**Merge Tree (combining back):**

```
  [50] [100]            [10] [200]
    \   /                 \   /
  [50,100]  [30]       [10,200]  [150]
      \     /              \      /
   [30,50,100]          [10,150,200]
         \                   /
      [10,30,50,100,150,200]
```

**Final sorted array: [10, 30, 50, 100, 150, 200]**

**Time Complexity:** O(n log n) for all cases.
- Splitting: log₂(6) ≈ 3 levels
- Each level does O(n) merge work
- Total: O(n log n)

---

## 6(a) Discuss: Hashing, Collision Resolution, Chaining. (03)

**(i) Hashing:** A technique to map data (keys) to fixed-size values (hash codes) using a **hash function** h(k). This allows O(1) average-time search, insert, and delete operations. Example: h(k) = k mod 10.

**(ii) Collision Resolution:** When two different keys map to the same hash index, a **collision** occurs. Collision resolution is the method used to handle this. Two main methods:
- Open Addressing (Linear Probing, Quadratic Probing)
- Separate Chaining

**(iii) Chaining:** A collision resolution method where each slot of the hash table contains a **linked list**. All keys that hash to the same index are stored in that slot's linked list.

```
Index 0: → NULL
Index 1: → 11 → 21 → NULL
Index 2: → 42 → NULL
Index 3: → 23 → 33 → NULL
```

---

## 6(b) Dijkstra's Algorithm from A. (06)

**Graph:** A→B(6), A→C(10), A→D(5), B→D(2), B→E(9), C→E(5), D→B(7), D→E(5)

**Initialization:**
| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | 0 | ∞ | ∞ | ∞ | ∞ |

**Iteration 1: Visit A (dist=0)**
- A→B: 0+6=6 < ∞ → update B=6
- A→C: 0+10=10 < ∞ → update C=10
- A→D: 0+5=5 < ∞ → update D=5

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | 6 | 10 | 5 | ∞ |

**Iteration 2: Visit D (dist=5, smallest unvisited)**
- D→B: 5+7=12 > 6 → no update
- D→E: 5+5=10 < ∞ → update E=10

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | 6 | 10 | **5** | 10 |

**Iteration 3: Visit B (dist=6)**
- B→D: 6+2=8 > 5 → no update
- B→E: 6+9=15 > 10 → no update

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | **6** | 10 | **5** | 10 |

**Iteration 4: Visit C (dist=10)**
- C→E: 10+5=15 > 10 → no update

| Node | A | B | C | D | E |
|---|---|---|---|---|---|
| Dist | **0** | **6** | **10** | **5** | 10 |

**Iteration 5: Visit E (dist=10)** — no outgoing edges to update.

**Final Shortest Paths from A:**

| Destination | Distance | Path |
|---|---|---|
| A → A | 0 | A |
| A → B | 6 | A → B |
| A → C | 10 | A → C |
| A → D | 5 | A → D |
| A → E | 10 | A → D → E |

---

## 6(c) Insert 80, 75 into Max Heap. (03)

**Initial Heap:**
```
       100
      /   \
    50     70
   / \    /
  40  45  60
```

**Step 1: Insert 80** — Place at next position (right child of 70), then bubble up.
- 80 > 70 → swap 80 and 70

```
       100
      /   \
    50     80
   / \    / \
  40  45 60  70
```

**Step 2: Insert 75** — Place at next position (left child of 40), then bubble up.
- 75 > 40 → swap
- 75 > 50 → swap

```
        100
       /    \
     75      80
    / \     / \
   50  45  60  70
  /
 40
```

---

## 7(a) Draw graph from adjacency matrix. (04)

**Matrix indicates an undirected graph (symmetric). Self-loop at node 3.**

Edges from matrix:
- 1—2, 1—3, 1—4
- 2—3, 2—5
- 3—3 (self-loop)
- 4—5
```
    1 --- 2
   /|     |
  / |     |
 3--+     5
 ↺  |    /
    4---+
```
Edges: {(1,2), (1,3), (1,4), (2,3), (2,5), (3,3), (4,5)}
Node 3 has a self-loop (matrix[3][3]=1).

---

## 7(b) DFS on directed graph. (04)

**Graph:** BD→UAE, BD→UK, UAE→USA, UAE→AUS, UK→JAP, AUS→RUS, RUS→UAE

**DFS starting from BD (visit left/first neighbor first):**

1. Visit **BD** → neighbors: UAE, UK
2. Visit **UAE** → neighbors: USA, AUS
3. Visit **USA** → no unvisited neighbors, backtrack
4. Visit **AUS** → neighbor: RUS
5. Visit **RUS** → neighbor: UAE (already visited), backtrack
6. Backtrack to BD → visit **UK** → neighbor: JAP
7. Visit **JAP** → no unvisited neighbors

> **DFS Order: BD → UAE → USA → AUS → RUS → UK → JAP**

---

## 7(c) Connected component and BFS proof. (04)

**Connected Component:** A connected component of an undirected graph G is a maximal subgraph in which every pair of vertices is connected by a path. A graph may have one or more connected components.

**Proof that BFS(v) visits all vertices in v's connected component:**

1. BFS starts at vertex v, marks it visited, and adds it to a queue.
2. For each dequeued vertex u, BFS visits all unvisited neighbors of u and enqueues them.
3. Since the component is connected, for any vertex w in the same component, there exists a path v → ... → w.
4. BFS explores vertices layer by layer (by distance). At each layer, it discovers all vertices at distance d before moving to distance d+1.
5. Since a path exists from v to every vertex w in the component, BFS will eventually reach w through some sequence of edges.
6. Vertices outside v's component have no path to v, so they are never reached.

Therefore, BFS(v) visits **exactly** all vertices in v's connected component. ∎

---

## 8(a) Advantages of BST over sorted array and linked list. (03)

| Operation | Sorted Array | Linked List | BST (balanced) |
|---|---|---|---|
| Search | O(log n) | O(n) | **O(log n)** |
| Insert | O(n) shifting | O(n) finding | **O(log n)** |
| Delete | O(n) shifting | O(n) finding | **O(log n)** |
| Space | Fixed size | Dynamic | Dynamic |

**Key Advantages:**
1. BST provides O(log n) search like sorted array, BUT also O(log n) insert/delete unlike sorted array which needs O(n) shifting.
2. BST allows dynamic size like linked list, BUT provides O(log n) search unlike linked list's O(n).
3. BST combines the best of both — fast search AND fast insert/delete.

---

## 8(b) All spanning trees and MST. (05)

**Graph:** ECE—CSE(2), CSE—CE(8), ECE—EEE(4), CE—ME(5), EEE—ME(5), CSE—ME(7), CSE—EEE(3)

5 nodes → spanning tree needs exactly 4 edges.

**Some possible spanning trees (of many):**

**ST1:** ECE—CSE(2), CSE—EEE(3), CSE—CE(8), CE—ME(5) → Total = 18
**ST2:** ECE—CSE(2), CSE—EEE(3), EEE—ME(5), CSE—CE(8) → Total = 18
**ST3:** ECE—CSE(2), CSE—EEE(3), EEE—ME(5), CE—ME(5) — ✗ (cycle via ME)
**ST4:** ECE—CSE(2), CSE—EEE(3), CE—ME(5), CSE—ME(7) — ✗ (cycle via ME)
**ST5:** ECE—CSE(2), CSE—EEE(3), EEE—ME(5), CSE—ME(7) — ✗ (cycle)
**ST6:** ECE—EEE(4), ECE—CSE(2), CSE—CE(8), CE—ME(5) → Total = 19

**MST using Kruskal's (sort edges, pick smallest without cycle):**

| Edge | Weight | Action |
|---|---|---|
| ECE—CSE | 2 | ✅ Add |
| CSE—EEE | 3 | ✅ Add |
| ECE—EEE | 4 | ✗ Cycle (ECE-CSE-EEE) |
| CE—ME | 5 | ✅ Add |
| EEE—ME | 5 | ✗ Cycle |
| CSE—ME | 7 | ✗ Cycle |
| CSE—CE | 8 | ✅ Add (connects CE) |

**MST:** ECE—CSE(2), CSE—EEE(3), CE—ME(5), CSE—CE(8)
> **MST Total Weight = 2 + 3 + 5 + 8 = 18**

This is the MST because at each step we chose the minimum weight edge that doesn't form a cycle, guaranteeing the minimum total cost by Kruskal's greedy property.

---

## 8(c) Advantages of Header node in Header linked list. (04)

A **Header Linked List** is a linked list that has a special node at the beginning called the **header node**. This node does not store actual data but serves as a permanent first node.

**Advantages:**

1. **Simplified Insertion/Deletion:** The header node ensures the list is never truly empty (START always points to header). This eliminates special-case handling for inserting/deleting the first element.

2. **Storing Metadata:** The header node can store useful information like the total number of nodes, making operations like counting O(1) instead of O(n).

3. **Uniform Operations:** Without a header, inserting at the beginning requires updating the START pointer. With a header, all insertions happen after some node, making the algorithm uniform.

4. **Circular List Support:** In a grounded header list, the last node's LINK = NULL. In a circular header list, the last node's LINK points back to the header, making circular traversal easy.

**Example:**
```
Header → [count=3] → [10] → [20] → [30] → NULL
```
Without header: inserting before 10 requires changing START.
With header: insert after header — no pointer change needed for START.
