# Example code, write your program here
from datetime import datetime as dt
from datetime import timedelta, timezone
fmt = '%m-%d-%Y %H:%M'
print(dt.strftime(dt.now(tz = timezone.utc)+timedelta(days=7), fmt))
