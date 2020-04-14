from tws.grid import Grid
from tws.io import InputParser
from tws.position import Position
from tws.rover import Rover, RoverNavigator


def main(i):
    grid_dimensions, instructions = InputParser(i).parse()

    grid = Grid(*grid_dimensions)

    for instruction in instructions:
        rover = Rover(Position(instruction[0]))

        RoverNavigator(grid, rover).navigate(instruction[1])

        print(rover.position)
