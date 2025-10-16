from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorator")

greet()
print(greet.__name__) # prints "wrapper", needs wraps to preserve the name (greet)