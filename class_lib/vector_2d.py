from math import sqrt


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)

    def __str__(self):
        return f'[{round(self.x, 2)}, {round(self.y, 2)}]'
