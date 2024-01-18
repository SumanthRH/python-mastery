
class Frange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        start = self.start
        while start < self.stop:
            yield start
            start += self.step

f = Frange(0, 2, 0.25)
for x in f:
    print(x, end=" ")
print("\n")
for x in f:
    print(x, end=" ")