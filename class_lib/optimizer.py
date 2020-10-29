from math import exp
from random import sample, randint, random


class Optimizer:
    def __init__(self, region, initial_temperature=100, final_temperature=.1, num_iterations=None):
        self.region = region
        self.temperature = initial_temperature
        self.final_temperature = final_temperature
        self.num_iterations = num_iterations if num_iterations is not None else 200 * len(self.region.cities)
        self.temp_decay_rate = (final_temperature / initial_temperature) ** (1 / self.num_iterations)
        self.route = region.cities.copy()  # sample(region.cities, len(region.cities))
        self.current_cost = cost(self.route, self.region)

    def __two_random_indices(self):
        first_index = randint(0, len(self.route) - 1)
        while True:
            second_index = randint(0, len(self.route) - 1)
            if second_index != first_index:
                break
        return first_index, second_index

    def make_change(self):
        change_happened = False
        probability = 1
        first_index, second_index = self.__two_random_indices()
        new_route = self.route.copy()
        new_route[first_index], new_route[second_index] = new_route[second_index], new_route[first_index]
        new_cost = cost(new_route, self.region)
        if new_cost < self.current_cost:
            self.route = new_route
            self.current_cost = new_cost
            change_happened = True
        else:
            probability = exp((self.current_cost - new_cost) / self.temperature)
            r = random()
            if r <= probability:
                self.route = new_route
                self.current_cost = new_cost
                change_happened = True
        self.temperature *= self.temp_decay_rate
        return change_happened, probability

    def __str__(self):
        return f'Temperature: {self.temperature} °C\nRoute:\n\t' + '\n\t'.join(map(lambda city: city.name, self.route))


def cost(route, region):
    acc_cost = 0
    for i in range(len(route)):
        acc_cost += region.dist(route[i], route[i - 1])
    return acc_cost
