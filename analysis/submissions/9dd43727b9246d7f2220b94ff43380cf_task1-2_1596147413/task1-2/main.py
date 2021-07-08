# Example code, write your program here
from datetime import datetime
from datetime import timedelta
from dateutil import tz
current_time = datetime.now()
#print(current_time)
time = timedelta(days = 7)
current_time = current_time + time
#print (current_time)
current_time = current_time.strftime("%d-%m-%Y %H:%M")
print (current_time)