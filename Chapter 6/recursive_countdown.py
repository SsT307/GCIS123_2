def countdown(num):
    if num == 0:
        print(0)
        return 0
    print(num)
    countdown(num-1)
    
countdown(3)


def factorial(num):
    if num == 1: # factorial doesnt go to zero
        return 1
    return num*factorial(num-1) # going backwards

print(factorial(4))


# input a base and exponent and the user inputs the base case


# -------------------------------- DUMB STUFF -------------------------------- #
""""def exponent(base, exp):
    if exp == 0:
        return 0
    print(base**exp)
    exponent(base, exp-1)
    
# exponent(2, 3)

def what(num ,ex):
    total = 1
    for i in range(ex):
        total = total*num
    print(total)

what(2,3)"""
# ----------------------------------- WHAAA ---------------------------------- #

def exponent(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else: 
        return base * exponent(base, exp - 1)

print(exponent(2,5))
    