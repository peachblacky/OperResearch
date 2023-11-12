# INPUT IN TEMPLATE : TOTAL_WEIGHT; ITEMS_NUMBER; [ITEM_WEIGHT]; [ITEM_COST]
# sample in : 17; 4; 2 5 6 7; 15 29 35 46
input_string = input()
input_string = input_string.split("; ")

W = int(input_string[0])
total_items = int(input_string[1])
weights = [int(s) for s in input_string[2].split(" ")]
costs = [int(s) for s in input_string[3].split(" ")]

dynamic_table = [W + 1]
configurations = [W + 1]

dynamic_table[0] = 0 if weights[0] > 1 else costs[0]
configurations[0] = [0] * total_items


def add_item_to_configuration(prev_config, new_item_index):
    next_config = prev_config.copy()
    next_config[new_item_index] += 1
    return next_config


for w in range(1, W + 1):
    max_cost = 0
    added_item = None
    prev_configuration = None
    for i in range(total_items):
        space_left = w - weights[i]
        cur_cost = dynamic_table[space_left] + costs[i] if space_left > -1 else 0
        if cur_cost > max_cost:
            max_cost = cur_cost
            added_item = i
            prev_configuration = configurations[space_left]
    if added_item is None or prev_configuration is None:
        dynamic_table.append(0)
        configurations.append([0] * total_items)
        continue
    dynamic_table.append(max_cost)
    new_config = add_item_to_configuration(prev_configuration, added_item)
    configurations.append(new_config)

print(dynamic_table)
print(configurations)

print("Best cost : " + str(dynamic_table[-1]))
print("Best configuration : " + str(configurations[-1]))