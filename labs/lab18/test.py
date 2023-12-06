import data
from tabu_search import TabuSearcher
from tabu_annealing import TabuAnnealing


def test_tabu():
    for test_number in range(5):
        searcher = TabuSearcher(cities, neighbourhood_probability=0.2, history_length=10)
        print(
            'TEST ' + str(test_number) + ' Starting cost is ' + str(searcher.calculate_cost(searcher.cur_combination)))
        best_combination, solution_cost = searcher.solve()
        print('TEST ' + str(test_number) + ' Solution cost: ' + str(solution_cost))
        print('TEST ' + str(test_number) + ' Solution: ' + str(searcher.get_combination_cities(best_combination)))


def test_tabu_annealing():
    for test_number in range(1):
        searcher = TabuAnnealing(
            cities,
            neighbourhood_probability=0.25,
            history_length=3,
            starting_temperature=100000,
            cool_down_coef=0.99)
        print(
            'TEST ' + str(test_number) + ' Starting cost is ' + str(searcher.calculate_cost(searcher.cur_combination)))
        best_combination, solution_cost = searcher.solve()
        print('TEST ' + str(test_number) + ' Solution cost: ' + str(solution_cost))
        print('TEST ' + str(test_number) + ' Solution: ' + str(searcher.get_combination_cities(best_combination)))


if __name__ == '__main__':
    # cities, cost_per_shop = data.read_data('data/euq/1711.txt')
    # cities, cost_per_shop = data.read_data('data/euq/2711.txt')
    cities, cost_per_shop = data.read_data('data/rupture/1632.txt')
    test_tabu()
    # test_tabu_annealing()

