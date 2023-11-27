import math

from tsp import TSPRoute, City
import random
import numpy as np

random.seed(42)
np.random.seed(42)


class AnnealingSimulator:
    def __init__(self, cities: [City], starting_temperature: float = -1, cool_down_coef: float = 0.95):
        self.cool_down_coef = cool_down_coef
        random.shuffle(cities)
        self.route = TSPRoute(cities)
        self.temperature = self.__calculate_starting_temperature() if starting_temperature < 0 else starting_temperature
        self.stop_parameter = 50
        self.logging_frequency = 10
        print('Starting route is : ' + str(self.route))
        print('Starting route length : ' + str(self.route.route_length()))
        print('Starting temperature is : ' + str(self.temperature))

    def anneal(self):
        active = True
        best_route = self.route
        epoch = 0
        unchanged_iterations = 0
        while active:
            unchanged_iterations += 1
            for _ in range(self.route.cities_number):
                neighbour = self.select_random_neighbour()
                cur_route_length = self.route.route_length()
                neighbour_route_length = neighbour.route_length()
                delta = cur_route_length - neighbour_route_length
                if delta >= 0:
                    self.route = neighbour
                else:
                    exponential_power = delta / self.temperature
                    if random.random() < math.exp(exponential_power):
                        self.route = neighbour
                if self.route.route_length() < best_route.route_length():
                    best_route = self.route
                    unchanged_iterations = 0
            self.temperature *= self.cool_down_coef
            if unchanged_iterations > self.stop_parameter:
                active = False
            if epoch % self.logging_frequency == 0:
                self.print_progress(epoch, best_route)
            epoch += 1

        return best_route

    def print_progress(self, epoch, cur_best_route: TSPRoute):
        print('Epoch ' + str(epoch) + ' Temp: ' + str(self.temperature) + '. Cur. best: ' + str(cur_best_route.route_length()))

    def select_random_neighbour(self):
        swapping_indexes = np.random.choice(self.route.cities_number, 2)
        swapping_indexes.sort()
        return self.route.get_2opt_neighbour(swapping_indexes[0], swapping_indexes[1])

    def __calculate_starting_temperature(self):
        max_delta = 0
        for i in range(self.route.cities_number - 1):
            for j in range(i + 1, self.route.cities_number):
                neighbour = self.route.get_2opt_neighbour(i, j)
                cur_route_length = self.route.route_length()
                neighbour_route_length = neighbour.route_length()
                delta = cur_route_length - neighbour_route_length
                if delta > max_delta:
                    max_delta = delta
        return max_delta


