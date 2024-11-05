import random
import time
'''
SORTING NUMBERS IN NUMERICAL ORDER:

 Pick the first (or any) element on the index, make into pivot
 
 Sort everything based on if the number is greater than or less than the pivot
 
 Pick more pivots, one from the numbers less than and/or one from the numbers more than
 
 Continue till all numbers are pivoted
 
'''

# ---------------------------------- SIMPLE ---------------------------------- #
def quick_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        # pivot = arr[0] # Choosing the first element
        # pivot = arr[random.randrange(0,len(arr)-1)] # Choosing a random element
        pivot = arr[len(arr)-1] # Choosing the last element
        # pivot = arr[len(arr)//2] # Choosing the middle element
        smaller = []
        equal = [] # Incase of repeating elements
        larger = []
        
        for x in arr:
            if x < pivot:
                smaller.append(x) # Add to the array with the smaller variables
            elif x == pivot:
                equal.append(x) # Add to the array when its the same element
            else:
                larger.append(x) # Add to the array with the larger variables
        
        # Call the function again to sort everything        
        return quick_sort(smaller) + equal + quick_sort(larger)

   
# EXAMPLE USE
arr = [98,34,100,3,8]
print('Original array:', arr) # Printing the original array
print(len(arr))

# Finding out the time it takes to run
begin = time.perf_counter()
sorted_arr = quick_sort(arr) # Running the function
end = time.perf_counter()
# Total time equation
total_time = end - begin


print('The amount of time it took to run the function:', total_time)
print('Sorted array:', sorted_arr)

'''
EXPERIMENT TIMEEE: 
# UNSORTED
    # First element
        - 5 elements
            2.539997e-05 seconds
        - 15 elements
            3.2e-05 seconds
            
    # Middle element
        - 5 elements
            1.19999e-05 seconds
        - 15 elements
            4.53999e-05 seconds
            
    # Last element
        - 5 elements
            4.21999e-05 seconds
        - 15 elements
            3.19e-05 seconds
             
    # Random element
        - 5 elements
            4.449999e-05 seconds
        - 15 elements
            4.59e-05 seconds
             
'''

'''           
# SORTED
    # First element
        - 5 elements
            5.0400e-05 seconds
        - 15 elements
            3.0399999e-05 seconds
            
    # Middle element
        - 5 elements
            0.00011 seconds
        - 15 elements
            3.0499883e-05 seconds
             
    # Last element
        - 5 elements
            1.910003e-05 seconds 
        - 15 elements
            4.539988e-05 seconds
             
    # Random element
        - 5 elements
            0.000123 seconds
        - 15 elements
            5.27001e-05 seconds
'''