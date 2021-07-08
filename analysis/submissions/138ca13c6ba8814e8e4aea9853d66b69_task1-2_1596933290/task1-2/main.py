# Print datetime in some specified format (mm-dd-yyyy hh:mm)
from datetime import datetime
now = datetime.now()
print(now.strftime("%m-%d-%Y %H:%M"))