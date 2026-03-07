def f1(n): # O(n)
    for i in range(n):
        print("Hello")
        
def f2(n): # O(1)
    for i in range(500):
        print("Hello")
        
def f3(n): # O(n^2)
    # n + n + n + ... + n <- n times
    for i in range(n): # O(n)
        for j in range(n): # O(n)
            print("Hello")
            
def f4(n): # O(logn)
    if n == 1:
        return 1
    
    return n * f4(n // 2) # n * (n // 2) * (n // 4) * ... * 2 * 1

def f5(n): # O(sqrt(n))
    i = 1
    
    while i*i < n:
        print(i)
        
        i += 1