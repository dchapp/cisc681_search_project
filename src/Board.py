import numpy as np

"""
A function for generating a board from a user-specified file.
The file is expected to be whitespace-delimited and consist of rows containing the same number of entries each. 
"""
def generate_board_from_file(board_file_name):
    ### Load in raw board data
    board_array = []
    with open(board_file_name) as board_file:
        row_count = 0
        for row in board_file:
            ### Skip empty rows
            if row == "\n":
                continue
            ### Remove leading and trailing whitespace
            row = row.strip()
            ### Split on interior whitespace
            row = row.split()
            ### Get row length from first row
            if row_count == 0:
                row_length = len(row)
            ### Convert to numeric types
            row = [int(x) for x in row]
            ### Check for improper entries
            for x in row:
                if x != 0 and x != 1 and x != 2:
                    print "Improper entry: " + str(x) + " in row: " + str(row)
                    print "Exiting now."
                    exit()
            ### Check for proper row length 
            if len(row) != row_length:
                print "Rows of different lengths detected."
                print "Exiting now."
                exit()
            ### Append to board and update row count
            board_array.append(row)
            row_count += 1

    ### Convert to numpy 2D array and return
    return np.array(board_array)

"""
A function for generating a M x N board with a user-specified number of obstacles and objectives.
Obstacles and objectives are distributed randomly according to user-specified randomization policies.
Requires:
    - M = number of rows
    - N = number of columns
    - X = number of obstacles
    - Y = number of objectives
    - P = randomization policy for obstacles (default = uniform)
    - Q = randomization policy for objectives (default = uniform)
Returns:
    - An MxN NumPy array 'board' where:
        - board[i][j] = 0 --> square contains nothing
        - board[i][j] = 1 --> square contains obstacle
        - board[i][j] = 2 --> square contains objective
"""
def generate_board_fixed(M, N, X, Y, P=0, Q=0):
    ### Initialize board to all zeros
    board = np.zeros((M,N))

    ### Place obstacles according to policy P
    num_obstacles_to_place = X
    while num_obstacles_to_place:
        ### Uniform random placement
        if P == 0:
            ### Generate random coordinates.
            x_coord = np.random.randint(0, M)
            y_coord = np.random.randint(0, N)
            if board[x_coord][y_coord] == 0:
                board[x_coord][y_coord] = 1
                num_obstacles_to_place -= 1
        else:
            print "Unsupported placement policy specified. Exiting."
            exit()

    ### Place objectives according to policy P
    num_objectives_to_place = Y
    while num_objectives_to_place:
        ### Uniform random placement
        if P == 0:
            ### Generate random coordinates.
            x_coord = np.random.randint(0, M)
            y_coord = np.random.randint(0, N)
            if board[x_coord][y_coord] == 0:
                board[x_coord][y_coord] = 2
                num_objectives_to_place -= 1
        else:
            print "Unsupported placement policy specified. Exiting."
            exit()

    return board


"""
A function for generating a M x N board with a user-specified fraction of squares containing obstacles and objectives.
Obstacles and objectives are distributed randomly according to user-specified randomization policies.
Requires:
    - M = number of rows
    - N = number of columns
    - f = fraction of squares that should conatin obstacles
    - g = fraction of squares that should contain objectives
    - P = randomization policy for obstacles (default = uniform)
    - Q = randomization policy for objectives (default = uniform)
Returns:
    - An MxN NumPy array 'board' where:
        - board[i][j] = 0 --> square contains nothing
        - board[i][j] = 1 --> square contains obstacle
        - board[i][j] = 2 --> square contains objective
"""
def generate_board_fractional(M, N, f, g, P=0, Q=0):
    ### Initialize board to all zeros
    board = np.zeros((M,N))

    ### Determine how many obstacles and objectives to place.
    num_squares = M * N
    if f != 0:
        num_obstacles_to_place = max(1, M * N * f)
    else:
        num_obstacles_to_place = 0
    if g != 0:
        num_objectives_to_place = max(1, M * N * g)
    else:
        num_objectives_to_place = 0

    ### Determine if requirements are feasible
    if num_obstacles_to_place + num_objectives_to_place > (M * N) - 1:
        print "Unsatisfiable board."
        print "Exiting now."
        exit()

    ### Place obstacles according to policy P
    while num_obstacles_to_place:
        ### Uniform random placement
        if P == 0:
            ### Generate random coordinates.
            x_coord = np.random.randint(0, M)
            y_coord = np.random.randint(0, N)
            if board[x_coord][y_coord] == 0:
                board[x_coord][y_coord] = 1
                num_obstacles_to_place -= 1
        else:
            print "Unsupported placement policy specified. Exiting."
            exit()

    ### Place objectives according to policy P
    while num_objectives_to_place:
        ### Uniform random placement
        if P == 0:
            ### Generate random coordinates.
            x_coord = np.random.randint(0, M)
            y_coord = np.random.randint(0, N)
            if board[x_coord][y_coord] == 0:
                board[x_coord][y_coord] = 2
                num_objectives_to_place -= 1
        else:
            print "Unsupported placement policy specified. Exiting."
            exit()

    return board


"""
Function that generates a board exactly as described in the project
rubric/description.
Inputs:
    - n = length of each side of the board
    - M = number of mice (0 < M <= (n^2)/4)
Returns:
    - An nxn NumPy array 'board' where:
        - board[i][j] = 0 --> square contains nothing
        - board[i][j] = 1 --> square contains obstacle
        - board[i][j] = 2 --> square contains objective
    - k obstacles on board (0 <= k <= (n^2)/3)
"""
def generate_board_rubric(n, M):
    # Initialize board to all zeros
    board = np.zeros((n,n))

    # Calculate total number of squares
    squares = n ** 2

    # Determine if valid M value
    if (M <= 0) or (M > squares/4):
        M = (n ** 2)/4
        print "Invalid value for M, setting M to %d" % M

    # Determine number of obstacles to place
    k = np.random.randint(squares/3 + 1) # +1 because inclusive

    # Place obstacles and mice on board
    while k or M:
        if k:
            # Place obstacles
            coord = np.random.randint(n, size=2)
            if not board[coord[0], coord[1]]:
                board[coord[0], coord[1]] = 1
                k -= 1
        if M:
            # Place mice
            coord = np.random.randint(n, size=2)
            if not board[coord[0], coord[1]]:
                board[coord[0], coord[1]] = 2
                M -= 1

    return board
