"""
Day 3, part 2

https://adventofcode.com/2024/day/3#part2
"""
import re

input_file = '/Users/ryg366/Desktop/aocDay3input.txt'

with open(input_file, 'r') as input:
    # new lines in the input file bork the regex, so strip them down to a single text line
    content = input.read().replace('\n', '')

def kill_the_donts(content: str):
    # find don't() followed by either do() or the end of the file and get rid of them
    dont_pattern = r'don\'t\(\).+?(?:do\(\)|$)'
    new_content = re.sub(dont_pattern, '', content)

    return new_content

ptrn = r'mul\([0-9]+,[0-9]+\)'

content = kill_the_donts(content)

instructions = re.findall(ptrn, content)

accumulator = 0
for instruction in instructions:
    d1, d2 = re.findall('[0-9]+', instruction)
    accumulator += int(d1) * int(d2)

print(f'Sum of valid instructions is {accumulator}')
