import time

import algorithm as alg

test_file_name = "./data/knapPI_1_1000_1000.csv"


def test_dynamical(max_weight, total_items, weights, costs):
    result_cost, result_config = alg.solve_dynamically(max_weight, total_items, weights, costs)
    result_w = 0
    for i in range(len(result_config)):
        if result_config[i]:
            result_w += weights[i]
    print('Best dynamical cost is : ' + str(result_cost))
    # print('Best dynamical weight is : ' + str(result_w))
    # print('Best dynamical config is : ' + str(result_config))


def test_dynamical_tinkoff(max_weight, total_items, costs):
    result_cost = alg.solve_dynamically_tinkoff(max_weight, total_items, costs)
    print('Best dynamical cost is : ' + str(result_cost))


def test_g(max_weight, total_items, weights, costs):
    result_cost = alg.solve_g(max_weight, total_items, weights, costs)
    result_w = 0
    # for i in range(len(result_config)):
    #     if result_config[i]:
    #         result_w += weights[i]
    print('Best G cost is : ' + str(result_cost))
    # print('Best G weight is : ' + str(result_w))


def test_simple_greedy(max_weight, total_items, weights, costs):
    result_cost = alg.solve_greedy(max_weight, weights, costs)
    print('Best simple greedy cost is : ' + str(result_cost))


if __name__ == '__main__':
    max_weights, total_items, weights, costs = alg.read_input(test_file_name)
    # start = time.time_ns()
    # test_dynamical(max_weights, total_items, weights, costs)
    # test_g(max_weights, total_items, weights, costs)
    # test_simple_greedy(max_weights, total_items, weights, costs)
    test_dynamical_tinkoff(24, 7, [5, 4, 1, 3, 2, 2, 7])
    # end = time.time_ns()
    # print('G3/4 elapsed time is ' + str((end - start) / 10**9) + ' seconds')
