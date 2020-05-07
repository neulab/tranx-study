#!/bin/bash

if [ "$#" -ne 3 ]
  then
    echo "Usage: ./start-task.sh USERID TASK USE_PLUGIN(0 or 1)"
    exit -1
fi

## Clear up any previous leftover logs
rm -f /vagrant/timeline.log

## Start browser monitoring process
if pgrep -x "mitmdump" > /dev/null
then
    echo "Monitoring already running? Maybe an ERROR."
else
    echo "Starting monitoring"
    ## Clear up any previous leftover logs
    rm -f /vagrant/browser_requests.log
    /usr/local/bin/mitmdump -q --set stream_large_bodies=1 -s /vagrant/browser-request-logger.py &
fi

python3 manual.py $1 ${2%/} $3

## log
TIMESTAMP=`date +"%s"`
echo -e "${TIMESTAMP}\tTask started" >> /vagrant/timeline.log
