
class student:
    __slots__ = ["__name", "__id", "__course"]
    def __init__(self, name='Shaikha', id=1222, course='CIT'):
        self.__name = name
        self.__id = id
        self.__course = course
    
    def get_name(self):
        return self.__name
    def set_name(self, new_value):
        self.__name = new_value
    # ------------------------------------- - ------------------------------------ #
    def get_id(self):
        return self.__id
    def set_id(self, new_value):
        self.__id = new_value
    # ------------------------------------- - ------------------------------------ #
    def get_course(self):
        return self.__course
    def set_course(self, new_value):
        self.__course = new_value
    
    def __eq__(self, other):
        return self.get_name() == other.get_name() and self.get_id() == other.get_id() and self.get_course() == other.get_course()
    
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        return self.get_id() < other.get_id()

    
    def __gt__(self, other):
        return self.get_id() > other.get_id()
    
    
    def __str__(self):
        return f"Name: {self.get_name()}, ID: {self.get_id()}, Major: {self.get_course()}"
        
s1 = student('Omar', '1345', 'CSEC')
print(s1)

s2 = student('D', '1111', 'CIT')

print(s2.__lt__(s1))