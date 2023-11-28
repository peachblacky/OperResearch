import data
from tabu_search import TabuSearcher

if __name__ == '__main__':
    cities, cost_per_shop = data.read_data('data/euq/111.txt')
    print(cities[0].distances)
    searcher = TabuSearcher(cities)
    print(searcher.cur_combination)
    print('Starting cost is ' + str(searcher.calculate_cost()))

