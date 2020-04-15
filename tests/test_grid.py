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

    def test_grid_init_wrong_data(self):
        data = [
            ('x', 'y'),
            ('L', 'M'),
            ('[]', '{}')
        ]

        for d in data:
            with self.assertRaises(ValueError):
                Grid(*d)


if __name__ == '__main__':
    unittest.main()
