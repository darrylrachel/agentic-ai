from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kargs)
        print(f"Finsihed: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai with {milk} milk")

brew_chai("Masala")