n = 0

while n < 20:
    print(n)
    
    n += 2 # equiv. to n = n + 2
    
x = 0

while x != 20:
    print(x)
    
    x += 2
    
while False: # will never run
    print(3)
    
#while True: # runs indefinitely
    #print(3)
    
print()

y = 1

while True:
    if y == 21:
        break
    
    print(y)
    y += 2
    
print()
floor = 1

while floor <= 15:
    if floor == 13:
        floor += 1
        continue
    
    print(floor)
    floor += 1