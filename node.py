class Node(object):
    def __init__(self):
        left = None
        right = None
        up = None
        down = None


'''
General idea:
    first get the width of the entry point of the maze (for example 20 pixels)
    then, find 20x20 squares, make them into a node
    if the node has an empty path above it, then it should have an up node
    if the node has an empty path to the right, then it should have a right node
    same goes for left and down
    the entry and exit nodes will be a special case because they are at the edges of the map
        there are no pixels above/below then (depending on if its on the top/bottom of the image)
    keep constructing nodes and linking them with other nodes, and at the end we should have a linked list of nodes
        we'll have the head node from the begining, and that will be the entry point into the maze, and that's all
        we need to pass to the search algorithm



head_node = Node()
prev = head_node()
loop through maze:
    find the next Node dir
        cur_node = Node()
        if dir = 'right':
            prev_node.right = cur_node
            cur_node.left = prev_node
        ...

'''