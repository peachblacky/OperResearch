import math
import random
import sys

import numpy as np
from objects import City, TabuSearchCombination
from collections import deque


# np.random.seed(42)


class TabuAnnealing:
    cur_combination: TabuSearchCombination
    # best_combination: TabuSearchCombination
    best_cost: int

    def __init__(self,
                 cities: [City],
                 cost_per_shop=3000,
                 neighbourhood_probability=0.25,
                 neighbourhood_radius=2,
                 history_length=3,
                 starting_temperature: float = -1,
                 cool_down_coef: float = 0.95):
        self.cities = cities
        self.cities_number = len(cities)
        self.cost_per_shop = cost_per_shop
        self.neighbourhood_probability = neighbourhood_probability
        self.neighbourhood_radius = neighbourhood_radius
        self.history_length = history_length
        self.stop_threshold = 300

        self.cool_down_coef = cool_down_coef
        self.temperature = starting_temperature

        self.generate_starting_combination()

        self.tabu_list = deque()
        self.tabu_list = deque()

        self.best_cost = sys.maxsize
        self.best_combination = None

    def solve(self) -> (TabuSearchCombination, int):
        active = True
        iteration = 0
        unchanged_iterations = 0
        while active:
            unchanged_iterations += 1
            for _ in range(self.cities_number):
                neighbour = self.__select_random_neighbour()
                cur_cost = self.calculate_cost(self.cur_combination)
                neighbour_cost = self.calculate_cost(neighbour)
                delta = cur_cost - neighbour_cost
                if delta >= 0:
                    self.cur_combination = neighbour
                else:
                    exponential_power = delta / self.temperature
                    if random.random() < math.exp(exponential_power):
                        self.cur_combination = neighbour
                if self.calculate_cost(self.cur_combination) < self.best_cost:
                    self.best_combination = self.cur_combination
                    self.best_cost = self.calculate_cost(self.cur_combination)
                    unchanged_iterations = 0
            self.temperature *= self.cool_down_coef

            if unchanged_iterations > self.stop_threshold:
                active = False

            if iteration % 10 == 0:
                print('Iteration ' + str(iteration) + ': T= ' + str(self.temperature) + ' Cost= ' + str(self.best_cost))
            iteration += 1
        return self.best_combination, self.best_cost

    def generate_starting_combination(self):
        combination = np.zeros(self.cities_number, dtype='int')
        number_of_shops = np.random.randint(0, self.cities_number // 5)
        shop_indexes = set(np.random.randint(0, self.cities_number, number_of_shops))
        combination[list(shop_indexes)] = 1
        self.cur_combination = TabuSearchCombination(combination)

    def calculate_cost(self, combination: TabuSearchCombination) -> int:
        cost = 0
        cur_combination_bool = combination.combination != 0
        for city_index in range(self.cities_number):
            if combination.combination[city_index] == 1:
                cost += self.cost_per_shop
            else:
                cost += self.cities[city_index].find_nearest_shop_distance(cur_combination_bool)
        return cost

    @staticmethod
    def get_combination_cities(combination: TabuSearchCombination) -> [int]:
        return [i + 1 for i, elem in enumerate(combination.combination) if elem == 1]

    def __is_tabu(self, indexes: [int]) -> bool:
        return indexes in self.tabu_list

    def __update_tabu_v1(self, indexes: [int]):
        self.tabu_list.append(indexes)
        if len(self.tabu_list) > self.history_length:
            self.tabu_list.popleft()

    def __select_random_neighbour(self):
        for i in range(self.cities_number - 1):
            for j in range(i + 1, self.cities_number):
                if np.random.random() < self.neighbourhood_probability and not self.__is_tabu([i, j]):
                    self.__update_tabu_v1([i, j])
                    return self.cur_combination.get_hamming_neighbour([i, j])
