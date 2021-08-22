#!/usr/bin/env python3

import os
import reports
import datetime
import glob
import emails

date = datetime.date.today().strftime('%B %m, %Y')
title = 'Processed Update on ' + date

fruit_info = glob.glob('/supplier-data/descriptions/*.txt')

report_body = []

for file in fruit_info:
    with open(file, 'r') as text_file:
        counter = 0
        for line in text_file:
            counter += 1
            if counter == 1:
                report_body.append('name: ', line, '\n')
            if counter == 2: 
                report_body.append('weight: ', line, '\n')
            if counter == 3:
                report_body.append('\n')
            

if __name__ == "__main__":
    reports.generate_report('/tmp/processed.pdf', title, report_body)
    sender = automation@example.com
    receiver = <username>@example.com
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    message = emails.generate_email(sender, receiver, subject, body, '/tmp/processed.pdf')
    emails.send(message)




            



