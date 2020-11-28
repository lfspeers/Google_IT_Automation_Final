#!/usr/bin/env python3
from PIL import Image
import os


def reformat_image(directory, dimensions):
    """Reformats all of the tiff image files in the provided directory and changes
    them into 600x400 JPEGs. Functionality could be improved with glob.

    :param directory: path to the directory of tiff images
    :param dimensions: desired dimensions of the reformatted image
    :return: None
    """
    for file in os.listdir(directory):
        if f"{file}".lower().endswith('.tiff'):
            try:
                with Image.open(directory + file) as im:
                    im.convert('RGB').resize(dimensions).save(directory + file[:-5] + '.jpeg', "JPEG")
            except OSError:
                print('cannot open', im)
    return


if __name__ == '__main__':
    image_directory = '/home/student-02-0b808829f77e/supplier-data/images/'
    dim = (600, 400)
    reformat_image(image_directory, dim)
