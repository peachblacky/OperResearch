from tsp import TSPRoute, City
import random

random.seed(42)


class AnnealingSimulator:
    def __init__(self, cities: [City], starting_temperature: float = 100, cool_down_coef: float = 0.95):
        self.temperature = starting_temperature
        self.cool_down_coef = cool_down_coef
        random.shuffle(cities)
        self.route = TSPRoute(cities)
        print('Starting route is : ' + str(self.route))

    def anneal(self):
        pass
