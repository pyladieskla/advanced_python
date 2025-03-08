"""
A class method is a function that is associated with a class or class instance
"""

# Example of Class Method

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # This is a class method
    def bark(self): 
        print("Woof! Woof!")


my_dog = Dog("Squishy", 6)

my_dog.bark()