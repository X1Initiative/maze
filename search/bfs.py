from Queue import Queue
from time import time
import copy

WALL = 1
PATH = 0

def bfs(maze):
    """BFS algorithm
    params:
        maze (2D int array) - represents the maze image in 1s and 0s
    returns:
        list of coords which represent the shortest path
        None if no path found
    """
    x_0, y_0 = find_point(maze, 'entry')
    x_f, y_f = find_point(maze, 'exit')
    q = Queue()
    q.put([(x_0, y_0)])
    maze_tmp = copy.deepcopy(maze)
    while not q.empty():
        pth = q.get()
        x, y = pth[-1]
        maze_tmp[y][x] = WALL
        if x == x_f and y == y_f:
            return pth
        load_queue(maze_tmp, pth, q)


def find_point(maze, tpe):
    """Find either the entry or exit point in a maze
    params:
        maze (2D int array) - represents the maze image in 1s and 0s
        tpe (string) - 'entry' or 'exit'
    returns:
        (x, y) int coords of exit/entry point
        None if bad input or could not find point
    """
    if tpe == 'entry':
        y = len(maze)-1
    elif tpe == 'exit':
        y = 0
    else:
        return
    for x in range(0, len(maze[y])):
        if maze[y][x] == PATH:
            return (x, y)

def load_queue(maze, pth, q):
    """Fills the BFS queue with all possible coords
    params:
        maze (2D int array) - represents the maze image in 1s and 0s
        pth (array) - contains the x,y coords from where we are moving
        q (Queue) - the queue of all potential points to travel to next
    """
    x, y = pth[-1]
    if x + 1 < len(maze) and maze[y][x+1] == PATH:
        q.put(pth + [(x+1, y)])
    if x - 1 < len(maze) and maze[y][x-1] == PATH:
        q.put(pth + [(x-1, y)])
    if y + 1 < len(maze) and maze[y+1][x] == PATH:
        q.put(pth + [(x, y+1)])
    if y - 1 < len(maze) and maze[y-1][x] == PATH:
        q.put(pth + [(x, y-1)])

def get_dir(x0, y0, x1, y1):
    """Get the direction in which someone is traveling given their
        initial coords and their final coords
    params:
        x0, y0 (int) - initial coords
        x1, y1 (int) - final coords
    returns:
        string 'left', 'right', 'up' or 'down' depending on dir
    """
    if x0 - x1 == 1 and y0 - y1 == 0:
        return 'left'
    if x0 - x1 == -1 and y0 - y1 == 0:
        return 'right'
    if x0 - x1 == 0 and y0 - y1 == 1:
        return 'up'
    if x0 - x1 == 0 and y0 - y1 == -1:
        return 'down'

def convert_bfs_to_data(maze, soln):
    """Given a solution to a maze and the maze itself, writes
        the solution to a file in the desired format to be
        read later. The format which it will write to the file
        is as follows:
            [number of turns][direction turned]
            [number of turns][direction turned]
            ...
        where each newline is a new instruction.
        For example, if the solution to the maze is turn on your 
        first right, then on your third left, then go straight to
        the exit, the following will be written to the file:
            1R
            3L
        The direction is in relation to what direction the vehicle
        is traveling in
    params:
        maze (2D int array) - represents the maze image in 1s and 0s
        soln (list) - list of coords which represent the path through the maze
    """
    prev = soln[0]
    prev_direc = 'up'
    rights = 0
    lefts = 0
    t = time()
    for coord in soln[1:]:
        direc = get_dir(prev[0], prev[1], coord[0], coord[1])
        prev = coord
        if prev_direc != direc:
            with open('data/data_%f' % t, 'a') as f:
                if prev_direc == 'up' and direc == 'right':
                    f.write('%iR\n' % rights)
                elif prev_direc == 'up' and direc == 'left':
                    f.write('%iL\n' % lefts)
                elif prev_direc == 'down' and direc == 'right':
                    f.write('%iL\n' % lefts)
                elif prev_direc == 'down' and direc == 'left':
                    f.write('%iR\n' % rights)
                elif prev_direc == 'left' and direc == 'up':
                    f.write('%iR\n' % rights)
                elif prev_direc == 'left' and direc == 'down':
                    f.write('%iL\n' % lefts)
                elif prev_direc == 'right' and direc == 'up':
                    f.write('%iL\n' % lefts)
                elif prev_direc == 'right' and direc == 'down':
                    f.write('%iR\n' % rights)
            rights = 0
            lefts = 0
            prev_direc = direc
        l = len(maze[coord[1]])
        l2 = len(maze)
        if direc == 'up':
            if coord[0] >= 1 and maze[coord[1]][coord[0]-1] == PATH:
                lefts += 1
            if coord[0] <= l-2 and maze[coord[1]][coord[0]+1] == PATH:
                rights += 1
        elif direc == 'down':
            if coord[0] >= 1 and maze[coord[1]][coord[0]-1] == PATH:
                rights += 1
            if coord[0] <= l-2 and maze[coord[1]][coord[0]+1] == PATH:
                lefts += 1
        elif direc == 'left':
            if coord[1] >= 1 and maze[coord[1]-1][coord[0]] == PATH:
                rights += 1
            if coord[1] <= l2-2 and maze[coord[1]+1][coord[0]] == PATH:
                lefts += 1
        elif direc == 'right':
            if coord[1] >= 1 and maze[coord[1]-1][coord[0]] == PATH:
                lefts += 1
            if coord[1] <= l2-2 and maze[coord[1]+1][coord[0]] == PATH:
                rights += 1
