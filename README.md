## University of Delaware CISC-481/681 Project 2: Search
This project contains our team's implementation of the A\* algorithm with two heuristics

### Single-Objective Heuristics
1. Manhattan
2. Euclidean

### Multi-Objective Heuristics
1. Nearest Neighbor
2. Minimum Spanning Path

### Dependencies
Python 2.7
numpy

### Usage
./src/Driver.py will run the algorithm with default settings:
```
$python ./src/Driver.py
```

Several options can be specified regarding board generation and herustics:

-o: Desired multi-objective heuristic.  Valid options are 'nn' and 'msp'
-hr: Desired single-object heuristic.  Valid options are 'manhattan' and 'euclidean'
-m: number of mice to place on a board
-n: size of the board
-ix: location of the cat on the x axis
-iy: location of the cat on the y axis

The program may also be run with one of several pre-defined boards found in ./test/:

-b: board file to load

Running the algorithm with options:
```
$ python ./src/Driver.py -o msp -hr euclidean -ix 0 -iy 0 -b ./test/multiple_obstacles_3.txt
```

### Output
The program will output the following:
- Graphical representation of the original board
- Optimal path in the form of a set of vertices
- Graphical representation of the path
    - The path is represented by numbers on the board.  The number represents how many times the cat will walk through a board space (e.g., 1 is once, 3 is three times)
- Total path cost

Example output:
```
$ python ./src/Driver.py
████████████████████████
████    😸             ██
████              🐭   ██
██  ██    ████  🐭     ██
██      ██        ██████
██          ██    ██  ██
██  ██              🐭 ██
████      ██          ██
██🐭                   ██
██  ██    ██      🐭   ██
██  ████      ████  ████
████████████████████████
Path: c(0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), m(1, 8), (1, 7), m(2, 7), (3, 7), (4, 7), (5, 7), (5, 8), m(5, 9), (5, 8), (5, 7), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (6, 2), (6, 1), (7, 1), m(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), m(8, 8), 

████████████████████████
████    😸 1 1 1 1 1   ██
████            1 🐭   ██
██  ██    ████  🐭     ██
██      ██      1 ██████
██          ██  1 ██  ██
██  ██1 1 1 1 1 2 2 🐭 ██
████1 1   ██          ██
██🐭 2 1 1 1 1 1 1 1   ██
██  ██    ██      🐭   ██
██  ████      ████  ████
████████████████████████
The path length is: 33
```
