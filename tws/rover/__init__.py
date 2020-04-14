class Rover:
    def __init__(self, position):
        self.position = position


class RoverNavigator:
    def __init__(self, grid, rover):
        self.grid = grid
        self.rover = rover

    def navigate(self, instructions):
        if instructions == '':
            return False

        move = RoverMove.get_instance(self.rover, instructions[0])
        move.move()

        return self.navigate(instructions[1:])


class RoverMove:
    data = {}

    def __init__(self, rover):
        self.rover = rover

    def move(self):
        self.rover.position.x += self.data[self.rover.position.c]['x']
        self.rover.position.y += self.data[self.rover.position.c]['y']

    @staticmethod
    def get_instance(rover, instruction):
        if instruction == 'L':
            return RoverMoveLeft(rover)

        if instruction == 'R':
            return RoverMoveRight(rover)

        if instruction == 'M':
            return RoverMoveForward(rover)


class RoverMoveRotate(RoverMove):
    def move(self):
        self.rover.position.c = self.data[self.rover.position.c]


class RoverMoveForward(RoverMove):
    data = {
        'N': {'x': 0, 'y': 1},
        'S': {'x': 0, 'y': -1},
        'W': {'x': -1, 'y': 0},
        'E': {'x': 1, 'y': 0}
    }


class RoverMoveLeft(RoverMoveRotate):
    data = {
        'N': 'W',
        'S': 'E',
        'W': 'S',
        'E': 'N'
    }


class RoverMoveRight(RoverMoveRotate):
    data = {
        'N': 'E',
        'S': 'W',
        'W': 'N',
        'E': 'S'
    }
