"""
A decorator is a small function that takes another function as an
argument and extends its behavior without modifying the original
function.
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()