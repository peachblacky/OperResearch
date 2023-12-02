import numpy as np
import matplotlib.pyplot as plt


class City:
    def __init__(self, index: int, distances: [int]):
        self.city_index = index
        self.distances = np.array(distances)

    def find_nearest_shop_distance(self, opened_shops: [bool]):
        return min(self.distances[opened_shops])


class TabuSearchCombination:
    def __init__(self, combination: [int]):
        self.combination = combination

    def get_hamming_neighbour(self, indexes: [int]):
        new_combination = self.combination.copy()
        new_combination[indexes] ^= 1
        return TabuSearchCombination(new_combination)

    def get_hamming_distance(self, other):
        return np.count_nonzero(self.combination != other.combination)
