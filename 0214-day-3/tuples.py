p1 = (2, 3)
p2 = (1, -5)

print(p1, p2)
print(p1[0])
# p1[0] = 3 -- DOES NOT WORK, tuples are immutable

def dist(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**(1/2)
    
d = dist(p1, p2)
print(d)

x = (3) # same as saying x = 3
y = (3,) # 1-tuple

print(type(x), type(y))