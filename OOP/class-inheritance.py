"""
Inheritance allows one class to inherit the properties and behavior of another class
"""

"""
Bas Class: the base class is the class that is being inherited from
"""
class Animal:
    def __init__(self, name):
        self.name = name
        # self.tail = tail
    
    def eat(self):
        print(f"{self.name} is eating.")

"""
Derived Class: the derived class is the class that is doing the inheriting.
"""
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def bark(self):
        print("Woof!")

my_dog = Dog("Fido", 3)
my_dog.eat()