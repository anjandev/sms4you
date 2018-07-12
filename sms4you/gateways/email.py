#!/usr/bin/env python
# coding=utf-8

from sms4you.gateways.gateway import Gateway


class GatewayEmail(Gateway):

    def send(self, message):
        print "send message via email"

    def check(self):
        print "check email messages"
        return {"a", "b"}
