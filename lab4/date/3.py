'''Write a Python program to drop microseconds from datetime.'''

from datetime import datetime

now = datetime.now()

print(now.strftime("%x  %X"))