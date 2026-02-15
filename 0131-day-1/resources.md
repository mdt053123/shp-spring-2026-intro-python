# Day 1 — Resources

This folder introduces the basics of Python: running code, data types, math, user input, and simple programs. Files are ordered from foundational (print, variables) to building blocks (operations, casting, f-strings, input) to small applications (conversion, bio, mad libs), then errors and one optional advanced topic. Note that the creation of this guide was aided by Cursor AI.

---

## Content Videos/Resources -- Please Watch/Read!
*Note that not all of this will neatly map to everything we covered, so review all files, topics below. Some of these may actually cover more than necessary, but they should be helpful. What is really important is that you can understand (and recreate yourself) every file in this directory, key terms, constructs, etc. If these videos do not sufficiently cover each topic for you, feel free to email me at **mfd2141@columbia.edu** or look up any of these on YouTube, general internet.*
1. Strings, Output: https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2
2. Ints, Floats, Operators: https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=3
3. User Input: https://www.youtube.com/watch?v=we54H-T1AL0
4. General Variables, Types: https://www.youtube.com/watch?v=LKFrQXaoSMQ
5. Thonny (IDE) Installation: https://thonny.org/

---

## What Each File Does

### 1. `print_output.py`
**Purpose:** How to display text and run your first Python.

- Uses `print()` to send text to the console.
- Shows **escape sequences**: `\n` (newline) and `\t` (tab).
- Demonstrates **string delimiters**: single quotes `'...'`, double quotes `"..."`, and triple quotes `'''...'''` for multi-line strings.
- Covers quoting: e.g. `'Quote: "quote text"'` to put double quotes inside a string.

**Key idea:** `print()` is your main way to see output; escape sequences control formatting.

---

### 2. `variables.py`
**Purpose:** Storing values and understanding basic types.

- **Variables:** names that hold values (e.g. `x = 3`).
- **Types shown:**
  - `int` — whole numbers (e.g. `3`).
  - `float` — decimals (e.g. `3.2`).
  - `bool` — `True` / `False` (used in conditions and math).
  - `str` — text in quotes (e.g. `"abc"`).
  - `list` — ordered collection (e.g. `[3, 4, 7]`).
- Uses `type()` to inspect the type of a value.

**Key idea:** Every value has a type; variables are just names for those values.

---

### 3. `operations.py`
**Purpose:** Arithmetic and division behavior in Python.

- **Operators:** `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- **Division:**
  - `/` — always gives a `float` (e.g. `3/5` → `0.6`, `4/2` → `2.0`).
  - `//` — integer (floor) division (e.g. `3//5` → `0`, `4//2` → `2`).
  - `-3//2` shows floor division with negatives.
- **Modulo `%`:** remainder (e.g. `7 % 4` → `3`, `3 % 8` → `3` when dividend is smaller than divisor).

**Key idea:** `/` vs `//` and what `%` means (remainder) are used everywhere later (loops, parity, indexing).

---

### 4. `casting.py`
**Purpose:** Converting between types explicitly.

- **Casting functions:** `int()`, `float()`, `str()`.
- Examples: `float(3)` → `3.0`, `int("7")` → `7`, `str(3.85)` → `"3.85"`.
- Brief mention of `4j` (complex numbers); not central to Day 1.

**Key idea:** Input and string concatenation often require casting (e.g. `int(input(...))`, `str(x)` in old-style strings).

---

### 5. `fstring.py`
**Purpose:** Building strings that include variables (f-strings).

- **Ways to mix text and values:**
  - Concatenation: `"My number is " + str(x)`.
  - Comma in `print`: `print("My number is", x)`.
  - **F-string:** `f"My number is {x}"` — preferred for readability.
- Uses `input()` and embeds the result in an f-string.
- **`end` in print:** `print("text", end='')` avoids a newline so the next `print` continues on the same line.
- Literal backslash: `"\\n"` prints `\n` as characters.

**Key idea:** F-strings (`f"…{variable}…"`) are the cleanest way to format output with variables.

---

### 6. `user_input.py`
**Purpose:** Reading input from the user.

- `input("prompt: ")` returns a **string**.
- To do math, cast: `x = int(input("Enter a number: "))` then use `x` (e.g. `x*3`).

**Key idea:** Always treat `input()` as text; convert with `int()` or `float()` when you need numbers.

---

### 7. `ftoc.py`
**Purpose:** A short “formula” program: Fahrenheit → Celsius.

- Stores a temperature in a variable, applies `c = (f - 32)*(5/9)`, and prints the result.
- Reinforces variables, arithmetic, and print — no input.

**Key idea:** Programs often compute one or more formulas and display the result.

---

### 8. `bio.py`
**Purpose:** Combine input, variables, and f-strings in one program.

- Prompts for name, birth year, hobby, food.
- Uses f-strings to print a summary and computes approximate age (e.g. `2026 - birth_year`).

**Key idea:** Real programs combine input, variables, math, and formatted output.

---

### 9. `mad_libs.py`
**Purpose:** Template for a Mad Libs–style exercise.

- Uses `...` (Ellipsis) as placeholders for variables (name, adjective, animal).
- Builds a multi-line story with an f-string (`f""" ... """`).
- You fill in the variables and the story string.

**Key idea:** F-strings and variables are perfect for fill-in-the-blank text.

---

### 10. `errors.py`
**Purpose:** Recognize common error types (code is commented out).

- **NameError:** using a variable that doesn’t exist (e.g. `print(x)` when `x` isn’t defined).
- **SyntaxError:** invalid Python (e.g. mismatched quote `print(3")`).
- **TypeError:** wrong type for an operation (e.g. `"abc" / 3`).
- **Logic error:** code runs but does the wrong thing (e.g. printing the string `"x"` instead of the variable `x`).

**Key idea:** Learning to read error messages and classify these four helps debugging a lot.

---

### 11. `modulo.py` — **Optional / Advanced (Skip for Now)**

**What it does:** This file is about the **modulo operator** and **recursion**, which are **optional and too difficult for this stage**. Feel free to skip it for now and **check back in a future session** when you’re comfortable with functions and conditionals.

- **Custom modulo:** Defines `mod(a, b)` as `a - b*(a//b)` — the remainder when dividing `a` by `b` (aligned with Python’s `%` for positive numbers).
- **GCD (Euclidean algorithm):** Defines `gcd(a, b)` using **recursion**: if `b == 0` then answer is `a`, otherwise `gcd(b, a % b)`. This relies on:
  - **Recursion** (a function calling itself).
  - **Conditionals** (`if`).
  - **Modulo** in the recursive step.

**Why it’s marked optional:** It uses recursion and a mathematical idea (GCD) that we don’t assume on Day 1. Once you’ve done **functions**, **conditionals**, and **loops**, this file will make more sense. **Check back later** when you want to go deeper.

---

## Topics Covered (General)

1. **Running Python** — writing scripts and using `print()` to see output.
2. **Values and types** — `int`, `float`, `bool`, `str`, `list`; checking with `type()`.
3. **Variables** — assigning and reusing values.
4. **Arithmetic** — `+`, `-`, `*`, `/`, `//`, `%`, `**`; difference between `/` and `//`.
5. **Type conversion** — `int()`, `float()`, `str()` and when to use them.
6. **Strings** — quotes, escape sequences (`\n`, `\t`), and f-strings.
7. **User input** — `input()`, that it returns a string, and casting to numbers.
8. **Simple programs** — formulas (ftoc), biographical summary (bio), Mad Libs–style story.
9. **Errors** — NameError, SyntaxError, TypeError, and logic errors.

---

## Key Terms

| Term | Meaning |
|------|--------|
| **print** | Built-in that writes to the console. |
| **variable** | A name that refers to a value. |
| **type** | The kind of data: int, float, bool, str, list, etc. |
| **int** | Integer; whole number. |
| **float** | Floating-point number; decimal. |
| **bool** | Boolean; `True` or `False`. |
| **str** | String; text in quotes. |
| **list** | Ordered, mutable sequence of values. |
| **escape sequence** | `\n` (newline), `\t` (tab), `\\` (backslash). |
| **f-string** | `f"…{expression}…"` — string with embedded values. |
| **casting** | Converting types with `int()`, `float()`, `str()`. |
| **input()** | Reads one line from the user as a string. |
| **operator** | Symbol for an operation: `+`, `-`, `*`, `/`, `//`, `%`, `**`. |
| **division** | `/` (float), `//` (integer/floor). |
| **modulo** | `%`; remainder after division. |
| **NameError** | Using an undefined variable. |
| **SyntaxError** | Invalid Python grammar. |
| **TypeError** | Operation applied to wrong type. |
| **logic error** | Program runs but produces wrong result. |

---

*Suggested order to work through this folder: print_output → variables → operations → casting → fstring → user_input → ftoc → bio → mad_libs → errors. Leave modulo.py for later.*
