import csv

import numpy as np


# В первой строчке вместимость рюкзака
# В следующих строчках параметры предметов в виде пар ценность (первый столбец) - вес (второй столбец)
def read_input(input_file_name: str):
    weighs = []
    costs = []
    max_weight = 0
    with open(input_file_name, newline='') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] == "knapsack capacity":
                max_weight = int(row[1])
                continue
            costs.append(int(row[0]))
            weighs.append(int(row[1]))
    return max_weight, len(costs), weighs, costs



def solve_dynamically(max_weight, total_items, weights, costs):
    dynamic_table = [[0 for _ in range(max_weight + 1)] for _ in range(total_items)]

    for w in range(max_weight):
        dynamic_table[0][w] = costs[0] if weights[0] <= w else 0

    for item in range(1, total_items):
        item_weight = weights[item]
        item_cost = costs[item]
        for w in range(max_weight + 1):
            pick_cost = dynamic_table[item - 1][w - item_weight] + item_cost if item_weight <= w else 0
            skip_cost = dynamic_table[item - 1][w]
            dynamic_table[item][w] = max(pick_cost, skip_cost)

    configuration = [0] * total_items
    capacity = max_weight
    item_i = total_items - 1
    while capacity > 0 and item_i > 0:
        if dynamic_table[item_i][capacity] != dynamic_table[item_i - 1][capacity]:
            configuration[item_i] = 1
            capacity -= weights[item_i]
        item_i -= 1
    if capacity > weights[item_i]:
        configuration[0] = 1
    return dynamic_table[-1][-1], configuration


def solve_g(max_weight, total_items, weights, costs):
    best_cost = max(costs)
    costs = np.array(costs)
    weights = np.array(weights)
    weights = weights[costs.argsort()]
    costs = costs[costs.argsort()]
    for i in range(total_items - 1):
        for k in range(i + 1, total_items):
            pair_weight = weights[i] + weights[k]
            if pair_weight > max_weight:
                continue
            cost_subset, weight_subset = costs[:i], weights[:i]
            subset_solution = solve_greedy(max_weight - pair_weight, weight_subset, cost_subset)
            current_cost = costs[i] + costs[k] + subset_solution
            if current_cost > best_cost:
                best_cost = current_cost
    return best_cost


def solve_greedy(max_weight, weights, costs):
    stacked = np.stack([costs, weights], axis=1)
    stacked = stacked[(stacked[:, 0] / stacked[:, 1]).argsort()]
    stacked = stacked[::-1]
    running_cost = 0
    W = max_weight
    for e in stacked:
        cur_weight = e[1]
        if W - cur_weight >= 0:
            W -= cur_weight
            running_cost += e[0]
    max_cost = max(costs) if len(costs) > 0 else 0
    return max(running_cost, max_cost)
