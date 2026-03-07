nums = [3, 7, -4, 5, 9, 10, -3]

def linear_search(nums, target):
    '''
    Input: nums (list[int]), target (int)
    Output: index (int)
    
    Instructions:
        Go one by one through each element in nums. If that element
        matches target, return the index at which that element occurs.
        
        If by the end, we have not encountered target, return -1.
    '''
    
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        
    return -1

print(linear_search(nums, 5))