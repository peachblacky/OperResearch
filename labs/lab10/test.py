import data
from tsp import TSPRoute, City
from annealing import anneal

if __name__ == '__main__':
    cities = data.read_data()
    print([str(c) for c in cities])
    route = anneal(cities, 1)
    route.draw_route()
