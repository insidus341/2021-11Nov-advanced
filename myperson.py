#!/usr/bin/env python3

class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    def greet(self):
        return f'Hello, {self.name}!'

    def __del__(self):  # this method runs *JUST BEFORE* the garbage collector destroys it
        return f'I am dead! {self.name}'


print(f'Before, population = {Person.population}')
p1 = Person('name1')
p2 = Person('name2')

print(f'After, population = {Person.population}')
print(f'After, p1.population = {p1.population}')
print(f'After, p2.population = {p2.population}')

print(p1.greet())
print(p2.greet())
