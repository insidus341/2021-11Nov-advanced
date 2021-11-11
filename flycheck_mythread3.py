#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor

import time
import random



    for i in range(10):
        executor.submit(hello, i)  # call hello(i) inside of a thread

print('Done!')
