from Queue import PriorityQueue

from SimpleGraph import *
from BoardToGraph import *

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
def a_star_search(board, init_position, goal_positions, heuristic):
    ### Convert board to graph
    g = board_to_graph(board)

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
            n_cost = cost_to_reach[current] + 1
            if n not in cost_to_reach or n_cost < cost_to_reach[n]:
                cost_to_reach[n] = n_cost
                priority = n_cost + heuristic(n, goal_positions)
                frontier.put(n, priority)
                parent[n] = current

    ### Check for existence of solution.
    for goal in goal_positions:
        if goal in parent.keys():
            return parent, cost_to_reach, goal

    print "No solution possible"
    exit()
