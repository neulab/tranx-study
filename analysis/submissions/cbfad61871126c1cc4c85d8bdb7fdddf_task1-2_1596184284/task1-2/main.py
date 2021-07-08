import datetime

print((datetime.datetime.utcnow() + datetime.timedelta(days=7)).strftime("%m-%d-%Y %H:%M"))
