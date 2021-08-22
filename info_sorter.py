#!/usr/bin/env python3

import os
from PIL import Image
import requests
import glob
from pathlib import Path

fruit_info = {}
text_files = glob.glob('*.txt')

for files in text_files:
    with open(files, 'r') as file:
        counter = 0
        filename = Path(file).stem
        imagename = (filename + '.JPEG')
        for line in file:
            counter += 1
            if counter == 1:
                fruit_info['name'] = line
            if counter == 2:
                weight = line[:-3]
                fruit_info['weight'] = int(weight)
            if counter == 3:
                fruit_info['description'] = line
                fruit_info['image_name'] = imagename
                response = requests.post(r'http://<IP>/fruit', data=fruit_info)
                print('Response', response_status_code) 

