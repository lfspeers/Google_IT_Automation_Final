#! /usr/bin/env python3

import glob
import reports
import datetime

dir = '/home/student-02-e77b4fa32e09/supplier-data/descriptions/*'
text = ''

for file in sorted(glob.glob(dir)):
	with open(file) as f:
		text += f"name: {f.readline().strip().title()}<br/>"
		text += f"weight: {f.readline().strip()}<br/><br/>"

if __name__ == '__main__':
	attachment = '/tmp/processed.pdf'
	title = f"Processed Update on {datetime.date.today()}"
	reports.generate_report(attachment, title, paragraph=text)
