import time
import math

def binary_search(arr, target):
    left  = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [2.2, 9.5, 10.3, 12.6, 21.6, 36, 37, 38, 39, 41, 56, 57, 77, 79.3, 83, 93, 98]
target  = 79
begin = time.perf_counter()
index = binary_search(arr, target)
end = time.perf_counter()
if index != -1:
    print(f'Element {target} found at index {index} in {(end-begin)}secs')
else:
    print(f'Element {target} not found in index in {(end-begin)}secs')
    
    
