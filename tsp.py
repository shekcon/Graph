from node import Node
from graph import Graph
from csv import reader
from argparse import ArgumentParser
from time import time


def init_args():
    parser = ArgumentParser()
    parser.add_argument('file', help="city name, latitude, longitude")
    return parser.parse_args()


def main():
    arg = init_args()
    graph = Graph()
    with open(arg.file, 'r') as f:
        for row in reader(f):
            graph.add_node(
                Node(row[0], float(row[1].strip()), float(row[2].strip())))
    path, distance = graph.find_shortest_path()
    print("-->".join(path))
    print("Total of distance: " + str(distance))


if __name__ == "__main__":
    start = time()
    main()
    print("Time run:", time() - start)
