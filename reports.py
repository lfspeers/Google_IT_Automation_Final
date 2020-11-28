#! /usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, paragraph):
    """Generates a PDF report containing a title sentence and body.
    Report has the following format:
        Processed Update on <Today's date>

        name: Apple
        weight: 500 lbs

        name: Avocado
        weight: 200 lbs

    :param attachment: Filepath of the pdf
    :param title: Title sentence of the report
    :param paragraph: Main body of the report
    :return: None
    """
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    title = Paragraph(title, styles["h1"])
    body = Paragraph(paragraph)
    report.build([title, body])
    return None

