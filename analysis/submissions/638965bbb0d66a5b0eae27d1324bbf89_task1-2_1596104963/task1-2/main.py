import datetime
from pytz import timezone


week_date = datetime.datetime.now(timezone('GMT')) + datetime.timedelta(days=7)


print(week_date.strftime('%m-%d-%Y %H:%M'))


