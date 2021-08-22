#!/usr/bin/env python3

import os
import glob
from PIL import Image

size = 600, 400

files = glob.glob('*.tiff')

for file in files:
    print('file found ' + file)
    print(os.getcwd())
    wrong_picture = Image.open(file).convert('RGB')
    save_path = os.getcwd() + '/' + file[:-5] + '.jpeg'
    print(save_path)
    wrong_picture.resize((size)).save(save_path, 'JPEG')

print('pictures converted')
