from math import sqrt


class Graph:
    def __init__(self):
        self.path = []
        self.nodes = []
        self.distance = 0

    def add_node(self, other):
        self.nodes.append(other)

    def _NNHeuristic(self, other):
        if self.nodes:
            mini_distance = None
            for i, n in enumerate(self.nodes):
                distance = sqrt(abs(n.latitude - other.latitude) ** 2 +
                                     abs(n.longitude - other.longitude) ** 2)
                if not mini_distance or distance < mini_distance:
                    node = i
                    mini_distance = distance
            self.path.append(self.nodes.pop(node))
            self.distance += mini_distance

    def find_shortest_path(self):
        total = len(self.nodes)
        self.path.append(self.nodes.pop(0))
        for node in self.path:
            self._NNHeuristic(node)
            print("Processing: " + str(round(len(self.path) / total * 100, 2)) + "%")
        return [node.city for node in self.path], self.distance
