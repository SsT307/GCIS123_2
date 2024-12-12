def m(i):
    if (i<=0):
        return 0
    else:
        return (i/(2*i+1) + m(i-1))
    
# print(m(3))



"""
Question 1:
(a, b, c, d, e, f, g, h, i, j, k, l)
"""
import math
# ---------------------------------- PART A ---------------------------------- #
class Circle:
    __slots__ = ['__radius'] # PART A
    # ---------------------------------- PART B ---------------------------------- #
    def __init__(self, radius=10): # PART B
        self.__radius = radius
    # ---------------------------------- PART C ---------------------------------- #
    def getRadius(self): # PART C
        return self.__radius
    # ---------------------------------- PART D ---------------------------------- #
    def setRadius(self, new_value): # PART D
        self.__radius = new_value
    # ---------------------------------- PART E ---------------------------------- #
    def computeArea(self): # PART E
        return math.pi*(self.getRadius()^2)
    # ---------------------------------- PART F ---------------------------------- #
    def __eq__(self, other): # PART F
        if type(self) == type(other):
            return self.__radius == other.getRadius()
        else:
            return False
    # ---------------------------------- PART G ---------------------------------- #
    def __str__(self): # PART G
        return f"This circle has radius: {self.__radius}"

# PART H 
c1 = Circle()
c2 = Circle()
# PART I
print(c1.__eq__(c2))
# PART J
print(c1.getRadius())
# PART K
print(c2)
# PART L
print(c2.computeArea())