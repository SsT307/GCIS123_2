''''
Classes: models represented by code, where each variable, contains another variable
State/Members is what the class contains
Behavior is what the class does
'''

# ------------------------- Creating a student class ------------------------- #
class student:
    '''Class representation of a student'''
    def __init__(self,name,id,age,major, grades): # The function has to be called __init__, because it initializes the class,  CONSTRUCTOR
        ''' Members of student: '''
        ''' These memebers will apply to the whole class, and not just the function '''
        self.name = name
        self.student_id = id
        self.age = age
        self.major = major
        self.grades = grades
    
    def calculate_birthyear(self):
        return 2024-self.age
    
    def calculate_average(self):
        return sum(self.grades)/len(self.grades)
    
"""    
s1 = student('Ben', 1715, 23, 'CIT', [99,93,97,100])
# print(s) ---> wont work because its not calling a specific thing in the class
print(f'Student 1 is: {s1.name}, {s1.age}')
print(s1.calculate_birthyear())
print(s1.calculate_average())

s2= student('Majed', 6001, 75, 'Philosophy', [76,89,56,100])
print(f'Student 2 is: {s2.student_id}, {s2.major} - Born in {s2.calculate_birthyear()}')
print(s2.calculate_average())

"""



# ----- create a fruit class with 3 members: name of fruit, color, sweet (yes or no) ---- #
class fruit:
    ''' Class representation of a fruit '''
    def __init__(self, name, color, sweet):
        ''' Attributes of the fruit: '''
        self.name = name
        self.color = color
        self.sweet = sweet
    def set_color(self, new_color):
        self.color = new_color

'''    
apple = fruit('Apple', 'Red', 'True')
print(f'Fruit1 is: {apple.name}, and {apple.color}. Is it sweet? {apple.sweet}')

apple.set_color('Green')
print(f'Fruit1 is now {apple.color}')
'''



# --------------------------- Creating a card class -------------------------- #
class card:
    ''' Class representation of a solitare card '''
    
    __slots__ = ['rank', 'suit', 'name', 'shorthand'] # Only allowed to use these members, otherwise ATTRIBUTE ERROR will occur
    
    def __init__(self, rank, suit): # Self: automatically passed in
        ''' Members of the '''
        self.rank = rank
        self.suit = suit
        ''' Deriving the values of some attributes to other members'''
        self.name = str(rank) + " of " + suit
        self.shorthand = str(rank) + suit[0]
        
# Card: Call the constructor with the same name as the class
# You dont need to call an argument for the self parameter

a_card = card(5, 'Hearts')
print(a_card.name, a_card.shorthand) # Calling members (the ones not in the argument)

b_card = card('K', 'Spades')
print(b_card.name, b_card.shorthand) # Calling members (the ones not in the argument)

