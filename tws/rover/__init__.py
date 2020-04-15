DATA = {
    'L': {
        'N': 'W',
        'S': 'E',
        'W': 'S',
        'E': 'N'
    },
    'R': {
        'N': 'E',
        'S': 'W',
        'W': 'N',
        'E': 'S'
    },
    'M': {
        'N': {'x': 0, 'y': 1},
        'S': {'x': 0, 'y': -1},
        'W': {'x': -1, 'y': 0},
        'E': {'x': 1, 'y': 0}
    }
}


class Rover:
    def __init__(self, position):
        self.position = position

    def move(self, i):
        if i == 'L' or i == 'R':
            self.position.c = DATA[i][self.position.c]
        elif i == 'M':
            self.position.x += DATA['M'][self.position.c]['x']
            self.position.y += DATA['M'][self.position.c]['y']
        else:
            raise ValueError(f'Wrong instruction passed to rover model: {i}.')


class RoverNavigatorException(Exception):
    pass


class RoverNavigatorInstructionError(RoverNavigatorException):
    pass


class RoverNavigatorOutOfGrid(RoverNavigatorException):
    pass


class RoverNavigator:
    def __init__(self, grid, rover):
        self.grid = grid
        self.rover = rover

    def validate(self, instruction):
        if instruction not in list('MLR'):
            raise RoverNavigatorInstructionError(f'The instruction: {instruction} is wrong.')

        if instruction == 'M':
            x = self.rover.position.x + DATA['M'][self.rover.position.c]['x']
            y = self.rover.position.y + DATA['M'][self.rover.position.c]['y']

            if x < 0 or x > self.grid.x or y < 0 or y > self.grid.y:
                raise RoverNavigatorOutOfGrid(
                    (
                        f'Rover can\'t travel outside the grid. Grid dimensions: {self.grid.x} x {self.grid.y}. '
                        f'Trying travel to field: {x} {y}.'
                    )
                )

        return True

    def navigate(self, instructions):
        if instructions == '':
            return False

        if self.validate(instructions[0]):
            self.rover.move(instructions[0])

        return self.navigate(instructions[1:])
