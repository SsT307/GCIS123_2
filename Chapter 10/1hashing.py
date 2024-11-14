gcis123={'a':'Basma', True:'Omar', False:'Fatma', 'c':'Layan'}
print(gcis123[1])


k = gcis123.keys()
print(k)


set1={4,5,7,9}
print(set1)


set1.add(99)
print(set1)


set1.add(7)
print(set1)


"""
{9, 4, 5, 7}
{99, 4, 5, 7, 9}
{99, 4, 5, 7, 9}
"""
for i in set1:
    print(i)


"""
{9, 4, 5, 7}
{99, 4, 5, 7, 9}
{99, 4, 5, 7, 9}
99
4
5
"""
# To access a specific key that is a number:
    for i in k:
       if i == (keyNumber):
             print(dictionary_name[i]
       else:
