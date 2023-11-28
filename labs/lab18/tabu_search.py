import random
import numpy as np
from placement import City

np.random.seed(42)


class TabuSearcher:
    def __init__(self, cities: [City], cost_per_shop=3000, neighbourhood_probability=0.25):
        self.cities = cities
        self.cities_number = len(cities)
        self.neighbourhood_probability = neighbourhood_probability

        self.cur_combination = np.zeros(self.cities_number, dtype='int')
        self.generate_starting_combination()

        self.cost_per_shop = cost_per_shop

    def generate_starting_combination(self):
        number_of_shops = np.random.randint(0, self.cities_number // 5)
        shop_indexes = set(np.random.randint(0, self.cities_number, number_of_shops))
        self.cur_combination[list(shop_indexes)] = 1

    def calculate_cost(self):
        cost = 0
        cur_combination_bool = self.cur_combination != 0
        for city_index in range(self.cities_number):
            if self.cur_combination[city_index] == 1:
                cost += self.cost_per_shop
            else:
                cost += self.cities[city_index].find_nearest_shop_distance(cur_combination_bool)
        return cost
