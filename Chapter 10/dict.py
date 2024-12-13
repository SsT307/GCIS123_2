# To access elements:
dict_name = {'a':123, 'b':111}
# Printing: 
u= dict_name['a']
print(u)

# To access keys:
x= dict_name.keys() 
print(x)

# To access a specific key that is a number:
for i in x:
    if i == ('a'):
        print(dict_name[i])
    else:
        print('Error')
        
for i in dict_name.keys():
    print(dict_name)