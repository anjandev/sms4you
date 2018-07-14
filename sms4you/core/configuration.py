# coding=utf-8

import os
import sys


class Configuration(object):
    """The Configuration class validates and prepares configuration data from
    the environment variables for further use in the script.

    """

    def __init__(self):
        """Contructor function

        This function gets called when Configuration object are created.

        Based on the environment variables the configuration is validated and
        prepared all mandatory configuration elements.


        """

        #
        try:
            self.email_username = os.environ.get('SMS4YOU_EMAIL_USERNAME')
        except AttributeError:
            sys.stderr.write(
                "Error: Required environment variable SMS4YOU_EMAIL_USERNAME is not set" + "\n")
            sys.exit()

        if self.email_username == None:
            sys.stderr.write(
                "Error: Required environment variable SMS4YOU_EMAIL_USERNAME is not set" + "\n")
            sys.exit()            

        #
        try:
            self.email_password = os.environ.get('SMS4YOU_EMAIL_PASSWORD')
        except AttributeError:
            sys.stderr.write(
                "Error: Required environment variable SMS4YOU_EMAIL_PASSWORD is not set" + "\n")
            sys.exit()

        if self.email_username == None:
            sys.stderr.write(
                "Error: Required environment variable SMS4YOU_EMAIL_PASSWORD is not set" + "\n")
            sys.exit()

        #
        try:
            self.email_smtp_host = os.environ.get('SMS4YOU_SMTP_HOST')
        except AttributeError:
            sys.stderr.write(
                "Error: Required environment variable SMS4YOU_SMTP_HOST is not set" + "\n")
            sys.exit()

        if self.email_username == None:
            sys.stderr.write(
                "Error: Required environment variable SMS4YOU_SMTP_HOST is not set" + "\n")
            sys.exit()

        self.email_smtp_port = os.getenv('SMS4YOU_SMTP_PORT', 465)

        #
        try:
            self.email_imap_host = os.environ.get('SMS4YOU_IMAP_HOST')
        except AttributeError:
            sys.stderr.write(
                "Error: Required environment variable SMS4YOU_IMAP_HOST is not set" + "\n")
            sys.exit()

        if self.email_username == None:
            sys.stderr.write(
                "Error: Required environment variable SMS4YOU_IMAP_HOST is not set" + "\n")
            sys.exit()

        #
        self.email_imap_port = os.getenv('SMS4YOU_IMAP_PORT', 993)

        #
        try:
            self.target_email = os.environ.get('SMS4YOU_TARGET_EMAIL')
        except AttributeError:
            sys.stderr.write(
                "Error: Required environment variable SMS4YOU_TARGET_EMAIL is not set" + "\n")
            sys.exit()

        if self.email_username == None:
            sys.stderr.write(
                "Error: Required environment variable SMS4YOU_TARGET_EMAIL is not set" + "\n")
            sys.exit()

        # Currently only 'email' is supported. Other protocols such as
        # xmpp or matrix are to be implemented
        self.target_gateway = os.getenv('SMS4YOU_TARGET_GATEWAY', "email")
