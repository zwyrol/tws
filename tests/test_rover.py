import unittest

from tws.rover import (
    Rover,
    RoverNavigator,
    RoverNavigatorInstructionError,
    RoverNavigatorOutOfGrid
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

    def test_rover_moving(self):
        data = [
            [Rover(Position('0 1 N')), 'L', Position('0 1 W')],
        ]

        for d in data:
            d[0].move(d[1])
            self.assertEqual(d[0].position.x, d[2].x)
            self.assertEqual(d[0].position.y, d[2].y)
            self.assertEqual(d[0].position.c, d[2].c)

    def test_rover_moving_wrong_instructions(self):
        data = [
            [Rover(Position('0 1 N')), 'X'],
            [Rover(Position('0 1 N')), '5'],
            [Rover(Position('0 1 N')), 'LL'],
            [Rover(Position('0 1 N')), 'LLLL'],
            [Rover(Position('0 1 N')), 'MMM'],
            [Rover(Position('0 1 N')), 'RR'],
        ]

        for d in data:
            with self.assertRaises(ValueError):
                d[0].move(d[1])

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

    def test_rover_navigator_moving_out_of_grid(self):
        data = [
            [Grid(3, 3), Rover(Position('0 0 N')), 'MMMMMMMMMM'],
            [Grid(5, 5), Rover(Position('0 1 W')), 'MM'],
            [Grid(5, 5), Rover(Position('5 5 E')), 'M'],
            [Grid(5, 5), Rover(Position('1 0 S')), 'M'],
            [Grid(5, 5), Rover(Position('5 5 N')), 'M'],
        ]

        for d in data:
            with self.assertRaises(RoverNavigatorOutOfGrid):
                rover_navigator = RoverNavigator(d[0], d[1])
                rover_navigator.navigate(d[2])

    def test_rover_navigator_moving_wrong_instructions(self):
        data = [
            [Grid(5, 5), Rover(Position('0 0 N')), '12345'],
            [Grid(5, 5), Rover(Position('0 1 W')), 'ZZZ'],
            [Grid(5, 5), Rover(Position('5 5 E')), 'X'],
            [Grid(5, 5), Rover(Position('1 0 S')), '[]'],
            [Grid(5, 5), Rover(Position('5 5 N')), '---'],
        ]

        for d in data:
            with self.assertRaises(RoverNavigatorInstructionError):
                rover_navigator = RoverNavigator(d[0], d[1])
                rover_navigator.navigate(d[2])

    def test_rover_init(self):
        rover = Rover(Position('0 1 N'))

        self.assertEqual(rover.position.x, 0)
        self.assertEqual(rover.position.y, 1)
        self.assertEqual(rover.position.c, 'N')


if __name__ == '__main__':
    unittest.main()
