from Queue import Queue

WALL = 1
PATH = 0

# BFS, takes in 2D array w/ 1s and 0s
def bfs(maze):
    x_0, y_0 = find_point(maze, 'entry')
    x_f, y_f = find_point(maze, 'exit')
    q = Queue()
    q.put([(x_0, y_0)])
    while not q.empty():
        pth = q.get()
        x, y = pth[-1]
        if x == x_f and y == y_f:
            return pth
        load_queue(maze, pth, q)


def find_point(maze, tpe):
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
    if x0 - x1 == 1 and y0 - y1 == 0:
        return 'left'
    if x0 - x1 == -1 and y0 - y1 == 0:
        return 'right'
    if x0 - x1 == 0 and y0 - y1 == 1:
        return 'up'
    if x0 - x1 == 0 and y0 - y1 == -1:
        return 'down'

def convert_bfs_to_data(maze, soln):
    prev = soln[0]
    prev_direc = 'up'
    rights = 0
    lefts = 0
    for coord in soln[1:]:
        direc = get_dir(prev[0], prev[1], coord[0], coord[1])
        prev = coord
        if prev_direc != direc:
            if prev_direc == 'up' and direc == 'right':
                print '%iR' % rights
            elif prev_direc == 'up' and direc == 'left':
                print '%iL' % lefts
            elif prev_direc == 'down' and direc == 'right':
                print '%iL' % lefts
            elif prev_direc == 'up' and direc == 'left':
                print '%iR' % rights
            elif prev_direc == 'left' and direc == 'up':
                print '%iR' % rights
            elif prev_direc == 'left' and direc == 'down':
                print '%iL' % lefts
            elif prev_direc == 'right' and direc == 'up':
                print '%iL' % lefts
            elif prev_direc == 'right' and direc == 'down':
                print '%iR' % rights
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
