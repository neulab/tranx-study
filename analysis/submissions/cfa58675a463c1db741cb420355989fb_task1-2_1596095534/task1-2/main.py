# Example code, write your program here

from datetime import datetime, timezone,  timedelta
import pytz

fmt = '%m-%d-%Y %H:%M'

tz = pytz.timezone('GMT')
d = datetime.now(tz)

print(d.strftime(fmt))
