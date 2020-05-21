import time
import requests
import sys
from retrieve_assignments import read_current_user_task

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Args: msg")
        exit(-1)
    msg = sys.argv[1]

    usi, task = read_current_user_task()
    payload = {
        "local_timestamp": int(time.time()),
        "event_msg": msg,
        "userid": usi,
        "task": task
    }
    requests.post("http://moto.clab.cs.cmu.edu:8081/user_timeline_log", json=payload, timeout=2.0)

