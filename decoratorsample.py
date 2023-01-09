import time


def delay_decorator(function):
    def wrapper_function():
        print("function starting")
        time.sleep(3)
        function()
        function()
        function()
        print("function stopped")
        time.sleep(5)
    return wrapper_function


@delay_decorator
def say_hello():
    print("hello")


@delay_decorator
def say_bye():
    print("bye")


def say_greeting():
    print("How are you?")


decorated_function = delay_decorator(say_bye)
decorated_function()
