import unittest
import sys
import os
import random


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part1, part2


class MyTestCase(unittest.TestCase):
    def test_example_part_1(self):
        input_list = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''
        self.assertEqual(114, part1(input_list))

    def test_example_part_2(self):
        input_list = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''
        self.assertEqual(2, part2(input_list))


if __name__ == '__main__':
    unittest.main()
