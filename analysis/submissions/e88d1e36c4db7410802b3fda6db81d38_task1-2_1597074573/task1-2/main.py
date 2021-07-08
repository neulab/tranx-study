# Example code, write your program here
from datetime import datetime, timedelta
import pytz # $ pip install pytz
#print(str(datetime.now(pytz.timezone("GMT")))[0:26])

dt = datetime.now(pytz.timezone("GMT"))
#print(str(dt))
td = timedelta(days=7)
my_date = dt + td

date_time_str = str(my_date)[0:26]
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

my_month = date_time_obj.month
my_year = date_time_obj.year
my_day = date_time_obj.day
my_hours = date_time_obj.hour
my_minutes = date_time_obj.minute

print(my_month,'-',my_day,'-',my_year,' ', my_hours,':',my_minutes,sep='')



