import sys
import time

from Board import *



def main():
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
    
    print "Testing board-generation from improperly formatted file:\n"
    b = generate_board_from_file(bad_file_1)
    print b
    print type(b)
    
    return 0


main()
