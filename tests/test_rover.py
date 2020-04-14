import unittest

from tws.rover import (
    Rover,
    RoverNavigator,
    RoverMove,
    RoverMoveForward,
    RoverMoveLeft,
    RoverMoveRight
)

from tws.position import Position
from tws.grid import Grid


class TestRover(unittest.TestCase):
    def test_rover_navigator_init(self):
        grid = Grid(5, 5)
        rover = Rover(Position('0 1 N'))

        rover_navigator = RoverNavigator(
            grid,
            rover,
        )

        self.assertEqual(rover_navigator.grid, grid)
        self.assertEqual(rover_navigator.rover, rover)

    def test_rover_navigator_move_getting_instance(self):
        data = {
            'L': RoverMoveLeft,
            'R': RoverMoveRight,
            'M': RoverMoveForward
        }

        for e in data:
            instance = RoverMove.get_instance(Rover(Position('0 1 N')), e)
            self.assertIsInstance(instance, data[e])

    def test_rover_navigator_moving(self):
        data = [
            [Grid(5, 5), Rover(Position('0 1 N')), 'L', Position('0 1 W')],
            [Grid(5, 5), Rover(Position('0 1 N')), 'MM', Position('0 3 N')],
            [Grid(5, 5), Rover(Position('0 1 N')), 'RMM', Position('2 1 E')],
        ]

        for d in data:
            rover_navigator = RoverNavigator(d[0], d[1])

            rover_navigator.navigate(d[2])

            self.assertEqual(rover_navigator.rover.position.x, d[3].x)
            self.assertEqual(rover_navigator.rover.position.y, d[3].y)
            self.assertEqual(rover_navigator.rover.position.c, d[3].c)

    def test_rover_init(self):
        rover = Rover(Position('0 1 N'))

        self.assertEqual(rover.position.x, 0)
        self.assertEqual(rover.position.y, 1)
        self.assertEqual(rover.position.c, 'N')


if __name__ == '__main__':
    unittest.main()
