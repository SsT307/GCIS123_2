ls1 = [n for n in range(1, 10)]
print(ls1)

ls2 = [x//2 for x in range(19)] # Floor division with each number till 18
print(ls2)

ls3 = [5 for _ in range(10)] # ten 5's
print(ls3)

ls4 = [q for q in range(10) if q % 2 == 0] # will print anything (divisible by 2)
print(ls4)

ls5 = [a+3 for a in range(9)]
print(ls5)

ls6 = [a*10 for a in range(10,100,10) if a%3==0]
print(ls6)


lst2=[a*10 for a in range(10,100,10) if a%3==0] 
# if divisible by 3 multiply by 10
#10 20 30 40 50 60 80 80 90
print(lst2)
# 300  600  900