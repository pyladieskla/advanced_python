"""
Operator polymorphism is when operators such as +, -, * etc
can be redefined for user-defined classes.
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    

vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

vector3 = vector1 + vector2
print(vector3.x)
print(vector3.y)