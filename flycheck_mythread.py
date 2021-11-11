#!/usr/bin/env python3

import threading


def hello(n):
    print(f'{n} Hello!')


all_threads = []
for i in range(10):
    t = threading.Thread(target=hello)   # create a new Thread object
    t.start()   # run the thread's function in a new thread
    a
