import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np

from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
from skimage.util import img_as_ubyte

import sys

def average_gs(pixel):
    return (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3
def weighted_average_gs(pixel):
    return 0.299*int(pixel[0]) + 0.587*int(pixel[1]) + 0.114*int(pixel[2])
def convert_to_gs(image, weighted=False):
    grey = np.zeros((image.shape[0], image.shape[1])).astype(np.uint8)
    for r in range(len(image)):
        for c in range(len(image[r])):
            if weighted:
                grey[r][c] = weighted_average_gs(image[r][c])
            else:
                grey[r][c] = average_gs(image[r][c])
    return grey

PICS = ['imgs/bird.jpg', 'imgs/mazegreen.jpg']
if len(sys.argv) == 1:
    pic = PICS[0]
elif int(sys.argv[1]) >= len(PICS):
    print("Please use a picture number 0 through %i" % (len(PICS)-1))
    sys.exit(0)
else:
    pic = PICS[int(sys.argv[1])]

matplotlib.rcParams['font.size'] = 9

PICS = ['imgs/bird.jpg', 'imgs/mazegreen.jpg']
img_orig = mpimg.imread(pic)
img = convert_to_gs(img_orig)

radius = 15
selem = disk(radius)

local_otsu = rank.otsu(img, selem)
threshold_global_otsu = threshold_otsu(img)
global_otsu = img >= threshold_global_otsu


imgplot = plt.imshow(img_orig)
plt.show()
imgplot = plt.imshow(local_otsu, cmap=plt.cm.gray)
plt.show()
imgplot = plt.imshow(img >= local_otsu, cmap=plt.cm.gray)
plt.show()
imgplot = plt.imshow(global_otsu, cmap=plt.cm.gray)
plt.show()

