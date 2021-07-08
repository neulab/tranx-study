# Example code, write your program here
import datetime

cur_dt = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
end_dt = cur_dt + datetime.timedelta(days=7)
print('{0:%m-%d-%Y %H:%M}'.format(end_dt))
