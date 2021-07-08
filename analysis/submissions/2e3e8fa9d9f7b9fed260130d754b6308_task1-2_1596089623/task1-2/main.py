# Example code, write your program here
from datetime import datetime
from pytz import timezone
gmt=timezone('GMT')
day=datetime.now(gmt)
try:
    week=datetime(day.year,day.month,day.day+7,day.hour,day.minute,day.second)
except:
    week = datetime(day.year, day.month+1, day.day + 7-30, day.hour, day.minute, day.second)
print("{:02d}-{:02d}-{:02d}".format(week.month,week.day,week.year),end=' ')
if day.strftime("%p")=="PM":
    print("{:02d}:{:02d}".format(day.hour+12,day.minute))
else:
    print("{:02d}:{:02d}".format(day.hour, day.minute))