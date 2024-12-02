"""Day 2, part 1

https://adventofcode.com/2024/day/2

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

"""
def checksafe(value_list:list[str]) -> bool:
    direction = ''

    for i in range(0, len(value_list)-1):
        sv, d = checkvals(int(value_list[i]), int(value_list[i+1]))
    
        if sv == False:
            return False
    
        if direction == '':
            direction = d
        elif direction != d:
            return False

    return True

def checkvals(v1:int, v2:int) -> tuple[bool, str]:
    if v1 - v2 == 0:
        direction = '0'
    elif v1 - v2 < 0:
        direction = '+'
    else:
        direction = '-'

    variance = abs(v1 - v2)
    if variance >= 1 and variance <= 3:
        safe_variance = True
    else:
        safe_variance = False
    
    return (safe_variance, direction)

infile = "./input.txt"

# prod data
with open(infile, 'r') as input:
    val_list = [line.split() for line in input]

# # test data
# val_list = [
#     [7,6,4,2,1],
#     [1,2,7,8,9],
#     [9,7,6,2,1], 
#     [1,3,2,4,5],
#     [8,6,4,4,1],
#     [1,3,6,7,9]
# ]

safe_count = 0
for i,v in enumerate(val_list):
    result = checksafe(v)
    print(f'Value list rown {i} is safe: {result}')
    if result == True:
        safe_count += 1

print(f'Total safe records: {safe_count}')