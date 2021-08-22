#!/usr/bin/env python3

import requests
import glob

url = 'http://<IP>/upload/'
images = glob.glob('*.JPEG')

for image in images:
    with open(image, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
        print('image uploaded')
