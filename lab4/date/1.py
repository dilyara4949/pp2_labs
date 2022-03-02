'''Write a Python program to subtract five days from current date.'''

import datetime

now = datetime.datetime.now()
fiveDaysAgo = now - datetime.timedelta(days = 5)
print(fiveDaysAgo.strftime("%x"))