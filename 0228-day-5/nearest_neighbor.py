data = [((0, 0), 'red'),
        ((0, 1), 'red'),
        ((1, 2), 'red'),
        ((5, 5), 'blue'),
        ((6, 6), 'blue'),
        ((10, 0), 'green')]

x = float(input("Enter x-val: "))
y = float(input("Enter y-val: "))

p = (x, y)

def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**(1/2)

def classify(p):
    for point, color in data:
        if p == point:
            return color
        
        
    nearest_distance = float("inf") # gives a very large float value
    nearest_color = None
    
    for point, color in data:
        dist = distance(p, point)
        
        if dist < nearest_distance:
            nearest_distance = dist
            nearest_color = color
            
    data.append((p, nearest_color))
    
    return nearest_color

print(classify(p))
        
    