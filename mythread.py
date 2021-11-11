#!/usr/bin/env python3

import threading


def hello(n):
    print(f'{n} Hello!')


all_threads = []
for i in range(10):
    # create a new Thread object
    t = threading.Thread(target=hello, args=(i,))

    t.start()   # run the thread's function in a new thread
    all_threads.append(t)
