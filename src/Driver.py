import sys
import time
import pprint
from itertools import combination
import numpy as np

from Board import *
from SimpleGraph import *
from BoardToGraph import *
from Search import *


def complete_path(start, solutions, goal_len):
    paths = list(combinations(solutions, goal_len))
    complete_paths = []
    for path in paths:
        complete = True
        begin = start
        visited = [begin]
        begins = [x[2] for x in path]
        ends = [x[3] for x in path]
        if begin not in begins:
            if begin not in ends:
                continue
        for i in range(goal_len):
            if begin in begins:
                j = begins.index(begin)
                if path[j][3] in visited:
                    complete = False
                    break
                visited.append(path[j][3])
                begin = path[j][3]
            elif begin in ends:
                j = ends.index(begin)
                if path[j][2] in visited:
                    complete = False
                    break
                visited.append(path[j][2])
                begin = path[j][2]
        if complete:
            complete_paths.append(path)

    return complete_paths


def combinatorial_a_star(board):
    ### Generate board, starting position, and goal positions
    start = find_legal_starting_position(board)
    goals = zip(*np.where(board == 2))
    goals.append(start)
    pairs = list(combinations(goals, 2))
    solutions = []
    for pair in pairs:
        parent, cost_to_reach, goal = a_star_search(board, pair[0], [pair[1]])
        solutions.append((parent, cost_to_reach, pair[0], goal))

    paths = complete_path(start, solutions, len(goals)-1)

    min_cost = sys.maxint
    min_path = None
    for path in paths:
        cost = [x[1][x[3]] for x in path]
        cost = sum(cost)
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path

def solve_multi_objective_board(board):
    ### Generate board, starting position, and goal positions
    g = board_to_graph(board)
    start = find_legal_starting_position(board)
    goals = zip(*np.where(board == 2))
    solutions = []

    ### Solve board
    start_time = time.time()
    while goals:
        parent, cost_to_reach, goal = a_star_search(board, start, goals)
        del goals[goals.index(goal)] # Remove found goal
        solutions.append((parent, cost_to_reach, start, goal))
        start = goal # Make found goal starting position

    end_time = time.time()
    return end_time - start_time



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

    scaling_test()

#    board_file = sys.argv[1]
#    b = generate_board_from_file(board_file)
#    print b
#    g = board_to_graph(b)
#    #print g.edges
#    init_pos = (0, 0)
#    start = init_pos
#    goals = zip(*np.where(b == 2))
#    solutions = []
#    while goals:
#        parent, cost_to_reach, goal = a_star_search(b, start, goals)
#        del goals[goals.index(goal)] # Remove found goal
#        solutions.append((parent, cost_to_reach, start, goal))
#        start = goal # Make found goal starting position
#
#    path = []
#    for sub_soln in solutions:
#        parent, cost, start, goal = sub_soln
#        path.append(goal)
#        current = goal
#        while parent[path[-1]] != start:
#            path.append(parent[current])
#            current = parent[current]
#    path.append(init_pos)
#
#    print path
#
#    solution = np.array(b)
#
#    solution_board = []
#    for i in xrange(len(solution)):
#        solution_board.append(solution[i][:])
#
#    solution_board = [ list(x) for x in solution_board ]
#    solution_board = [ [str(int(y)) for y in x] for x in solution_board ]
#
#
#    for p in path:
#        x = p[0]
#        y = p[1]
#        solution_board[x][y] = "#"
#
#    for row in solution_board:
#        print '[%s]' % ' '.join(map(str, row))
#
#    #for row in solution_board:
#    #    print row
#
#
#    write_solution_to_file(solution_board)


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



    return 0


main()
