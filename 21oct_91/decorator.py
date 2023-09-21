# Define a simple decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Define a function to be decorated
@my_decorator  # This line applies the decorator to the function
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()