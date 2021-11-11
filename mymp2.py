#!/usr/bin/env python3

from concurrent.futures import ProcessPoolExecutor


def square(x):
    return x ** 2


with ProcessPoolExecutor(max_workers=4) as executor:
    output = executor.map(square, range(10))

print('Done!')
print(list(output))
