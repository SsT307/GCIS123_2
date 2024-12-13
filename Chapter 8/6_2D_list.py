'''
A list in a list
'''

list_2d = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
print(f'This is the whole list: {list_2d}') # print the list

n = 0
for a in list_2d:
    print(f'Row {n}: {a}') # print each NESTED LIST
    n += 1
    

for i in list_2d:
    for j in i:
        print(j) # print each NUMBER in a new line
        
print(f'Element in the {n-1} row, and {a} column: {list_2d[2][1]}') # prints the number '8' from the array


# ----------- function that recieves 2D lists, and finds the target ---------- #
# DOES NOT WORK !! FIX LATER !!
# ls_2d = [[1,26,32], [24,75,6], [74,81,19], [10,41,12]]
# target = 10
# def target_in_2d(list, target):
#     for i in list:
#         for j in i:
#             if j == target:
#                 print(f'The target {target} is found at index ({i},{j})')
                
# target_in_2d(ls_2d, target)