from abc import abstractmethod
from math import sqrt


class Node:
    def __init__(self, city, latitude, longitude):
        self.city = city
        self.latitude = float(latitude.strip())
        self.longitude = float(longitude.strip())


class Graph:
    
    def __init__(self, nodes):
        self.nodes = nodes
        self.route = []
        self.total_distance = 0

    def _calcu_distance(self, route):
        distance = 0
        for i in range(1, len(route)):
            distance += sqrt((route[i - 1].latitude - route[i].latitude) ** 2 +
                             (route[i - 1].longitude - route[i].longitude) ** 2)
        return distance

    @abstractmethod
    def find_shortest_path(self):
        raise NotImplementedError()
