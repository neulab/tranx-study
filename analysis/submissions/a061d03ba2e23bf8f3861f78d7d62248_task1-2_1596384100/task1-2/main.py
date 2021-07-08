# Example code, write your program here
import time

print(time.strftime("%m-%d-%Y %H:%M", time.gmtime(time.time() + 7*24*60*60)))