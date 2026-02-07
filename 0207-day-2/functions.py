def f(x):
    return x * x

    # print("Hello") - gets ignored

for i in range(10):
    print(f(i), end = ' ')
    
def is_even(n):
    """
    This function returns True if n is even,
    False if n is not even
    """
    
    if n % 2 == 0:
        return True
    return False

print()

for i in range(20):
    print(f"Is {i} even: {is_even(i)}")
    
print()

def g():
    print("Hello")
    
print(g()) # prints 'Hello', returns 'None'

print()

g() # prints 'Hello'