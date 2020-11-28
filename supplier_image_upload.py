#!/usr/bin/env python3

import os
import requests


def upload_supplier_images(url, image_dir):
    """Uploads the reformatted jpeg images to the Django server on localhost.
    Readability could be improved with glob.

    :param url: Supplier image uploader API (provided in Qwiklabs)
    :param image_dir: Directory of the supplier data images
    :return: int: the status code of the request
    """
    files = [f for f in os.listdir(image_dir) if f.endswith('.jpeg')]
    for file in files:
        with open(image_dir+file, 'rb') as f:
            r = requests.post(url, files={'file': f})
    return r.status_code


if __name__ == '__main__':
    url = 'http://localhost/upload/'
    image_dir = '/home/student-02-0b808829f77e/supplier-data/images/'
