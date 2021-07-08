# Example code, write your program here
import datetime

dt = datetime.datetime.now() + datetime.timedelta(weeks=1)
print(dt.strftime("%m-%d-%y %H:%M"))
