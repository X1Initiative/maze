#!/usr/bin/env python
import os,sys
import subprocess
import glob
import numpy as np
import pprint

from os import path
from PIL import Image

np.set_printoptions(threshold=np.inf)

WALL = 1
PATH = 0

ERROR_MARGIN = 0.2
WIDTH_MARGIN = 0.85

def get_starting_coords(maze):
    """Gets the top left and top right coords of the exit point at the top of the maze.
        Uset to calculate the width.
    """
    cols = maze.shape[1]
    x0 = None
    x1 = None
    for i in xrange(cols):
        if maze[0][i] == PATH:
            if x0 == None:
                x0 = i
        elif x0 is not None:
            x1 = i
            return x0, 0, x1, 0
    return 0, 0, 0, 0

def condense(maze, margin=WIDTH_MARGIN):
    """Condenses the maze into a smaller maze. Scans the maze in squares of size
        width*margin by width*margin. If most of the elements of the square are
        path spaces, then all the squares will be condensed into one path.
        Likewise for if they are mostly wall elements.
    params:
        maze - the maze grid of 1s and 0s
        margin - float which controls how much to condense the maze
    returns:
        condensed version of the maze
    """
    x0,y0,x1,y1 = get_starting_coords(maze)
    width = x1-x0
    width = int(width*margin)
    buff = int(width*ERROR_MARGIN)
    x0 = 0
    y0 = 0
    x1 = width
    y1 = width
    last = False
    arr = []
    i = 0
    while y1 < maze.shape[0]:
        arr.append([])
        while x1 < maze.shape[1]:
            m = np.mean(maze[y0:y1+1,x0:x1+1])
            if m < 0.5:
                arr[i].append(0)
            else:
                arr[i].append(1)
            x0 += width+1
            x1 += width+1
        i += 1
        y0 += width+1
        y1 += width+1
        x0 = 0
        x1 = width
    # pprint.pprint(arr)
    return arr

"""
main function
"""
def main():
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
    simplified_maze = condense(listed)
    
    numrows = len(simplified_maze)
    numcols = len(simplified_maze[0])
    print "number of 1s: {}".format(oneCount)
    print "number of 0s: {}".format(zeroCount)
    print "updated width and height of maze"
    print "width of maze: {}".format(numrows)
    print "height of maze: {}".format(numcols)
    with open('output.txt','w') as f:
        for row in simplified_maze:
            f.write(str(row))
            f.write('\n')

if __name__ == "__main__":
    main()
