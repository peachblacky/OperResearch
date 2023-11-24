import data
from tsp import TSPRoute, City


if __name__ == '__main__':
    cities = data.read_data()
    print([str(c) for c in cities])

    route = TSPRoute(cities)
