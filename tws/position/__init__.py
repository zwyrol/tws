class Position:
    def __init__(self, position):
        x, y, self.c = position.split()
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'{self.x} {self.y} {self.c}'

