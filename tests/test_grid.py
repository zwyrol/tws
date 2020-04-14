import unittest
from tws.grid import Grid


class TestGrid(unittest.TestCase):
    def test_grid_init(self):
        data = [
            (5, 10),
            (3, 200),
            (25, 25)
        ]

        for d in data:
            grid = Grid(*d)
            self.assertEqual(grid.x, d[0])
            self.assertEqual(grid.y, d[1])


if __name__ == '__main__':
    unittest.main()
