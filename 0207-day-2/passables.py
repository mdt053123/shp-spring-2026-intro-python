def f(g, x):
    return g(x) * g(x)

def g(x):
    return x / 2

print(f(g, 4))
print(f(g, 3))