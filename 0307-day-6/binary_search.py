nums = [-5, -3, -1, 2, 5, 7, 9]

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
            
    return -1

print(binary_search(nums, 5))