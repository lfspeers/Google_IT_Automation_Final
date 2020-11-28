#! /usr/bin/env python3

import requests
import glob
import re


dir = '/home/student-02-0b808829f77e/supplier-data/descriptions/'


def generate_dict(file):
	fruit_dict = {}
	with open(file, encoding='utf-8') as f:
		fruit_dict['name'] = f.readline().strip()
		weight = f.readline().strip()
		weight = re.sub(r"[^\d]*", '', weight)
		fruit_dict['weight'] = int(weight)
		fruit_dict['description'] = f.readline().strip()
		fruit_dict['image_name'] = file[-7:-4] + '.jpeg'  # f"{a:0=3d}.jpeg"
	return fruit_dict


def post_fruit(fruit_dict):
	url = "http://34.121.140.237/fruits"
	r = requests.post(url, data=fruit_dict)
	print(r.status_code)
	return r


def process_files(dir):
	image_counter = 1
	for file in glob.glob(dir + '*'):
		fruit_dict = generate_dict(file)
		image_counter += 1
		post_fruit(fruit_dict)


def all_fruits_dict():
	all_fruits = {}
	for file in glob.glob(dir + "*"):
		with open(file) as f:
			name = f.readline().strip()
			weight = f.readline().strip()
			all_fruits[name] = weight
	return all_fruits


if __name__ == '__main__':
	process_files(dir)
