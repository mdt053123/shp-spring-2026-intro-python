# Day 7 — Resources

This folder ties together **numerical arrays (NumPy)**, **matrices as nested lists**, **matrix multiplication**, a **lightning review** script, and a minimal **Flask web app** with HTML templates. Order: NumPy basics → list-of-lists matrices → `matmul` → review → web stack.

---

## What Each File Does

### 1. `arrays.py`
**Purpose:** **NumPy** `ndarray` basics.

- **`import numpy as np`**
- **`np.array([1, 2, 3, 4, 5])`** — 1D array; **`type(arr)`** shows it’s not a plain Python list.
- Indexing: **`arr[1]`**.
- **Memory:** **`arr.itemsize * arr.size`** (bytes per element × number of elements) — rough footprint.
- **`arr.prod()`** — product of all elements.

**Key idea:** NumPy arrays are **homogeneous** and **efficient** for numeric work vs lists of Python objects.

---

### 2. `matrix.py`
**Purpose:** Matrices as **lists of rows** (nested lists).

- **`M = [[1, 2], [2, 1]]`** — row 0, row 1; access **`M[r][c]`**.
- Prints rows and double loops: by index **`M[r][c]`** and by **`for row in M`** then **`for num in row`**.

**Key idea:** **`M[i]`** is the **i-th row**; **`M[i][j]`** is row **i**, column **j**.

---

### 3. `matmul.py`
**Purpose:** **Matrix multiplication** **`M1 @ M2`** concept implemented manually.

- **`matmul(M1, M2)`:** Returns **`None`** if empty or if **inner dimensions** don’t match: **`len(M1[0]) != len(M2)`**.
- Builds **`result`** as zeros with shape **`len(M1) × len(M2[0])`**.
- Triple loop: **`result[i][j] += M1[i][k] * M2[k][j]`** — standard definition.

Test matrices **`M1`**, **`M2`** are 2×2; product printed.

**Key idea:** Entry **`(i, j)`** is dot product of row **`i`** of **`M1`** with column **`j`** of **`M2`**.

---

### 4. `review.py`
**Purpose:** Commented **cheat-sheet style** recap of the course.

- **Functions** — `my_func` with ints and with **strings** (same `+` operator, different meaning: concatenation).
- **Conditionals** — `if` / `elif` / `else`.
- **`for`** loop with **`range(1, 10)`**.
- **Data structures** — list, tuple, set (dedup), dict; loop printing **`d[i % 3]`** cycles keys **`0, 1, 2`**.

**Key idea:** One file skimming syntax from earlier weeks; uncomment sections to practice.

---

### 5. `web-app/app.py`
**Purpose:** Minimal **Flask** application.

- **`Flask(__name__)`** — app instance.
- **`@app.route('/')`** → **`index.html`** via **`render_template('index.html')`**.
- **`@app.route('/aboutme')`** → **`aboutme.html`**.
- **`app.run(debug=True)`** — development server with reload/debug (don’t use **`debug=True`** in production).

**Note:** **`request`** is imported but unused in this file — harmless; you could drop it or use it for forms later.

**Key idea:** Routes map **URLs** to **Python functions** that return **HTML** (via templates).

---

### 6. `web-app/templates/index.html`
**Purpose:** Simple **home** page.

- Valid HTML5 skeleton; **`<h1>Hello World</h1>`**.

**Key idea:** Flask looks in **`templates/`** by default for **`render_template`**.

---

### 7. `web-app/templates/aboutme.html`
**Purpose:** Richer **About** page with **embedded CSS**.

- **Nav** links to **`/`** and **`/aboutme`**.
- **Layout:** profile block, cards (About, Skills, Interests, Fun Facts), **footer**.
- Styling: gradient background, flex/grid, “pill” skill tags — template text like **“Your Name Here”** for students to customize.

**Key idea:** Static HTML/CSS can be served through Flask; same app can later add **Jinja** variables if you extend it.

---

## Topics Covered (General)

1. **NumPy** — `array`, dtype, indexing, `prod()`, memory size idea.
2. **Matrices as nested lists** — row/column indexing, nested iteration.
3. **Matrix multiplication** — dimension rules, triple-loop implementation.
4. **Review** — functions, branching, loops, list/tuple/set/dict.
5. **Web apps** — Flask routes, templates, local dev server.
6. **HTML/CSS** — structure, navigation, styling (About page).

---

## Key Terms

| Term | Meaning |
|------|--------|
| **NumPy** | Library for fast numeric arrays and linear algebra. |
| **`ndarray`** | NumPy’s n-dimensional array type. |
| **`itemsize` / `size`** | Bytes per element; number of elements (memory discussion). |
| **matrix (nested list)** | List of rows; each row is a list of numbers. |
| **row / column** | **`M[i]`** row i; column j is **`M[0][j], M[1][j], ...`**. |
| **matrix multiplication** | `(m×k)·(k×n) → (m×n)`; inner dimensions must match. |
| **Flask** | Lightweight Python web framework. |
| **route** | URL path tied to a view function (`@app.route`). |
| **`render_template`** | Renders an HTML file from **`templates/`**. |
| **template** | HTML (optionally with Jinja) returned to the browser. |
| **debug mode** | `debug=True` — easier errors and auto-reload in development only. |

---

## Running the Web App

From the **`web-app`** directory (or with correct working directory so templates resolve):

```bash
pip install flask
python app.py
```

Then open the URL Flask prints (usually **`http://127.0.0.1:5000/`**). Visit **`/aboutme`** for the second page.

---

*Suggested order: arrays.py → matrix.py → matmul.py → review.py → read/run web-app/app.py with templates.*
