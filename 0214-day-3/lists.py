nums = [3, 4, 6, 8, 10, 11, -3]

elements = ["Michael", True, 4j, 3]

#print(nums)
#print(elements)

for num in nums:
    print(num, end = ' ')
    
print()

i = 0

while i < len(nums):
    print(nums[i], end = ' ')
    i += 1
    
print()

for i in range(len(nums)):
    print(nums[i], end = ' ')
    
print()

nums.append(3) # adds element 3 to the end of nums

for num in nums:
    print(num, end = ' ')
print()

nums.pop(3)
for num in nums:
    print(num, end = ' ')
print()

nums.insert(3, 8) # inserts element 8 at index 3
for num in nums:
    print(num, end = ' ')
print()

nums.sort()
for num in nums:
    print(num, end = ' ')
print()