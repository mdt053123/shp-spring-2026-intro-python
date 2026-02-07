x = 3

def f(x):
    x += 2
    
f(x)

print(x)

y = 5

def g():
    global y
    y += 2
    
g()

print(y)