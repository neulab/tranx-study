import pytz
import datetime
gmt = pytz.timezone('GMT')
now = datetime.datetime.now(gmt)
print(now.strftime('%m-%d-%Y %H:%M'))
