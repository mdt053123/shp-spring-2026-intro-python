# Day 4 — Resources

This folder moves from scripts to **object-oriented programming**, **equality vs identity**, **recursion**, **string techniques**, **lambda expressions**, and **list comprehensions**. Files are ordered from quick type review → reference equality → classes → recursion → strings → lambdas → comprehensions → a capstone exercise class.

---

## What Each File Does

### 1. `types.py`
**Purpose:** Quick review of built-in types with `type()`.

- Assigns an `int`, `bool`, and `str`, then prints `type(x)` for each.

**Key idea:** `type()` tells you the class of a value at runtime.

---

### 2. `py_types.py`
**Purpose:** Same as `types.py` in this repo — prints `type()` for an `int`, `bool`, and `str`.

- **Note:** Content is **identical** to `types.py` here; keep one for demos or differentiate later (e.g. add type hints in one file).

---

### 3. `ref_equality.py`
**Purpose:** **`==` vs `is`** and a peek at **`__eq__`**.

- Two lists with the same contents: `l1 == l2` is **True** (value equality), but `l1 is l2` is **False** (different objects in memory).
- `l3 = l1` makes `l3` reference the **same** list as `l1`, so `l1 is l3` is **True**.
- Integers `x` and `y` both `3`: `x.__eq__(y)` shows the underlying equality method (same idea as `==` for ints).

**Key idea:** **`==`** compares *values* (usually); **`is`** compares *object identity* (same object in memory).

---

### 4. `student.py`
**Purpose:** A full **class** example with methods and **dunder** (special) methods.

- **`class Student`:** Blueprint for student objects.
- **`__init__(self, name, grade, missing_assignments)`:** Constructor — sets **instance attributes** `self.name`, `self.grade`, `self.missing_assignments`.
- **`get_info(self)`:** Returns a formatted multi-line string about the student.
- **`advance(self)`:** Mutates state — if few enough missing assignments, increments grade and clears missing count; otherwise prints a message.
- **`__str__(self)`:** Defines how `print(s1)` / `str(s1)` look — tuple-like string.
- **`__eq__(self, other)`:** Defines **`s1 == s2`** by comparing all three fields.
- **`__getitem__(self, key)`:** Allows **bracket access** like `s1["name"]` (dictionary-style keys for attributes).

Demo code creates instances, calls methods, compares equality, and shows `__getitem__`.

**Key idea:** Classes bundle **data** (attributes) and **behavior** (methods); dunder methods hook into Python operators and built-ins.

---

### 5. `car.py`
**Purpose:** A smaller class focused on **`__eq__`** and **`__str__`**.

- **`Car`** with `model`, `color`, `year`.
- Two cars with same model/year but different color are **not** equal; duplicate attributes match **`==`**.

**Key idea:** You control what “equal” means by implementing **`__eq__`**.

---

### 6. `recursion.py`
**Purpose:** Functions that **call themselves** with a **base case**.

- **`factorial(n)`:** Base case `n == 0` → `1`; else `n * factorial(n - 1)`.
- **`fib(n)`:** Fibonacci — base cases `0` and `1`; else sum of two recursive calls (classic but exponential work for large `n`).
- **`sumNums` / `sumNumsHelper`:** Sum a list by index — base case `i == len(nums)` → `0`; else current element plus recursive call with `i + 1`.

**Key idea:** Recursion needs a **base case** that stops the chain and a **recursive step** that moves toward it.

---

### 7. `strings.py`
**Purpose:** **Indexing**, **slicing**, **palindrome check**, **`split`**, **`join`**.

- Indexing: `s[1]`, `s[-1]` (last character).
- Slicing: `s[0:3]`, `s[0::2]` (step 2), `s[::-1]` (reverse).
- Palindrome: `word == word[::-1]`.
- **`split('.')`** breaks a string into a list; **`'.'.join(u)`** rebuilds a string from a list.
- **`''.join(chrs)`** concatenates a list of single-character strings into one word.

**Key idea:** Strings are **sequences**; slicing and `join`/`split` are everyday tools.

---

### 8. `lambda.py`
**Purpose:** **Anonymous one-line functions**.

- **`def f(x): return x * x`** vs **`g = lambda x: x * x`** — same behavior for simple cases.

**Key idea:** `lambda` is shorthand for a tiny function; often used with `sorted`, `map`, `filter` (not shown here).

---

### 9. `list_comprehension.py`
**Purpose:** Build lists (and nested lists) in one expression.

- Loop version vs **`[i for i in range(1, 101)]`**.
- **Nested comprehension:** `mat = [[i for i in range(10)] for i in range(10)]` builds a 10×10 matrix (each row is 0..9).

**Key idea:** List comprehensions are concise and often read as “make a list of *expr* for each *item* in *iterable*”.

---

### 10. `exercises.py` (`StringAnalyzer`)
**Purpose:** Practice class design with string algorithms.

- **`is_palindrome`:** Compare string to its reverse.
- **`contains_only_vowels`:** Every character (uppercased) must be in `'AEIOUY'`.
- **`contains(sub)`:** Manual substring search — find starting character, then slice-compare `self.s[i : i + len(sub)]`.

**Key idea:** Encapsulating string logic in a class keeps tests and reuse clean.

---

## Topics Covered (General)

1. **Types** — `type()`, built-in `int`, `bool`, `str`.
2. **Equality vs identity** — `==`, `is`, `__eq__`.
3. **Classes and OOP** — `class`, `__init__`, `self`, instance attributes, methods.
4. **Special methods** — `__str__`, `__eq__`, `__getitem__`.
5. **Recursion** — base case, recursive call, factorial, Fibonacci, list summation.
6. **Strings** — indexing, slicing, reverse slice, `split`, `join`.
7. **Lambda** — anonymous functions.
8. **List comprehensions** — single and nested.
9. **Mini project** — `StringAnalyzer` with palindrome, vowel-only, and substring checks.

---

## Key Terms

| Term | Meaning |
|------|--------|
| **class** | Blueprint for objects; defines attributes and methods. |
| **instance / object** | A concrete value created from a class (e.g. `Student(...)`). |
| **`__init__`** | Initializer; runs when you construct an instance. |
| **`self`** | Reference to the current instance inside methods. |
| **attribute** | Data stored on an object (e.g. `self.name`). |
| **method** | Function defined on a class, usually with `self`. |
| **dunder method** | Special method with double underscores (e.g. `__str__`, `__eq__`). |
| **`==`** | Value equality (uses `__eq__` when defined). |
| **`is`** | True if two names refer to the same object. |
| **recursion** | Function calling itself with a base case. |
| **base case** | Condition where recursion stops. |
| **slice** | `s[start:stop:step]` — substring by index ranges. |
| **`split` / `join`** | String ↔ list conversions. |
| **lambda** | `lambda args: expression` — small anonymous function. |
| **list comprehension** | `[expr for var in iterable]` (optional `if` filter). |

---

*Suggested order: types.py → py_types.py (or skip if redundant) → ref_equality.py → student.py → car.py → recursion.py → strings.py → lambda.py → list_comprehension.py → exercises.py.*
