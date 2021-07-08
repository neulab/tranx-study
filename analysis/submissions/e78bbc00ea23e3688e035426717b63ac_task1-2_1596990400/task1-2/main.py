# Example code, write your program here
from datetime import date, datetime, timedelta, time

#Find the date a week from now(wfn)
today = datetime.now()
week = timedelta(days=7)
wfn = today + week

#Find the GMT time
now = datetime.now()
hours = timedelta(hours=4)
gmt = now + hours

#Display the date and time in the correct format
print(wfn.strftime("%m-%d-%Y") + ' ' + gmt.strftime("%H:%M"))

