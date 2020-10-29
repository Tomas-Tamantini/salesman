class City:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def dist(self, other):
        return self.position.dist(other.position)

    def __str__(self):
        return f'{self.name} - {self.position}'
