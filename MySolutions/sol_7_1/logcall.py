
def logged(func):
    # creates a wrapper function that prints a statement every time it's called
    print("Adding logging to : ", func.__name__)
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper