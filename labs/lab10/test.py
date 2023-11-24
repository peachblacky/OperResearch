import data
from tsp import TSPRoute, City


if __name__ == '__main__':
    cities = data.read_data()
    print([str(c) for c in cities])

    route = TSPRoute(cities)
    print(str(route))
    opt2_neighbour = route.get_2opt_neighbour(15, 29)
    print(str(opt2_neighbour))