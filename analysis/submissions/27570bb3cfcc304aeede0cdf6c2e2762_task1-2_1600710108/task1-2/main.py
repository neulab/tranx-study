# Example code, write your program here
from datetime import date
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M")
print(dt_string)