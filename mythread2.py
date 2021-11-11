#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor

import time
import random
import threading


def hello(n):
    time.sleep(random.randint(0, 3))
    q.put(f'{n} Hello!')        # add this to the end of the queue


all_threads = []
for i in range(10):
    # create a new Thread object
    t = threading.Thread(target=hello, args=(i,))

    t.start()   # run the thread's function in a new thread
    all_threads.append(t)


# make sure that all threads have finished running
# before they get to this point

# we can wait for a thread to finish with the "join" method
for one_thread in all_threads:
    one_thread.join()

print('Done!')

while not q.empty():
    print(q.get())   # retrieve from the top of the queue
