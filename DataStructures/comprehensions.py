"""
Comprehensions are a concise way to create lists, dicts, or sets
"""
# List comprehensions
numbers = [x**2 for x in range(5)]
print(numbers)

# Dict comprehensions
squares = {x: x**2 for x in range(5)}
print(squares)

# Set comprehensions
unique_numbers = {x for x in [1, 2, 2, 3, 4, 4, 4]}
print(unique_numbers)
