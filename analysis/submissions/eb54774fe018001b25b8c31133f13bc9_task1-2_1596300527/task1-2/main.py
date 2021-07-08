# Example code, write your program here
import datetime
start_date=datetime.date.today()
current_time=datetime.datetime.now().time()
x=start_date+datetime.timedelta(days=7)
print(x.strftime("%m-%d-%y") + " " + str(current_time.hour) + ":" + str(current_time.minute))
