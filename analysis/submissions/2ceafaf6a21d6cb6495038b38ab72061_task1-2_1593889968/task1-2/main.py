# Example code, write your program here
from datetime import datetime, timedelta
time = datetime.today() + timedelta(days=7, hours=4)
time = time.strftime('%m-%d-%Y %H:%M')
print(time)
