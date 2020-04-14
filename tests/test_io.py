import unittest
from tws.io import InputParser


class TestInputParser(unittest.TestCase):
    def test_input_parser(self):
        grid_x, grid_y = 5, 5
        instructions_data = [('1 2 N', 'LMLMLMLMM'), ('3 3 E', 'MMRMMRMRRM')]

        i = (
            f'{grid_x} {grid_y}\n'
            f'{instructions_data[0][0]}\n'
            f'{instructions_data[0][1]}\n'
            f'{instructions_data[1][0]}\n'
            f'{instructions_data[1][1]}\n'
        )

        grid_dimensions, instructions = InputParser(i).parse()

        self.assertEqual(grid_dimensions, (5, 5))
        self.assertEqual(instructions_data, instructions)


if __name__ == '__main__':
    unittest.main()
