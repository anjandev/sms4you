#!/usr/bin/env bash

# Run sms4you once
if [ "$1" == "execute" ]; then
    sms4you "$@"

# Start sms4you "daemon"
elif [ "$1" == "daemon" ]; then

    # start cron
    service cron start

    # trap SIGINT and SIGTERM signals and gracefully exit
    trap "service cron stop; kill \$!; exit" SIGINT SIGTERM

    # start "daemon"
    while true
    do
        # watch /var/log/cron.log restarting if necessary
        cat /var/log/cron.log & wait $!
    done

# Simple sms send (for testing purposes)
elif [ "$1" == "send" ]; then
    python /sms.py "$@"

# Execute gammu directly (for testing purposes)
elif  [ "$1" == "gammu" ]; then
    gammu "$@"

else
    echo "FAILED: No valid command found."
fi
