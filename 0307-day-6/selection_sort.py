def selection_sort(arr):
    # O(n^2)
    
    n = len(arr)
    
    # total =  (n-1) + (n-2) + (n-3) + ... + 2 + 1 = n(n-1)/2 = (1/2)n^2 - (1/2)n ~ n^2
    
    for i in range(n - 1): # n - 1 times
        min_idx = i
        
        for j in range(i + 1, n): # n - (i + 1) times
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr