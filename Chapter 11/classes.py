''''
Classes: models represented by code, where each variable, contains another variable
'''

class student:
    '''Class representation of a student'''
    def __init__(self,name,id,age,major, grades): # The function has to be called __init__, because it initializes the class
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
    
    
s1 = student('Ben', 1715, 23, 'CIT', [99,93,97,100])
# print(s) ---> wont work because its not calling a specific thing in the class
print(f'Student 1 is: {s1.name}, {s1.age}')
print(s1.calculate_birthyear())
print(s1.calculate_average())

s2= student('Majed', 6001, 75, 'Philosophy', [76,89,56,100])
print(f'Student 2 is: {s2.student_id}, {s2.major} - Born in {s2.calculate_birthyear()}')
print(s2.calculate_average())
