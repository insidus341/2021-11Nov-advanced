#!/usr/bin/env python3

# let's rewrite mythread.py to use multiprocessing -- a module
# that uses (almost the) same API as threading, but it launches
# processes instead

import time
import random
import multiprocessing

q = multiprocessing.Queue()               # thread-safe data structure!
l = multiprocessing.Lock()            # create a "mutex"


def hello(n):
    time.sleep(random.randint(0, 3))

    # From here, treat it as atomic -- don't let multiple threads in this region simulteously

    with l:
        q.put(f'{n} Hello!')        # add this to the end of the queue
        time.sleep(random.randint(0, 3))
        q.put(f'{n} Goodbye!')      # add this to the end of the queue

    # Above here, treat it as atomic -- don't let multiple threads in this region simulteously


all_processes = []
for i in range(10):
    # create a new Process object
    p = threading.Thread(target=hello, args=(i,))

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
