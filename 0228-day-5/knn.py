data = [((0, 0), 'red'),
        ((0, 1), 'red'),
        ((1, 2), 'red'),
        ((5, 5), 'blue'),
        ((6, 6), 'blue'),
        ((10, 0), 'green')]

x = float(input("Enter x-val: "))
y = float(input("Enter y-val: "))
k = int(input("Enter k-val: "))

p = (x, y)

def distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**(1/2)

def classify(p, k):
    # assume k is odd, k <= len(data)
    
    for point, color in data:
        if p == point:
            return color
        
    dists = []
    idx = 0
    
    for point, color in data:
        dist = distance(p, point)
        dists.append((dist, idx, color))
        idx += 1
        
    dists_sorted = sorted(dists)
    
    k_neighbors = dists_sorted[:k]
    
    counts = {}
    for dist, idx, color in k_neighbors:
        if color in counts:
            counts[color] += 1
        else:
            counts[color] = 1
            
    majority_color = None
    majority_count = -1
    for color, count in counts.items():
        if count > majority_count:
            majority_count = count
            majority_color = color
            
    data.append((p, majority_color))
    
    return majority_color

print(classify(p, k))