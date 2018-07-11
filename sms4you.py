#!/usr/bin/env python
# coding=utf-8

import os
import sys
import argparse


# Handle arguments
parser = argparse.ArgumentParser(
    prog='sms4you', description='Send and reveive SMS via an email account.')
group = parser.add_mutually_exclusive_group()
group.add_argument('--you2sms', action="store_true",
                help='Only check for new emails and send out sms.')
group.add_argument('--sms2you', action="store_true",
                help='Only check for new sms and send out emails.')
args = parser.parse_args()


def main():

    # Check if the flag to only run one direction is set.
    # If nothing is set, both will run (default behaviour).

    config = {}

    if args.you2sms:
        _you2sms(config)
    elif args.sms2you:
        _sms2you(config)
    else:
        _sms2you(config)
        _you2sms(config)

    # TODO: Shut off the state_machine
    sys.exit()


def _you2sms(config):

    # Check sms for new messages, loop through them and send one email for each.
    for message in _check_messages_of('you'):
        _send_message_to('sms', message)


def _sms2you(config):

    # Check emails for new messages, loop through them and send one sms for each.
    for message in _check_messages_of('sms'):
        _send_message_to('you', message)


def _send_message_to(gateway, message):
    print "send message to " + gateway


def _check_messages_of(gateway):
    print "check messages of " + gateway
    return {'a', 'b'}


if __name__ == "__main__":
    main()
