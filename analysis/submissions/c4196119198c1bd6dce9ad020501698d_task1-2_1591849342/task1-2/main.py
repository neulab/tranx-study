# Example code, write your program here

from datetime import datetime, timedelta

now = datetime.now()
d = timedelta(weeks=1)

one_week_later = now + d
print((one_week_later.strftime('%m-%d-%Y %H:%M')))


