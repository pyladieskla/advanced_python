"""
A dictionary is a collection of key-value pairs.
"""

# Create a dictionary
person = {"name":"John", "age":30, "city":"Kampala"}
# african_cities = {"Uganda":"kampala", "Kenya":"Nairobi", "Tanzania":"Dodoma"}

# Accessing values
print(person["name"])
# print(person["city"])
# print(person["age"])

# Modifying values
person["age"] = 31
print(person)

# Adding key-value pairs
person["Country"] = "Uganda"
print(person)

# Removing key-value pairs
del person["city"]
print(person)

