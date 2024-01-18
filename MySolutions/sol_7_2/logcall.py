from functools import wraps

def logformat(fmt):
    def logged(func):
        # creates a wrapper function that prints a statement every time it's called
        print("Adding logging to : ", func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged

logged = logformat("Calling {func.__name__}")


class Spam:
    @logged
    def instance_method(self):
        pass

    @classmethod
    @logged
    def class_method(cls):
        pass

    @staticmethod
    @logged
    def static_method():
        pass

    @property
    @logged
    def property_method(self):
        pass