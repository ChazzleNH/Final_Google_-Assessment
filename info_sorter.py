#!/usr/bin/env python3

import os
from PIL import Image
import requests
import glob
from pathlib import Path

text_files = glob.glob('*.txt')

for files in text_files:
    fruit_info = {}
    with open(files, 'r') as file:
        counter = 0
        filename = files[:-4]
        imagename = (filename + '.jpeg')
        for line in file:
            counter += 1
            if counter == 1:
                fruit_info['name'] = line[:-1]
            if counter == 2:
                weight = line[:-5]
                fruit_info['weight'] = int(weight)
            if counter == 3:
                fruit_info['description'] = line[:-1]
                fruit_info['image_name'] = imagename
                print(fruit_info)
                url = 'http://34.72.122.216/fruits/'
                response = requests.post(url, data = fruit_info)
                print('Response', response.status_code) 

