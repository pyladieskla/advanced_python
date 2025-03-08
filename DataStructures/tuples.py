"""
A tuple collection of items that can be of 
any data type including strings, integers, floats etc
Tuples are immutable
"""

# Create a tuple
colors = ('red', 'green', 'blue')

# Accessing elements
print(colors[0])

# Trying to modify an element will raise an error
try:
    colors[0] = 'yellow'
except TypeError:
    print('Tuples are immutable')


pyladies_names = [
    {
        "mentor": "Monica",
        "age": 27,
        "community": "PyLadies"
    },
    {
        "assistant":"Brenda",
        "age": 26,
        "community":"PyLadies"
    },
]

print(pyladies_names)
