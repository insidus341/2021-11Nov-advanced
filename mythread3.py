#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor

import time
import random


def hello(n):
    time.sleep(random.randint(0, 3))
    return f'{n} Hello!'


with ThreadPoolExecutor(max_workers=4) as executor:
    for i in range(10):
        future = executor.submit(hello, i)
        print(future.result())

print('Done!')
