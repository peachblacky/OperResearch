import random

import numpy as np

np.random.seed(42)


class TabuSearcher:
    def __init__(self, cities, cost_per_shop = 3000, neighbourhood_probability=0.25):
        self.cities = cities
        self.neighbourhood_probability = neighbourhood_probability

        self.cur_combination = np.zeros(100)
        self.generate_starting_combination()

        self.cost_per_shop = cost_per_shop

    def generate_starting_combination(self):
        number_of_shops = np.random.randint(0, 101)
        shop_indexes = set(np.random.randint(0, 100, number_of_shops))
        self.cur_combination[shop_indexes] = 1
