'''Create a class Employee with attributes name, id, and salary. Please use slots to limit members. 
Create contructor, getters, setters, eq, ne, str, and hash (multiply hash of ID with salary). 
Create 5 objects of employee and create dictionary using only id of employee to store number of days
off for each employee
'''

class Employee:
    __slots__ = ['__name', '__id','__salary']
    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary
        
    # -------------------------- accessors and mutators -------------------------- #
    def get_name(self):
        return self.__name
    def set_name(self, new_value):
        self.__name = new_value
        
    def get_id(self):
        return self.__id
    def set_id(self, new_value):
        self.__id = new_value
        
    def get_salary(self):
        return self.__salary
    def set_salary(self, new_value):
        self.__salary = new_value
    
    # ------------------------------- constructors ------------------------------- #
    def __eq__(self, other):
        if type(self) == type(other):
            return self.get_name() == other.get_name() and self.get_id() == other.get_id() and self.get_salary() == other.get_salary()
        else:
            return False
    
    def __ne__(self, other):
        return not self.__eq__(self, other)
    
    def __str__(self):
        return f'Employee: {self.get_name()}, {self.get_id()} earning {self.get_salary()}'
    
    def __hash__(self):
        return (hash(self.get_id()) * self.get_salary())


employee1 = Employee('Liba', 3387, 50)
employee2 = Employee('Basma', 2261, 40)
employee3 = Employee('Simra', 4750, 10)
employee4 = Employee('Shaikha', 2693, 100)
employee5 = Employee('Danilo', 2345, 150)

# ----- creating a dictionary for employee id and number of vacation days ---- #
num_vacay = {employee1.get_id(): employee1.__hash__(), employee2.get_id(): employee2.__hash__(), employee3.get_id(): employee3.__hash__(), employee4.get_id(): employee4.__hash__(), employee5.get_id(): employee5.__hash__()}
print(num_vacay) # prints the whole dictionary

# ---------- creating a dictionary with the whole object as the key ---------- #
dict_obj = {}
dict_obj[employee1]= 40
print(dict_obj[employee1]) # prints 40, aka the value of said key

for i in dict_obj.keys(): # prints the key of the dictionary
    print(i)

'''
Make a list of the time complexities
'''