import random

''' 
*           *           *           *           *           *
Merge sort, splitting the dataset into odd and even indexes 
multiple times till the data is split into individual indexes 
and then merge them together based off of the needed, 
either in acending or decending order 
*           *           *           *           *           *
'''
    
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
# large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]
large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44]
''' Runs the function to sort the large dataset '''
generate_sort_data(large_data)
''' Prints out the sorted data, it still uses the original variable for the data because its an in-place sort, meaning it destroyed the original array '''
print('New Array:', large_data)
    

    






