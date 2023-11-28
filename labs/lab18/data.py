from labs.lab18.placement import City


def read_data(file_path: str):
    with open(file_path) as f:
        lines = f.readlines()
        parameters = lines[2].strip().split(" ")
        dimension = int(parameters[0])
        cost_per_shop = int(parameters[-1])

        cities = []
        i = 4
        for city_index in range(dimension):
            distances = []
            for client_index in range(dimension):
                line = lines[i].strip().split(" ")
                distances.append(int(line[-1]))
                i += 1
            cities.append(City(city_index, distances))

        return cities, cost_per_shop
