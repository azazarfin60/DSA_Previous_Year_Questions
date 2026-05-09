[⬅️ Previous](./9.2_Huffman_Coding_with_Probabilities_UGC_NET_Previous_Year_Question.md) | [🏠 Home](./README.md) | [Next ➡️](./Introduction_to_Data_Structure_and_Algorithm.md)

---

# Binary Search Introduction | Theory + Code | Order Agnostic Binary Search

📺 [Watch on YouTube](https://www.youtube.com/watch?v=WPnN41Er_sU)

---

## 📌 Executive Summary

This lecture covers **Order Agnostic Binary Search** — a variant that works regardless of whether the array is sorted in **ascending or descending** order. It detects the sort order first, then adjusts the search direction.

---

## 📐 Order Agnostic Algorithm

```c
int orderAgnosticBS(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    int isAsc = (arr[low] < arr[high]);   // Detect order

    while (low <= high) {
        int mid = low + (high - low) / 2;  // Avoid overflow

        if (arr[mid] == key) return mid;

        if (isAsc) {  // Ascending
            if (key < arr[mid])
                high = mid - 1;
            else
                low = mid + 1;
        } else {      // Descending
            if (key > arr[mid])
                high = mid - 1;
            else
                low = mid + 1;
        }
    }
    return -1;
}
```

---

## ⚠️ Overflow Prevention

```c
// BAD:  mid = (low + high) / 2        → may overflow for large values
// GOOD: mid = low + (high - low) / 2   → safe
```

---

## 📐 Example: Descending Array

```
Array: [91, 72, 56, 38, 23, 16, 12, 8, 5, 2]   Key = 23

isAsc = (91 < 2) = false → Descending!

Pass 1: mid=4, arr[4]=23 = 23 → Found at index 4! ✅
```

---

## 💡 Key Takeaways

- Check `arr[low] < arr[high]` to detect ascending/descending
- Reverse the comparison logic for descending arrays
- Use `low + (high - low) / 2` to avoid integer overflow
- Same O(log n) complexity

<br>

---
[⬅️ Previous](./9.2_Huffman_Coding_with_Probabilities_UGC_NET_Previous_Year_Question.md) | [🏠 Home](./README.md) | [Next ➡️](./Introduction_to_Data_Structure_and_Algorithm.md)
