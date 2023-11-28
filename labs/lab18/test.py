import data
import tabu_search

if __name__ == '__main__':
    cities, cost_per_shop = data.read_data('data/euq/111.txt')
    print(cities[0].client_distances)
