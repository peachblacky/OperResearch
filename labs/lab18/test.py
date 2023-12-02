import data
from tabu_search import TabuSearcher

if __name__ == '__main__':
    cities, cost_per_shop = data.read_data('data/euq/1711.txt')
    searcher = TabuSearcher(cities)
    print('Starting cost is ' + str(searcher.calculate_cost(searcher.cur_combination)))
    best_combination, solution_cost = searcher.solve()
    print('Solution cost: ' + str(solution_cost))
    print('Solution: ' + str(searcher.get_combination_cities(best_combination)))

