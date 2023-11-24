import data
from tsp import TSPRoute, City
from annealing import AnnealingSimulator

if __name__ == '__main__':
    cities = data.read_data()
    # print([str(c) for c in cities])
    algo = AnnealingSimulator(cities)
    print(algo.route.route_length())
    # algo.route.draw_route()
