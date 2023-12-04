from labs.lab18.objects import City


def read_data(file_path: str):
    with open(file_path) as f:
        lines = f.readlines()
        parameters = lines[2].strip().split(" ")
        dimension = int(parameters[0])
        cost_per_shop = int(parameters[-1])

        city_dict = dict()
        for line in lines[4:]:
            line_data = [a for a in line.strip().split(" ") if a != '']
            city_index = int(line_data[0]) - 1
            client_index = int(line_data[1]) - 1
            transportation_cost = int(line_data[2])
            if city_index not in city_dict:
                city_dict[city_index] = City(city_index, [100000] * dimension)
            city_dict[city_index].add_distance(client_index, transportation_cost)

        # i = 4
        # for city_index in range(dimension):
        #     distances = [0] * dimension
        #     for client_index in range(dimension):
        #         distances.append(int(line[-1]))
        #         i += 1
        #     cities.append(City(city_index, distances))

        return list(city_dict.values()), cost_per_shop
