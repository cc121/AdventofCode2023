import unittest
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part1, part2


class MyTestCase(unittest.TestCase):
    def test_example_part_1(self):
        input_list = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''
        self.assertEqual(142, part1(input_list))

    def test_example_part_2(self):
        input_list = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''
        self.assertEqual(281, part2(input_list))

    def test_example_part_2_spot_check(self):
        test_cases = [
            'eight3c,83',
            'xbdqfpdnfour7,47',
            'gvzqtjslsmbzqzfgc2,22',
            'knttsixseven73ninebsjkdxxlp5,65',
            'one48eightjxjfmxljvs,18',
            'kxcxtnqsixseven2rnjncvbcbbrxhbgtwonine,69',
            'meightwoeightfournineqjjxfourvkxsvcbn58,88',
            'zcjcnnvfive852hrqlktzskpqgtchjb,52',
            'fbznfkxhvd9nhvpvqhlmzvr66five,95',
            '1gbfj86xntxgnine55gsmz,15',
            'j5eightfhxzhjmjcthrrtxf3,53',
            'bjbvskthreeseven29mrmt,39',
            'pceightwosixfourthreemkqtncvztwopqdvmtqlleightrjnmm9,89',
            '7ninesevensix6xtlzkhgrjxzngqvg,76',
            '8b,88',
            'lzgrvsflljtkcs3fiveonenxnrljrbdvs,31',
            'four1twooneightkvm,48',
            '558rtsqsgpgjknine,59',
            'vqvfbxfsix13sdhjznmttnine1,61',
            'mxkfpmmvhtwo8rbxrvgbsgzmcrfsfhmqcxkr5jxzzb,25',
            'fourspjcvlfkm9,49',
            'lcseven3,73',
            'five37three,53',
            'twofive5nine,29',
            'fourzlqhcpn8eight,48',
            '4ldcmctd4j,44',
            '3six67threehq6ldh,36',
            'eight99five,85',
            '4mxpfdq7zlmvslnj99,49',
            'mqhhlf3eightonen,31',
            'sdhtrdsdtjdsqvzsix1jnclhjsd,61',
            '76smqztbhqsixfourthree1zvn,71',
            '8fourkoneeight9three,83',
            'vdnxzc53g,53',
            'fvjlchqlfivetwo1,51',
            '2cljsix1twoqvqbzg,22',
            'qhcdv73vn,73',
            'qcptwone1fiveqxfrtmbpdtdtfceightstfivenine,29',
            '2lrlzvdpklf4five8two4,24',
            '7onetwovxmtvrjxb1,71',
        ]

        for test_case in test_cases:
            input_list, expected = test_case.split(',')

            print(input_list, expected)
            self.assertEqual(int(expected), part2(input_list))


if __name__ == '__main__':
    unittest.main()
