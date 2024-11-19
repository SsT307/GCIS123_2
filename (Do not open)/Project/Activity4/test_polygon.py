from polygon import Polygon

def test_polygon_initialization():
    polygon = Polygon("Triangle", [3, 3, 3])  
    assert polygon.get_name() == "Triangle" 
    assert polygon.get_sides() == [3, 3, 3] 

def test_set_sides():
    polygon = Polygon("Square", [4, 4, 4, 4])
    polygon.set_sides([5, 5, 5, 5])  
    assert polygon.get_sides() == [5, 5, 5, 5]
    
def __eq__(self, other):
        if type(self) == type(other):
            return self.name == other.name and self.sides == other.sides
        else:
            return False

def __ne__(self, other):
        return not self.__eq__(other)

def test_polygon_equality():
    first_polygon= Polygon("Triangle", [3, 3, 3])
    second_polygon= Polygon("Triangle", [3, 3, 3])
    
    assert first_polygon == second_polygon #will return True bcs they are equal

def test_polygon_inequality():
    first_polygon = Polygon("Triangle", [3, 3, 3])
    second_polygon = Polygon("Square", [3, 3, 3, 3])
    
    assert first_polygon == second_polygon #will return False bcs they are not equal