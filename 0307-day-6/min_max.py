def minimum(arr):
    '''
    Return the minimum element in arr
    '''
    
    if len(arr) == 0:
        return
    
    min_seen = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < min_seen:
            min_seen = arr[i]
            
    return min_seen
    
def maximum(arr):
    '''
    Return the maximum element in arr
    '''
    
    if len(arr) == 0:
        return
    
    max_seen = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > max_seen:
            max_seen = arr[i]
            
    return max_seen