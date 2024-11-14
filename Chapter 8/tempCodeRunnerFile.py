list_2d = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
print(f'This is the whole list: {list_2d}') # print the list

n = 0
for i in list_2d:
    print(f'Row {n}: {i}') # print each NESTED LIST
    n += 1
    

for i in list_2d:
    for j in i:
        print(j) # print each NUMBER in a new line
        
print(f'Element in the 3rd row, and 2nd column: {list_2d[2][1]}') # prints the number '8' from the array

