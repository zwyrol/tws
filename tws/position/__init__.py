class Position:
    def __init__(self, position):
        x, y, self.c = position.split()

        try:
            self.x = int(x)
        except ValueError:
            raise ValueError(f'The argument x passed to Position is wrong: {x}')

        try:
            self.y = int(y)
        except ValueError:
            raise ValueError(f'The argument y passed to Position is wrong: {y}')

        if self.c not in list('NSWE'):
            raise ValueError(f'Wrong cardinal compass point passed to Position: {self.c}')

    def __str__(self):
        return f'{self.x} {self.y} {self.c}'
