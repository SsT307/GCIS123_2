'''
Calling a function within a function
'''
def func_caller(a_func, x):
    print(a_func.__name__) # name = private name of the function (prints name of function)
    result = a_func(x)
    print(result)

def square_it(y):
    return y*y

# func_caller(square_it, 5)



'''
Function 2
'''
def evens(func, n):
    print(func.__name__)
    result = func(n)
    print(result)
    
def runner(n):
    sum = 0
    for i in range(0, n+1, 2):
        sum += i
    return sum


# evens(runner, 7)
