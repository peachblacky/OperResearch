from algorithm import solveDynamicaly, solveGreedy

test_files = [
    'data/a_example.in',
    'data/b_small.in',
    'data/c_medium.in',
    # 'data/d_quite_big.in',
    # 'data/e_also_big.in'
]

for input_file_path in test_files:
    with open(input_file_path, 'r') as file:
        input = file.read().replace('\n', ' ')
    # print(data)
    input = input.strip()
    input = input.split(" ")

    print('TEST ' + input_file_path)

    W = int(input[0])
    total_items = int(input[1])
    weights = [int(x) for x in input[2:]]
    costs = [int(x) for x in input[2:]]  # weights are also costs here

    print('Max weight is : ' + str(W))
    # print(str(total_items))
    print(str(weights))

    result_cost, result_config = solveDynamicaly(W, total_items, weights, costs)
    # result_cost, result_config = solveGreedy(W, total_items, weights)
    print('Best weight is : ' + str(result_cost))
    print('Best config is : ' + str(result_config))
    print("\n\n\n")
    # break
