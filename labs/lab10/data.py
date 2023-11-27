from labs.lab10.tsp import City


def read_data(file_path : str):
    with open(file_path) as f:
        lines = f.readlines()
        i = 0
        while lines[i].strip() != 'NODE_COORD_SECTION':
            i += 1
        i += 1
        cities = []
        while lines[i].strip() != 'EOF':
            line = lines[i].strip().split(" ")
            x_coord = float(line[1])
            y_coord = float(line[2])
            index = int(line[0])
            cities.append(City(x_coord, y_coord, index))
            i += 1
        return cities
