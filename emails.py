#! /usr/bin/env python3

from email.message import EmailMessage
import os.path
import mimetypes
import smtplib


def generate_email(sender, recipient, subject, body, has_attachment=True):
	"""Creates an email message with the sender, recipient, subject, body, and possible attachment.

	:param str sender:
	:param str recipient:
	:param str subject:
	:param str body:
	:param bool has_attachment:
	:return: email.message.EmailMessage: A string representation of the email
	"""

	message = EmailMessage()
	message['From'] = sender
	message['To'] = recipient
	message['Subject'] = subject
	message.set_content(body)

	if has_attachment:
		attachment_path = '/tmp/processed.pdf'
		attachment_filename = os.path.basename(attachment_path)
		mime_type, _ = mimetypes.guess_type(attachment_path)
		mime_type, mime_subtype = mime_type.split('/', 1)
		with open(attachment_path, 'rb') as att:
			message.add_attachment(
								att.read(),
								maintype=mime_type,
								subtype=mime_subtype,
								filename=attachment_filename
								)

	return message


def send_email(message):
	"""Sends the EmailMessage provided through the localhost mail server.

	:param email.message.EmailMessage message: Formatted contents of email
	:return: None
	"""
	mail_server = smtplib.SMTP('localhost')
	mail_server.send_message(message)
	return


if __name__ == "__main__":
	sender = 'automation@example.com'
	recipient = 'student-02-e77b4fa32e09@example.com'
	subject = 'Upload Completed - Online Fruit Store'
	body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

	message = generate_email(sender, recipient, subject, body)
	send_email(message)
