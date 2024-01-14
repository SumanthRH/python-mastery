from concurrent.futures import Future

def parse_line(line):
    splits = line.split("=")
    if len(splits) != 2:
        raise ValueError("line should be of the format `name=value`")
    name, value = splits
    return (name, value)

# Design: might be better to just raise an exception here instead

import time
def worker(x, y):
        print('About to work')
        time.sleep(20)
        print('Done')
        return x + y

def do_work(x, y, fut):
    fut.set_result(worker(x, y))

import threading

fut= Future()
t = threading.Thread(target=do_work, args=(2, 3, fut))
t.start()

result=  fut.result()