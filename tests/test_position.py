import unittest
from tws.position import Position


class TestPosition(unittest.TestCase):
    def test_position_init(self):
        data = ['1 1 N', '0 0 N', '10 50 E']

        for d in data:
            x, y, c = d.split()

            position = Position(d)
            self.assertEqual(position.x, int(x))
            self.assertEqual(position.y, int(y))
            self.assertEqual(position.c, c)

    def test_position_init_wrong_data(self):
        data = ['N E 30', '0 0 ~', '10 50 Z', '@ 0 N', '0 # E', '', '[]', '{']

        for d in data:
            with self.assertRaises(ValueError):
                Position(d)


if __name__ == '__main__':
    unittest.main()
