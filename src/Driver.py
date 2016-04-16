import sys
import time
import pprint
from itertools import combinations
import numpy as np
import argparse

from Board import *
from SimpleGraph import *
from BoardToGraph import *
from Search import *
from MultiobjectiveSearch import *
from Heuristics import *

def get_char(i):
    if i == 0:
        return ' '
    if i == 1:
        return u'\u2588'
    if i == 2:
        return u'\U0001F42D'
    if i == 3:
        return u'\U0001F638'
    else:
        return -i

def print_board(board):
    border = ''.join([u'\u2588' for i in range(len(board)+2)])
    print border
    for row in board:
        row = [get_char(i) for i in row]
        print u'\u2588' + '%s' % ''.join(row) + u'\u2588'
    print border

def print_solution_board(path, board):
    print 'nah'

def print_solution_path(path):
    for vertex in path:
        print vertex

# Builds the list of vertices for the path, starting at the initial position
def get_path(path, init_pos):
    path_vertices = []
    total_cost = 0

    while path:
        # Find the subpath
        sub_index = [init_pos in x for x in path].index(True)
        sub_path = path[sub_index]
        del path[sub_index]

        parent, cost, start, end = sub_path
        total_cost += cost[end]
        print cost[end]

        tmp_vertices = [end]
        current = end
        while parent[tmp_vertices[-1]] != start:
            tmp_vertices.append(parent[current])
            current = parent[current]

        if start != init_pos:
            init_pos = start
        else:
            tmp_vertices.reverse()
            init_pos = end

        path_vertices += tmp_vertices

    return path_vertices, total_cost

def scaling_test():
    board_sizes = range(10, 100)
    for s in board_sizes:
        ### Generate number of mice
        num_mice = np.random.randint(1, ((s**2)/4)+1)
        ### Generate guaranteed solvable board
        b = generate_solvable_board_rubric(s, num_mice)
        t = solve_multi_objective_board(b)
        print "Board size: " + str(s) + " Time to solve: " + str(t)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bfile', type=str, required=False,
            default=False, help='file containing board')
    parser.add_argument('-o', '--multiheuristic', type=str, required=False,
            default='nn', choices=['nn', 'mst'], help='''desire multiobjective
            heuristic to use with A*.  Valid inputs are "nn" and "mst", which
            are "nearest neighbor" and "minimum spanning tree",
            respectively''')
    parser.add_argument('-hr', '--heuristic', type=str, required=False,
            default='manhattan', choices=['manhattan', 'euclidean'],
            help='''Heuristic to use with single objective A*.  Valid inputs
            are "manhattan" and "euclidean"''')
    parser.add_argument('-m', '--mice', type=int, required=False,
            default=5, help='number of mice to place on board')
    parser.add_argument('-n', '--size', type=int, required=False,
            default=10, help='size of the board: nxn')
    args = parser.parse_args()

    # Generate Board
    if args.bfile:
        board = generate_board_from_file(args.bfile)
    else:
        board = generate_board_rubric(args.size, args.mice)

    # Get appropriate heuristics for multiobjective and single objective A*
    if args.multiheuristic == 'nn':
        solver = nearest_neighbor_a_star
    if args.multiheuristic == 'mst':
        solver = combinatorial_a_star
    if args.heuristic == 'manhattan':
        heuristic = heuristic_manhattan
    if args.heuristic == 'euclidean':
        heuristic = heuristic_euclidean

    # find valid starting position on the board
    init_pos = find_legal_starting_position(board)

    # print the board for user inspection
    p_board = board
    p_board[init_pos[0], init_pos[1]] = 3
    print_board(p_board)

    # Solve the board with chosen heuristics
    path = solver(board, init_pos, heuristic)

    # Extract the path of (x,y) positions
    path, cost = get_path(path, init_pos)

    # Print the vertices which form solution path
    print_solution_path(path)

    # Print the board with solution overlay
    print_solution_board(path, board)


    print 'The path length is: %d' % cost

    #for row in solution_board:
    #   : print row


    #write_solution_to_file(solution_board)


    """
    M = int(sys.argv[1])
    N = int(sys.argv[2])
    X = int(sys.argv[3])
    Y = int(sys.argv[4])

    good_file_1 = sys.argv[5]
    good_file_2 = sys.argv[6]
    bad_file_1  = sys.argv[7]

    print "Testing board-generation from fixed parameters:\n"
    b = generate_board_fixed(M, N, X, Y)
    print b
    print type(b)

    print "Testing board-generation from one properly formatted file:\n"
    b = generate_board_from_file(good_file_1)
    print b
    print type(b)
    
    print "Testing board-generation from another properly formatted file:\n"
    b = generate_board_from_file(good_file_2)
    print b
    print type(b)
    """
    
    """
    print "Testing board-generation from improperly formatted file:\n"
    b = generate_board_from_file(bad_file_1)
    print b
    print type(b)
    """

    """
    print "Testing graph data structure implementation."
    pp = pprint.PrettyPrinter(indent=4)
    connections = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('E', 'F'), ('F', 'C')]
    g = Graph(connections, directed=True)
    pp.pprint(g._graph) 

    print "Testing graph data structure implementation with object nodes."
    node_A = Node("A")
    node_B = Node("B")
    node_C = Node("C")
    node_D = Node("D")
    node_E = Node("E")
    node_F = Node("F")
    connections = [(node_A, node_B), (node_B, node_C), (node_B, node_D), (node_C, node_D), (node_E, node_F), (node_F, node_C)]
    g = Graph(connections, directed=True)
    pp.pprint(g._graph)
    """
