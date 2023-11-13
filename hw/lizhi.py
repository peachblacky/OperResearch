# INPUT TEMPLATE  :  TOTAL_STAGES; [BUY_COST]; [SELL_COST]; [MAINTAIN_COST]
# sample in : 6; 100 105 120 125 135 140; 80 75 70 60 50 40; 30 35 40 65 95 100
input_string = input()
input_string = input_string.split("; ")

TOTAL_STAGES = int(input_string[0])
BUY_COST = [int(s) for s in input_string[1].split(" ")]
SELL_COST = [int(s) for s in input_string[2].split(" ")]
MAINTAIN_COST = [int(s) for s in input_string[3].split(" ")]

dynamic_table = [[0 for i in range(TOTAL_STAGES)] for j in range(TOTAL_STAGES)]
# горизонтально - возраст лыж к данному этапу, вертикально - номер этапа
change_strategy = [[0 for i in range(TOTAL_STAGES)] for j in range(TOTAL_STAGES)]

for t in range(0, TOTAL_STAGES):  # варируем возраст лыж к 6му этапу
    KEEP_COST = MAINTAIN_COST[t] - SELL_COST[t]  # обслужили + продали после последней гонки
    CHANGE_COST = BUY_COST[TOTAL_STAGES-1] + MAINTAIN_COST[0] - SELL_COST[t] - SELL_COST[1]  # поменяли перед последней гонкой
    dynamic_table[TOTAL_STAGES - 1][t] = min(KEEP_COST, CHANGE_COST)
    change_strategy[TOTAL_STAGES - 1][t] = 0 if KEEP_COST < CHANGE_COST else 1

for stage in range(TOTAL_STAGES - 2, -1, -1):
    for t in range(0, stage + 1):
        KEEP_COST = MAINTAIN_COST[t] + dynamic_table[stage + 1][t + 1]  # оставили лыжи -> на следующем этапе они старше на 1 гонку
        CHANGE_COST = BUY_COST[stage] + MAINTAIN_COST[0] + dynamic_table[stage + 1][1] - SELL_COST[t - 1]  # поменяли лыжи -> на следующем этапе они новые
        dynamic_table[stage][t] = min(KEEP_COST, CHANGE_COST)
        change_strategy[stage][t] = 0 if KEEP_COST < CHANGE_COST else 1

cur_ski_age = 0
best_change_strategy = [0] * TOTAL_STAGES
for t in range(TOTAL_STAGES):  # обратный ход
    if change_strategy[t][cur_ski_age] == 1:
        best_change_strategy[t] = 1
        cur_ski_age = 1
        continue
    cur_ski_age += 1

best_cost = BUY_COST[0]+dynamic_table[0][0]
print('Best cost is ' + str(BUY_COST[0]+dynamic_table[0][0]))
print('Best strategy is ' + str(best_change_strategy))
# print(dynamic_table)
# print(change_strategy)