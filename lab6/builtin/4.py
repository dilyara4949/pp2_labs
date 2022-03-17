import time
num = int(input())
ms = int(input())


time.sleep(ms/1000)
print(f'Square root of {num} after {ms} miliseconds is {num**0.5}')
