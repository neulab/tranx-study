#!/bin/bash

STUDY_CONFIG_FILE="/vagrant/.user_study_current_status"
if [[ ! -f $STUDY_CONFIG_FILE ]]
then
    echo "ERROR: study config file not found!"
    exit 1
fi

readarray -t line < $STUDY_CONFIG_FILE

USERID=${line[0]}
TASKNAME=${line[1]}

if [ ! -d $TASKNAME ]; then
    echo "Task directory $TASKNAME does not exist!"
    exit 1
fi

echo "UserID: $USERID"
echo "Task directory: $TASKNAME"
echo "Zipping..."


TIMESTAMP=`date +"%s"`

ZIPNAME="${USERID}_${TASKNAME%/}_${TIMESTAMP}.zip"

## stop web monitoring
pkill mitmdump
## stop pycharm
pkill java
## stop keylogging
if pgrep -f "keylogger.py" > /dev/null
then
    kill $(pgrep -f keylogger.py)
fi

sleep 1

pushd $TASKNAME
rm -f pycharm.log
popd

cp pycharm.log $TASKNAME

zip -r $ZIPNAME $TASKNAME

echo "Submitting $ZIPNAME"

STATUS=`curl -s -o /dev/null -w "%{http_code}" -F "file=@${ZIPNAME}" http://moto.clab.cs.cmu.edu:8081/task_submission`

if [ $STATUS -eq 200 ]; then
    echo "Submission success! Please complete the following post-task survey:"
    python3 post_task_study.py
    ## log
    python3 log_user_event_timeline.py submit_success
else
    echo "Submission failed! Check your UserID or Internet connection, or maybe you have already submitted this task."
    ## log
    python3 log_user_event_timeline.py submit_failed
fi

echo "Clean up..."
rm -f $ZIPNAME

