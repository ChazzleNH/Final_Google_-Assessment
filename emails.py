#!/usr/bin/env python3

import email.message
import smtplib
import mimetypes
import os.path 

''' the script to be imported so the emails can be generated sent after the reports are generated '''

def generate_email(sender, receiver, subject, body, attachment_path):

    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.set_content(body)

    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=os.path.basename(attachment_path))

    return message

def generate_error_email(sender, receiver, subject, body):

    message = email.message.EmailMessage()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.set_contect(body)

    return message

def send(message):

    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
