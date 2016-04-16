import numpy as np
from itertools import combinations
import sys

from Search import *

# Makes every combination of subpaths
# Then returns only paths which are "complete" (visit all goals and start node)
def complete_path(init_pos, paths, path_num):
    # find all possible paths from subpaths
    paths = list(combinations(paths, path_num))
    complete_paths = []
    # Check completeness of each path
    for path in paths:
        begin = init_pos
        visited = [begin]
        begins = [x[2] for x in path] # list of start points for subpaths
        ends = [x[3] for x in path] # list of end points for subpaths
        if begin not in begins:
            if begin not in ends:
                # if position of cat not in path, reject immediately
                continue
        # Find all goals which are reachable from path(s)
        # Some paths may not be connected, so always start with cat position
        for i in range(path_num):
            if begin in begins:
                j = begins.index(begin)
                visited.append(ends[j]) # add end position to visited nodes
                begin = ends[j]
                del ends[j]
                del begins[j]
            elif begin in ends:
                j = ends.index(begin)
                visited.append(begins[j]) # add start position to visited nodes
                begin = begins[j]
                del ends[j]
                del begins[j]
            else:
                break
        # Check if all the goals were in path
        if len(set(visited)) == path_num+1:
            complete_paths.append(path)

    return complete_paths

"""
Multiobjective A* Heuristic for finding optimal path to all goals from a given
starting point.  This function works to find the Minimum Spanning Tree (MST)
which visits all goals.  It finds the MST by creating all possible path(s)
between goal nodes and selecting the path which is complete and has the lowest
cost.
Inputs:
    - board: numpy array representation of the board
    - init_pos: starting position of path (the cat)
    - heuristic: a heuristic function for A*
        Inputs:
            - current position tuple
            - list of goal position tuples
        Returns:
            - (under)-estimation of cost to goal
Returns:
    - A path in the form of a list of tuples, each which represent a subpath
    - subpath tuples contain:
        - parent: dictionary of node: parent
        - cost: dictionary of node: cost to reach
        - start: starting position of subpath
        - end: ending position of subpath
"""
def combinatorial_a_star(board, init_pos, heuristic):
    # find x,y coordinates of goals
    goals = zip(*np.where(board == 2))
    goals.append(init_pos)
    # get all possible pairs of nodes to visit
    pairs = list(combinations(goals, 2))
    paths = []
    # Find shortest path between each of the pairs
    for pair in pairs:
        begin, end = pair
        parent, cost, goal = a_star_search(board, begin, [end], heuristic)
        paths.append((parent, cost, begin, end))

    # Identify which paths are complete (visit all goals)
    paths = complete_path(init_pos, paths, len(goals)-1)

    # Select the complete path which has the lowest cost
    min_cost, min_path = (sys.maxint, None)
    for path in paths:
        cost = sum([x[1][x[3]] for x in path])
        if cost < min_cost:
            min_cost, min_path = (cost, path)

    return list(min_path)


"""
Multiobjective A* Heuristic for finding a path to all goals from a given
starting point, which is not guaranteed to be optimal.  The algorithm
iteratively finds paths from a start position to an end position.  The end
position is always the goal which is closest (least cost) to the start
position.
Inputs:
    - board: numpy array representation of the board
    - init_pos: starting position of path (the cat)
    - heuristic: a heuristic function for A*
        Inputs:
            - current position tuple
            - list of goal position tuples
        Returns:
            - (under)-estimation of cost to goal
Returns:
    - A path in the form of a list of tuples, each which represent a subpath
    - subpath tuples contain:
        - parent: dictionary of node: parent
        - cost: dictionary of node: cost to reach
        - start: starting position of subpath
        - end: ending position of subpath
"""
def nearest_neighbor_a_star(board, init_pos, heuristic):
    start = init_pos
    goals = zip(*np.where(board == 2))
    path = []

    ### Solve board
    while goals:
        parent, cost, goal = a_star_search(board, start, goals, heuristic)
        del goals[goals.index(goal)] # Remove found goal
        path.append((parent, cost, start, goal))
        start = goal # Make found goal starting position

    return path
