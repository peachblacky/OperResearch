import data
from tabu_search import TabuSearcher

if __name__ == '__main__':
    # cities, cost_per_shop = data.read_data('data/euq/1711.txt')
    cities, cost_per_shop = data.read_data('data/rupture/1632.txt')
    for test_number in range(10):
        searcher = TabuSearcher(cities)
        print('TEST ' + str(test_number) + ' Starting cost is ' + str(searcher.calculate_cost(searcher.cur_combination)))
        best_combination, solution_cost = searcher.solve()
        print('TEST ' + str(test_number) + ' Solution cost: ' + str(solution_cost))
        print('TEST ' + str(test_number) + ' Solution: ' + str(searcher.get_combination_cities(best_combination)))

