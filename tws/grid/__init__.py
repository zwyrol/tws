class Grid:
    def __init__(self, x, y):
        try:
            self.x = int(x)
        except ValueError:
            raise ValueError(f'Wrong argument x passed to Grid: {x}')

        try:
            self.y = int(y)
        except ValueError:
            raise ValueError(f'Wrong argument y passed to Grid: {y}')

