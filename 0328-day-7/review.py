# basic input, output, variables

#print("Hello!")

#name = input("Enter your name: ")
#print(f"Hello, {name}!")

# conditionals, loops, functions

def my_func(x, y):
    return x + y

z = my_func(3, 2)
#print(z)

concat = my_func("apple", "sauce")
print(concat)

if 2 > 2:
    print("2 > 2")
elif 4 > 2:
    print("4 > 2")
else:
    print("Invalid")
    
for i in range(1, 10):
    print(i, end=' ')
    
# data structures
l = [1, 2, 3, 4, 5]
t = (1, 2, 3)
s = {1, 2, 2, 3}
d = { 0 : "zero",
      1 : "one",
      2 : "two" }

print()
for i in range(20):
    print(d[i % 3])