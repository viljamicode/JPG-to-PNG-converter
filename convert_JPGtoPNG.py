# This is a simple script that uses Pillow (Python Imaging Library fork for python3)
# to convert JPGs to PNGs within a folder.
# You should have Pillow installed. (https://pillow.readthedocs.io/en/stable/installation.html)
# Check README.md for further instructions.

import sys
import os
import time
from PIL import Image


original_image = sys.argv[1]
converted_image = sys.argv[2]

# Checks for output folder and creates it if it doesn't exist
if not os.path.exists(converted_image):
    os.makedirs(converted_image)

start_time = time.time()

# Cleans up the file name(s) by removing ".jpg" and saves the converted image(s)
for filename in os.listdir(original_image):
    img = Image.open(f'{original_image}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{converted_image}{clean_name}.png', 'png')
    print('Image converted to PNG!')

end_time = time.time()

# This prints out how many seconds it took to convert the image(s)
print('This took ', (end_time-start_time), 'seconds')
