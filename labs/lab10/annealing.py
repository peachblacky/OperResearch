from tsp import TSPRoute, City
import random

random.seed(42)


def anneal(cities: [City], temperature : int):
    # random.shuffle(cities)
    starting_route = TSPRoute(cities)
    print('Starting route is : ' + str(starting_route))
    return starting_route