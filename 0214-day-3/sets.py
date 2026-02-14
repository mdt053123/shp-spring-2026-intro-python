empty_set = set()

nums = {1, 2, 2, 3, 4, 5, 5, 5}

print(nums)
print(type(nums))

A = {1, 2, 3, 4, 5}
B = {1, 4, 5, 7}

print(A.intersection(B))
print(A.union(B))
print(A.difference(B))
print(A.issubset(B))
print(B.issubset(A))
print(A.issubset(A))