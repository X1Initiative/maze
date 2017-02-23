#!/usr/bin/env python
import os,sys
import subprocess
import glob
from os import path
from PIL import Image

f = open('output.txt','w')

# somehow, the image generated from otsu's method is not grayscale so I had to convert it to grayscale
# and save the file.
img = Image.open('bw_maze_mod.png','r')

pixel_value = list(img.getdata()) # pixel_value is a list that contains all the pixel values

print img.format, img.size, img.mode # check size and type of image

width, height = Image.open(open('bw_maze_mod.png')).size
print width*height

print(pixel_value)
f.close()
