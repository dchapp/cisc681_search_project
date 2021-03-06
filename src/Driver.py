import sys
import time
import numpy as np
import argparse

from Board import *
from SimpleGraph import *
from BoardToGraph import *
from Search import *
from MultiobjectiveSearch import *
from Heuristics import *
from Printing import *


def scaling_test():
    board_sizes = range(10, 100)
    for s in board_sizes:
        ### Generate number of mice
        num_mice = np.random.randint(1, ((s**2)/4)+1)
        ### Generate guaranteed solvable board
        b = generate_solvable_board_rubric(s, num_mice)
        t = solve_multi_objective_board(b)
        print "Board size: " + str(s) + " Time to solve: " + str(t)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bfile', type=str, required=False,
            default=False, help='file containing board')
    parser.add_argument('-o', '--multiheuristic', type=str, required=False,
            default='nn', choices=['nn', 'msp'], help='''desire multiobjective
            heuristic to use with A*.  Valid inputs are "nn" and "comb", which
            are "nearest neighbor" and "minimum spanning path",
            respectively''')
    parser.add_argument('-hr', '--heuristic', type=str, required=False,
            default='manhattan', choices=['manhattan', 'euclidean'],
            help='''Heuristic to use with single objective A*.  Valid inputs
            are "manhattan" and "euclidean"''')
    parser.add_argument('-m', '--mice', type=int, required=False,
            default=5, help='number of mice to place on board')
    parser.add_argument('-n', '--size', type=int, required=False,
            default=10, help='size of the board: nxn')
    parser.add_argument('-ix', '--init_x', type=int, required=False,
            default=-1, help='initial x position')
    parser.add_argument('-iy', '--init_y', type=int, required=False,
            default=-1, help='initial y position')
    args = parser.parse_args()

    # Generate Board
    if args.bfile:
        board = generate_board_from_file(args.bfile)
    else:
        board = generate_board_rubric(args.size, args.mice)

    # Get appropriate heuristics for multiobjective and single objective A*
    if args.multiheuristic == 'nn':
        solver = nearest_neighbor_a_star
    if args.multiheuristic == 'msp':
        solver = combinatorial_a_star
    if args.heuristic == 'manhattan':
        heuristic = heuristic_manhattan
    if args.heuristic == 'euclidean':
        heuristic = heuristic_euclidean

    # find valid starting position on the board
    if args.init_x >= 0 and args.init_y >= 0:
        init_pos = (args.init_x, args.init_y)
    else:
        init_pos = find_legal_starting_position(board)

    # print the board for user inspection
    p_board = np.array(board)
    p_board[init_pos[0], init_pos[1]] = 3
    print_board(p_board)

    # Solve the board with chosen heuristics
    path = solver(board, init_pos, heuristic)

    # Extract the path of (x,y) positions
    path, cost = get_path(path, init_pos)

    # Print the vertices which form solution path
    print_solution_path(path, p_board)

    # Print the board with solution overlay
    print_solution_board(path, p_board)

    print 'The path length is: %d' % cost

    return 0

main()
