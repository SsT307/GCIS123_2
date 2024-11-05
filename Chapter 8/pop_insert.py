
a_list = ['a','b','c','d','e']
a = a_list.pop(0) # removes element with index 0 -- QUEUE
e = a_list.pop() # removes the last element -- STACK
# POP IS BY INDEX
print(e)

# insert 1 element in the begging and one second to last

another_list = [',', 'what', 'is', '?']
sentence = another_list.insert(0, 'Hi') #First element // BY INDEX
sentence = another_list.insert(-1,'is') #Second to last
print(sentence)

sentence.remove('?') # BY VALUE
print(sentence)