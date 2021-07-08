# Example code, write your program here
import datetime
def task1_2():
    dat=datetime.datetime.now().date()
    dat=str(dat)
    year,month,day=(int(x) for x in dat.split("-"))
    tim=datetime.datetime.now().time()
    tim=str(tim)
    hour,min,sec=tim.split(":")
    hour=int(hour)
    min=int(min)

    hour=hour+4
    if hour>=24:
        day=day+1
    hour=hour%24
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%4==0:
        months[1]=29;
    day=day+7
    day1=months[month-1]
    if day>day1:
        day=day-day1
        month=month+1
    if month>12:
        month=month-12
        year=year+1
    print(str(month).zfill(2)+"-"+str(day).zfill(2)+"-"+str(year).zfill(4)+" "+str(hour).zfill(2)+":"+str(min).zfill(2))
    
task1_2()