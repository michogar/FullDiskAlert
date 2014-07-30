__author__ = 'michogarcia'

import smtplib
from os import environ
from config import Config

config = Config()

EMAIL_HOST = environ.get('EMAIL_HOST', config.host['host'])
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', config.host['password'])
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', config.host['user'])
EMAIL_PORT = environ.get('EMAIL_PORT', config.host['port'])

class SendMail():

    server=None
    message=""

    def __init__(self, config=None):
        self.server = smtplib.SMTP()
        self.server.connect(EMAIL_HOST, EMAIL_PORT)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)

    def setMessage(self, message=""):
        self.message = message

    def send(self):

        msg = """\From: %s\nTo: %s\nSubject: %s\n\n%s
                """ % (config.email['from'], config.receivers, config.email['subject'], self.message)

        self.server.sendmail(EMAIL_HOST_USER, config.receivers, msg)
        self.server.quit()

