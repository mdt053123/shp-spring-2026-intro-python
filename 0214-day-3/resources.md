# Day 3 — Resources

This folder focuses on **data structures**: **lists** (already glimpsed in Day 1), **tuples**, **dictionaries**, and **sets**. The order is: lists (indexing, iteration, mutating), then tuples (immutable sequences), then dicts (key–value mapping), then sets (unique, unordered), and finally exercises that use all of them. Note that the creation of this guide was aided by Cursor AI.

---

## Content Videos/Resources -- Please Watch/Read!
*Note that not all of this will neatly map to everything we covered, so review all files, topics below. Some of these may actually cover more than necessary, but they should be helpful. What is really important is that you can understand (and recreate yourself) every file in this directory, key terms, constructs, etc. If these videos do not sufficiently cover each topic for you, feel free to email me at **mfd2141@columbia.edu** or look up any of these on YouTube, general internet.*
1. Lists, Tuples, Sets: https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=4
2. Dictionaries: https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=5

---

## What Each File Does

### 1. `lists.py`
**Purpose:** Create lists, index them, iterate, and mutate them with common methods.

- **Lists:** Ordered, mutable sequences; can mix types (e.g. `["Michael", True, 4j, 3]`).
- **Indexing:** `nums[i]` — zero-based; first element is `nums[0]`.
- **Iteration:**  
  - `for num in nums:` — loop over elements.  
  - `while i < len(nums):` and `for i in range(len(nums)):` — loop over indices when you need the index.
- **`len(nums)`:** number of elements.
- **Mutating methods:**  
  - **`append(x)`** — add `x` to the end.  
  - **`pop(i)`** — remove and return the element at index `i` (default last).  
  - **`insert(i, x)`** — insert `x` at index `i`, shifting later elements.  
  - **`sort()`** — sort in place (for comparable elements).

**Key idea:** Lists are the workhorse “ordered collection”; indexing is 0-based; methods like append, pop, insert, and sort change the list in place.

---

### 2. `tuples.py`
**Purpose:** Immutable sequences; using tuples for coordinates and multiple return values.

- **Syntax:** `(2, 3)` — comma-separated values in parentheses.
- **Indexing:** Same as lists — `p1[0]`, `p1[1]` (e.g. x, y for a point).
- **Immutability:** You cannot do `p1[0] = 3`; tuples don’t support assignment to indices.
- **Use case:** Representing fixed-size data (e.g. 2D/3D points); safe to use as dict keys or in sets later.
- **Distance example:** `dist(p1, p2)` uses the Euclidean formula with tuple indexing.
- **Single-element tuple:** `(3)` is just the integer `3`; `(3,)` is a one-element tuple — the comma makes it a tuple.

**Key idea:** Tuples are like lists but immutable; great for coordinates, pairs, or any fixed structure you don’t want changed.

---

### 3. `dicts.py`
**Purpose:** Dictionaries — key–value mapping; access, iterate, and build counts.

- **Syntax:** `{'Alice': 76, 'Michael': 91, 'Bob': 52}` — keys and values separated by `:`.
- **Access:**  
  - **`grades['Alice']`** — raises KeyError if key is missing.  
  - **`grades.get('Alice')`** — returns value or `None` (or a default) if key is missing.
- **Views:**  
  - **`grades.keys()`** — keys.  
  - **`grades.values()`** — values.  
  - **`grades.items()`** — (key, value) pairs.  
  Wrapping in `list(...)` gives a list when you need one.
- **Iteration:** `for key, value in student_rosters.items():` — unpack each pair.
- **Nested structure:** Values can be lists (e.g. class rosters as lists of names).
- **Building a dict:** Start with `counts = {}`, then `counts[1] = 3` and `counts[1] += 1` to count occurrences.

**Key idea:** Dicts map keys to values; use `.get()` for safe access; `.items()` is ideal for looping; dicts are perfect for counting and grouping.

---

### 4. `sets.py`
**Purpose:** Unordered collections of unique elements; set operations.

- **Syntax:** `set()` for empty set; `{1, 2, 2, 3, 4, 5, 5, 5}` — duplicates are removed, so you get unique elements.
- **Unordered:** No indexing by position; membership and set operations are what matter.
- **Operations (examples with sets A and B):**  
  - **`A.intersection(B)`** — elements in both.  
  - **`A.union(B)`** — elements in either.  
  - **`A.difference(B)`** — elements in A but not in B.  
  - **`A.issubset(B)`** — True if every element of A is in B.

**Key idea:** Sets store unique items and support mathematical set operations; use them when order doesn’t matter and you care about membership or relations between groups.

---

### 5. `exercises.py`
**Purpose:** Apply lists, tuples, and dicts in small functions.

- **first_occurrence(nums, num):** Linear search — loop with `range(len(nums))`, return first index where `nums[i] == num`, or `-1` if not found.
- **print_reverse(nums):** Loop from `len(nums)-1` down to `0` (using `range(len(nums)-1, -1, -1)`) and print each element — reinforces indexing and reverse range.
- **dist_3d(p1, p2):** Same idea as 2D distance but with three components; takes tuples `(x, y, z)` and uses indexing `p1[0]`, `p1[1]`, `p1[2]`.
- **value_counts(nums):** Count how many times each number appears — use a dict: for each `num`, do `counts[num] = counts.get(num, 0) + 1` or check `if num not in counts` then set/update. Prints the counts (e.g. `1: 2, 2: 1, ...`).

**Key idea:** Lists and indexing for search and reverse order; tuples for multi-part data (e.g. 3D points); dicts for counting and grouping.

---

## Topics Covered (General)

1. **Lists** — creation, indexing (0-based), length, iteration (by element and by index), and mutating methods (append, pop, insert, sort).
2. **Tuples** — creation, indexing, immutability, and use for coordinates or fixed-size data.
3. **Dictionaries** — key–value pairs, access vs `.get()`, keys/values/items, iterating, and building structures (e.g. counts, nested lists).
4. **Sets** — uniqueness, no duplicates, no order; intersection, union, difference, subset.
5. **Combining structures** — lists of tuples, dicts mapping to lists, using dicts for frequency counts; indexing and loops across these types.

---

## Key Terms

| Term | Meaning |
|------|--------|
| **list** | Ordered, mutable sequence; `[a, b, c]`. |
| **index** | Integer position (0-based); `lst[i]` is the element at index `i`. |
| **len()** | Returns the length (number of elements) of a sequence or dict. |
| **append(x)** | Add `x` to the end of a list (in place). |
| **pop(i)** | Remove and return element at index `i` (default last). |
| **insert(i, x)** | Insert `x` at index `i`, shifting later elements. |
| **sort()** | Sort list in place (for comparable elements). |
| **tuple** | Immutable sequence; `(a, b, c)`; often for coordinates or fixed data. |
| **immutable** | Cannot be changed after creation (e.g. tuple, str). |
| **mutable** | Can be changed in place (e.g. list, dict). |
| **dictionary (dict)** | Mapping from keys to values; `{key: value}`. |
| **key** | Index-like label in a dict; must be hashable (e.g. str, int, tuple). |
| **value** | Data stored under a key in a dict. |
| **KeyError** | Error when accessing a missing key with `d[key]`. |
| **.get(key, default)** | Safe dict access; returns value or default if key missing. |
| **.keys()** | View of dict keys. |
| **.values()** | View of dict values. |
| **.items()** | View of (key, value) pairs. |
| **set** | Unordered collection of unique elements; `{a, b, c}`. |
| **intersection** | Elements in both sets. |
| **union** | Elements in either set. |
| **difference** | Elements in first set but not second. |
| **subset** | Every element of one set is in another; `issubset()`. |
| **hashable** | Type that can be used as dict key or set element (e.g. int, str, tuple). |

---

*Suggested order: lists → tuples → dicts → sets → exercises.*
