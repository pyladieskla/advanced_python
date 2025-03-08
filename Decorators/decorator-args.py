"""
In this example, repeat is a decorator factory that takes num_times
as an argument. The decorator function is defined inside repeat and 
returns the wrapper.
"""
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}")

greet("john")