from algorithms import NearestNeighbor, TwoOpt, BruteForce
from time import time


def create_nodes(file):
    from os import access, path, R_OK
    if path.isfile(file) and access(file, R_OK):
        try:
            from csv import reader
            from graph import Node
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
    parser.add_argument('--algo', choices=['NNH',
                                           'BruteForce', "TwoOpt"])
    return parser.parse_args()


def main():
    start = time()
    arg = init_args()
    nodes = create_nodes(arg.file)
    if arg.algo == 'BruteForce':
        algorithm = BruteForce(nodes)
    elif arg.algo == "TwoOpt":
        algorithm = TwoOpt(nodes)
    else:
        algorithm = NearestNeighbor(nodes)
    route, distance = algorithm.find_shortest_path()
    print("File input:", arg.file)
    print(" --> ".join(route))
    print("Total of distance:", str(distance))
    print("Total of city:", len(route))
    print("Time run:", time() - start)


if __name__ == "__main__":
    main()
