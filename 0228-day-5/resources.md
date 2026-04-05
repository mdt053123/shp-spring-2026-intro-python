# Day 5 — Resources

This folder introduces **machine-learning-style ideas from scratch** (nearest neighbors, linear regression) and a **scikit-learn** teaser. You use **distance**, **labeled data** (points with classes), and **fitting / predicting** with a library. Files progress from 1-nearest-neighbor with input, to closed-form linear regression, to k-NN with majority vote, to sklearn, then exercises that **`import knn`**.

---

## What Each File Does

### 1. `nearest_neighbor.py`
**Purpose:** **1-nearest-neighbor classification** on 2D points with string labels (colors).

- **`data`:** List of `((x, y), 'label')` tuples — your training set.
- User enters **`x`** and **`y`**; **`p = (x, y)`** is the query point.
- **`distance(p1, p2)`:** Euclidean distance in 2D (same formula as earlier geometry examples).
- **`classify(p)`:**  
  - If **`p`** exactly equals a stored point, return that point’s label.  
  - Otherwise scan all points, track **smallest distance** and its label (`float("inf")` as initial “very large” distance).  
  - **Side effect:** **`data.append((p, nearest_color))`** — adds the classified point to the dataset (so the model “learns” the new point in memory).

**Key idea:** 1-NN = “guess the label of the closest training point.”

---

### 2. `linear_regression.py`
**Purpose:** **Least-squares line** through paired data (no sklearn).

- **`x`**, **`y`** are parallel lists of numbers (same length).
- **`x_bar`**, **`y_bar`:** means of `x` and `y`.
- **Slope `m`:** `sum((xi - x_bar)(yi - y_bar)) / sum((xi - x_bar)^2)` — covariance-style numerator, variance of x denominator.
- **Intercept `b`:** `y_bar - m * x_bar`.
- Prints **`y = mx + b`** (rounded).

**Key idea:** Linear regression finds the best-fit line; this is the standard closed-form for simple linear regression.

---

### 3. `knn.py`
**Purpose:** **k-nearest neighbors** with **majority vote** (k odd, k ≤ len(data) assumed).

- Same **`distance`** helper as above.
- **`classify(p, k, data)`:** Exact match shortcut; else build **`dists`** list of `(distance, index, color)`, **`sorted(dists)`**, take first **`k`**, count votes per color, return label with highest count (ties broken by iteration order in the code).
- **Side effect:** **`data.append((p, majority_color))`** like the 1-NN script.
- Input lines are **commented out** — you can uncomment to run interactively or call **`classify`** from another module.

**Key idea:** k-NN uses the **k** closest points and picks the **most common** label.

---

### 4. `skl.py`
**Purpose:** Same flavor of problem using **libraries**: **pandas**, **scikit-learn**.

- Builds a **`pd.DataFrame`** with columns `x`, `y`, and `color`.
- **`KNeighborsClassifier(n_neighbors=1)`** — 1-NN.
- **`fit`** on feature columns `[['x','y']]` and target **`color`**.
- **`predict([[3, 2]])`** for a single query point.

**Note:** **`LinearRegression`** is imported but not used in this snippet — you could extend the file to compare models.

**Key idea:** sklearn separates **fit** (learn from data) and **predict** (apply to new points).

---

### 5. `exercises.py`
**Purpose:** Use **`knn.classify`** as a **library** from your own project.

- **`import knn`** — imports **`knn.py`** from the same folder (when run as a script from that directory or with proper path).
- **`points`:** Synthetic 2D data for three classes **A**, **B**, **C** in different regions of the plane.
- **`print(knn.classify((0.1, 0.3), 3, points))`** — classify with **k = 3** (expect class **A** near the origin).

**Key idea:** Your **`knn.py`** is reusable; **`exercises.py`** is a small test harness.

---

## Topics Covered (General)

1. **Supervised learning intuition** — labeled examples `(features, label)`.
2. **Euclidean distance** in 2D for feature vectors.
3. **1-NN** — nearest single neighbor decides the label.
4. **k-NN** — majority vote over k neighbors; sorting by distance.
5. **Linear regression** — mean, slope, intercept, line equation.
6. **sklearn API** — `fit` / `predict`; **`KNeighborsClassifier`**.
7. **pandas DataFrame** — tabular data for features and labels.
8. **Modules** — `import knn` to reuse your own code.

---

## Key Terms

| Term | Meaning |
|------|--------|
| **feature** | Input used to predict (here, `x` and `y` coordinates). |
| **label / class** | What you predict (e.g. `'red'`, `'A'`). |
| **training data** | Labeled examples the algorithm uses. |
| **Euclidean distance** | Straight-line distance between two points. |
| **1-NN** | Nearest neighbor classification (k = 1). |
| **k-NN** | k nearest neighbors; often majority vote. |
| **majority vote** | Most common label among neighbors. |
| **linear regression** | Fitting a line `y = mx + b` to minimize squared error (here, closed form). |
| **slope / intercept** | `m` and `b` in `y = mx + b`. |
| **fit** | Train a model on data (sklearn). |
| **predict** | Apply a trained model to new inputs (sklearn). |
| **`KNeighborsClassifier`** | sklearn classifier implementing k-NN. |
| **`pandas.DataFrame`** | 2D labeled table of data. |

---

## Running Notes

- **`nearest_neighbor.py`** needs **`input()`** for x and y.
- **`exercises.py`** must be run so Python can find **`knn.py`** (e.g. from **`0228-day-5/`**: `python exercises.py`).
- **`skl.py`** requires **`pip install scikit-learn pandas`** (and dependencies).

---

*Suggested order: nearest_neighbor.py → linear_regression.py → knn.py → skl.py → exercises.py.*
