import unittest
import sys
import os
import random


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part1, part2, sort_hand, convert_hand_to_number, cards


class MyTestCase(unittest.TestCase):
    def test_conversion(self):
        hands = [
            '33333',
            '33332',
            '33323',
            '33322',
            '33233',
            '33232',
            '33223',
            '33222',
            '32333',
            '32332',
            '32323',
            '32322',
            '32233',
            '32232',
            '32223',
            '32222',
            '23333',
            '23332',
            '23323',
            '23322',
            '23233',
            '23232',
            '23223',
            '23222',
            '22333',
            '22332',
            '22323',
            '22322',
            '22233',
            '22232',
            '22223',
            '22222',
        ]

        for i, hand in enumerate(hands[::-1]):
            converted_number = convert_hand_to_number(hand, cards, 2)
            self.assertEqual(i, converted_number)

    def test_sorting(self):
        hands = [
            '33333',
            '33332',
            '33323',
            '33322',
            '33233',
            '33232',
            '33223',
            '33222',
            '32333',
            '32332',
            '32323',
            '32322',
            '32233',
            '32232',
            '32223',
            '32222',
            '23333',
            '23332',
            '23323',
            '23322',
            '23233',
            '23232',
            '23223',
            '23222',
            '22333',
            '22332',
            '22323',
            '22322',
            '22233',
            '22232',
            '22223',
            '22222',
        ]

        shuffled_hands = hands[:]
        random.shuffle(shuffled_hands)
        self.assertEqual(hands, sort_hand(shuffled_hands, cards))

    def test_example_part_1(self):
        input_list = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''
        self.assertEqual(6440, part1(input_list))

    def test_example_part_2(self):
        input_list = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''
        self.assertEqual(5905, part2(input_list))


if __name__ == '__main__':
    unittest.main()
