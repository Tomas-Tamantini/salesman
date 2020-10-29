from math import inf
from random import uniform

from class_lib.city import City
from class_lib.vector_2d import Vector2D


class Region:
    def __init__(self, cities, store_distances=True):
        self.cities = cities
        self.distances = None
        if store_distances:
            self.__store_dists()

    @property
    def dimensions(self):
        min_x, min_y = inf, inf
        max_x, max_y = -inf, -inf
        for city in self.cities:
            if city.position.x < min_x:
                min_x = city.position.x
            if city.position.y < min_y:
                min_y = city.position.y
            if city.position.x > max_x:
                max_x = city.position.x
            if city.position.y > max_y:
                max_y = city.position.y
        return {'min_x': min_x, 'min_y': min_y, 'max_x': max_x, 'max_y': max_y}

    def dist(self, city_a, city_b):
        if self.distances is None:
            return city_a.dist(city_b)
        else:
            pass
            # TODO: return stored distance

    def __store_dists(self):
        pass
        # TODO: Store distances

    @staticmethod
    def random_region(num_cities):
        min_distance = 50
        cities = []
        for i in range(num_cities):
            while True:
                pos = random_position()
                valid_position = True
                for city in cities:
                    distance = pos.dist(city.position)
                    if distance < min_distance:
                        valid_position = False
                        break
                if valid_position:
                    new_city = City(str(i), pos)
                    cities.append(new_city)
                    break
        return Region(cities)

    def __str__(self):
        return '\n'.join(map(str, self.cities))


def random_position():
    x = uniform(100, 500)
    y = uniform(100, 500)
    return Vector2D(x, y)
