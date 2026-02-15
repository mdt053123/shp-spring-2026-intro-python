# Day 2 — Resources

This folder builds on Day 1 by adding **functions**, **control flow** (conditionals and loops), and **scope**. The order is: defining and using functions (including passables and local/global scope), then conditionals and logical operators, then `for` and `while` loops, then small applications (parity, grades, random numbers), and finally review plus exercises. Note that the creation of this guide was aided by Cursor AI.

---

## Content Videos/Resources -- Please Watch/Read!
*Note that not all of this will neatly map to everything we covered, so review all files, topics below. Some of these may actually cover more than necessary, but they should be helpful. What is really important is that you can understand (and recreate yourself) every file in this directory, key terms, constructs, etc. If these videos do not sufficiently cover each topic for you, feel free to email me at **mfd2141@columbia.edu** or look up any of these on YouTube, general internet.*
1. Conditionals, Booleans: https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=6
2. For/While Loops, Iteration: https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=8
3. Functions: https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=8
4. Random Module: https://www.youtube.com/watch?v=KzqSDvzOFNA

---

## What Each File Does

### 1. `functions.py`
**Purpose:** Define and call functions; return values vs side effects.

- **Defining a function:** `def f(x):` with a body and optional `return`.
- **Return:** `return x * x` sends a value back to the caller; code after `return` in the same block is not run.
- **Using functions:** e.g. `f(i)` in a loop; functions can be called many times with different arguments.
- **Docstrings:** `""" ... """` under the `def` line to describe what the function does (e.g. `is_even`).
- **Functions that “return nothing”:** A function without a `return` or with `return` and no value returns `None`. Example: `g()` only prints; `print(g())` shows "Hello" then "None".

**Key idea:** Functions encapsulate reusable logic; `return` gives a result; no return means `None`.

---

### 2. `passables.py`
**Purpose:** Functions can take other functions as arguments (first-class functions).

- `f(g, x)` takes a function `g` and a value `x`, and computes `g(x) * g(x)`.
- So `f(g, 4)` uses `g(4)` (e.g. `4/2` → `2`) and returns `2 * 2` → `4`.
- Shows that function names are values; you can pass them like any other argument.

**Key idea:** In Python, functions are values; you can pass them into other functions for flexibility (e.g. callbacks, mapping behavior).

---

### 3. `local_global.py`
**Purpose:** Variable scope — local vs global.

- **Local variable:** Inside `f(x)`, the parameter `x` and any assignment (e.g. `x += 2`) affect only that function’s local `x`. The global `x` stays unchanged after `f(x)`.
- **Global variable:** `global y` inside `g()` means the `y` that `g()` uses is the module-level `y`; `y += 2` there actually changes the global `y`.

**Key idea:** Assignments inside a function create or change local names unless you use `global`; parameters are always local.

---

### 4. `conditionals.py`
**Purpose:** Branching with `if` and `else`.

- **Syntax:** `if condition:` and optional `else:` with indented blocks.
- `if is_raining:` is equivalent to `if is_raining == True:` — you usually write the shorter form.
- Exactly one of the branches runs based on whether the condition is truthy.

**Key idea:** Conditionals let your program choose different behavior based on data (e.g. weather, user input).

---

### 5. `logical_operators.py`
**Purpose:** Combining conditions with `and`, `or`, and `not`.

- **and:** True only when both conditions are True.
- **or:** True when at least one condition is True.
- **not:** Flips True ↔ False.
- Used inside `if` to build compound conditions (e.g. “if A and B”, “if not C”).

**Key idea:** Logical operators let you express “both”, “either”, and “the opposite” in conditions.

---

### 6. `for.py`
**Purpose:** Iteration with `for` and `range`, and iterating over sequences.

- **`range(n)`:** 0 through `n-1` (e.g. `range(10)` → 0, 1, …, 9).
- **`range(start, stop)`:** from `start` up to but not including `stop` (e.g. `range(3, 10)` → 3,…,9).
- **`range(start, stop, step)`:** e.g. `range(0, 10, 2)` → 0, 2, 4, 6, 8.
- **Iterating a list:** `for num in nums:` — `num` takes each element in order.
- **`end=' '` in print:** prints a space instead of newline so output can stay on one line.

**Key idea:** `for` is for “do this once per item”; `range()` gives integer sequences; you can loop over lists directly.

---

### 7. `while.py`
**Purpose:** Loops that run while a condition is true; `break` and `continue`.

- **Basic while:** `while n < 20:` — body runs repeatedly until the condition is false; you must update variables (e.g. `n += 2`) so the loop can eventually stop.
- **Infinite loop:** `while True:` runs forever unless something exits (e.g. `break`).
- **break:** Exits the loop immediately (e.g. when `y == 21`).
- **continue:** Skips the rest of the current iteration and goes to the next (e.g. skip floor 13 in the elevator example).
- **Condition design:** `while x != 20` vs `while x < 20` — choose conditions that match your intent and avoid off-by-one or infinite loops.

**Key idea:** Use `while` when you don’t know how many iterations; always ensure the condition can become false or use `break`; `continue` skips to the next iteration.

---

### 8. `parity.py`
**Purpose:** Combine input, modulo, and conditionals for even/odd.

- Reads an integer with `int(input(...))`.
- Uses `n % 2 == 0` for even, `else` for odd, and prints the result.

**Key idea:** Modulo by 2 is the standard way to test even/odd; conditionals turn that into different messages.

---

### 9. `grades.py`
**Purpose:** Multi-way branching with `if` / `elif` / `else`.

- One variable `grade`; a chain of conditions: `>= 90` → A, `>= 80` → B, etc.
- **elif:** “else if” — only checked when previous conditions were false; ensures exactly one branch runs.

**Key idea:** For many exclusive categories, `if` / `elif` / `else` keeps the logic clear and efficient.

---

### 10. `random_nums.py`
**Purpose:** Generate random integers with the `random` module.

- **Import:** `import random` to use the module.
- **`random.randint(a, b)`:** returns a random integer N such that `a <= N <= b` (inclusive). Example: `random.randint(2, 5)` → 2, 3, 4, or 5.

**Key idea:** Use `import` to get extra functionality; `random.randint()` is the standard way to get random integers in a range.

---

### 11. `review_week_1.py`
**Purpose:** Short review of input, arithmetic, and modulo.

- Reads a number, adds 2, prints.
- Shows `21 % 30` (remainder) as a quick modulo reminder.

**Key idea:** Reinforces type conversion for input and the meaning of `%`.

---

### 12. `exercises.py`
**Purpose:** Practice with functions, conditionals, loops, and randomness.

- **divisible_by_3(n):** returns `True` if `n % 3 == 0`, else `False` — uses modulo and return.
- **sqrt(x):** Newton’s method in a `while` loop; handles `x < 0` (returns `None`) and `x == 0`; uses a tolerance (e.g. `1e-6`) to stop.
- **guess_the_number():** uses `random.randint(1, 100)`, then a `while not guessed` loop with `input()`, comparisons, and “too high” / “too low” / “You guessed it!” / “Out of bounds!”.

**Key idea:** Combines functions, conditionals, loops, modulo, and `random` into small but complete programs.

---

## Topics Covered (General)

1. **Functions** — defining with `def`, parameters, `return`, docstrings, and `None`.
2. **Functions as values** — passing functions as arguments (passables).
3. **Scope** — local variables and parameters vs `global`.
4. **Conditionals** — `if`, `else`, `elif` and branching.
5. **Logical operators** — `and`, `or`, `not` in conditions.
6. **for loops** — `range()` (one, two, or three arguments) and iterating over lists.
7. **while loops** — condition-based iteration, `break`, `continue`, and avoiding infinite loops.
8. **Applications** — parity (modulo + if/else), grade tiers (elif chain), random numbers.
9. **Modules** — `import random` and using `random.randint()`.
10. **Review and integration** — input, arithmetic, modulo, then full exercises (sqrt, guess-the-number).

---

## Key Terms

| Term | Meaning |
|------|--------|
| **function** | Reusable block of code defined with `def name(params):`. |
| **parameter** | Variable listed in the function definition; receives an argument. |
| **argument** | Value passed to a function when you call it. |
| **return** | Sends a value back to the caller and exits the function. |
| **docstring** | Triple-quoted string right after `def` describing the function. |
| **None** | Value returned by functions that don’t explicitly return something. |
| **first-class function** | Functions can be stored in variables and passed as arguments. |
| **scope** | Where a variable is visible; function body vs module level. |
| **local variable** | Variable that exists only inside one function. |
| **global variable** | Variable defined at module level; `global` allows a function to modify it. |
| **conditional** | `if` / `elif` / `else` — choice of which code runs. |
| **branch** | One of the blocks in an if/elif/else chain. |
| **and** | Logical “both must be true”. |
| **or** | Logical “at least one true”. |
| **not** | Logical “opposite” of a boolean. |
| **for loop** | Iteration over a sequence or `range()`. |
| **range()** | Produces a sequence of integers (start, stop, step). |
| **while loop** | Repeats body while condition is true. |
| **break** | Exits the current loop immediately. |
| **continue** | Skips to the next iteration of the loop. |
| **infinite loop** | Loop that never stops (e.g. `while True` without break). |
| **import** | Loads a module so you can use its names (e.g. `random`). |
| **module** | A file or package of reusable code (e.g. `random`). |
| **random.randint(a, b)** | Random integer from a to b inclusive. |

---

*Suggested order: functions → passables → local_global → conditionals → logical_operators → for → while → parity → grades → random_nums → review_week_1 → exercises.*
