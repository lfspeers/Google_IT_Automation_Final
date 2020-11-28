#! /usr/bin/env python3

"""
format:
Processed Update on <Today's date>

name: Apple
weight: 500 lbs

name: Avocado
weight: 200 lbs

"""

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date


def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    title = Paragraph(title, styles["h1"])
    body = Paragraph(paragraph)
    report.build([title, body])

