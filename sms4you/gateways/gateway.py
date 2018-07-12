#!/usr/bin/env python
# coding=utf-8


class Gateway(object):

    def __init__(self, config):
        self.config = config

    def __repr__(self):
        rep = ""
        if self.config is not None:
            rep += str(self.config) + " | "
        return rep

    def send(self, message):
        raise NotImplementedError

    def check(self):
        raise NotImplementedError
