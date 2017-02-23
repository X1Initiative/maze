#!/usr/bin/env python
import os,sys
import subprocess
import glob
from os import path
from PIL import Image

WALL = 1
PATH = 0

f = open('output.txt','w')

# cropped out the maze image that starts with the black border line
img = Image.open('bw_maze_mod.png','r')

pixel_value = list(img.getdata()) # pixel_value is a list that contains all the pixel values
# (0,0,0,255) as black and (255,255,255,255) as white

# set newline each width and convert black(wall) to 1 and white(path) to 0
# save the outputs to output.txt

for i in range(len(pixel_value)):
	if pixel_value[i] == (0,0,0,255):
		pixel_value[i] = WALL
	if pixel_value[i] == (255,255,255,255):
		pixel_value[i] = PATH

width, height = Image.open(open('bw_maze_mod.png')).size
mazesize = width*height
print "width of maze: {}".format(width)
print "height of maze: {}".format(height)
print "total number of pixels: {}".format(mazesize)

for i in range(1/width):
	join(pixel_value[i*width:(i+1)*width]) + "\n"

print >> f, pixel_value
f.close()
