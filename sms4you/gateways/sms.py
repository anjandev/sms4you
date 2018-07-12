#!/usr/bin/env python
# coding=utf-8

import gammu
from sms4you.gateways.gateway import Gateway


class GatewaySms(Gateway):


    def send(self, message):

        print "num: " + message[0]
        print " -- text: " + message[1]
        
        sm = gammu.StateMachine()
        sm.ReadConfig()
        sm.Init()

        sms = {
            'Text': message[1],
            'SMSC': {'Location': 1},
            'Number': message[0],
        }

        sm.SendSMS(sms)
        print "send message via sms to " + message[0]

    def check(self):

        print "check sms messages"

        messages = []

        sm = gammu.StateMachine()
        sm.ReadConfig()
        sm.Init()

        status = sm.GetSMSStatus()

        remain = status['SIMUsed'] + status['PhoneUsed'] + status['TemplatesUsed']

        start = True

        try:
            while remain > 0:
                if start:
                    sms = sm.GetNextSMS(Start=True, Folder=0)
                    start = False
                else:
                    sms = sm.GetNextSMS(
                        Location=sms[0]['Location'], Folder=0
                    )
                remain = remain - len(sms)

                for m in sms:
                    messages.append([m['Number'], m['Text']])

        except:
            # This error is raised when we've reached last entry - gammu.ERR_EMPTY
            # It can happen when reported status does not match real counts
            print('Failed to read sms messages!')

        return messages

