import os
import sys
from PIL import Image

parent_folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(f'.{new_folder}'):
    os.mkdir(f'.{new_folder}')

err_counter = 0
name_list = []

for img in os.listdir(f'.{parent_folder}'):
    path_tuple = os.path.splitext(img)
    if img.endswith('jpg') or img.endswith('JPG'):
        image = Image.open(f'.{parent_folder}/{img}')
        image.save(f'.{new_folder}/{path_tuple[0]}.png', 'png')
    else:
        err_counter += 1
        name_list.append(img)
        continue

for name in name_list:
    print(f'{name} was skipped')

print(f'In total {err_counter} files have been skipped')

