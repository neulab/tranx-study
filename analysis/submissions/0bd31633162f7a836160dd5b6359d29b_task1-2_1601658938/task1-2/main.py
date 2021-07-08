# Example code, write your program here
import datetime

today_date = datetime.datetime.utcnow().date()
today_time = datetime.datetime.utcnow().time()

from datetime import datetime, timedelta
d = datetime.today() - timedelta(days=7)



print(str(d.month) + "-" + str(d.day) + "-" + str(d.year) + " " + str(today_time.hour) +":"+str(today_time.minute))
