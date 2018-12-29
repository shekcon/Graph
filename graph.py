from math import sqrt
from abc import abstractmethod


class Graph:
    def __init__(self):
        self.path = []
        self.nodes = []
        self.distance = 0

    def add_node(self, other):
        self.nodes.append(other)

    @abstractmethod
    def find_shortest_path(self):
        pass

class NNH(Graph):

    def _find_nearest_neighbor(self, other):
        if self.nodes:
            mini_node = None
            distance = 0
            for i, n in enumerate(self.nodes):
                new_distance = sqrt(abs(n.latitude - other.latitude) ** 2 +
                                    abs(n.longitude - other.longitude) ** 2)
                if not mini_node or new_distance < distance:
                    node = i
                    distance = new_distance
            self.path.append(self.nodes.pop(node))
            self.distance += distance

    def find_shortest_path(self):
        total = len(self.nodes)
        self.path.append(self.nodes.pop(0))
        for node in self.path:
            self._find_nearest_neighbor(node)
            print("Processing: " + str(round(len(self.path) / total * 100, 2)) + "%")
        return [node.city for node in self.path], self.distance


