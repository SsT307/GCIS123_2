from polygon import polygon

def test_polygon_initialization(object):
    # Checking if object of the polygon class has been correctly innitilized
    # Check for name of object being a string
    assert isinstance(object.get_name(), str)
    # Check for sides of the polygon being a list
    assert isinstance(object.get_sides(), list)
    
myobject = polygon('Square',[4,4])
test_polygon_initialization(myobject)  # This will run the test function with the object myobject