import data
import tsp


if __name__ == '__main__':
    cities = data.read_data()
    print([str(c) for c in cities])