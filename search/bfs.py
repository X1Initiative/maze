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

