"""
A list is a collection of items that can be of any data type, 
including strings, integers, floats, and others
"""

#  Create a list
fruits = ['apple', 'banana', 'cherry']

# Accessing elements
print(fruits[0])
print(fruits[1])
print(fruits[2])

#  Modifying elements
fruits[0] = "mango"
print(fruits)


# Adding elements to the list
fruits.append("orange")
print(fruits)

# Removing elements
fruits.remove("banana")
print(fruits)