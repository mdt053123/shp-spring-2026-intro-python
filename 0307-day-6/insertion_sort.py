def insertion_sort(arr):
    # O(n^2) worst, O(n) best
    
    n = len(arr)
    
    for i in range(1, n):
        curr = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > curr:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = curr
        
    return arr

arr = [-5, 7, 2, 9, -3, 11, 99]

print(insertion_sort(arr))