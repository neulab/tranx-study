import datetime  
from datetime import timedelta

date_after_week = datetime.datetime.now(datetime.timezone.utc)+ timedelta(days=7)
print(date_after_week.strftime('%m-%d-%y %H:%M'))