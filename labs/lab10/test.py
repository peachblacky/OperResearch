import data
from tsp import TSPRoute, City
from annealing import AnnealingSimulator

if __name__ == '__main__':
    # cities = data.read_data("./data/wi29.tsp")
    # cities = data.read_data("./data/dj38.tsp")
    cities = data.read_data("./data/qa194.tsp")
    # print([str(c) for c in cities])
    algo = AnnealingSimulator(cities, cool_down_coef=0.99)
    # print(algo.route.route_length())
    # algo.route.draw_route()
    solution = algo.anneal()
    print(str(solution))
    print(solution.route_length())
    solution.draw_route()
