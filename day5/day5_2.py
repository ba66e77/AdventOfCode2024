"""day5_2.py

https://adventofcode.com/2024/day/5#part2
"""
from math import floor

with open('./input.txt', 'r') as infile:
    input_lines = infile.readlines()

midpoints = [] #midpoint value accumulator

# split the file into rulesets and updates
rulesets = []
updates = []

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

def fix_update(violated_rule, update):
    before, after = violated_rule

    bi = update.index(before)
    ai = update.index(after)

    # remove the after value
    del(update[ai])
    # insert the after value immediately after the before value
    update.insert(bi+1, after)

    return update

def check_and_fix_update(update: list[int], rules:list[tuple[int,int]]) -> list:
    for rule in rules:
        valid = check_rule(rule, update)
        if not valid:
            update = fix_update(rule, update)
            # retest with the fixed value
            check_and_fix_update(update, rules)
    
    return update

# get al the ones that are wrong
incorrect_updates = [update for update in updates 
                     if not check_update_correctly_ordered(update, rulesets)
                    ]

# build a list of fixed ones, by fixing the ones that are wrong
corrected = []
for update in incorrect_updates:
    corrected.append(check_and_fix_update(update, rulesets))

answer = sum([get_middle_element(update) for update in corrected])

print(f'The answer is {answer}')
