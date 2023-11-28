import numpy as np
import matplotlib.pyplot as plt


class City:
    def __init__(self, index: int, client_distances: [int]):
        self.city_index = index
        self.client_distances = client_distances

