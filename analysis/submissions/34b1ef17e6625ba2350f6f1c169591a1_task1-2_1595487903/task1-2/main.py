# Example code, write your program here
from datetime import timedelta, datetime
import time

current_date = time.gmtime()

x = datetime(
    current_date.tm_year,
    current_date.tm_mon,
    current_date.tm_mday,
    current_date.tm_hour,
    current_date.tm_min)
days_after = x + timedelta(days=7)

print(days_after.strftime("%m-%d-%Y %I:%M"))