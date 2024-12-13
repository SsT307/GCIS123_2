def add_5_string(x):
    x = str(x) + 'd'
    print(x)
    
a = 'abc'
add_5_string(a)
print(a) # Used a as a refrence, meaning that a didnt change


# ---------------------------------- DO THIS --------------------------------- #
def add_5_array(x):
    x = list(x) + ['d']
    print(x)
    
l1 = ['a', 'v', 'b', 'k']
l2 = ['e', 'f', 'g', 'l']
add_5_array(l1)

