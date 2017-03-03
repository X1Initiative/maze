#!/usr/bin/env python
import os,sys
import subprocess
import glob
import numpy as np
from os import path
from PIL import Image

WALL = 1
PATH = 0

f = open('output.txt','w')

# open (cropped out) maze image that starts with the black border line
img = Image.open('bw_maze_mod.png','r')

pixel_value = list(img.getdata()) # pixel_value is a list that contains all the pixel values
# (0,0,0,255) as black and (255,255,255,255) as white
# while for some values are not dead on (0,0,0,255) or (255,255,255,255), any value that is
# not (0,0,0,255) will be considered as black(WALL)

# set newline each width and convert black(wall) to 1 and white(path) to 0
# save the outputs to output.txt

for i in range(len(pixel_value)):
	if pixel_value[i] == (0,0,0,255):
		pixel_value[i] = WALL
        elif pixel_value[i] == (255,255,255,255):
		pixel_value[i] = PATH
        else:
                pixel_value[i] = PATH

# scale down the number of 0s and 1s to a single 0 or 1 value. (50:1 ratio)
#for i in len(pixel_value[i]):
#    for num in 0 ...
zeroCount = 0;
oneCount = 0;


width, height = Image.open(open('bw_maze_mod.png')).size
mazesize = width*height

# create to a 2d array from original list
# 2d array based on (width x height) size
listed = np.array(pixel_value).reshape(width, height)

print "width of maze: {}".format(width)
print "height of maze: {}".format(height)
print "total number of pixels: {}".format(mazesize)

for i in range(1/width):
	join(listed[i*width:(i+1)*width]) + "\n"

print >> f, listed
f.close()
