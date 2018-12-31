from graph import Graph
from math import sqrt


class BruteForce(Graph):

    def find_shortest_path(self):
        if len(self.nodes) > 11:
            from sys import exit
            print("Too many cities")
            exit(1)
        try:
            from itertools import permutations
            mini_distance = None
            start = [self.nodes[0]]
            for route in permutations(self.nodes[1:]):
                distance = self._calcu_distance(start + list(route))
                if not mini_distance or distance < mini_distance:
                    best_route = start + list(route)
                    mini_distance = distance
        except IndexError:
            pass
        return [node.city for node in best_route], mini_distance


class NearestNeighbor(Graph):

    def find_shortest_path(self):
        # total = len(self.nodes)
        temp_nodes = self.nodes[:]
        self.route.append(temp_nodes.pop(0))
        for current in self.route:
            mini_distance = None
            for i, other in enumerate(temp_nodes):
                distance = sqrt((current.latitude - other.latitude) ** 2 +
                                (current.longitude - other.longitude) ** 2)
                if not mini_distance or distance < mini_distance:
                    nearest_node = i
                    mini_distance = distance
            self.route.append(temp_nodes.pop(nearest_node))
            self.total_distance += mini_distance
            # print("Processing: " +
            #       str(round(len(self.route) / total * 100, 2)) + "%")
            if not temp_nodes:
                break
        return [node.city for node in self.route], self.total_distance


class TwoOpt(Graph):
    def __init__(self, nodes, isNNH):
        super().__init__(nodes)
        if isNNH:
            nearest_neighbor = NearestNeighbor(nodes)
            nearest_neighbor.find_shortest_path()
            self.nodes = nearest_neighbor.route

    def find_shortest_path(self):
        total = len(self.nodes)
        best_route = self.nodes
        mini_distance = self._calcu_distance(best_route)
        improved = True
        while improved:
            improved = False
            for c in range(1, total - 1):
                for k in range(c + 1, total):
                    # reverse at c to k - 1
                    new_route = best_route[:c] + \
                        best_route[c:k + 1][::-1] + best_route[k + 1:]
                    distance = self._calcu_distance(new_route)
                    # print("Current: %.4f Best distance: %.4f" % (round(distance, 4)
                    #       , round(mini_distance, 4)))
                    if distance < mini_distance:
                        mini_distance = distance
                        best_route = new_route
                        improved = True

        return [node.city for node in best_route], mini_distance
