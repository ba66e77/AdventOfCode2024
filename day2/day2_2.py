"""Day 2, part 2

https://adventofcode.com/2024/day/2#part2

The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""
def checksafe(value_list:list[str], iterate = True) -> bool:
    direction = ''
    failcount = 0

    for i in range(0, len(value_list)-1):
        sv, d = checkvals(int(value_list[i]), int(value_list[i+1]))

        if direction == '':
            direction = d

        if (sv == False or direction != d):
            failcount += 1
            if iterate:
                value_list.pop(i+1)
                return checksafe(value_list, False)
    
    if failcount < 1:
        return True
    else:
        return False

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
# from itertools import pairwise
# from more_itertools import sliding_window

infile = "./input.txt"

# prod data
with open(infile, 'r') as input:
    levels = input.read()

levels_list = [
    list(map(int, one_line.split())) for one_line in levels.splitlines()
]

## test data
# val_list = [
#     [7,6,4,2,1],
#     [1,2,7,8,9],
#     [9,7,6,2,1], 
#     [1,3,2,4,5],
#     [8,6,4,4,1],
#     [1,3,6,7,9]
# ]

# safe_count = 0
# for i,v in enumerate(val_list):
#     result = checksafe(v)
#     print(f'Value list row {i} is safe: {result}')
#     if result == True:
#         safe_count += 1

# print(f'Total safe records: {safe_count}')

# def is_safe(report: list[int]) -> bool:
#     safe_step = [
#         True if 1 <= abs(int(v1) - int(v2)) <= 3 else False
#         for v1, v2 in pairwise(report)
#     ]
#     safe_direction = [
#         (v1-v2) * (v2-v3) > 0
#         for v1, v2, v3 in sliding_window(report, 3)
#     ]
#     return all(safe_direction) and all(safe_step)


# def is_safe2(report: list[int]) -> bool:
#     if is_safe(report):
#         return True
#     else:
#         return any(
#             [
#                 is_safe(report.copy()[:i]+report.copy()[i+1:])
#                 for i in range(len(report))
#             ]
#         )


# safe_levels = [
#     1
#     for x in levels_list
#     if is_safe2(x)
# ]

# print(sum(safe_levels))

safe_count = 0
for i,v in enumerate(levels_list):
    result = checksafe(v)
    print(f'Value list row {i} is safe: {result}')
    if result == True:
        safe_count += 1

print(f'Total safe records: {safe_count}')