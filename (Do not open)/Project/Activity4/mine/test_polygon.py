from polygon import polygon

'''
Test for negative
Zeroes
test setters

'''


def test_polygon_initialization():
    triangle1 = polygon("Triangle", [3, 3, 3]) 
    total = 0
    for i in triangle1.get_sides():
        total += i
    if total != 0:
        assert triangle1.get_name() == "Triangle" 
        assert triangle1.get_sides() == [3, 3, 3]
    else:
        assert False

def test_set_sides():
    square = polygon("Square", [4, 4, 4, 4])
    assert square.get_sides() == [4,4,4,4]
    square.set_sides([5, 5, 5, 5])  
    assert square.get_sides() == [5, 5, 5, 5]


   
def __eq__(self, other):
        if type(self) == type(other):
            return self.__name == other.get_name() and self.__sides == other.get_sides()
        else:
            return False

def __ne__(self, other):
        return not self.__eq__(other)

def test_polygon_equality():
    triangle2 = polygon("Triangle", [3, 3, 3])
    triangle3 = polygon("Triangle", [3, 3, 3])
    assert triangle2.__eq__(triangle3) #will return True bcs they are equal

def test_polygon_inequality():
    triangle5 = polygon("Triangle", [3, 3, 3])
    square2 = polygon("Square", [3, 3, 3, 3])
    assert triangle5.__ne__(square2) #will return True bcs they are not equal
    
