'''Write a Python program to calculate the area of regular polygon.
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625'''
import math
n, l = map(int, input().split())
a = l / (2 * math.tan(math.radians(180/n)))           # apothem
area = n * l * a / 2
print(int(area))
