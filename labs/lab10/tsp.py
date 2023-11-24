import numpy as np
import matplotlib.pyplot as plt


class City:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index

    def distance(self, other):
        return np.linalg.norm((self.x - other.x, self.y - other.y))

    def __str__(self):
        return 'City ' + str(self.index) + ' : x=' + str(self.x) + ', y=' + str(self.y)


class TSPRoute:
    def __init__(self, route: [City]):
        self.route = route
        self.cities_number = len(route)

    def __str__(self):
        result = ''
        for city in self.route:
            result += str(city.index) + ' -> '
        return result

    def route_length(self):
        total_length = 0
        for i in range(-1, self.cities_number - 1):
            cur_city = self.route[i]
            next_city = self.route[i + 1]
            total_length += cur_city.distance(next_city)
        return total_length

    def get_2opt_neighbour(self, first_index, second_index):
        new_route = []
        for c in self.route[:first_index]:
            new_route.append(c)
        for i in range(second_index - 1, first_index - 1, -1):
            new_route.append(self.route[i])
        for c in self.route[second_index:]:
            new_route.append(c)

        return TSPRoute(new_route)

    def draw_route(self):
        x = [c.x for c in self.route]
        x.append(x[0])
        y = [c.y for c in self.route]
        y.append(y[0])
        plt.plot(x, y, color='green', linestyle='dashed', linewidth=1,
                 marker='o', markerfacecolor='blue', markersize=4)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Route graph')
        plt.show()
