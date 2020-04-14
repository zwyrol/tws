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


if __name__ == '__main__':
    unittest.main()
