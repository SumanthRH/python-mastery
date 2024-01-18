import os
import time

# function that can be used to monitor server logs, debugging logs, etc
def follow(filename):
    with open(filename) as f:
        f.seek(0, os.SEEK_END) # Move file pointer 0 bytes from end of file
        while True:
            line = f.readline()
            if line == "":
                time.sleep(0.1) # keep waiting
                continue
            yield line

for line in follow(filename="../Data/stocklog.csv"):
    fields = line.split(",")
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print("%10s %10.2f %10.2f" % (name, price, change))