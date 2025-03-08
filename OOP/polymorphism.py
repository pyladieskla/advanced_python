"""
Polymorphism is the ability of an object to take on multiple forms.
"""

"""
Method Polymorphism: This is when objects of different classes can be
treated as objects of a common superclass.
"""
# Example of Method Polymorphism
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)


square = Square(4)
circle = Circle(5)

print(square.area()) 
print(circle.area())