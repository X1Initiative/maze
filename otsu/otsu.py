import numpy as np

from skimage import color, io
from skimage.morphology import disk
from skimage.filters import threshold_otsu, rank
from skimage.util import img_as_ubyte

import sys



PICS = ['imgs/bird.jpg', 'imgs/mazegreen.jpg', 'imgs/building.jpg', 'imgs/diff_colors.jpg']

def run_otsu(image_path):
    # img = color.rgb2gray(io.imread(image_path))
    img = io.imread(image_path, as_grey=True)
    radius = 15
    selem = disk(radius)
    local_otsu = rank.otsu(img, selem)
    threshold_global_otsu = threshold_otsu(img)
    global_otsu = img >= threshold_global_otsu

    x = global_otsu.shape[1]
    y = global_otsu.shape[0]
    global_otsu = global_otsu.tolist()
    for i in xrange(y):
        for j in xrange(x):
            if global_otsu[i][j] == False:
                global_otsu[i][j] = 1
            else:
                global_otsu[i][j] = 0
    global_otsu = np.array(global_otsu)

    return global_otsu