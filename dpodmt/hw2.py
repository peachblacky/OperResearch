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
model.verbose = 0
model.optimize()

# checking if a solution was found
if model.num_solutions:
    out.write('route with total distance %g found: %s'
              % (model.objective_value, places[0]))
    cur_city = 0
    while True:
        cur_city = [i for i in V if x[cur_city][i].x >= 0.99][0]
        out.write(' -> %s' % places[cur_city])
        if cur_city == 0:
            break
    out.write('\n')

#### YOUR CODE HERE VVVVVVVVVVVVVVVVVV

# TASK 1
print('\n ---------------------------- TASK 1 SECTION START')

integer_solution = model.objective_value

mixed_integer_model = Model(solver_name=CBC)
mixed_integer_model.verbose = 0

x = [[mixed_integer_model.add_var() for j in V] for i in V]

y = [mixed_integer_model.add_var() for i in V]

mixed_integer_model.objective = minimize(xsum(c[i][j] * x[i][j] for i in V for j in V))

for i in V:
    mixed_integer_model += xsum(x[i][j] for j in V - {i}) == 1

for i in V:
    mixed_integer_model += xsum(x[j][i] for j in V - {i}) == 1

for (i, j) in product(V - {0}, V - {0}):
    if i != j:
        mixed_integer_model += y[i] - (n + 1) * x[i][j] >= y[j] - n

mixed_integer_model.optimize()

mixed_integer_solution = mixed_integer_model.objective_value

print('F_integer = ', integer_solution)
print('F_mixed = ', mixed_integer_solution)
print('Absolute Integer Gap is: ', integer_solution - mixed_integer_solution)
print('---------------------------- TASK 1 SECTION END\n')

# TASK 2
print('\n ---------------------------- TASK 2 SECTION START')
task2_model = Model(solver_name=CBC)

x = [[task2_model.add_var(var_type=BINARY) for j in V] for i in V]

task2_model.objective = minimize(xsum(c[i][j] * x[i][j] for i in V for j in V))

for i in V:
    task2_model += xsum(x[i][j] for j in V - {i}) == 1
for i in V:
    task2_model += xsum(x[j][i] for j in V - {i}) == 1

task2_model.verbose = 0
task2_model.optimize()

if task2_model.num_solutions > 0:
    print('Optimal tour length is: ', task2_model.objective_value)
    visited_places = V.copy()
    print('Cycles are: ')
    while True:
        cur_city = visited_places.pop()
        visited_places.add(cur_city)
        start = cur_city
        print('\n -> ', places[cur_city], end='')
        while True:
            for i in visited_places:
                if x[cur_city][i].x > 0.99:
                    cur_city = i
                    break
            visited_places.remove(cur_city)
            if cur_city == start:
                break
            print(' -> ', places[cur_city], end='')
        if len(visited_places) == 0:
            break
print('\n ---------------------------- TASK 2 SECTION END')

# TASK 3
print('\n ---------------------------- TASK 3 SECTION START')

cities_indexes = {0, 2, 4, 6, 8, 10, 11, 12}
selected_cities = [places[i] for i in cities_indexes]
print(selected_cities)

n, V = len(selected_cities), set(range(len(selected_cities)))
task3_model = Model(solver_name=CBC)
task3_model.verbose = 0

c = [[0 if i == j else dists[i][j - i - 1] if j > i else dists[j][i - j - 1] for j in cities_indexes] for i in
     cities_indexes]

x = [[task3_model.add_var(var_type=BINARY) for j in V] for i in V]

for i in V:
    task3_model += xsum(x[i][j] for j in V - {i}) == 1
for i in V:
    task3_model += xsum(x[j][i] for j in V - {i}) == 1

task3_model.objective = minimize(xsum(c[i][j] * x[i][j] for i in V for j in V))

iteration = 0
time_start = time.time()
while True:
    iteration = iteration + 1
    cycle_counter = 0
    first_cycle = set()
    task3_model.optimize()
    if task3_model.num_solutions:
        print('ITERATION ', iteration)
        print('Current solution = ', task3_model.objective_value)
        visited_places = V.copy()
        print('Paths: ')
        while True:
            nc = visited_places.pop()
            visited_places.add(nc)
            start = nc
            print(' ->', selected_cities[nc], end='')
            cycle_counter += 1
            if cycle_counter == 1:
                first_cycle.add(nc)
            while True:
                for i in visited_places:
                    if x[nc][i].x > 0.99:
                        nc = i
                        break
                visited_places.remove(nc)
                if cycle_counter == 1:
                    first_cycle.add(nc)
                if nc == start:
                    print()
                    break
                print(' ->', selected_cities[nc], end='')
            if len(visited_places) == 0:
                break

    if cycle_counter == 1:
        break
    else:
        task3_model += xsum(x[i][j] for i in first_cycle for j in V - first_cycle) >= 1

time_end = time.time()
cuts_elapsed_time = time_end - time_start


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

model.verbose = 0
time_start = time.time()
model.optimize()
time_end = time.time()
template_model_elapsed_time = time_end - time_start

if model.num_solutions:
    print('\n\nTemplate model solution length is ', model.objective_value)
    nc = 0
    while True:
        nc = [i for i in V if x[nc][i].x >= 0.99][0]
        out.write(' -> %s' % selected_cities[nc])
        if nc == 0:
            break
    out.write('\n')

print('\n\nCuts elapsed optimizing time: ', cuts_elapsed_time, ' sec')
print('Template model elapsed working time: ', template_model_elapsed_time, 'sec')
print('\n ---------------------------- TASK 3 SECTION END')
