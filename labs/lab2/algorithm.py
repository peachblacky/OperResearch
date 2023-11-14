import numpy as np


def add_item_to_configuration(prev_config, new_item_index):
    next_config = prev_config.copy()
    next_config[new_item_index] += 1
    return next_config


def solveDynamicaly(max_weight, total_items, weights, costs):
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

    # print(dynamic_table)
    # print(configurations)
    #
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


def solveGreedy(max_weight, total_items, weights):
    weights = np.array(weights)
    indexes = np.array([i for i in range(total_items)])
    sorted_weight_indexes = weights.argsort()
    indexes_sorted = indexes[sorted_weight_indexes[::-1]]
    weights_sorted = weights[sorted_weight_indexes[::-1]]

    current_weight = 0
    optimal_configuration = np.zeros(total_items)
    for i in range(len(weights_sorted)):
        w = weights_sorted[i]
        new_weight = current_weight + w
        if new_weight <= max_weight:
            current_weight += w
            optimal_configuration[indexes_sorted[i]] = 1
    return current_weight, optimal_configuration
