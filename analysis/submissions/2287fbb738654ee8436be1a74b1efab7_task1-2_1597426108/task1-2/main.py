# ---- BEGIN AUTO-GENERATED CODE ----
# ---- nok5dakwkdcr5b4jq7fh452d0 ----
# query: print date and time in GMT in 24hr format
# to remove these comments and send feedback press alt-G
import parser
from time import gmtime, strftime
import datetime

Enddate = datetime.date.today() + datetime.timedelta(days=7)
formattedDate = datetime.date.strftime(Enddate, "%m/%d/%Y")
print(formattedDate)
print(strftime('%H:%M:%S', gmtime()))
# ---- END AUTO-GENERATED CODE ----
