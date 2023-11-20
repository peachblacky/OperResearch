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

def extract_subset(weights, costs, i, j):
    max_cost = min(costs[i], costs[i])
    weight_subset = []
    cost_subset = []
    for

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
    for i in range(total_items - 1):
        for k in range(i + 1, total_items):




def solve_greedy(max_weight, total_items, weights):
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
