""" Day 9, part 1

https://adventofcode.com/2024/day/9
"""
TEST = False

# test input
if TEST:
    input = '2333133121414131402'
else:
    with open('./input.txt', 'r') as infile:
        input = infile.read().strip()

# build the expanded representation
long_form = []
for i, v in enumerate(input):
    # sort files from gaps
    if i%2 == 0:
        # file
        representation = [str(int(i/2))] * int(v)
    else:
        # gap
        representation = ['.'] * int(v)
    
    long_form += representation

# if testing, assert aginst the right value
if TEST:
    assert ''.join(long_form) == '00...111...2...333.44.5555.6666.777.888899'

# condense the list

## walk backward through long_form finding non-gaps and moving to first_gap
for i,v in enumerate(reversed(long_form), start=1):
    ### find the first gap in the list
    first_gap = long_form.index('.')
    if first_gap == -1:
        print(f'No gap found in {long_form}')
        exit(1)
    
    if first_gap > len(long_form)-i:
        break

    if v == '.':
        continue # we don't move free space

    # set the first gap to this value and add a gap at the end of the list
    long_form[first_gap] = v
    long_form[-i] = '.'

if TEST:
    assert ''.join(long_form) == '0099811188827773336446555566..............'

# calculate checksum
file_structure = [v for v in long_form if v != '.']

checksum = 0
for i,v in enumerate(file_structure):
    checksum += i * int(v)

if TEST:
    assert checksum == 1928

print(f'Checksum = {checksum}')
