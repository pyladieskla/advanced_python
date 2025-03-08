"""
Instance Attributes are variables that are unique to each instance of a class.
"""
# Example of Class Instance Attribute

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

# class instance
my_dog = Dog("Squishy", 6)
print(my_dog.name)
print(f'{my_dog.name} is {my_dog.age} years old! Yeahhhhhhh!!!!!!!!!!!!!!')


