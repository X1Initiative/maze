Functions to perform BFS on a maze represented by a 2D array

bfs function gathers a solution and outputs list of nodes it visited
in order. convert_bfs_to_data takes in the maze and the solution provided
by bfs and converts that solution to a data format that the on board team wants.
convert_bfs_to_data writes solution to a data directory, so be sure you have one
before running. All files are of the format data_[timestamp].txt, and all files
of this format will be ignored with git because of the .gitignore.

To get a bfs solution, run the function bfs(maze) where maze is the 2d array
of 1s and 0s that represent the binary maze image. To output this solution
to the desired format in a file, run convert_bfs_to_data(maze, soln) where
soln is the output to the bfs(maze) function and maze is the same maze variable
used before.