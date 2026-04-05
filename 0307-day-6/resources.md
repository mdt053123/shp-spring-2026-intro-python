# Day 6 — Resources

This folder covers **searching**, **sorting**, **min/max**, and **Big-O intuition**. The natural flow is: scan the list (linear search) → exploit sorted order (binary search, iterative then recursive) → simple selection problems (min/max) → classic sorts (selection, insertion, merge) → read complexity sketches in **`big_o.py`**.

---

## What Each File Does

### 1. `linear_search.py`
**Purpose:** Find a **target** in an unsorted list by checking each index.

- **`linear_search(nums, target)`:** Loop `i` from `0` to `len(nums)-1`; if `nums[i] == target`, return **`i`**; if none match, return **`-1`**.

**Key idea:** Works on **any** list; cost grows **linearly** with length in the worst case.

---

### 2. `binary_search.py`
**Purpose:** **Binary search** on a **sorted** list — iterative version.

- Maintains **`left`** and **`right`** indices; **`while left <= right`**, compute **`mid = (left + right) // 2`**.
- If **`nums[mid] == target`**, return **`mid`**; if target smaller, search left half (`right = mid - 1`); if larger, search right half (`left = mid + 1`).
- If the loop ends, return **`-1`**.

**Key idea:** Each step **halves** the search space — requires **sorted** input.

---

### 3. `binary_search_recursive.py`
**Purpose:** Same algorithm as binary search, **recursive** helper.

- **`binary_search(arr, target)`** calls **`helper(arr, target, left, right)`**.
- Base case: **`left > right`** → not found, **`-1`**.
- Otherwise compare **`arr[mid]`** to target and recurse on left or right half.

**Key idea:** Same logic as the loop version; recursion makes the “smaller subproblem” explicit.

---

### 4. `min_max.py`
**Purpose:** Single pass to find **minimum** and **maximum** in a list.

- **`minimum(arr)` / `maximum(arr)`:** If empty, return **`None`** (implicit); else track **`min_seen`** / **`max_seen`** and update in a loop from index `1` onward.

**Key idea:** One pass, **O(n)** time, **O(1)** extra space.

---

### 5. `selection_sort.py`
**Purpose:** **Selection sort** — repeatedly choose the smallest unsorted element and swap it forward.

- Outer loop **`i`** from `0` to **`n-2`**; inner loop finds **`min_idx`** from **`i+1`** to end; swap **`arr[i]`** with **`arr[min_idx]`**.
- Comment notes **~n²** comparisons in the worst case.

**Key idea:** Simple, in-place, but **quadratic** time typical for this pattern.

---

### 6. `insertion_sort.py`
**Purpose:** **Insertion sort** — build sorted prefix by shifting larger elements right.

- For each **`i`** from `1` to **`n-1`**, take **`curr = arr[i]`** and slide elements left while they are **`> curr`**, then insert **`curr`**.

**Key idea:** **O(n²)** worst case; can be **O(n)** on **already nearly sorted** data (good adaptive behavior).

---

### 7. `merge_sort.py`
**Purpose:** **Divide and conquer** sort with **O(n log n)** typical analysis.

- **`merge_sort(arr)`:** If length ≤ 1, return; else split at **`mid`**, recurse on **`arr[:mid]`** and **`arr[mid:]`**, then **`merge(left, right)`**.
- **`merge`:** Two-pointer merge of two sorted lists into **`result`**, then **`extend`** leftovers.

**Key idea:** Splitting and merging gives predictable **log-depth** recursion with **linear** merge work per level.

---

### 8. `big_o.py`
**Purpose:** **Informal complexity** examples (comments label intended Big-O).

- **`f1`:** Loop **`n`** times — labeled **O(n)**.
- **`f2`:** Loop **500** times regardless of **`n`** — labeled **O(1)** (constant *with respect to n*).
- **`f3`:** Nested loops both **`range(n)`** — labeled **O(n²)**.
- **`f4`:** Recursive with **`n // 2`** — file labels **O(log n)**; useful for *discussion* of halving recursion (the exact cost of this specific function is a good advanced question).
- **`f5`:** **`while i*i < n`** — labeled **O(√n)**.

**Key idea:** Big-O describes **growth** of work as input size grows; constants and low-order terms are dropped in rough analysis.

---

## Topics Covered (General)

1. **Linear search** — sequential scan, index or -1.
2. **Binary search** — sorted array, two pointers or recursion, halving.
3. **Min / max** — linear scans, empty list edge case.
4. **Selection sort** — pick minimum, swap, repeat.
5. **Insertion sort** — insert each element into sorted prefix.
6. **Merge sort** — split, sort halves, merge sorted lists.
7. **Algorithm analysis (intro)** — O(1), O(n), O(n²), O(log n), O(√n) as rough categories.

---

## Key Terms

| Term | Meaning |
|------|--------|
| **linear search** | Check each element in order until found or exhausted. |
| **binary search** | Search sorted data by repeatedly halving the index range. |
| **sorted** | Elements in non-decreasing (or non-increasing) order — required for binary search. |
| **index** | Integer position in a list. |
| **in-place sort** | Sorting that rearranges the original list (selection/insertion); merge sort here builds new slices/lists. |
| **stable sort** | Equal elements keep relative order (merge sort can be stable; not the focus of every file here). |
| **divide and conquer** | Split problem, solve recursively, combine (merge sort). |
| **Big-O** | Upper bound on growth rate of runtime vs input size (asymptotic). |
| **O(n)** | Linear time — proportional to n. |
| **O(n²)** | Quadratic — nested loops over n in the typical pattern. |
| **O(log n)** | Logarithmic — problem size shrinks by a constant factor each step (e.g. binary search). |

---

*Suggested order: linear_search.py → binary_search.py → binary_search_recursive.py → min_max.py → selection_sort.py → insertion_sort.py → merge_sort.py → big_o.py.*
