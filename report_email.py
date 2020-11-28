#! /usr/bin/env python3

import glob
import reports
import datetime


def generate_report_body(directory):
	"""Generates the body of the pdf report from the descriptions provided by
	the manufacturer.

	:param directory: The path to the directory of the supplier descriptions
	:return: str text, The main body of the report
	"""
	text = ''
	for file in sorted(glob.glob(directory+'*')):
		with open(file) as f:
			text += f"name: {f.readline().strip().title()}<br/>"
			text += f"weight: {f.readline().strip()}<br/><br/>"
	return text


if __name__ == '__main__':
	directory = '/home/student-02-e77b4fa32e09/supplier-data/descriptions/'
	attachment = '/tmp/processed.pdf'
	title = f"Processed Update on {datetime.date.today()}"
	body = generate_report_body(directory)
	reports.generate_report(attachment, title, paragraph=body)
