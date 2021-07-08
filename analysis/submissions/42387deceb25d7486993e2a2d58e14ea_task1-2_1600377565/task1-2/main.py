# Example code, write your program here
from datetime import datetime, timedelta

now = datetime.now()
delta = timedelta(days=7)
res = (now + delta).strftime("%m-%d-%Y %H:%M")
print(res)