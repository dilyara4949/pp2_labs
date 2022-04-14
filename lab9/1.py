import datetime as dt, time
a = dt.datetime.now()


print(a.second)


time.sleep(2)
a = dt.datetime.now()
print(a.second )