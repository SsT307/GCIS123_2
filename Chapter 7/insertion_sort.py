import random
import time

# Divides array into sorted and unsorted partitions

# Compares element by element, with the rightmost element one by one, but compares from left to right as it compares

# Flips each element (if needed) after comparing it with the one before it

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0...i-1]
        j = i -1
        while j >=0 and key <arr[j]: # Check if the number is greater than the key - Sorting in asending order
            arr[j+1] = arr[j]
            j-=1 # To stop the while loop
        arr[j+1] = key # Replace the element with key
    return arr

x = [13,35,86,25,10]
print(insertion_sort(x))


''' Time Complexity for sorting'''
def create_elements(n):
    print("Running...")
    arr = []
    for i in range(n):
        arr.append(random.randrange(1, 700, 1)) # Adding random numbers to an array, from 1-700, skipping 1
    begin = time.perf_counter()
    insertion_sort(arr)
    end = time.perf_counter()
    total_time = end-begin
    print("Elapsed time for creation: ", total_time)
    
create_elements(5000)