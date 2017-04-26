from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections=None, directed=False):
        if connections is None:
            connections = []
        self._graph = defaultdict(list)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node_a, node_b in connections:
            self.add(node_a, node_b)

    def add(self, node_a, node_b):
        """ Add connection between node_a and node_b """

        self._graph[node_a].append(node_b)
        if not self._directed:
            self._graph[node_b].append(node_a)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node_a, node_b):
        """ Is node_a directly connected to node_b """

        return node_a in self._graph and node_b in self._graph[node_a]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))