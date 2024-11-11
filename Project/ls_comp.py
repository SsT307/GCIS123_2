ls = [n for n in range(1, 10)]
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

ls2 = [n for n in range(1, 10, 2)]
    # [1, 3, 5, 7, 8, 9]

ls3 = [char for char in "Bang!"]
    # ['B', 'a', 'n', 'g', '!',]

ls4 = ['x' for _ in range(10)]
    # ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']

ls5 = [0 for _ in "Tootsie Pop"]
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print('1',ls,'\n\b2',ls2,'\n\b3',ls3,'\n\b4',ls4,'\n\b5',ls5,'\n',)