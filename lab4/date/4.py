'''Write a Python program to calculate two date difference in seconds.'''
import datetime as dt
a = dt.datetime.now()
b = dt.datetime(2020, 4, 17, 13, 35, 59)

print((a-b).seconds + (a-b).days * 24 * 3600)


