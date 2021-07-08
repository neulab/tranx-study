# Example code, write your program here

from datetime import timedelta, datetime
datee = datetime.utcnow()+timedelta(days=7)
print(datee.strftime('%m-%d-%Y %H:%M '))

