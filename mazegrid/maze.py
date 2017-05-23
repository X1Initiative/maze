#!/usr/bin/env python
import os,sys
import subprocess
import glob
import numpy as np
import pprint

from os import path

np.set_printoptions(threshold=np.inf)

WALL = 1
PATH = 0

ERROR_MARGIN = 0.1
WIDTH_MARGIN = 1
IMG_PATH = 'bigmaze.png'

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
    while y1 <= maze.shape[0]:
        arr.append([])
        while x1 <= maze.shape[1]:
            m = np.mean(maze[y0:y1,x0:x1])
            if m < 0.5:
                arr[i].append(0)
            else:
                arr[i].append(1)
            x0 += width
            x1 += width
        i += 1
        y0 += width
        y1 += width
        x0 = 0
        x1 = width
    # pprint.pprint(arr)
    return arr



'''The next two functions go together with the new attempt at simplifying the maze
by extending the number of ones
'''
def condense_loop(maze, width, buff, x_lim, y_lim):
    checking = False
    for y in xrange(0, y_lim):
        for x in xrange(0, x_lim):
            if checking:
                if maze[y][x] == WALL:
                    t_width = x - start
                    # if t_width >= width - buff and t_width <= width + buff:
                    if t_width > 1 and t_width <= width + buff:
                        for i in xrange(start, x-2):
                            maze[y][i] = WALL
                    else:
                        checking = False
            else:
                if maze[y][x] == PATH:
                    checking = True
                    start = x
    checking = False
    for x in xrange(0, x_lim):
        for y in xrange(0, y_lim):
            if checking:
                if maze[y][x] == WALL:
                    t_width = y - start
                    if t_width >= width - buff and t_width <= width + buff:
                        for i in xrange(start+1, y+1):
                            maze[i][x] = WALL
                    else:
                        checking = False
            else:
                if maze[y][x] == PATH:
                    checking = True
                    start = y
    return maze


def condense_with_ones(maze, margin=WIDTH_MARGIN, error_margin=ERROR_MARGIN):
    x0,y0,x1,y1 = get_starting_coords(maze)
    width = x1-x0
    width = int(width*margin)
    buff = int(width*error_margin)
    x_lim = maze.shape[1]
    y_lim = maze.shape[0]
    maze = maze.tolist()
    maze = condense_loop(maze, width, buff, x_lim, y_lim)
    maze = condense_loop(maze, width, buff, x_lim, y_lim)
    maze = condense_loop(maze, width, buff, x_lim, y_lim)
    return maze

def main():
    if len(sys.argv) > 1:
        pth = sys.argv[1]
    else:
        pth = IMG_PATH
    simplified_maze = create_simplified_maze(pth)
    with open('output.txt','w') as f:
        for row in simplified_maze:
            f.write(str(row))
            f.write('\n')

if __name__ == '__main__':
    main()
