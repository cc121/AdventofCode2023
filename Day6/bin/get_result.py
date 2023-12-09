import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from main import part1, part2

input_list = '''Time:        58     99     64     69
Distance:   478   2232   1019   1071'''

print(f"My result for part 1 is: {part1(input_list)}")
print(f"My result for part 2 is: {part2(input_list)}")
