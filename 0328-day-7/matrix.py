M = [[1, 2],
     [2, 1]]

print(M)

print(M[0])
print(M[1])

print(M[0][0])

print()

print(M[1][0])

print()

for r in range(len(M)):
    for c in range(len(M[r])):
        print(M[r][c], end = ' ')
    print()
    
print()

for row in M:
    for num in row:
        print(num, end = ' ')
    print()