x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

x_bar = sum(x) / len(x)
y_bar = sum(y) / len(y)

n = sum((xi - x_bar) * (yi - y_bar) for xi, yi in zip(x, y))
d = sum((xi - x_bar) ** 2 for xi in x)

m = n / d                   # slope
b = y_bar - m * x_bar       # intercept

print(f"y = {round(m, 3)}x + {round(b, 3)}")