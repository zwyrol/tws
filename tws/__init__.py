from tws.grid import Grid
from tws.io import InputParser
from tws.position import Position
from tws.rover import Rover, RoverNavigator, RoverNavigatorException
import sys


def main(i):
    grid_dimensions, instructions = InputParser(i).parse()

    try:
        grid = Grid(*grid_dimensions)
    except ValueError:
        print('Can\'t set grid, wrong dimensions provided in input file. Exiting.')
        sys.exit(0)

    for instruction in instructions:
        try:
            rover = Rover(Position(instruction[0]))
        except ValueError as e:
            print(f'Wrong instruction: {str(e)}. Skipping')
            continue

        try:
            RoverNavigator(grid, rover).navigate(instruction[1])
        except RoverNavigatorException as e:
            print(str(e))

        print(rover.position)
