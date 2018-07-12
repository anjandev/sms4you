#!/usr/bin/env python
# coding=utf-8

from sms4you.gateways.gateway import Gateway


class GatewaySms(Gateway):

    def send(self, message):
        print "send message via sms"

    def check(self):
        print "check sms messages"
        return {"a", "b"}
