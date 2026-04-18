# List Comprehension

squares = [x*x for x in range(10)]
print(squares)

evens = [x for x in range(20) if x % 2 == 0]
print(evens)

print()
print()
print()

# Ternary Operator

score = 59
status = "pass" if score >= 60 else "fail"
print(status)

print()
print()
print()

# Multiple Assignement and Unpacking

x, y = 2, 3
print(x, y)

x, y = y, x # swap
print(x, y)

a, b, c = [1, 2, 3]
print(a, b, c)

print()
head, *body, tail = [1, 2, 3, 4, 5]
print(head)
print(body)
print(tail)

print()
print()
print()

# Enumerate

names = ["Alice", "Bob", "Karen"]

for i, name in enumerate(names):
    print(i, name)
    
print()
print()
print()

# Zip

names = ["Alice", "Bob", "Karen"]
ages = [25, 30, 20]

for name, age in zip(names, ages):
    print(f"{name} is {age}")
    
print()
print()
print()

# F-Strings

name = "Mike"
print(f"Hello, {name.upper()}!")

print()
print()
print()

# ANY/ALL

nums = [1, 2, 3, 0]
print(any(nums))
print(all(nums))

print()
print()
print()

# LAMBDA

def f(x):
    return x * x

g = lambda x : x * x

print(f(3), g(3))

print()
print()
print()

# MAP/FILTER

nums = [1, 2, 3, 4]
squared = list(map(lambda x : x**2, nums))
evens = list(filter(lambda x : x % 2 == 0, nums))

print(squared)
print(evens)

print()
print()
print()

# SET/DICT COMPREHENSIONS

unique_squares = {x**2 for x in range(5)}
squares_dict = {x:x**2 for x in range(5)}

print(unique_squares)
print(squares_dict)

print()
print()
print()

# WALRUS OPERATOR

data = [1, 2, 3]

if (n := len(data)) > 2:
    print(f"Length is {n}")
    
print()
print()
print()

# CHAINED COMPARISONS

x = 5
if 0 < x < 10:
    print("x is in (0, 10)")
    
print()
print()
print()

# TRY/EXCEPT/ELSE/FINALLY

x = 0

try:
    result = 1 / x
except ZeroDivisionError:
    result = None
    print("Error: Division by Zero")
else:
    print("No error")
finally:
    print("Done")
    
print()
print()
print()

# *ARGS and **KWARGS

def f(*args, **kwargs):
    print(args)
    print(kwargs)
    
f(1, 2, a=3, b=4)

def print_args(*args):
    for arg in args:
        print(arg)
        
print()
print_args("Apple", "Banana", "Cherry", "Blueberry")

# TYPE HINTS

def greet(name: str) -> str:
    return f"Hello, {name}"

def greet(name):
    return f"Hello, {name}"