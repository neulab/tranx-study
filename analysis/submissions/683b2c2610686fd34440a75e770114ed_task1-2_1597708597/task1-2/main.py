# Example code, write your program here
import datetime

now = datetime.datetime.now()
ans = now + datetime.timedelta(days=7)
current_time = now.strftime("%m-%d-%Y %H:%M")
print(current_time)