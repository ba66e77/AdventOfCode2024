"""Day 6, part 1

https://adventofcode.com/2024/day/6
"""
from itertools import cycle

def move_guard(current_position: tuple[int, int], heading: str) -> tuple[tuple[int,int], str]:
    new_position = calculate_new_position(current_position, heading)

    content = check_for_impediments(new_position)

    if content in ['.','^']: #include starting guard marker because she can move freely through her start position
        guard_position_log.append(new_position)
        return (new_position, heading)
    elif content == '#':
        return (current_position, next(guard_heading))   
    else:
        raise Exception('Welp, something shit the bed.')

def calculate_new_position(current_position: tuple[int, int], heading: str) -> tuple[int, int]:
    # calculate new position
    match heading:
        case '^':
            new_position = (current_position[0]-1, current_position[1])
        case '>':
            new_position = (current_position[0], current_position[1]+1)
        case 'v':
            new_position = (current_position[0]+1, current_position[1])
        case '<':
            new_position = (current_position[0], current_position[1]-1)
        case _:
            raise Exception('Unexpected heading: {heading}')
    
    return new_position

def check_for_impediments(new_position: tuple[int, int]):
    try:
        position_content = grid_lines[new_position[0]][new_position[1]]
    except IndexError:
        raise Exception("Game over: guard has left the map")
    
    return position_content

#read input file
with open('./input.txt', 'r') as infile:
    grid_lines = [line.strip() for line in infile.readlines()]

# indicates heading of guard
guard_heading = cycle(['^', '>', 'v', '<'])

# representation of an impediment in the grid
impediment_indicator = '#'

# log of guard positions
guard_position_log = []

# find the start position of the guard
for row_number, columns in enumerate(grid_lines):
    try:
        guard_column = columns.index('^')
        guard_position = (row_number, guard_column)
        guard_position_log.append(guard_position)
        break
    except ValueError:
        continue

guard = move_guard(guard_position, next(guard_heading))
while True:
    try:
        guard = move_guard(guard[0], guard[1])
    except Exception as e:
        print(f'Guard position log has {len(set(guard_position_log))} unique positions.')
        break
