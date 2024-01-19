import os
import time

# function that can be used to monitor server logs, debugging logs, etc
def follow(filename):
    try:
        with open(filename) as f:
            f.seek(0, os.SEEK_END) # Move file pointer 0 bytes from end of file
            while True:
                line = f.readline()
                if line == "":
                    time.sleep(0.1) # keep waiting
                    continue
                yield line
    except GeneratorExit:
        print("Following done")

if __name__ == "__main__":
    f = follow(filename="../Data/stocklog.csv")