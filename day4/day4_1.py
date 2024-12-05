"""
Day 4, part 1

https://adventofcode.com/2024/day/4
"""
search_term = 'XMAS'

def find_all_X(s):
    """Find all Xs in a string.

    Stolen from https://stackoverflow.com/questions/52452911/finding-all-positions-of-a-character-in-a-string

    use 
        # >>> print(*find_all_X(str))
        # 4 5
    """
    idx = s.find('X')
    while idx != -1:
        yield idx
        idx = s.find('X', idx + 1)

def get_valid_search_directions(line_number: int, character_index: int, input_line_count: int, line_length:int) -> list[str]:
    """Determine the valid directions in which XMAS could possibly appear
    """
    search_directions = []

    # if line < 4, don't search up
    if line_number >= 3:
        search_directions.append('up')
    
    # if line(-1) < 4, don't search down
    if input_line_count - line_number >= 4:
        search_directions.append('down')
    
    # if position < 4, don't search backward
    if character_index >= 3:
        search_directions.append('backward')
    
    # if position(-1) < 4, don't search forward
    if line_length - character_index >= 4:
        search_directions.append('forward')
    
    # diagonals
    # forward up
    if 'forward' in search_directions and 'up' in search_directions:
        search_directions.append('forward-up')
    # forward down
    if 'forward' in search_directions and 'down' in search_directions:
        search_directions.append('forward-down')
    # backward up
    if 'backward' in search_directions and 'up' in search_directions:
        search_directions.append('backward-up')
    # backward down
    if 'backward' in search_directions and 'down' in search_directions:
        search_directions.append('backward-down')

    return search_directions

def get_search_position(start_position: tuple[int,int], direction: str) -> tuple[int, int]:
    match direction:
        case 'forward':
            next_position = (start_position[0]+1, start_position[1])
        case 'backward':
            next_position = (start_position[0]-1, start_position[1])
        case 'up':
            next_position = (start_position[0], start_position[1]-1)
        case 'down':
            next_position = (start_position[0], start_position[1]+1)
        case 'forward-up':
            next_position = (start_position[0]+1, start_position[1]-1)
        case 'forward-down':
            next_position = (start_position[0]+1, start_position[1]+1)
        case 'backward-up':
            next_position = (start_position[0]-1, start_position[1]-1)
        case 'backward-down':
            next_position = (start_position[0]-1, start_position[1]+1)
        case _:
            raise Exception(f'Unrecognized direction: {direction}')
    
    return next_position

def get_letter_at_position(position:tuple[int, int]) -> str:
    """Get the letter in a particular position in lines of letters
    """
    try:
        letter = input_lines[position[1]][position[0]]
    except IndexError as e:
        raise e 
    
    return letter
    

# read input file
input_path= '/Users/ryg366/Desktop/aoc_day4_input.txt'

with open(input_path,'r') as input_file:
    input_lines = input_file.readlines()
    input_lines = [line.strip() for line in input_lines]

input_line_count = len(input_lines) # needed for negative position checking

xmas_counter = 0 # incrementer of times we found XMAS

# for each line,
for line_number, line in enumerate(input_lines):
    
    line_length = len(line) # needed for negative poisition checking
    
    # find X
    x_generator = find_all_X(line)

    # for each X..
    for x_position in x_generator:
        
        # determine valid search directions
        search_directions = get_valid_search_directions(line_number, x_position, input_line_count, line_length)

        #print(f'For line {line_number}, position {x_position} in line of {line_length}, we\'ll look in: {search_directions}')
        
        # search each valid direction for next characters in sequence
        for direction in search_directions:
            #print(f'Searching in {direction}')
            search_position = get_search_position((x_position, line_number), direction)
            for l in search_term[1:]:
                #print(f'Searching position {search_position} for {l}')
                current_letter = get_letter_at_position(search_position)
                #print(f'found {current_letter}')
                if l != current_letter:
                    break
                if l == 'S':
                    xmas_counter += 1
                    #print('found xmas*****')
                search_position = get_search_position((search_position), direction)
        # for direction in search_directions:
            # continue if next character not found
            # if all characters found, incremement a counter

print(f'Found {xmas_counter} instances of {search_term}')