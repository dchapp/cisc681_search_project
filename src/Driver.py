import sys
import time
import pprint 

from Board import *
from SimpleGraph import *
from SimpleNode import *
from BoardToGraph import *


def main():
    
    board_file = sys.argv[1]
    b = generate_board_from_file(board_file)
    print b
    g = board_to_graph(b)
    print g.edges


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
