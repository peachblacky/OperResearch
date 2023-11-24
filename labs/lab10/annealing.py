from tsp import TSPRoute, City
import random
import numpy as np

random.seed(42)


class AnnealingSimulator:
    def __init__(self, cities: [City], starting_temperature: float = 100, cool_down_coef: float = 0.95):
        self.temperature = starting_temperature
        self.cool_down_coef = cool_down_coef
        random.shuffle(cities)
        self.route = TSPRoute(cities)
        print('Starting route is : ' + str(self.route))

    def anneal(self):
        active = True
        while active:
            for _ in range(self.route.cities_number):
                neighbour = self.select_random_neighbour()
                cur_route_length = self.route.route_length()
                neighbour_route_length = neighbour.route_length()
                delta = cur_route_length - neighbour_route_length
                if delta >= 0:
                    self.route = neighbour
                else:
                    #TODO
                    pass

    def select_random_neighbour(self):
        swapping_indexes = np.random.choice(self.route.cities_number, 2)
        return self.route.get_2opt_neighbour(swapping_indexes[0], swapping_indexes[1])

    def __calculate_starting_temperature(self):
        # TODO max distance to the neighbour of the starting_route
        pass
