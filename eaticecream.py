#!/usr/bin/env python3

from icecream import Scoop, Bowl, BigBowl

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')
s6 = Scoop('flavor 6')

print(s1.flavor)  # prints chocolate

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)
b.add_scoops(s6)
print(b.flavors())

bb = BigBowl()
bb.add_scoops(s1, s2)
bb.add_scoops(s3)
bb.add_scoops(s4, s5)
bb.add_scoops(s6)
print(bb.flavors())

print(s1)
print(s2)
print(b)
print(bb)
