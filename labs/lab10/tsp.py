import numpy as np


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return np.linalg.norm((self.x - other.x, self.y - other.y))

    def __str__(self):
        return 'City : x=' + str(self.x) + ', y=' + str(self.y)


class TSPRoute:
    def __init__(self, route: [City]):
        self.route = route
        self.length = len(route)

    def get_2opt_neighbour(self, first_index, second_index):
        new_route = []
        for c in self.route[:first_index]:
            new_route.append(c)
        for i in range(second_index - 1, first_index, -1):
            new_route.append(self.route[i])
        for c in self.route[second_index:]:
            new_route.append(c)

        return TSPRoute(new_route)
