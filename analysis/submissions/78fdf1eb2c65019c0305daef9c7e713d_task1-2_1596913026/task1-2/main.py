# Example code, write your program here

import time
import datetime

def Date():
    result = datetime.date.today()
    week = datetime.timedelta(days=7)
    result = result + week
    print(result.strftime("%m-%d-%Y"),end=' ')
    print(time.strftime("%H:%M", time.gmtime()))
    return
if __name__ == '__main__':
    Date()