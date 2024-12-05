"""day5_1.py

https://adventofcode.com/2024/day/5
"""
from math import floor

with open('./input.txt', 'r') as infile:
    input_lines = infile.readlines()

# split the file into rulesets and updates
rulesets = []
updates = []

midpoints = []

for i,line in enumerate(input_lines):
    line = line.strip()
    if line.find('|') != -1:
        rulesets.append(
            tuple(line.split('|'))
        )
    elif line.find(',') != -1:
        updates.append(
            [d for d in line.split(',')]
        )
    else:
        print(f'No separator found in line {i}: {line}')

def check_rule(rule: tuple[int, int], update: list[int]) -> bool:
    before, after = rule
    if before not in update or after not in update:
        # rule is moot because one of the numbers isn't present
        return True
    bi = update.index(before)
    ai = update.index(after)

    if bi >= ai:
        return False
    else:
        return True

def check_update_correctly_ordered(update: list[int], rules:list[tuple[int,int]]) -> bool:
    for rule in rules:
        valid = check_rule(rule, update)
        if not valid:
            return False
    
    return True

def get_middle_element(update: list[int]) -> int:
    if len(update) % 2 == 0:
        raise Exception(f'Even numbered length list: {update}')

    i = floor(len(update) / 2) # using floor to account for 0-indexing

    return int(update[i])

for update in updates:
    if check_update_correctly_ordered(update, rulesets):
        midpoints.append(
            get_middle_element(update)
        )

print(f'Sum of all midpoints of correctly ordered updates is: {sum(midpoints)}')
