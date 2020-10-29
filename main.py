from random import seed
from time import sleep

from class_lib.optimizer import Optimizer
from class_lib.region import Region
from gui.canvas import root
from gui.data_plot import plot
from gui.draw_methods import draw_region
from io_module import region_from_csv

num_it = 20000
initial_temp = 50
final_temp = .1

rnd_seed = 9

seed(rnd_seed)

#  = Region.random_region(50)
region = region_from_csv('test_files/cities2.txt')

solver = Optimizer(region, initial_temp, final_temp, num_it)

draw_region(region)
root.update()

cost_values = []
temperature_values = []


def iterate(animate=True):
    cost_values.append(solver.current_cost)
    temperature_values.append(solver.temperature)

    solver.make_change()
    if animate:
        draw_region(region, solver.route)
        root.update()
        sleep(.1)


animate = num_it < 1000
previous_progress = -1
for i in range(num_it):
    progress = int(100 * i / num_it)
    if progress != previous_progress and progress % 5 == 0:
        print(f'{progress}%')
    previous_progress = progress
    iterate(animate)

print(f'Solution:\n{str(solver)}')

draw_region(region, solver.route)
root.update()

plot(num_it, cost_values, temperature_values)
