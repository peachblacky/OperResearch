# INPUT TEMPLATE  :  TOTAL_ENGINE_TYPES; [REQUIRED_PER_TYPE]; [COST_PER_TYPE]; [START_PRODUCING_PER_TYPE]
# sample in : 3; 1 1 1; 5 2 1; 2 2 2       3; 11 7 9; 5 2 1; 2 2 2     3; 11 11 13; 5 7 1; 2 2 2
# task input : 8; 20 10 50 20 80 40 20 50; 30 27 24 21 18 15 12 9; 1100 1050 1000 950 900 850 800 750
input_string = input()
input_string = input_string.split("; ")

total_engine_types = int(input_string[0])
required_engines_per_type = [int(s) for s in input_string[1].split(" ")]
cost_per_type = [int(s) for s in input_string[2].split(" ")]
start_producing_per_type = [int(s) for s in input_string[3].split(" ")]


total_engines_required = sum(required_engines_per_type)

dynamic_table = [[None for i in range(total_engines_required - required_engines_per_type[0] + 1)] for j in range(total_engine_types)]


for i in range(required_engines_per_type[0], total_engines_required + 1):
    value = i * cost_per_type[0]
    if i != 0:
        value += start_producing_per_type[0]
    dynamic_table[0][i - required_engines_per_type[0]] = value

for i in range(1, total_engine_types):
    for j in range(i + 1, total_engines_required + 1):
        for k in range(sum(required_engines_per_type[:i]), j + 1):  # searching for minimal value using prev row [Skj = min[0<=k<=j-1](S(k-1)j + f(x, y))]
            cval = dynamic_table[i-1][k-required_engines_per_type[0]] + (j - k) * cost_per_type[i]
            if j != k:
                cval += start_producing_per_type[i]
            tested_value = dynamic_table[i][j - required_engines_per_type[0]]
            if tested_value is None or cval <= tested_value:
                dynamic_table[i][j - required_engines_per_type[0]] = cval

# print(dynamic_table)
print(dynamic_table[total_engine_types - 1][total_engines_required - required_engines_per_type[0]])
