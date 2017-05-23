from mazegrid import maze
from search import bfs
from otsu import otsu
import sys

def print_maze(mze):
    for i in xrange(len(mze)):
        for j in xrange(len(mze[i])):
            sys.stdout.write(str(mze[i][j]))
        sys.stdout.write('\n')

def main():
    # CL arguements are an image path and a error margin
    # All images should be in the imgs directory and a good error margin is usually around 0.1
    # Example call:
    # python manage.py imgs/smallwall.png 0.1
    image_path = sys.argv[1]
    buff = float(sys.argv[2])

    # run otsu's, get the array, and print the array
    mze = otsu.run_otsu(image_path)
    print_maze(mze)
    print '\n\n\n\n\n\n\n\n'

    # simplify the array and print the output
    mze = maze.condense_with_ones(mze, 1, buff)
    print_maze(mze)

    # get the bfs solution. This should come as a list of tuples, or None if no solution found
    soln = bfs.bfs(mze)
    print soln

    # convert the tuple list to a list of directions, to be included in a new file
    # written in the data/ directory
    bfs.convert_bfs_to_data(mze, soln)

if __name__ == '__main__':
     main()