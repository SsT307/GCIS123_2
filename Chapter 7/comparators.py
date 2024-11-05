def print_first(comparator, a, b):
    if comparator(a,b):
        print(a,b)
    else:
        print(b, a)


def more_than(a, b):
    return a >= b

print_first(more_than, 6, 15)