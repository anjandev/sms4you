#!/usr/bin/env bash


# Simple sms send
if [ "$1" == "send" ]; then
    python /sms.py "$@"

# Start sms daemon
elif [ "$1" == "smsd" ]; then
    gammu-smsd "$@"

elif  [ "$1" == "gammu" ]; then
    gammu "$@"

# Run sms4you script
else
    sms4you "$@"
fi


