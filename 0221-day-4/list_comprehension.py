nums1 = []

for i in range(1, 101):
    nums1.append(i)
    
#print(nums1)

nums2 = [i for i in range(1, 101)]

#print(nums2)

mat = [[i for i in range(10)] for i in range(10)]

for row in mat:
    print(row)