import unittest
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part1, part2


class MyTestCase(unittest.TestCase):
    def test_example_part_1(self):
        input_list = '''Time:      7  15   30
Distance:  9  40  200'''
        self.assertEqual(288, part1(input_list))

    def test_example_part_2(self):
        input_list = '''Time:      7  15   30
Distance:  9  40  200'''
        self.assertEqual(71503, part2(input_list))


if __name__ == '__main__':
    unittest.main()
