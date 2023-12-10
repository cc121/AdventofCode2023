import unittest
import sys
import os
import random


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part1, part2


class MyTestCase(unittest.TestCase):
    def test_example_part_1(self):
        input_list = '''-L|F7
7S-7|
L|7||
-L-J|
L|-JF'''
        self.assertEqual(4, part1(input_list))

        input_list = '''7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ'''
        self.assertEqual(8, part1(input_list))

    def test_example_part_2(self):
        input_list = '''...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........'''
        self.assertEqual(4, part2(input_list))

        input_list = '''..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........'''
        self.assertEqual(4, part2(input_list))

#         input_list = '''.F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ...'''
#         self.assertEqual(8, part2(input_list))

#         input_list = '''FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L'''
#         self.assertEqual(10, part2(input_list))


if __name__ == '__main__':
    unittest.main()
