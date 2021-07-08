# Example code, write your program here
import datetime

current_timestamp = datetime.datetime.now()
end_timestamp = current_timestamp + datetime.timedelta(days=7)
print(datetime.datetime.strftime(end_timestamp, '%m-%d-%Y %H:%M'))