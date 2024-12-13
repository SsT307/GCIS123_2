#tuple
t= (2,3,"r",8,"hello",-7)
print(t) #entire tuple


print(t[1]) #3

t= (2,3,"r",8,"hello",-7)
print(t) #entire tuple
#t[4]="another one" # will give a type error because tuples arent mutable
print(t[1]) #3

#tuple
t= (2,3,"r",8,"hello",-7)
print(t[4]) 
t1=tuple([1,2,3,4])
print(t1)
# prints hello (1,2,3,4)

#list
l=[4,9,"hi",999]
print(l) #entire list
print(l[2])
l[2]="something else" #will print along with the index of choice because lists are mutable
print(l[2]) #hi


#list append and insert
l=[4,9,"hi",999]
print(l)
l.append(4) #specify
l.insert(2,"bye")
print(l)
l[2]="something else"
print(l)



L2=list((1,5,"hi","blabla"))
print(L2)

L2 += [5]
print(L2)