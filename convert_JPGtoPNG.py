# This is a simple script that uses Pillow (Python Imaging Library fork for python3)
# to convert JPGs to PNGs within a folder.
# To run:
# 1.  Open the cmd/terminal to the folder where "convert_JPGtoPNG.py" is
#     and make sure it has a subfolder with the JPG/JPGs that you wish to convert to PNG.
# 2.  Type: "python convert_JPGtoPNG.py 'existing_images_folder/' 'new_images_folder/'" with no quotation marks.
# 2.5.Change "existing_images_folder" and "new_images_folder" to the correct folder names.
#     The output folder doesn't have to be an existing folder, since the script will create it with the name
#     that you have written into the cmd/terminal (for example "new_images_folder").
# 3.  Press ENTER and your JPG images have been converted into PNGs and saved in the new folder.

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
