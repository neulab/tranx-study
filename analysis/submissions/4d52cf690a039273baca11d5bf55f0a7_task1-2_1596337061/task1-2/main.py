# Example code, write your program here
import datetime
a_week_from_now = datetime.datetime.now() + datetime.timedelta(days=7)
print(datetime.datetime.strftime(a_week_from_now, '%m-%d-%Y'))