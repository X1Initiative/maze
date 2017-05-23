Maze

given a maze image, compute the shortest path through the maze.
output the directions to a file to be read later

otsu dir contains all otsu method code
mazegrid dir contains all image simplification code
search dir contains search algorithm code
imgs dir contains all the images we use to test the code
the data dir is where the output files will be written

Setting up the environment:
    It is recommended that you use a virtual environment, but not required.
    To create and run a virtual environment, first install virtualenv, then
    run the following two commands:
        1) create virtual environment: virtualenv .venv
        2) activate virtual environment: source .venv/bin/activate

    Before running the code, you also need to install all the required packages
    with the following command:
        pip install -r requirements.txt

Running the code:
    manage.py calls the code from otsu, search, and mazegrid. It attempts to run 
    otsu to obtain a binary array representing the image. Then, it will run a 
    simplification algorithm to make the search more efficient. After, a search
    algorithm will be run (bfs), which will be converted to data which can later
    be used to solve the maze. This data will be output to the data dir.

    manage.py takes in two command line arguments. Run the script as follows:
        python manage.py [relative_image_path] [error_buffer]

    relative_image path should be the path of the image of the maze
    you which to solve relative to the manage.py script

    error_buffer should be a float between 0 and 1. This number gives an error
    margin for the simplification algorithm in detecting walls. A good value
    for this is usually 0.1

    Example call:
        python manage.py imgs/diff_colors2.png 0.1

mazegrid, otsu, and search each have their own README files as well