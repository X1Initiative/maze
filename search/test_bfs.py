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

# R R L L L L R R L R R L

t4 = [
    [W, W, W, W, W, W, W, W, P, W, W, W, W, W, W, W],
    [W, W, P, P, P, P, P, P, P, W, W, W, W, W, W, W],
    [W, W, P, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, W, P, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, W, P, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, W, P, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, W, P, P, P, P, P, W, W, W, W, W, W, W, W, W],
    [W, W, W, W, W, W, P, W, W, W, W, W, W, W, W, W],
    [W, W, W, W, W, W, P, W, W, W, W, W, W, W, W, W],
    [W, W, W, W, W, W, P, W, P, P, P, P, W, W, W, W],
    [W, P, P, P, P, W, P, W, P, W, W, P, W, W, W, W],
    [W, P, W, W, P, W, P, P, P, W, W, P, W, W, W, W],
    [W, P, W, W, P, W, W, W, W, W, W, P, W, W, W, W],
    [W, P, W, W, P, P, P, P, P, P, P, P, W, W, W, W],
    [W, P, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
    [W, P, W, W, W, W, W, W, W, W, W, W, W, W, W, W]
]

t5 = [
    [W, W, W, W, W, W, W, W, P, W, W, W, W, W, W, W],
    [W, W, P, P, P, P, P, P, P, W, W, W, W, P, W, W],
    [W, W, P, W, W, W, W, W, W, P, P, W, W, P, W, W],
    [W, W, P, W, W, W, W, W, W, W, P, P, P, P, P, W],
    [W, W, P, P, W, W, W, W, W, W, P, W, P, W, W, W],
    [W, W, P, W, W, P, W, W, W, W, P, W, W, W, W, W],
    [W, W, P, P, P, P, P, W, W, W, P, P, P, P, W, W],
    [W, W, W, W, W, W, P, W, W, W, W, W, W, P, P, W],
    [W, P, P, W, P, P, P, W, W, W, W, W, W, W, P, W],
    [W, P, W, W, W, W, P, W, P, P, P, P, W, W, P, W],
    [W, P, P, P, P, W, P, W, P, W, W, P, W, P, P, W],
    [W, P, W, W, P, W, P, P, P, W, W, P, W, P, P, W],
    [W, P, W, W, P, W, W, W, W, P, W, P, W, P, P, W],
    [W, P, W, W, P, P, P, P, P, P, P, P, P, P, P, W],
    [W, P, P, W, P, W, P, W, W, W, W, W, W, W, P, W],
    [W, P, W, W, W, W, W, W, W, W, W, W, W, W, W, W]
]

soln1 = bfs.bfs(t5)
bfs.convert_bfs_to_data(t5, soln1)