# INPUT TEMPLATE  :  TOTAL_STAGES; [BUY_COST]; [SELL_COST]; [MAINTAIN_COST]
# sample in : 6; 100 105 120 125 135 140; 80 75 70 60 50 40; 30 35 40 65 95 100
input_string = input()
input_string = input_string.split("; ")

TOTAL_STAGES = int(input_string[0])
BUY_COST = [int(s) for s in input_string[1].split(" ")]
SELL_COST = [int(s) for s in input_string[2].split(" ")]
MAINTAIN_COST = [int(s) for s in input_string[3].split(" ")]


dynamic_table = [W + 1]

dynamic_table[0] = 0 if BUY_COST[0] > 1 else SELL_COST[0]


def add_item_to_configuration(prev_config, new_item_index):
    next_config = prev_config.copy()
    next_config[new_item_index] += 1
    return next_config


for w in range(1, W + 1):
    max_cost = 0
    dynamic_table.append(max_cost)

print(dynamic_table)

print("Best cost : " + str(dynamic_table[-1]))
