#!/usr/bin/env python3

from PIL import Image
import os

dir = '/home/student-02-0b808829f77e/supplier-data/images/'

dim = (600, 400)

for file in os.listdir(dir):
    if f"{file}".lower().endswith('.tiff'):
        with Image.open(dir + file) as im:
            im.convert('RGB').resize(dim).save(dir + file[:-5] + '.jpeg', "JPEG")
