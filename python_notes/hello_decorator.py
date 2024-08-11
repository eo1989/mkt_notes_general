# noqa

"""
remember to set python 3.12 to run these via pyenv-win!
"""


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


# So, @decorator is just a shorter way of saying `say_whee = decorator(say_whee)`.
# Its how you apply a decorator to a function
@decorator
def say_whee():
    print("Whee!")


# This isnt needed anymore because of the @decorator syntax above.
# say_whee = decorator(say_whee)