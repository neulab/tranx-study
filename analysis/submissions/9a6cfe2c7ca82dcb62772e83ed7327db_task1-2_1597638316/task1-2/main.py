# Example code, write your program here

from datetime import datetime , timedelta
import pytz

# datetime object containing current date and time
now = datetime.now()
timezone = pytz.timezone("GMT")
now_gmt = timezone.localize(now)

one_week = timedelta(days=7)
time_after_aweek = now_gmt + one_week
time_after_aweek_string = time_after_aweek.strftime("%m-%d-%Y %H:%M")
print(time_after_aweek_string)

