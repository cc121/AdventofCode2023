import unittest
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part1, part2, bottom, top, left, right, top_left, top_right, bottom_left, bottom_right


class MyTestCase(unittest.TestCase):
    def test_left(self):
        rows = [
            '.....',
            '.....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, left(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '*123.',
            '.....',
            '.....',
        ]
        self.assertEqual(True, left(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '123..',
            '.....',
            '.....',
        ]
        self.assertEqual(False, left(2, [0, 1, 2], rows))

    def test_right(self):
        rows = [
            '.....',
            '.....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, right(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(True, right(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '..123',
            '.....',
            '.....',
        ]
        self.assertEqual(False, right(2, [2, 3, 4], rows))

    def test_bottom(self):
        rows = [
            '.....',
            '.....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, bottom(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '*....',
            '.....',
        ]
        self.assertEqual(False, bottom(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '.*...',
            '.....',
        ]
        self.assertEqual(True, bottom(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '..*..',
            '.....',
        ]
        self.assertEqual(True, bottom(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '...*.',
            '.....',
        ]
        self.assertEqual(True, bottom(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '....*',
            '.....',
        ]
        self.assertEqual(False, bottom(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.....',
            '.....',
            '.123.',
        ]
        self.assertEqual(False, bottom(4, [1, 2, 3], rows))

    def test_bottom(self):
        rows = [
            '.....',
            '.....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, top(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '*....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, top(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.*...',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(True, top(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '..*..',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(True, top(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '...*.',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(True, top(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '....*',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, top(2, [1, 2, 3], rows))

        rows = [
            '.123.',
            '.....',
            '.....',
            '.....',
            '.....',
        ]
        self.assertEqual(False, top(4, [1, 2, 3], rows))

    def test_top_left(self):
        rows = [
            '.....',
            '.....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, top_left(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '*....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(True, top_left(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '....*',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, top_left(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '*....',
            '.....',
        ]
        self.assertEqual(False, top_left(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '....*',
            '.....',
        ]
        self.assertEqual(False, top_left(2, [1, 2, 3], rows))

    def test_top_right(self):
        rows = [
            '.....',
            '.....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, top_right(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '*....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, top_right(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '....*',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(True, top_right(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '*....',
            '.....',
        ]
        self.assertEqual(False, top_right(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '....*',
            '.....',
        ]
        self.assertEqual(False, top_right(2, [1, 2, 3], rows))

    def test_bottom_left(self):
        rows = [
            '.....',
            '.....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, bottom_left(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '*....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, bottom_left(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '....*',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, bottom_left(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '*....',
            '.....',
        ]
        self.assertEqual(True, bottom_left(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '....*',
            '.....',
        ]
        self.assertEqual(False, bottom_left(2, [1, 2, 3], rows))

    def test_bottom_right(self):
        rows = [
            '.....',
            '.....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, bottom_right(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '*....',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, bottom_right(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '....*',
            '.123.',
            '.....',
            '.....',
        ]
        self.assertEqual(False, bottom_right(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '*....',
            '.....',
        ]
        self.assertEqual(False, bottom_right(2, [1, 2, 3], rows))

        rows = [
            '.....',
            '.....',
            '.123.',
            '....*',
            '.....',
        ]
        self.assertEqual(True, bottom_right(2, [1, 2, 3], rows))

        def test_bug_1(self):
            input_list = '''.....487.599...........411...........................................574..679.136..........................30......255.......432............
....*......*............*..........&586..........................375...@..*....../.....835.............610*........./...............582.....'''
            self.assertEqual(False, bottom(0, input_list))

    def test_example_part_1(self):
        input_list = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
        self.assertEqual(4361, part1(input_list))

    def test_example_part_2(self):
        input_list = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
        self.assertEqual(467835, part2(input_list))


if __name__ == '__main__':
    unittest.main()
