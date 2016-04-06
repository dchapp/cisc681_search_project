import sys
import numpy as np
import sympy as sp
import time

"""
Produces a 2D NumPy array from a file describing the map.
Open space is represented by 0.
Obstacles are represented by 1.
Objectives are represented by 2. 
"""
def load_map(map_file_name):
    ### Load in raw map data
    map_array = []
    with open(map_file_name) as map_file:
        for row in map_file:
            map_array.append(row)

    ### Convert to numpy 2D array and return
    return np.array(map_array)

def main():
    return 0


main()
