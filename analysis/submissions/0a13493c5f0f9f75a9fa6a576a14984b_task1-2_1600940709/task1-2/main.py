# Example code, write your program here
from time import gmtime, strftime
import datetime
time_now = strftime("%d-%m-%Y %H:%M", gmtime())
tt = ''.join(time_now)
t = datetime.datetime.strptime(tt,"%d-%m-%Y %H:%M")
time_future = t + datetime.timedelta(days=7)
final = time_future.strftime("%d-%m-%Y %H:%M")
print(final)


