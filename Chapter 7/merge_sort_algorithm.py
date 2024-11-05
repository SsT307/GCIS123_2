'''
Splitting an array, one array has odd Indexes, another array has even Indexes!
    Keep splitting ODD AND EVEN until they are individually split

Start merging
    When merging, SORT the elements NEXT TO EACH OTHER in asending/decending order, based off of your needs
    Merge slowly, 2 together, then 4 together, and so on...
    
!! IF ODD NUMBER OF ELEMENTS !!
    The odd number of indexes will have an EXTRA BOX for the extra element

# You dont have to know the code, but at least how to do it
'''

def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        
        # Split array into odd and even index parts
        # (SLICING) array_name[beggining:end:skip], if its empty its just says from the top or to the bottom, or not to skip
        odd_ind = arr[1::2] # ODD INDEXES, from 1-end, with step 2 
        even_ind = arr[::2] # EVEN INDEXES, from beggining-end, with step 2
        
        # Recursive calls for sorting
        merge_sort(odd_ind) # Split odd indexes
        merge_sort(even_ind) # Split even indexes
        
        # Once it is all split, move on to this:
        
        # Merge sorted parts
        i = j = k = 0
        while i < len(odd_ind) and j < len(even_ind):
            if odd_ind[i] < even_ind[j]:
                arr[k] = odd_ind[i]
                i += 1
            else:
                arr[k] = even_ind[j]
                j += 1
            k += 1
        
        # Check for any elements that are left
        while i < len(odd_ind):
            arr[k] = odd_ind[i]
            i += 1
            k += 1
        while j < len(even_ind):
            arr[k] = even_ind[j]
            j += 1
            k += 1


x = [12, 35, 24, 1, 78, 9]
print('Original Array:', x)
merge_sort(x)
print('New Array:', x)

