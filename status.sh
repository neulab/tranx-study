#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: ./status.sh USERID"
    exit -1
fi

python3 retrieve_assignments.py show $1
