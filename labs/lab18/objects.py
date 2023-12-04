import numpy as np
import matplotlib.pyplot as plt


class City:
    def __init__(self, index: int, distances: [int]):
        self.city_index = index
        self.distances = np.array(distances)

    def add_distance(self, client_index, distance):
        self.distances[client_index] = distance

    def find_nearest_shop_distance(self, opened_shops: [bool]):
        return min(d for d in self.distances[opened_shops]) if True in opened_shops else 100000


class TabuSearchCombination:
    def __init__(self, combination: [int]):
        self.combination = combination

    def get_hamming_neighbour(self, indexes: [int]):
        new_combination = self.combination.copy()
        new_combination[indexes] ^= 1
        return TabuSearchCombination(new_combination)

    def get_hamming_distance(self, other):
        return np.count_nonzero(self.combination != other.combination)
