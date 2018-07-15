#!/usr/bin/env python
# coding=utf-8

import gammu
from sms4you.gateways.gateway import Gateway


class GatewaySms(Gateway):


    def send(self, message):

        sm = gammu.StateMachine()
        sm.ReadConfig()
        sm.Init()

        sms = {
            'Number': message[0],
            'SMSC': {'Location': 1},
            'Text': message[1],
        }

        sm.SendSMS(sms)
        print "sent message via sms to " + message[0]

        sm.Terminate()

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
                    sms = sm.GetNextSMS(Location=location, Folder=0)
                    
                for m in sms:
                    messages.append([m['Number'], m['Text']])

                location = sms[0]['Location']
                remain = remain - len(sms)
                sm.DeleteSMS(Location=location, Folder=0)

        except:
            # This error is raised when we've reached last entry - gammu.ERR_EMPTY
            # It can happen when reported status does not match real counts
            print('Failed to read sms messages!')

        sm.Terminate()
        return messages

