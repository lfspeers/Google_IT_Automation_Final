#!/usr/bin/env python3

import os
import requests

url = 'http://localhost/upload/'
image_dir = '/home/student-02-0b808829f77e/supplier-data/images/'


files = [f for f in os.listdir(image_dir) if f.endswith('.jpeg')]
for file in files:
    with open(image_dir+file, 'rb') as f:
        r = requests.post(url, files={'file': f})
