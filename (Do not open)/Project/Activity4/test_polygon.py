from polygon import Polygon

def test_polygon_initialization():
    polygon = Polygon("Triangle", [3, 3, 3])  
    assert polygon.get_name() == "Triangle" 
    assert polygon.get_sides() == [3, 3, 3] 

def test_set_sides():
    polygon = Polygon("Square", [4, 4, 4, 4])
    polygon.set_sides([5, 5, 5, 5])  
    assert polygon.get_sides() == [5, 5, 5, 5]