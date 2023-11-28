import numpy as np
import matplotlib.pyplot as plt


class City:
    def __init__(self, index: int, distances: [int]):
        self.city_index = index
        self.distances = np.array(distances)

    def find_nearest_shop_distance(self, opened_shops: [bool]):
        return min(self.distances[opened_shops])
