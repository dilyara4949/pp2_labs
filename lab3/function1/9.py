'''Write a function that computes the volume of a sphere given its radius.'''

from math import pi
radius = int(input())

volume = lambda x: 4/3 * pi * x ** 3
print(volume(radius))


