#!/usr/bin/env python3

import glob
from PIL import Image

size = 600, 400

files = glob.glob('*.TIFF')

for file in files:
    wrong_picture = Image.open(file).convert('RGB')
    wrong_picture.resize((size)).save('/supplier-data/images' + file, 'JPEG')    

print('pictures converted')
