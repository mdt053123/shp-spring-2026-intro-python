def first_occurence(nums, num):
    '''
    Search through each number in nums,
    and return the first index at which num
    occurs in nums. If it does not occur at all,
    return -1.
    
    Example 1: nums = [1, 2, 3, 4, 3, 5], num = 3 -> return 2
    Example 2: nums = [1, 1, 1], num = 1 -> return 0
    Example 3: nums [1, 0], num = 2 -> return -1
    '''
    
    for i in range(len(nums)):
        if nums[i] == num:
            return i
        
    return -1
    
def print_reverse(nums):
    '''
    Print each element in nums in reverse order (on one line).
    
    Example 1: [1, 2, 3, 4] -> prints [4, 3, 2, 1]
    Example 2: [1, 2, 1, 2] -> prints [2, 1, 2, 1]
    '''
    
    for i in range(len(nums) - 1, -1, -1):
        print(nums[i], end=' ')
    
def dist_3d(p1, p2):
    '''
    Given p1 = (p1_x, p1_y, p1_z),
    p2 = (p2_x, p2_y, p2_z),
    
    Return euclidean distance between p1, p2
    '''
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)**(1/2)
    
def value_counts(nums):
    '''
    Given a list of numbers nums, print
    how many times each unique number appears.
    
    Example: nums = [1, 1, 2, 3, 3, 3, 4, 5, 5],
             prints 1: 2, 2: 1, 3: 3, 4: 1, 5: 2
    '''
    
    counts = {}
    
    for num in nums:
        if num not in counts.keys():
            counts[num] = 1
        else:
            counts[num] += 1
            
    print(counts)
    
print(first_occurence([1, 2, 3, 4, 4, 5], 4))
print_reverse([1, 2, 3, 4, 4, 5])
print()
print(dist_3d((1, 2, 3), (4, 5, 6)))
value_counts([1, 2, 3, 4, 4, 5])