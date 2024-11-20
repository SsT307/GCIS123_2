

def m(i):
    i +=1
    if i <= 1/3:
        return 1/3
    elif i == 0:
        return 0
    else:
        i-=1
        m((i-1)/(2*i+1))

print(m(3))