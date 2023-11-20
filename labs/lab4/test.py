import algorithm as alg

test_file_name = "./data/knapPI_1_1000_1000.csv"
def test_dynamical(max_weight, total_items, weights, costs):
    result_cost, result_config = alg.solve_dynamically(max_weights, total_items, weights, costs)
    result_w = 0
    for i in range(len(result_config)):
        if result_config[i]:
            result_w += weights[i]
    print('Best dynamical cost is : ' + str(result_cost))
    print('Best dynamical weight is : ' + str(result_w))
    print('Best dynamical config is : ' + str(result_config))
    print("\n\n\n")

if __name__ == '__main__':
    max_weights, total_items, weights, costs = alg.read_input(test_file_name)
    test_dynamical(max_weights, total_items, weights, costs)


