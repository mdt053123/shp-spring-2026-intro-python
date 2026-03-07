def binary_search(arr, target):
    return helper(arr, target, 0, len(arr) - 1)

def helper(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return helper(arr, target, mid + 1, right)
    else:
        return helper(arr, target, left, mid - 1)
    
print(binary_search([3, 4, 5, 6, 7], 6))