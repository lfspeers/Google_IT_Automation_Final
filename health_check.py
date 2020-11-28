#!/usr/bin/env python3

import psutil
import socket
import emails

# Check every 60 seconds
# Send email if issue detected
# All tests return Pass: True, Fail: False


def cpu_util():
	cpu_usage = psutil.cpu_percent(interval=0.1)
	if cpu_usage > 80:
		return False
	else:
		return True


def avail_disk():
	disk_remaining = psutil.disk_usage('/')
	if disk_remaining.percent < 20:
		return False
	else:
		return True


def mem_remaining():
	mem = psutil.virtual_memory()
	mem_threshold = 500 * 1024 * 1024
	if mem.available < mem_threshold:
		return False
	else:
		return True


def ip_check():
	localhost_ip = socket.gethostbyname(socket.gethostname())
	if localhost_ip != '127.0.0.1':
		return False
	else:
		return True


if __name__ == '__main__':

	system_checks = [cpu_util, avail_disk, mem_remaining, ip_check]

	failure_messages = {
		'cpu_util': 'Error - CPU usage is over 80%',
		'avail_disk': 'Error - Available disk space is less than 20%',
		'mem_remaining': 'Error - Available memory is less than 500MB',
		'ip_check': 'Error - localhost cannot be resolved to 127.0.0.1'
	}

	for check in system_checks:
		if not check():
			subject = failure_messages[f"{check}"]
			body = 'Please check your system and resolve the issue as soon as possible.'
			message = emails.generate_email(subject=subject, body=body, has_attachment=False)
			emails.send_email(message)

