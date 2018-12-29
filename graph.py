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

    def find_shortest_path(self):
        total = len(self.nodes)
        temp_nodes = self.nodes
        self.path.append(temp_nodes.pop(0))
        for current_node in self.path:
            if temp_nodes:
                mini_distance = None
                for i, other in enumerate(temp_nodes):
                    distance = sqrt(abs(current_node.latitude - other.latitude) ** 2 +
                                    abs(current_node.longitude - other.longitude) ** 2)
                    if not mini_distance or distance < mini_distance:
                        found = i
                        mini_distance = distance
                self.path.append(self.nodes.pop(found))
                self.distance += mini_distance
            print("Processing: " + str(round(len(self.path) / total * 100, 2)) + "%")
        return [node.city for node in self.path], self.distance
