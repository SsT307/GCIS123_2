"""
Activity 3, Group 6
Students: Shaikha Alhajri, Fatma Alsuwaidi, Fatma Almadani, Iliazya Alattar, Noha Abou Karnib
This activity guides us through a structured search and sort process, where each phase builds on the previous one.
"""

import random
import time


# Phase 1
def recursive_insertion_sort(arr, index):
    """
    Recursively sort an array using the Insertion Sort algorithm without using 'key' or slicing.
    Parameters:
    arr (list): The list to be sorted.
    index (int): The index of the last element to be considered for sorting.
    Returns:
    The sorted list.
    """
    # Base case: if index is 0, the array is already sorted
    if index == 0:
        return arr
    # Recursively sort the first index-1 elements of the array
    recursive_insertion_sort(arr, index - 1)
    # Get the current element (this will be the one we need to "insert")
    current_element = arr[index]  
    i = index - 1  # Start checking from the element before 'current_element'
    # Move elements of arr (the part before the current element) that are greater than current_element
    while i >= 0 and arr[i] > current_element:
        arr[i + 1] = arr[i]  # Shift arr[i] one position to the right
        i -= 1  # Move to the previous element
    # Insert the current element at its correct position
    arr[i + 1] = current_element
    # Return the sorted array
    return arr
# Example usage with a small list of numbers
small_data = [random.randint(1, 100) for _ in range(10)]
# Sort the small_data list using the recursive insertion sort
sorted_small_data = recursive_insertion_sort(small_data, len(small_data) - 1)
# Print the sorted list
print("Sorted small_data:", sorted_small_data)



# Phase 2
def binary_search(arr, target, start, end):
    """
    Perform a binary search to find the index of the target element in a sorted array.
    Parameters:
    arr (list): A sorted list of elements to search.
    target (int): The element to find in the list.
    start (int): The starting index of the search range.
    end (int): The ending index of the search range.
    Returns:
    The index of the target element if found, otherwise None.
    """
    # Base case: if start exceeds end, the value is not in the array
    if start > end:
        return None  # Return None if the target is not found
    # Calculate the middle index of the current range
    mid = (start + end) // 2
    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    # If the middle element is less than the target, search the right half
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    # If the middle element is greater than the target, search the left half
    else:
        return binary_search(arr, target, start, mid - 1)
# Define an array and a target value
arr = sorted_small_data
target = 23
# Initialize start and end for the search range
start = 0  # Starting index of the array
end = len(arr) - 1  # Ending index of the array
# Calling the binary_search function and storing the result 
index = binary_search(arr, target, start, end)
# If index is not None, print the index of the found element, else print "element not found"
if index is not None:
    print("Element", target, "is present at index", index)
else:
    print("Element", target, "is not present in the array.")



# Phase 3
def generate_sort_data(data):
    if len(data)>1:
        odd_ind = []
        even_ind = []
        ''' Split array into odd and even index parts '''
        for i in range(0,len(data)):
            if i%2 == 0:
                even_ind.append(data[i])
            else:
                odd_ind.append(data[i])
        ''' Recursive calls for sorting the odd and even indexes '''
        generate_sort_data(odd_ind) # Split odd indexes
        generate_sort_data(even_ind) # Split even indexes
        ''' Once it is all split, move on to this: '''
        ''' Merge sorted parts '''
        i = j = k = 0
        while i < len(odd_ind) and j < len(even_ind):
            if odd_ind[i] < even_ind[j]:
                data[k] = odd_ind[i]
                i += 1
            else:
                data[k] = even_ind[j]
                j += 1
            k += 1
        ''' Check for any elements that are left '''
        while i < len(odd_ind):
            data[k] = odd_ind[i]
            i += 1
            k += 1
        while j < len(even_ind):
            data[k] = even_ind[j]
            j += 1
            k += 1
''' Gets an array, with the first 10 elements set, and adds an array to it with 990 elements with random numbers from 1-100 '''
large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]
''' Runs the function to sort the large dataset '''
generate_sort_data(large_data)
''' Prints out the sorted data, it still uses the original variable for the data because its an in-place sort, meaning it destroyed the original array '''
print('New Array:', large_data)



"""
Phase 4:
This phase searches the sorted dataset from phase 3 using two searching methods and compares their execution time.
Method 4.1: Linear Search
Method 4.2: Binary Search
"""
# Phase 4.1 - Linear Search
def linear_search(target, array):
    """
    Performs a linear search on an array to find the index of the target value.
    Parameters:
        target (int): The value to search for in the array.
        array (list): The array to search in.
    Returns:
        int: The index of the target value if found, None if not found.
    """
    index = 0 
    while index < len(array):
        if array[index] == target:  # Return the index if found
            return index
        index += 1
    return None  # Return None if target is not found
# Using the array generated and sorted in Phase 3
target = 88  # Set the target value for search
# Measure the start and end time for linear search
begin_linear = time.perf_counter()
result_linear = linear_search(target, large_data)  # Perform the linear search
end_linear = time.perf_counter()
# Display results for linear search
if result_linear is not None:
    print("Linear Search: Target", target, "found at index", result_linear)
else:
    print("Linear Search: Target", target, "not found in the array.")
print("Linear Search Time:", end_linear - begin_linear, "seconds")  # Display elapsed time for linear search

## ------ ##

# Phase 4.2 - Binary Search (Recursive)
def recursive_binary_search(sorted_array, target_value, left_index, right_index):
    """
    Performs a binary search using recursion on a sorted array to find the target value.
    Parameters:
        sorted_array (list): The sorted array to search in.
        target_value (int): The value to search for.
        left_index (int): The starting index of the current subarray.
        right_index (int): The ending index of the current subarray.
    Returns:
        int: The index of the target value if found, None if not found.
    """
    if left_index > right_index:
        return None  # Base case: value not found
    mid_index = (left_index + right_index) // 2  # Calculate the mid index
    if sorted_array[mid_index] == target_value:
        return mid_index  # Target found
    elif sorted_array[mid_index] < target_value:
        return recursive_binary_search(sorted_array, target_value, mid_index + 1, right_index)  # Search right half
    else:
        return recursive_binary_search(sorted_array, target_value, left_index, mid_index - 1)  # Search left half
# Using the array generated and sorted in Phase 3
target = 88  # Set the target value for search
# Measure the start and end time for binary search
start_time = time.perf_counter()
search_result = recursive_binary_search(large_data, target, 0, len(large_data) - 1)  # Perform the binary search
elapsed_time = time.perf_counter() - start_time
# Display results for binary search
if search_result is not None:
    print("Binary Search: Target", target, "found at index", search_result)
else:
    print("Binary Search: Value is not found.")
print("Binary Search Time:", elapsed_time, "seconds")  # Display elapsed time for binary search