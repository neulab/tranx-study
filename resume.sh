#!/bin/bash

## Start browser monitoring process
if pgrep -x "mitmdump" > /dev/null
then
    echo "Monitoring already running? Killing."
    pkill mitmdump
fi

echo "Starting monitoring."
mitmdump -q --set stream_large_bodies=1 -s /vagrant/browser-request-logger.py &

## Retrieve task and configure & start pycharm
python3 retrieve_assignments.py resume not_used

## log
python3 log_user_event_timeline.py resume