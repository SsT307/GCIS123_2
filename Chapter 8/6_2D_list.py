'''
A list in a list
'''

list_2d = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
print(list_2d) # print the list

for i in list_2d:
    print(i) # print each NESTED LIST
    

for i in list_2d:
    for j in i:
        print(j) # print each NUMBER in a new line