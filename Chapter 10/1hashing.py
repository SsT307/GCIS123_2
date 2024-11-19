
gcis123={'a':'Basma', True:'Omar', False:'Fatma', 'c':'Layan'}
print(gcis123[1])
print(gcis123['a'])

k = gcis123.keys()
print(k)

for i in k:
    print(i,'\b,', gcis123[i])


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


