from datetime import datetime, timedelta
print((datetime.utcnow() + timedelta(days=7)).strftime("%m-%d-%Y %H:%M"))