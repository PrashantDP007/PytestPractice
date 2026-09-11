
# Decorator function
def main_welcome(func):
    def sub_welcome():
        print("Welcome to the main function!")
        func()
        print("Thank you for using the main function!")
    return sub_welcome

@main_welcome
def name_function():
    print("This is the name function.")

name_function()

# Decotor function with arguments example
def decorator_with_args(func):
    def wrapper(*args, **kwargs): # *args and **kwargs are used to pass a variable number of arguments to the function.
        print("Before the function call.")
        func(*args, **kwargs)
        print("After the function call.")
    return wrapper  
# use the decorator with arguments
@decorator_with_args
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")