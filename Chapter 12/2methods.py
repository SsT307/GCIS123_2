

class House:
    __slots__=['__no_rooms', '__facade_color','__address', '__type' ]
    def __init__(self, no_rooms, color, address, type):
        self.__no_rooms=no_rooms
        self.__facade_color=color
        self.__address=address
        self.__type=type
    # ------------------------------- no. of rooms ------------------------------- #
    def get_no_rooms(self): # Getters / Accessors
        return self.__no_rooms
    def set_no_rooms(self, new_value): # Setters / Mutators
        self.__no_rooms = new_value
        
    # ----------------------------- color of building ---------------------------- #
    def get_facade_color(self): # Getters / Accessors
        return self.__facade_color
    def set_facade_color(self, new_value): # Setters / Mutators
        self.__facade_color = new_value
        
    # ---------------------------- address of building --------------------------- #
    def get_address(self): # Getters / Accessors
        return self.__address
    def set_address(self, new_value): # Setters / Mutators
        self.__address = new_value
    
    # ----------------------------- type of building ----------------------------- #
    def get_type(self): # Getters / Accessors
        return self.__type    
    def set_type(self, new_value): # Setters / Mutators
        self.__type = new_value
    
    # ------------------------ Way to represent the object ----------------------- #
    def __str__(self): # Integrated function, has priority over __repr__
        return f'House: {self.__address}, {self.__facade_color}, {self.__type}'
    
    def __repr__(self): # Same exact thing as __str__, its just there just incase the __str__ fails or smthing
        return f'House: {self.__address}, {self.__facade_color}, {self.__type}'
    
    def __eq__(self, other): # Checking if objects are similar, using "==", check line 49
        if type(self)==type(other):
            return self.__address==other.get_address() and self.__no_rooms==other.get_no_rooms() and self.__facade_color==other.get_facade_color() and self.__type==other.get_type()
        else:
            return False
        
    def __ne__(self, other): # Checking if objects are NOT similar, using "!="
        return not self.__eq__(other) # Literally dont even need this btw
    
    def __lt__(self, other): # Checking greater than/less than using ">, <, <=, >=", line 64
        if self.__no_rooms<other.get_no_rooms():
            return True
        else:
            return False
    
    def __le__(self, other): # Checking greater than/less than using ">, <, <=, >=", line 64
        if self.__no_rooms<=other.get_no_rooms():
            return True
        else:
            return False
    
    def __gt__(self, other): # Checking greater than/less than using ">, <, <=, >=", line 64
        if self.__no_rooms>other.get_no_rooms():
            return True
        else:
            return False
    
    def __ge__(self, other): # Checking greater than/less than using ">, <, <=, >=", line 64
        if self.__no_rooms>=other.get_no_rooms():
            return True
        else:
            return False
        
    def __hash__(self):
        return hash(self.__no_rooms) * len(self.__address) # Hash something that does not change
        # Hash takes in a unique input of the object, it basically creats a unique id for the "house" in this case
    
        
house_a = House(9,'RED','The Palm', 'villa')
print(house_a)
print(house_a==house_a) # CALLING THE __eq__ FUNCTION !!!!!!!!!!!!! ------> TRUE
print(house_a!=house_a) # CALLING THE __ne__ FUNCTION !!!!!!!!!!!!! ------> FALSE

house_b = House(3,'GREEN','Mirdif', 'apt')
print(house_b>house_a) # CALLING THE __lt__ FUNCTION !!!!!!! ------> FALSE
print(house_b<house_a) # CALLING THE __lt__ FUNCTION !!!!!!! ------> TRUE

print(hash(house_a))
print(hash(house_b))

