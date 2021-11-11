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
print(len(bb))
print(bb[3])   # single index
print(bb[1:3])  # --> bb[slice(1,3)]

print(b + b)
b += b
print(b)

b = Bowl()
b.add_scoops(s1, s2, s2)
b2 = Bowl()
b2.add_scoops(s2, s1, s2)

print('-' * 60)
print(f'{b=}')
print(f'{b2=}')

print(f'b == b2? {b == b2}')
If you're like me, then you might enjoy having a glass with your dinner. 