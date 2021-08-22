#!/usr/bin/env python3

from requests.sessions import dispatch_hook
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles['h1'])
    report_info = Table(data=paragraph)
    print(report_info)
    report.build([report_title, report_info])
