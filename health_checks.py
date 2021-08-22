#!/usr/bin/env python3

import psutil
import shutil
import socket
import emails

sender = automation@example.com
receiver = <username>@example.com
body = 'Please check your system and resolve the issue as soon as possible.'

cpu_prcnt = psutil.cpu_percent(1)

if cpu_prcnt > 80:
    subject = 'Error - CPU usage is over 80%'
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send(message)

disk_used = shutil.disk_usage('/')
disk_prcnt = disk_used.free/disk_used.total * 100

if disk_prcnt > 20:
    subject = 'Error - Available disk space is less than 20%'
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send(message)

ram = psutil.virtual_memory()
if ram < 524288000:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send(message)


hostname = socket.gethostbyname('localhost')
if hostname != '127.0.0.1':
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send(message)
