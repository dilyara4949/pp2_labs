'''Write a Python program to calculate the area of a trapezoid.
Height: 5
Base, first value: 5
Base, second value: 6
Expected Output: 27.5'''

import math
h, b1, b2 = map(float, input().split())
print((b1 + b2)/2 * h)