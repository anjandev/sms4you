# coding=utf-8

import sys
import importlib


class GatewayFactory(object):

    def __init__(self, config):
        self.config = config
        self.selector = self.config.target_gateway

    def __repr__(self):
        rep = ""
        if self.config is not None:
            rep += str(self.config) + " | "
        if self.selector is not None:
            rep += self.selector
        return rep

    def get_sms_gateway(self):
        selector = "sms"
        try:
            module = importlib.import_module(
                ".gateways." + selector, package="sms4you")
            sms_gateway = getattr(
                module, "Gateway" + selector.capitalize())
            return sms_gateway(self.config)
        except ImportError:
            sys.stderr.write(
                "Error: No gateway found for " + selector + "\n")
            sys.exit()

    def get_you_gateway(self):
        selector = self.selector

        try:
            module = importlib.import_module(
                ".gateways." + selector, package="sms4you")
            you_gateway = getattr(
                module, "Gateway" + selector.capitalize())
            return you_gateway(self.config)
        except ImportError:
            sys.stderr.write(
                "Error: No gateway found for " + selector + "\n")
            sys.exit()
