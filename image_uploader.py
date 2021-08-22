#!/usr/bin/env python3

import requests
import glob

url = 'http://34.135.87.136/upload/'
images = glob.glob('*.jpeg')

for image in images:
    with open(image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
        print('image uploaded')
