"""
Method Overriding is when a derived class provides a different implementation
of a method that is already defined in the base class.
"""
class Animal:
    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("The dog barks.")

my_dog = Dog()
my_dog.sound()