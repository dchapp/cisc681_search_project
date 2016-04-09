from collections import defaultdict

"""
A simple graph data structure.
Adapted from accepted answer on StackOverflow thread:
http://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
"""
class Graph(object):
    ### Begin code from StackOverflow
    """
    Initialize a graph data structure. 
    """
    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    """
    Add list of connections--i.e. edges between nodes--to graph.
    """
    def add_connections(self, connections):
        for node_x, node_y in connections:
            self.add(node_x, node_y)

    """
    Add a single connection--i.e. edge--between two nodes.
    """
    def add(self, node_x, node_y):
        self._graph[node_x].add(node_y)
        if not self._directed:
            self._graph[node_y].add(node_x)

    """
    Remove a node and all edges to it.
    """
    def remove(self, node):
        for n, connections in self._graph.iteritems():
            try:
                connections.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    """
    Generate a string representation of the graph.
    """
    def __str__(self):
        return "{}({})".format(self.__class__.__name__, dict(self._graph))
    ### End code from StackOverflow

    """
    Get neighbors of a node.
    """
    def get_neighbors(self, node):
        return []


