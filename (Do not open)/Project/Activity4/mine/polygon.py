
class polygon:
    __slots__ = ['__name', '__sides']
    def __init__(self, name, sides):
        self.__name = name
        self.__sides = sides
    
    def get_name(self):
        return self.__name
    def set_name(self, new_value):
        self.__name = str(new_value)
    
    def get_sides(self):
        return self.__sides
    def set_sides(self, new_value):
        self.__sides = list(new_value)
        
def test_polygon_initialization(object):
    # Checking if object of the polygon class has been correctly innitilized
    # Check for name of object being a string
    assert isinstance(object.get_name(), str)
    # Check for sides of the polygon being a list
    assert isinstance(object.get_sides(), list)
    
myobject = polygon('Square',[4,4])
test_polygon_initialization(myobject)  # This will run the test function with the object myobject
    