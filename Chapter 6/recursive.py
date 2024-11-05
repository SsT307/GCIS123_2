def add_iterative(num):
    sum=0
    for i in range(num+1):
        sum += i
    return sum
        
# print(add_iterative(3))


def add_recursive(num):
    # base case - where we stop
    # go from num to zero and keep adding each number with the one less than it
    if num == 0: # base case
        return 0
    return num +add_recursive(num-1) # going backwards

# print(add_recursive(4))
'''
4+ call func
3+ call func
2+ call func
1+ call func
0 (return stops the function)
'''


def multiply_recurursive(num):
    # base case - where we stop
    # go from num to zero and keep adding each number with the one less than it
    if num == 1: # not zero because itll turn everything to zero!!
        return 1
    elif num >= 50: # till it reaches this number
        return 50
    return num*multiply_recurursive(num+1) # going backwards

print(multiply_recurursive(4))
