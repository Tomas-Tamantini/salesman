from class_lib.city import City
from class_lib.region import Region
from class_lib.vector_2d import Vector2D


def region_from_csv(filename, separator=','):
    with open(filename) as file:
        lines = file.readlines()
    cities = []
    for index, line in enumerate(lines):
        fields = line.split(separator)
        city = city_from_fields(fields, index)
        if city is not None:
            cities.append(city)
    return Region(cities)


def city_from_fields(fields, index):
    if len(fields) == 2:
        name = str(index)
        x = float(fields[0])
        y = float(fields[1])
    elif len(fields) == 3:
        name = fields[0]
        x = float(fields[1])
        y = float(fields[2])
    else:
        return None
    return City(name, Vector2D(x, y))
