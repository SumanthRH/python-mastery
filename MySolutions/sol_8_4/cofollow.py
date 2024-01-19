import os
import time
from functools import wraps

def follow(filename, target):
    with open(filename, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if line != "":
                target.send(line)
            else:
                time.sleep(0.1)


def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)
        return f
    return start

@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print("ERROR: %r" % e)

if __name__ == "__main__":
    # follow("../Data/stocklog.csv", printer())
    p = printer()
    