"""
Day 3, part 1

https://adventofcode.com/2024/day/3
"""
import re

input_file = '/Users/ryg366/Desktop/aocDay3input.txt'

with open(input_file, 'r') as input:
    content = input.read()

ptrn = r'mul\([0-9]+,[0-9]+\)'

instructions = re.findall(ptrn, content)

accumulator = 0
for instruction in instructions:
    d1, d2 = re.findall('[0-9]+', instruction)
    accumulator += int(d1) * int(d2)

print(f'Sum of valid instructions is {accumulator}')
