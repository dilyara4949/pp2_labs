'''Write a Python program to print yesterday, today, tomorrow.'''
import datetime
now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days = 1)
tomorrow = now + datetime.timedelta(days = 1)
print(yesterday.strftime("%x"), now.strftime("%x"), tomorrow.strftime("%x"), sep = '\n')