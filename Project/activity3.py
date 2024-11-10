"""
Activity 3, Group 6
Students: Shaikha Alhajri, Fatma Alsuwaidi, Fatma Almadani, Iliazya Alattar, Noha Abou Karnib
This activity guides us through a structured search and sort process, where each phase builds on the previous one.
"""
import random
import time



"""Phase 1"""
def insertion_sort(arr):
    """
    Sorts a given array using the insertion sort algorithm.
    Parameters:
        arr (list): A list of integers to be sorted.
    Returns:
        list: A sorted version of the input array.
    """
    '''Start from the second element'''
    for i in range(1, len(arr)):  # Start from the second element
        key = arr[i]  # Element to be inserted in the sorted portion of the array
        j = i - 1  # Index for comparing the key with the sorted portion of the array
        # Move elements of arr[0..i-1] that are greater than the key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1  # Move left
        arr[j + 1] = key  # Place the key in its correct position
    return arr  # Return the sorted array
def generate_sorted_data(size):
    """
    Generates a list of random integers, sorts it using insertion sort, and returns the sorted list.
    Parameters:
        size (int): The number of elements to generate in the array.
    Returns:
        list: The sorted list of randomly generated integers.
    """
    data = [random.randint(1, 100) for i in range(size)]  # Generate random integers between 1 and 100
    sorted_data = insertion_sort(data)  # Sort the random data using insertion sort
    return sorted_data  # Return the sorted data
# Initial small dataset
small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8]
# Sort the small dataset using insertion sort (we use copy to keep the original data unchanged)
sorted_small_data = insertion_sort(small_data)  
# Print the result
print("Sorted small_data:", sorted_small_data)


"""Phase 2"""
data = [5, 7, 8, 12, 23, 29, 32, 34, 40, 62]
def binary_search(data, target):
    """
    Performs a binary search on a sorted array to find the index of the target value.
    Parameters:
        data (list): The sorted array to search in.
        target (int): The value to search for in the array.
    Returns:
        int: The index of the target value if found, None if not found.
    """
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None
# Sample Target (only one target is given as per Phase 2)
target = 23  # You can change this to test other targets
index = binary_search(data, target)
if index is not None:
    print("Target is ",target,", found at index:", index)
else:
    print("Not found")



"""Phase 3"""
def generate_sort_data(data):
    if len(data)>1:
        ''' Split array into odd and even index parts '''
        odd_ind = data[1::2] # ODD INDEXES, from 1-end, with step 2 (skipping the even indexes)
        even_ind = data[::2] # EVEN INDEXES, from beginning-end, with step 2 (skipping the odd indexes)
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
Method 4.2: Binary Search, using recursive loops. 
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