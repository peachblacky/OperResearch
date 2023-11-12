# INPUT TEMPLATE  :  TOTAL_ENGINE_TYPES; [REQUIRED_PER_TYPE]; [COST_PER_TYPE]; [START_PRODUCING_PER_TYPE]
# sample in : 3; 1 1 1; 5 2 1; 2 2 2       3; 11 7 9; 5 2 1; 2 2 2     3; 11 11 13; 5 7 1; 2 2 2
# task input : 8; 20 10 50 20 80 40 20 50; 30 27 24 21 18 15 12 9; 1100 1050 1000 950 900 850 800 750
input_string = input()
input_string = input_string.split("; ")

TOTAL_ENGINE_TYPES = int(input_string[0])
REQUIRED_PER_TYPE = [int(s) for s in input_string[1].split(" ")]
COST_PER_TYPE = [int(s) for s in input_string[2].split(" ")]
START_PRODUCTION_PER_TYPE = [int(s) for s in input_string[3].split(" ")]

TOTAL_REQUIRED = sum(REQUIRED_PER_TYPE)


dynamic_table = [[None for i in range(TOTAL_REQUIRED - REQUIRED_PER_TYPE[0] + 1)] for j in range(TOTAL_ENGINE_TYPES)]


for i in range(REQUIRED_PER_TYPE[0], TOTAL_REQUIRED + 1):
    value = i * COST_PER_TYPE[0]
    if i != 0:
        value += START_PRODUCTION_PER_TYPE[0]
    dynamic_table[0][i - REQUIRED_PER_TYPE[0]] = value

for i in range(1, TOTAL_ENGINE_TYPES):
    for j in range(i + 1, TOTAL_REQUIRED + 1):
        for k in range(sum(REQUIRED_PER_TYPE[:i]), j + 1):  # searching for minimal value using prev row [Skj = min[0<=k<=j-1](S(k-1)j + f(x, y))]
            cval = dynamic_table[i-1][k - REQUIRED_PER_TYPE[0]] + (j - k) * COST_PER_TYPE[i]
            if j != k:
                cval += START_PRODUCTION_PER_TYPE[i]
            tested_value = dynamic_table[i][j - REQUIRED_PER_TYPE[0]]
            if tested_value is None or cval <= tested_value:
                dynamic_table[i][j - REQUIRED_PER_TYPE[0]] = cval

# print(dynamic_table)
print(dynamic_table[TOTAL_ENGINE_TYPES - 1][TOTAL_REQUIRED - REQUIRED_PER_TYPE[0]])
