import bfs

W = 1
P = 0

t1 = [
    [W, W, W, W, P, W, W, W],
    [W, W, W, W, P, W, W, W],
    [W, W, W, P, P, P, P, W],
    [W, P, P, P, W, P, W, W],
    [W, P, W, W, W, P, W, W],
    [W, P, W, W, W, P, W, W],
    [W, P, P, P, P, P, P, W],
    [W, W, W, P, W, W, W, W]
]

# Two equal distance paths
t2 = [
    [W, W, W, W, P, W, W, W],
    [W, W, W, W, P, W, W, W],
    [W, W, W, P, P, P, P, W],
    [W, P, P, P, W, P, W, W],
    [W, P, W, W, W, P, W, W],
    [W, P, W, W, W, P, W, W],
    [W, P, P, P, P, P, P, W],
    [W, W, P, W, W, W, W, W]
]

t3 = [
    [W, W, W, W, P, W, W, W],
    [W, W, W, W, P, W, W, W],
    [W, W, W, P, P, P, P, W],
    [W, P, P, P, W, P, W, W],
    [W, P, W, W, W, P, W, W],
    [W, P, W, P, W, P, W, W],
    [W, P, P, P, P, P, P, W],
    [W, W, P, W, W, W, W, W]
]

soln1 = bfs.bfs(t3)
bfs.convert_bfs_to_data(t3, soln1)