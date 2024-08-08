import filecmp
import os

all_images = os.listdir('images')

for img in all_images:
    if pic != '1.png':
        if filecmp.cmp("1.png",img):
            os.remove(img)
            print('remove')
        else:
            print('Not Similar')