import numpy as np

from Search import *

# Makes every combination of subpaths
# Then returns only paths which are "complete" (visit all goals and start node)
def complete_path(init_pos, paths, path_num):
    paths = list(combinations(paths, path_num))
    complete_paths = []
    for path in paths:
        begin = init_pos
        visited = [begin]
        begins = [x[2] for x in path]
        ends = [x[3] for x in path]
        if begin not in begins:
            if begin not in ends:
                continue
        for i in range(path_num):
            if begin in begins:
                j = begins.index(begin)
                visited.append(ends[j])
                begin = ends[j]
                del ends[j]
                del begins[j]
            elif begin in ends:
                j = ends.index(begin)
                visited.append(begins[j])
                begin = begins[j]
                del ends[j]
                del begins[j]
            else:
                break
        if len(set(visited)) == path_num+1:
            complete_paths.append(path)

    return complete_paths

def combinatorial_a_star(board, init_pos, heuristic):
    goals = zip(*np.where(board == 2))
    goals.append(init_pos)
    pairs = list(combinations(goals, 2))
    paths = []
    for pair in pairs:
        begin, end = pair
        parent, cost, goal = a_star_search(board, begin, [end], heuristic)
        paths.append((parent, cost, begin, end))

    # Identify which paths are complete (visit all goals)
    paths = complete_path(init_pos, paths, len(goals)-1)

    min_cost, min_path = (sys.maxint, None)
    for path in paths:
        cost = sum([x[1][x[3]] for x in path])
        if cost < min_cost:
            min_cost, min_path = (cost, path)

    return min_path

def nearest_neighbor_a_star(board, init_pos, heuristic):
    start = init_pos
    goals = zip(*np.where(board == 2))
    path = []

    ### Solve board
    while goals:
        parent, cost, goal = a_star_search(board, start, goals, heuristic)
        del goals[goals.index(goal)] # Remove found goal
        path.append((parent, cost, start, goal))
        start = goal # Make found goal starting position

    return path
