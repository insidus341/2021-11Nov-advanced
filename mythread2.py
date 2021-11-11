#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor

import time
import random
import threading


def hello(n):
    time.sleep(random.randint(0, 3))
    print(f'{n} Hello!')        # add this to the end of the queue


with ThreadPoolExecutor(max_workers=4) as executor:
    for i in range(10):
        executor.submit(hello, i)


print('Done!')
