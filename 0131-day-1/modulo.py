def mod(a, b):
    return a - b*(a//b)

print(mod(3, 2))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(6, 12))