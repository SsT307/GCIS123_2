'''
Special Methods:
    - `__init__`: Initializes the object.
    - `__str__`: Returns a string representation of the object.
    - `__repr__`: Returns a string representation of the object that could be used to recreate it
    - `__eq__`: Checks if two objects are equal.
    - `__ne__`: Checks if the two objects are not equal.
    - `__lt__`: Checks if one object is less than another.
    - `__le__`: Checks if one object is less than or equal to another.
    - `__gt__`: Checks if one object is greater than another.
    - `__ge__`: Checks if one object is greater than or equal to another.
'''

class airplane:
    __slots__=['__make', '__type','__no_passengers']
    def __init__(self, make, type, passengers):
        self.__make = make
        self.__type = type
        self.__no_passengers = passengers
    
    # ---------------------------- getters and setters --------------------------- #
    def get_make(self):
        return self.__make
    def set_make(self, new_value):
        self.__make = new_value
        
    def get_type(self):
        return self.__type
    def set_type(self, new_value):
        self.__type = new_value
        
    def get_no_passengers(self):
        return self.__no_passengers
    def set_no_passengers(self, new_value):
        self.__no_passengers = new_value
    
    # --------------------- set the string to call the object, either by printing the object OR by using the str() function -------------------- #
    def __str__(self):
        return f'Airplane {self.__make}, {self.__type}; Number of passengers: {self.__no_passengers}'
    
    # -------------------------------- operations -------------------------------- #
            # ------------------------ equal or not equal to ----------------------- #
        # EQUAL TO
    def __eq__(self, other):
        if type(self)==type(other):
            return self.__make == other.get_make() and self.__type == other.get_type() and self.__no_passengers == other.get_no_passengers()
        else:
            return False
        # NOT EQUAL TO
    def __ne__(self, other): 
        return not self.__eq__(other)
            # ------------------------------ less than ----------------------------- #
        # LESS THAN
    def __lt__(self, other):
        return self.get_no_passengers()<other.get_no_passengers()
        # LESS THAN OR EQUAL TO
    def __le__(self, other): 
        return self.get_no_passengers()<=other.get_no_passengers()
            # ---------------------------- greater than ---------------------------- #
        # GREATER THAN
    def __gt__(self, other):
        return self.get_no_passengers()>other.get_no_passengers()
        # GREATER THAN OR EQUAL TO
    def __ge__(self, other): 
        return self.get_no_passengers()>=other.get_no_passengers()
    
    # ----------------------------------- hash ----------------------------------- #
    def __hash__(self):
        return hash(self.get_no_passengers()) + len(self.get_make())
    

a1 = airplane('Boing', '747', 234)
a2 = airplane('Boing', '118', 102)
s = '11643sss'
print(str(a1))
print(a1.__eq__(a2)) # CALLING THE EQ BEHAVIOR IN A DIFFERENT WAY
