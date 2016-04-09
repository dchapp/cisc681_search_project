from SimpleGraph import *
from SimpleNode import *

#"""
#A function to get the coordinates of a square's neighbors.
#Assumes that diagonal moves are allowed.
#"""
#def get_board_neighbors(coordinates, board_dims): 
#    i, j = coordinates
#    M, N = board_dims
#    ### Lower left corner
#    if i == M-1 and j == 0:
#        return [(i-1, j), (i-1, j+1), (i, j+1)]
#    ### Upper left corner
#    if i == 0 and j == 0:
#        return [(i, j+1), (i+1, j+1), (i+1, j)] 
#    ### Upper right corner
#    if i == 0 and j == N-1:
#        return [(i, j-1), (i+1, j-1), (i+1, j)] 
#    ### Lower right corner
#    if i == M-1 and j == N-1:
#        return [(i, j-1), (i-1, j-1), (i-1, j)] 
#    ### Lower strip
#    if i == M - 1:
#        return [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1)]
#    ### Left strip
#    if j == 0:
#        return [(i-1, j), (i-1, j+1), (i, j+1), (i+1, j), (i+1, j+1)]
#    ### Upper strip
#    if i == 0:
#        return [(i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
#    ### Right strip
#    if j == N - 1:
#        return [(i-1, j-1), (i-1, j), (i, j-1), (i+1, j-1), (i+1, j)] 
#    ### Interior
#    else:
#        return [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]

"""
A function to get the coordinates of a square's neighbors.
Assumes that diagonal moves are not allowed.
"""
def get_board_neighbors(coordinates, board_dims): 
    i, j = coordinates
    M, N = board_dims
    ### Lower left corner
    if i == M-1 and j == 0:
        return [(i-1, j), (i, j+1)]
    ### Upper left corner
    if i == 0 and j == 0:
        return [(i, j+1), (i+1, j)] 
    ### Upper right corner
    if i == 0 and j == N-1:
        return [(i, j-1), (i+1, j)] 
    ### Lower right corner
    if i == M-1 and j == N-1:
        return [(i, j-1), (i-1, j)] 
    ### Lower strip
    if i == M - 1:
        return [(i-1, j), (i, j-1), (i, j+1)]
    ### Left strip
    if j == 0:
        return [(i-1, j), (i, j+1), (i+1, j)]
    ### Upper strip
    if i == 0:
        return [(i, j-1), (i, j+1), (i+1, j)]
    ### Right strip
    if j == N - 1:
        return [(i-1, j), (i, j-1), (i+1, j)] 
    ### Interior
    else:
        return [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]

"""
Removes coordinates from neighbor list that are obstacle squares on the board. 
"""
def prune_invalid_board_neighbors(neighbor_list, board):
    return [ (i, j) for (i, j) in neighbor_list if board[i][j] != 1 ] 


"""
Converts the array representation of the board to a graph representation.
The graph representation uses adjacency lists. 
"""
def board_to_graph(board):
    ### Initialize an empty graph
    g = Graph()

    ### Get board dimensions
    M, N = len(board), len(board[0])

    ### Loop over squares of board and determine neighbors.
    edges = {}
    for i in xrange(M):
        for j in xrange(N):
            ### If a square is empty, add it to the graph.
            if board[i][j] == 0 or board[i][j] == 2:
                #print "(" + str(i) + ", " + str(j) + ")"
                #print get_board_neighbors( (i, j), (M, N) )
                edges[(i, j)] = prune_invalid_board_neighbors( get_board_neighbors( (i, j), (M, N) ), board )
    g.edges = edges
    return g


