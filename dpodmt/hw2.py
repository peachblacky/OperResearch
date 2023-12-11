#############################
# the code is taken from the examples section for the MIP package (https://docs.python-mip.com/en/latest/examples.html)
# supplement the example code with your own one below

from itertools import product
from sys import stdout as out
from mip import Model, xsum, minimize, BINARY, CBC
import time

# names of places to visit
places = ['Antwerp', 'Bruges', 'C-Mine', 'Dinant', 'Ghent',
          'Grand-Place de Bruxelles', 'Hasselt', 'Leuven',
          'Mechelen', 'Mons', 'Montagne de Bueren', 'Namur',
          'Remouchamps', 'Waterloo']

# distances in an upper triangular matrix
dists = [[83, 81, 113, 52, 42, 73, 44, 23, 91, 105, 90, 124, 57],
         [161, 160, 39, 89, 151, 110, 90, 99, 177, 143, 193, 100],
         [90, 125, 82, 13, 57, 71, 123, 38, 72, 59, 82],
         [123, 77, 81, 71, 91, 72, 64, 24, 62, 63],
         [51, 114, 72, 54, 69, 139, 105, 155, 62],
         [70, 25, 22, 52, 90, 56, 105, 16],
         [45, 61, 111, 36, 61, 57, 70],
         [23, 71, 67, 48, 85, 29],
         [74, 89, 69, 107, 36],
         [117, 65, 125, 43],
         [54, 22, 84],
         [60, 44],
         [97],
         []]

# number of nodes and list of vertices
n, V = len(dists), set(range(len(dists)))

# distances matrix
c = [[0 if i == j
      else dists[i][j - i - 1] if j > i
else dists[j][i - j - 1]
      for j in V] for i in V]

model = Model(solver_name=CBC)

# binary variables indicating if arc (i,j) is used on the route or not
x = [[model.add_var(var_type=BINARY) for j in V] for i in V]

# continuous variable to prevent subtours: each city will have a
# different sequential id in the planned route except the first one
y = [model.add_var() for i in V]

# objective function: minimize the distance
model.objective = minimize(xsum(c[i][j] * x[i][j] for i in V for j in V))

# constraint : leave each city only once
for i in V:
    model += xsum(x[i][j] for j in V - {i}) == 1

# constraint : enter each city only once
for i in V:
    model += xsum(x[j][i] for j in V - {i}) == 1

# subtour elimination
for (i, j) in product(V - {0}, V - {0}):
    if i != j:
        model += y[i] - (n + 1) * x[i][j] >= y[j] - n

# optimizing
model.optimize()

# checking if a solution was found
if model.num_solutions:
    out.write('route with total distance %g found: %s'
              % (model.objective_value, places[0]))
    nc = 0
    while True:
        nc = [i for i in V if x[nc][i].x >= 0.99][0]
        out.write(' -> %s' % places[nc])
        if nc == 0:
            break
    out.write('\n')

#### YOUR CODE HERE VVVVVVVVVVVVVVVVVV

# TASK 1

print()
print('### TASK 1')

mip = model.objective_value
new_model = Model(solver_name=CBC)

x = [[new_model.add_var() for j in V] for i in V]

y = [new_model.add_var() for i in V]

new_model.objective = minimize(xsum(c[i][j] * x[i][j] for i in V for j in V))

for i in V:
    new_model += xsum(x[i][j] for j in V - {i}) == 1

for i in V:
    new_model += xsum(x[j][i] for j in V - {i}) == 1

for (i, j) in product(V - {0}, V - {0}):
    if i != j:
        new_model += y[i] - (n + 1) * x[i][j] >= y[j] - n

new_model.optimize()

lp = new_model.objective_value

print('F_mip = ', mip)
print('F_lp = ', lp)
print('F_mip - F_lp = ', mip - lp)
print('###')
print()

# TASK 2

print('### ЗАДАНИЕ 2')
new_model.clear()

x = [[new_model.add_var(var_type=BINARY) for j in V] for i in V]

new_model.objective = minimize(xsum(c[i][j] * x[i][j] for i in V for j in V))

for i in V:
    new_model += xsum(x[i][j] for j in V - {i}) == 1
for i in V:
    new_model += xsum(x[j][i] for j in V - {i}) == 1

new_model.optimize()

if new_model.num_solutions:
    print('Решение = ', new_model.objective_value)
    visited_places = V.copy()
    print('Путь: ')
    while True:
        nc = visited_places.pop()
        visited_places.add(nc)
        start = nc
        print(places[nc], end='')
        while True:
            for i in visited_places:
                if x[nc][i].x > 0.99:
                    nc = i
                    break
            print('->', places[nc], end='')
            visited_places.remove(nc)
            if nc == start:
                print()
                break
        if len(visited_places) == 0:
            break
print('###')
print()

# TASK 3

goroda = {0, 1, 2, 3, 9, 10, 11, 12}
print(goroda)

selected_places = [places[i] for i in goroda]
print('Выбрали города: ')
print(selected_places)
print()

n, V = len(selected_places), set(range(len(selected_places)))
new_model.clear()

c = [[0 if i == j
      else dists[i][j - i - 1] if j > i
else dists[j][i - j - 1]
      for j in goroda] for i in goroda]

x = [[new_model.add_var(var_type=BINARY) for j in V] for i in V]

for i in V:
    new_model += xsum(x[i][j] for j in V - {i}) == 1
for i in V:
    new_model += xsum(x[j][i] for j in V - {i}) == 1

new_model.objective = minimize(xsum(c[i][j] * x[i][j] for i in V for j in V))

my_time = 0
iteration = 0
# cycle_counter = 0
# first_cycle = set()
time_start = time.time()
while True:
    iteration = iteration + 1
    cycle_counter = 0
    first_cycle = set()
    new_model.optimize()
    if new_model.num_solutions:
        print('### Итерация ', iteration)
        print('Полученное решение = ', new_model.objective_value)
        visited_places = V.copy()
        print('Путь: ')
        while True:
            nc = visited_places.pop()
            visited_places.add(nc)
            start = nc
            print(selected_places[nc], end='')
            cycle_counter += 1
            if cycle_counter == 1:
                first_cycle.add(nc)
            while True:
                for i in visited_places:
                    if x[nc][i].x > 0.99:
                        nc = i
                        break
                print('->', selected_places[nc], end='')
                visited_places.remove(nc)
                if cycle_counter == 1:
                    first_cycle.add(nc)
                if nc == start:
                    print()
                    break
            if len(visited_places) == 0:
                break

    print()

    if cycle_counter == 1:
        break
    else:
        new_model += xsum(x[i][j] for i in first_cycle for j in V - first_cycle) >= 1

my_time = time.time() - time_start

print()

model.clear()

x = [[model.add_var(var_type=BINARY) for j in V] for i in V]

y = [model.add_var() for i in V]

model.objective = minimize(xsum(c[i][j] * x[i][j] for i in V for j in V))

for i in V:
    model += xsum(x[i][j] for j in V - {i}) == 1

for i in V:
    model += xsum(x[j][i] for j in V - {i}) == 1

for (i, j) in product(V - {0}, V - {0}):
    if i != j:
        model += y[i] - (n + 1) * x[i][j] >= y[j] - n

my_time_2 = 0
time_start = time.time()

model.optimize()

my_time_2 = time.time() - time_start

print('###')

if model.num_solutions:
    out.write('решение с длиной %g найдено: %s'
              % (model.objective_value, selected_places[0]))
    nc = 0
    while True:
        nc = [i for i in V if x[nc][i].x >= 0.99][0]
        out.write(' -> %s' % selected_places[nc])
        if nc == 0:
            break
    out.write('\n')

print()
print('Время методом генерации отсечений: ')
print(my_time, ' секунд')
print('Время встроенным методом: ')
print(my_time_2, 'секунд')
print()
print('###')
