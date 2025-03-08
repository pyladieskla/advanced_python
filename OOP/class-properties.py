"""
Properties provide a way to customize access to attributes using "getters" and "setters"

--> Getters: Return the value of an attribute
--> Setters: Modify the value of an attribute
"""
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        self._age = value

Person = Person("John", 18)
print(Person.name)
Person.name = "Jane"
print(Person.name)