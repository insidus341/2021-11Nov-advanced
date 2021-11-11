#!/usr/bin/env python3

import time
import random
import threading


def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello!')


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
