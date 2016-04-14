from Queue import PriorityQueue

from SimpleGraph import *
from BoardToGraph import *

import sys

"""
Implementation of A* search algorithm. 
Requires:
    - board = a 2D array representing the environment
    - init_position = a tuple of coordinates for the starting position
    - goal_position = a tuple of coordinates for the position of the goal
Returns:
    - parent = a dictionary whose keys are positions and whose values are the positions that lead to the key positions
    - cost_to_reach = a dictionary whose keys are position and whose values are the cost to get to that position
"""
def a_star_search(board, init_position, goal_positions):
    ### Unpack
    #init_row = init_position[0]
    #init_col = init_position[1]
    #goal_row = goal_position[0]
    #goal_col = goal_position[1]
    #board_dims = (len(board), len(board[0]))

    ### Convert board to graph
    g = board_to_graph(board)

    ### Initially the explored set is empty
    #explored = []

    ### Initially the frontier consists only of the initial node
    frontier = PriorityQueue()
    frontier.put(init_position, 0)

    ### A dict of parent nodes
    parent = {}
    parent[init_position] = None

    ### A dict of costs to get to nodes
    cost_to_reach = {}
    cost_to_reach[init_position] = 0

    ### Expand the frontier
    while not frontier.empty():
        current = frontier.get()

        ### Check if current node is the goal node
        if current in goal_positions:
            break

        ### Expand the frontier
        for n in g.neighbors(current):
            ### Right? Since n is adjacent to current the cost to reach n is 1 more than cost
            ### to reach current?
            n_cost = cost_to_reach[current] + 1
            if n not in cost_to_reach or n_cost < cost_to_reach[n]:
                cost_to_reach[n] = n_cost
                priority = n_cost + heuristic_b(n, goal_positions)
                frontier.put(n, priority)
                parent[n] = current

    ### Check for existence of solution.
    for goal in goal_positions:
        if goal in parent.keys():
            return parent, cost_to_reach, goal

    print "No solution possible"
    #exit()


def heuristic(position, goal):
    (x1, y1) = position
    (x2, y2) = goal
    return abs(x1 - x2) + abs(y1 - y2)


# Finds minimum manhattan distance to any goal
def heuristic_a(position, goals):
    (x1, y1) = position
    min_dist = sys.maxint
    for goal in goals:
        (x2, y2) = goal
        dist = abs(x1 - x2) + abs (y1 - y2)
        min_dist = min(dist, min_dist)
    return min_dist

# Finds minimum euclidean distance to any goal
def heuristic_b(position, goals):
    (x1, y1) = position
    min_dist = sys.maxint
    for goal in goals:
        (x2, y2) = goal
        dist = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
        min_dist = min(dist, min_dist)
    return min_dist


def multiobjective_a_star_search(board, start, goal_list):
    return 0
