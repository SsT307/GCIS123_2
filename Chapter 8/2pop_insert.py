
a_list = ['a','b','c','d','e']

'''          POP           '''
a_list.pop(0) # removes element with index 0 -- QUEUE
x = a_list.pop() # removes the last element -- STACK
# POP IS BY INDEX
print(a_list)
print(x)


# ------ WORK: insert 1 element in the beginning and one second to last ------ #

another_list = [',', 'what', 'is', '?']
print(another_list)

'''         INSERT          '''
another_list.insert(0, 'Hi') #First element // BY INDEX
another_list.insert(-1,'up') #Second to last
print(another_list)

'''         REMOVE          '''
another_list.remove('?') # BY VALUE
print(another_list)