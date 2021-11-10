#!/usr/bin/env python3

from icecream import Scoop, Bowl

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
s6 = Scoop('flavor ')

print(s1.flavor)  # prints chocolate

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b.flavors())  # ['chocolate', 'vanilla', 'coffee']
