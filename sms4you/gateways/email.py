#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import
import sys
import re
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sms4you.gateways.gateway import Gateway


class GatewayEmail(Gateway):

    def send(self, message):

        fromaddr = self.config.email_username
        toaddr = self.config.target_email

        # Prepare email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = message[0]        
        body = message[1]
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP_SSL(self.config.email_smtp_host, self.config.email_smtp_port)
        server.login(self.config.email_username, self.config.email_password)
        server.sendmail(self.config.email_username, self.config.target_email, msg.as_string())

        # Close smtp server
        server.quit()

    def check(self):

        messages = []

        # Open connection to IMAP server
        imap = imaplib.IMAP4_SSL(self.config.email_imap_host, self.config.email_imap_port)
        
        # Login and get list of unread emails
        try:
            imap.login(self.config.email_username, self.config.email_password)
            imap.select('INBOX')
            status, response = imap.uid('search', None, 'UNSEEN')
            unread_msg_nums = response[0].split()
        except imaplib.IMAP4.error, e:
            sys.stderr.write(str(e) + "\n")
            sys.stderr.write("Error: Failed to check emails" + "\n")

        # Fetch email contents
        if (unread_msg_nums):       
            messages = []
            for e_id in unread_msg_nums:
                _, response = imap.uid('fetch', e_id, '(BODY[1] BODY[HEADER.FIELDS (SUBJECT)])')
                messages.append([response[1][1], response[0][1]])

        # Format email contents
        messages = self._format_messages(messages)

        # Close imap server session
        imap.logout()

        # Return the formatted messages
        return (messages)

    def _format_messages(self, messages):

        # Clean up phone number
        # Send email back in case of problems

        return messages