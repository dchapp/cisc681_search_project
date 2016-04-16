import sys

# Finds minimum manhattan distance to any goal
# Input is current node position and list of goal positions
def heuristic_manhattan(position, goals):
    (x1, y1) = position
    min_dist = sys.maxint
    for goal in goals:
        (x2, y2) = goal
        dist = abs(x1 - x2) + abs(y1 - y2)
        min_dist = min(dist, min_dist)
    return min_dist

# Finds minimum euclidean distance to any goal
# Input is current node position and list of goal positions
def heuristic_euclidean(position, goals):
    (x1, y1) = position
    min_dist = sys.maxint
    for goal in goals:
        (x2, y2) = goal
        dist = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
        min_dist = min(dist, min_dist)
    return min_dist

