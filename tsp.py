from graph import NNH, Node
from time import time


def create_nodes(file):
    from os import access, path, R_OK
    if path.isfile(file) and access(file, R_OK):
        try:
            from csv import reader
            nodes = []
            with open(file, 'r') as f:
                for city, latitude, longitude in reader(f):
                    nodes.append(Node(city, latitude, longitude))
            return nodes
        except ValueError:
            error = "Invalid value\n"
    else:
        error = "Invalid file\n"
    from sys import exit, stderr
    stderr.write(error)
    exit(1)


def init_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('file', help="city name, latitude, longitude")
    return parser.parse_args()


def main():
    start = time()
    arg = init_args()
    graph = NNH()
    graph.add_node(create_nodes(arg.file))
    path, distance = graph.find_shortest_path()
    print("-->".join(path))
    print("Total of distance: " + str(distance))
    print("Time run:", time() - start)


if __name__ == "__main__":
    main()
