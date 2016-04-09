"""
A very basic graph data structure. 
"""
class Graph(object):
    def __init__(self):
        self.edges = {}

    def neighbors(self, node_id):
        return self.edges[node_id]

