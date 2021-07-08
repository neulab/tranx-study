# Example code, write your program here
from datetime import date
from datetime import datetime
import os
from datetime import timedelta


os.environ['TZ'] = 'IDL'
datetime=datetime.utcnow() + timedelta(days=7)
today=datetime.date()
time=datetime.time()
print(today.strftime("%m-%d-%Y"),end=" ")
print(time.strftime("%H:%M"))



