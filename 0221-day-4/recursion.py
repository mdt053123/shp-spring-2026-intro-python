def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(10):
    print(f"factorial({i}) = {factorial(i)}")

print()

for i in range(10):
    print(f"fib({i}) = {fib(i)}")
    
nums = [1, 2, 3, 4, 5]

def sumNums(nums):
    return sumNumsHelper(nums, 0)

print()

def sumNumsHelper(nums, i):
    if i == len(nums):
        return 0
    return nums[i] + sumNumsHelper(nums, i + 1)

print(sumNums(nums))