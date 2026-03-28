import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

print(arr[1])
print(f"total memory taken up: {arr.itemsize*arr.size}")
print(arr.prod())