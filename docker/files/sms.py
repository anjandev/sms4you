#!/usr/bin/env python
# coding=utf-8

import sys
import gammu

sm = gammu.StateMachine()
sm.ReadConfig()
sm.Init()

message = {
    'Text' : sys.argv[3],   
    'SMSC': {'Location': 1},   
    'Number': sys.argv[2],  
}

print "Sending the following message to " + sys.argv[2] + ": " + sys.argv[3]

sm.SendSMS(message)