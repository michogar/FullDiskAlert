=============
FullDiskAlert
=============

A simple script to check if you hard disk is full.

To configure
============
Do your changes in the config.yaml::

    path: / # Path to monitored partition
    threshold: 80 # Value of alarm, if disk space is over the value, then sends alarm
    receivers: # YAML array with receivers
        - fake@fakemail.fake
        - one_more@mail.com
    email:
        from: From fake # Mail from
        subject: Full disk alert!! # Mail subject
    host: # Mail server data (preconfigured to use Gmail)
        host : smtp.gmail.com
        password : fakepass
        user : fake@fakemail.fake
        port : 587

To use
======
The best choice to use this is creating a cron::

    crontab -e
    */30 * * * * /path/to/check_disk_usage.py

This cron executes this every 30 minutes