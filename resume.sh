#!/bin/bash

## Start browser monitoring process
if pgrep -x "mitmdump" > /dev/null
then
    echo "Monitoring already running"
else
    echo "Starting monitoring"
    /usr/local/bin/mitmdump -q --set stream_large_bodies=1 -s /vagrant/browser-request-logger.py &
fi

## Retrieve task and configure & start pycharm
python3 retrieve_assignments.py resume not_used

## log
TIMESTAMP=`date +"%s"`
echo -e "${TIMESTAMP}\tTask resumed" >> /vagrant/timeline.log
