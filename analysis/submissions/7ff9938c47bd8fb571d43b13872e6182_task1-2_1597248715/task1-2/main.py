# Example code, write your program here
import time

day =int(time.strftime("%d",time.gmtime()))
month = int(time.strftime("%m",time.gmtime()))
year= int(time.strftime("%Y",time.gmtime()))
t=time.strftime("%H:%M",time.gmtime())

day = day+7
if day > 28:
    if month==2:
        day=day-28
        month=3
    elif month == 12 and day > 31:
        day = day - 31
        month = 1
        year += 1
    elif (month == 1 or 3 or 5 or 7 or 8 or 10) and day>31 :
        day=day-31
        month+=1
    elif (month== 4 or 6 or 9 or 11 ) and day>30:
        day=day-30
        month+=1

print(str(day)+"-"+str(month)+"-"+str(year)+" "+t)