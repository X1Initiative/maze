#!/usr/bin/env python
import os,sys
import subprocess
import glob
import numpy as np
np.set_printoptions(threshold=np.inf)
from os import path
from PIL import Image

WALL = 1
PATH = 0

"""
main function
"""
def main():
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
    	if pixel_value[i] == (255,255,255,255):
	    pixel_value[i] = PATH
        elif pixel_value[i] == (0,0,0,255):
	    pixel_value[i] = WALL
        else:
            pixel_value[i] = WALL

    width, height = Image.open(open('bw_maze_mod.png')).size
    mazesize = width*height

    # create to a 2d array from original 1d list
    # 2d array based on (width x height) size
    listed = np.array(pixel_value).reshape(height, width)

    print "original width and height of maze"
    print "height of maze: {}".format(height)
    print "width of maze: {}".format(width)
    print "total number of pixels: {}".format(mazesize)

    # scale down the number of 0s and 1s to a single value (roughly 30:1 ratio but optimize it)
    zeroCount = 0;
    oneCount = 0;
    
    """
    This is where optimization/simplification code goes
    Basic idea is that every sequence of 30 1s will be replaced as one 1
    Any sequence less than 30 will also be replace as one 1, but the first condition comes first
    Same goes for 0, every sequence of 30 0s will be replaced as one 0 and any sequence less than 
    30 0s will also be replaced as one 0.
    """
    
    numrows = len(listed)
    numcols = len(listed[0])
    print "number of 1s: {}".format(oneCount)
    print "number of 0s: {}".format(zeroCount)
    print "updated width and height of maze"
    print "width of maze: {}".format(numrows)
    print "height of maze: {}".format(numcols)
    print >> f, listed
    f.close()

if __name__ == "__main__":
    main()
