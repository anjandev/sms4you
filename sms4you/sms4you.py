#!/usr/bin/env python
# coding=utf-8

import sys
import argparse
from dotenv import load_dotenv
from core.configuration import Configuration
from core.gateway_factory import GatewayFactory

load_dotenv(dotenv_path='.env', verbose=True)

# Handle arguments
parser = argparse.ArgumentParser(
    prog='sms4you', description='Send and reveive SMS via an email account.')
group = parser.add_mutually_exclusive_group()
group.add_argument(
    '--you2sms', action="store_true", help='Only check for new emails and send out sms.')
group.add_argument(
    '--sms2you', action="store_true", help='Only check for new sms and send out emails.')
args = parser.parse_args()


def main():

    # Load, prepare and validate configuration
    config = Configuration()

    # Initiate gateways for communication through an object factory
    factory = GatewayFactory(config)
    sms_gateway = factory.get_sms_gateway()
    you_gateway = factory.get_you_gateway()

    # Check if the flag to only run one direction is set.
    # If nothing is set, both will run (default behaviour).
    if args.you2sms:
        _you2sms(sms_gateway, you_gateway)
    elif args.sms2you:
        _sms2you(sms_gateway, you_gateway)
    else:
        _sms2you(sms_gateway, you_gateway)
        _you2sms(sms_gateway, you_gateway)

    sys.exit()


def _you2sms(sms_gateway, you_gateway):

    # Check sms for new messages, loop through them and send one email for each.
    for message in you_gateway.check():
        sms_gateway.send(message)


def _sms2you(sms_gateway, you_gateway):

    # Check emails for new messages, loop through them and send one sms for each.
    for message in sms_gateway.check():
        you_gateway.send(message)


if __name__ == "__main__":
    main()
