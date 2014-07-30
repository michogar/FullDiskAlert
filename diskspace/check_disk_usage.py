#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple example command line usage:

Usage: ./check_disk_space.py <percentage free space>

e.g:

$ ./check_disk_space.py 30
Running low on disk space. 20.0% remaining (Warning Threshold: 30%)
Total: 115.13GB
Used:  92.35GB
Avail: 22.77GB

The idea would be to put this in a Cron Job and have it email you when
the free disk space is lower than "n" percent.

"""

import sys

from diskspace import DiskSpace
from mail import SendMail
from config import Config

def main():

    config = Config()
    ds = DiskSpace(path=config.path)

    percent_limit = config.threshold

    if not ds.has_free_space(percent_limit):
    
        message = "Running low on disk space. %s%% remaining "\
           "(Warning Threshold: %s%%)" % (ds.percent_free(), percent_limit) + "\n"
        message += "Total: %s" % ds.humanize_bytes(ds.bytes_capacity(), 1000) + "\n"
        message += "Used:  %s" % ds.humanize_bytes(ds.bytes_used(), 1000) + "\n"
        message += "Avail: %s" % ds.humanize_bytes(ds.bytes_free(), 1000)

        sendMail = SendMail(config)
        sendMail.setMessage(message)
        sendMail.send()

if __name__ == '__main__':
    main()