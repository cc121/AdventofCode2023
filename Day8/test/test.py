import unittest
import sys
import os
import random


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part1, part2


class MyTestCase(unittest.TestCase):
    def test_example_part_1(self):
        input_list = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''
        self.assertEqual(2, part1(input_list))

        input_list = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''
        self.assertEqual(6, part1(input_list))

    def test_example_part_2(self):
        input_list = '''LR

11A = (11B, 11B)
11B = (11C, 11C)
11C = (11D, 11D)
11D = (11E, 11E)
11E = (11Z, 11Z)
11Z = (11B, 11B)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
33A = (33B, XXX)
33B = (XXX, 33C)
33C = (33D, XXX)
33D = (XXX, 33E)
33E = (33F, XXX)
33F = (XXX, 33G)
33G = (33H, XXX)
33H = (XXX, 33I)
33I = (33J, XXX)
33J = (XXX, 33K)
33K = (33Z, XXX)
33Z = (XXX, 33E)
XXX = (XXX, XXX)'''
        self.assertEqual(75, part2(input_list))


if __name__ == '__main__':
    unittest.main()
