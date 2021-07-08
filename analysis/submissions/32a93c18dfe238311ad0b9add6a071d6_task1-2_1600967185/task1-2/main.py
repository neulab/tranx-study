# Example code, write your program here
import datetime
from datetime import datetime, timedelta

d = datetime.today() + timedelta(days=7)
d = d.strftime('%m-%d-%Y %H:%M')

print(d)
