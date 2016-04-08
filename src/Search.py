import heapq as hq

from SimpleGraph import *
from SimpleNode import *
from BoardToGraph import *


"""
Implementation of A* search algorithm. 
"""
def a_star_search(board, init_position, goal_position):
    ### Unpack
    init_row = init_position[0]
    init_col = init_position[1]
    goal_row = goal_position[0]
    goal_col = goal_position[1]
    board_dims = (len(board), len(board[0]))

    ### Convert board to graph
    g = board_to_graph(board)

    ### Initially the explored set is empty
    explored = []

    ### Initially the frontier consists only of the initial node
    frontier = [(1, init_position)]
    hq.heapify(frontier)

    ### Expand the frontier
    while not frontier.empty():
        current = frontier.heappop()
        current_coords = current[1]

        ### Check if current node is the goal node
        if current_coords == goal_position:
            break

        ### Expand the frontier
        while not frontier.empty()


    return 0


def heuristic_a(position_x, position_y):
    return 0

def heuristic_b(position_x, position_y):
    return 0
