# Returns the correct unicode symbol for each object on the grid
def get_char(i):
    if i == 0:
        return '  '
    if i == 1:
        return u'\u2588'*2
    if i == 2:
        return u'\U0001F42D'+' '
    if i == 3:
        return u'\U0001F638'+' '
    else:
        return str(int(-i))+' '

# Prints the board to terimal
# Input is 2D numpy or python array/list
def print_board(board):
    border = ''.join([u'\u2588'*2 for i in range(len(board)+2)])
    print border
    for row in board:
        row = [get_char(i) for i in row]
        print u'\u2588'*2 + '%s' % ''.join(row) + u'\u2588'*2
    print border

# Adds information about the solution path to the board and prints the board
def print_solution_board(path, board):
    for vertex in path:
        x, y = vertex
        if board[x,y] <= 0:
            board[x,y] -= 1
    print_board(board)

# Prints solution path, denoting 'c' and 'm' for cat and mouse, respectively
def print_solution_path(path, board):
    print 'Path:',
    for vertex in path:
        x,y=vertex
        if board[x,y] == 3:
            print 'c'+str(vertex)+',',
        if board[x,y] == 2:
            print 'm'+str(vertex)+',',
        print str(vertex)+',',
    print '\n'

# Builds the list of vertices for the path, starting at the initial position
def get_path(path, init_pos):
    path_vertices = []
    total_cost = 0

    while path:
        # Finds the next subpath in the list of subpaths
        sub_index = [init_pos in x for x in path].index(True)
        sub_path = path[sub_index]
        del path[sub_index] # remove that subpath from the list

        # Get information about subpath
        parent, cost, start, end = sub_path
        total_cost += cost[end]

        # Gather vertices of subpath
        tmp_vertices = [end]
        current = end
        while parent[tmp_vertices[-1]] != start:
            tmp_vertices.append(parent[current])
            current = parent[current]

        # Account for if path was built forward or backward
        # This is necessary for the combinatorial solution finder because it
        # does not always make the cat the starting point of the first subpath
        if start != init_pos:
            init_pos = start
        else:
            tmp_vertices.reverse()
            init_pos = end

        # Append subpath to build whole path
        path_vertices += tmp_vertices

    return path_vertices, total_cost

