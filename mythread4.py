#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor

import time
import random

with ThreadPoolExecutor(max_workers=4) as executor:
    output = executor.map(lambda x: x**2, range(10))

print('Done!')
print(list(output))
