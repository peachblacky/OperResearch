import random
import numpy as np
from objects import City, TabuSearchCombination
from collections import deque

np.random.seed(42)


class TabuSearcher:
    cur_combination: TabuSearchCombination

    def __init__(self, cities: [City], cost_per_shop=3000, neighbourhood_probability=0.25, neighbourhood_radius=2,
                 history_length=5):
        self.cities = cities
        self.cities_number = len(cities)
        self.cost_per_shop = cost_per_shop
        self.neighbourhood_probability = neighbourhood_probability
        self.neighbourhood_radius = neighbourhood_radius
        self.history_length = history_length

        self.generate_starting_combination()

        self.tabu_list = deque()
        self.tabu_list = deque()

    def solve(self):
        active = True
        best_route = self.cur_combination
        epoch = 0
        unchanged_iterations = 0
        while active:
            # TODO
            pass

    def is_tabu(self, indexes: [int]):
        return indexes in self.tabu_list

    def update_tabu_v1(self, indexes: [int]):
        self.tabu_list.append(indexes)
        if len(self.tabu_list) > self.history_length:
            self.tabu_list.popleft()

    def generate_starting_combination(self):
        combination = np.zeros(self.cities_number, dtype='int')
        number_of_shops = np.random.randint(0, self.cities_number // 5)
        shop_indexes = set(np.random.randint(0, self.cities_number, number_of_shops))
        combination[list(shop_indexes)] = 1
        self.cur_combination = TabuSearchCombination(combination)

    def calculate_cost(self, combination : TabuSearchCombination):
        cost = 0
        cur_combination_bool = combination.combination != 0
        for city_index in range(self.cities_number):
            if combination.combination[city_index] == 1:
                cost += self.cost_per_shop
            else:
                cost += self.cities[city_index].find_nearest_shop_distance(cur_combination_bool)
        return cost

    def __get_stochastic_neighbourhood(self):
        neighbourhood = []
        for i in range(self.cities_number - 1):
            for j in range(i + 1, self.cities_number):
                if np.random.random() < self.neighbourhood_probability and not self.is_tabu([i, j]):
                    neighbourhood.append(self.cur_combination.get_hamming_neighbour([i, j]))
        return neighbourhood
