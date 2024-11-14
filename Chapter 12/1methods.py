'''
PPT IS VERY IMPORTANT, LOOK AT IT FOR CHAPTER 12
Constructor: constructs or creats an object ---> __init__
self : a referance to the object

methods: a function that is inside a class
'''


# SELF
class bike:
    def __init__(self, color, seat): # method/behavior
        self.color = color
        self.seat = seat
        
bike1 = bike('red','banana')
'''
This is like saying
bike1.color = 'red'
bike2.seat = 'banana'
'''

class House:
    __slots__=['no_rooms', 'facade_color','address', 'type' ]
    def __init__(self, no_rooms, color, address, type):
        self.no_rooms=no_rooms
        self.facade_color=color
        self.address=address
        self.type=type
"""        
house_a = House(7,'pink','Dubai Hills', 'villa')
print(f'The house in {house_a.address} has {house_a.no_rooms} rooms; it is a {house_a.facade_color} {house_a.type}.')
''' THE MEMBERS ARE VUNRABLE TO CHANGE : '''
house_a.address="Hatta"
print(f'The house in {house_a.address} has {house_a.no_rooms} rooms; it is a {house_a.facade_color} {house_a.type}.')

"""

# -------------------------- MAKING PRIVATE MEMBERS ------------------------- #

''' ADDING "__" TO THE BEGINNING OF THE MEMEBER NAME WILL MAKE IT UNACCESSABLE UNLESS ITS WITHIN THE CLASS '''
class House2:
    __slots__=['__no_rooms', '__facade_color','__address', '__type' ]
    def __init__(self, no_rooms, color, address, type):
        self.__no_rooms=no_rooms
        self.__facade_color=color
        self.__address=address
        self.__type=type
        
    def get_no_room(self): # Getters / Accessors
        return self.__address
    def set_no_room(self, new_value): # Setters / Mutators
        self.__address = new_value
    
    def get_facade_color(self): # Getters / Accessors
        return self.__facade_color
    def set_facade_color(self, new_value): # Setters / Mutators
        self.__facade_color = new_value
    
    def get_address(self): # Getters / Accessors
        return self.__address
    def set_address(self, new_value): # Setters / Mutators
        self.__address = new_value
    
    def get_type(self): # Getters / Accessors
        return self.__type    
    def set_type(self, new_value): # Setters / Mutators
        self.__type = new_value
"""
house_b1 = House2(7,'pink','Dubai Hills', 'villa') # ATTRIBUTE ERROR!!
print(f'The house in {house_b1.address} has {house_b1.no_rooms} rooms; it is a {house_b1.facade_color} {house_b1.type}.')
"""
house_b2 = House2(9,'RED','The Palm', 'villa')
print(f'The house in {house_b2.get_address()} has {house_b2.get_no_room()} rooms; it is a {house_b2.get_facade_color()} {house_b2.get_type()}.') # No error anymore!!
house_b2.set_facade_color('GREEN')
print(f'The house in {house_b2.get_address()} has {house_b2.get_no_room()} rooms; it is a {house_b2.get_facade_color()} {house_b2.get_type()}.') # No error anymore!!






