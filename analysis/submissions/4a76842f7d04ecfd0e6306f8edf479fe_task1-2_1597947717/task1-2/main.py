# Example code, write your program here
from datetime import datetime
import datetime
datee = datetime.datetime.utcnow()+ datetime.timedelta(days=7)
new_date = datetime.datetime.strftime(datee, "%m-%d-%Y %H:%M")
print(new_date)


