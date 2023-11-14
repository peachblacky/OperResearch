from algorithm import solve

test_files = ['data/a_example.in', 'data/b_small.in', 'data/c_medium.in', 'data/d_quite_big.in', 'data/e_also_big.in']

for input_file_path in test_files:
    with open(input_file_path, 'r') as file:
        input = file.read().replace('\n', ' ')
    # print(data)
    input = input.strip()
    input = input.split(" ")

    W = int(input[0])
    total_items = int(input[1])
    weights = [int(x) for x in input[2:]]
    costs = [int(x) for x in input[2:]]  # weights are also costs here

    # print(str(W))
    # print(str(total_items))
    # print(str(weights))

    result_cost, result_config = solve(W, total_items, weights, costs)
    print(str(result_cost))
    print(str(result_config))
    break
