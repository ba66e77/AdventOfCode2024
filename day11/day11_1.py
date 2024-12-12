""" Day 11, part 1

https://adventofcode.com/2024/day/11
"""
test_input = '125 17'
input = '572556 22 0 528 4679021 1 10725 2790'

def change_stone(stone: int) -> list[int]:
    """  
    If the stone is engraved with the number 0,
        - replaced by a stone engraved with the number 1.
    If the stone is engraved with a number that has an even number of digits, 
        - replaced by two stones. 
        - The left half of the digits are engraved on the new left stone
        - right half of the digits are engraved on the new right stone.
        - (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    If none of the other rules apply
        - stone is replaced by a new stone
        - the old stone's number multiplied by 2024 is engraved on the new stone.
    """
    match stone:
        case 0:
            new_stone = [1]
        case stone if len(str(stone)) % 2 == 0:
            s = str(stone)
            mid = int(len(s)/2)
            left = s[0:mid]
            right = s[mid:]
            new_stone = [int(left), int(right)]
        case _:
            v = stone * 2024
            new_stone = [v]
        
    return new_stone

def blink(stone_list: list[int]) -> list[int]:
    """
    Change all the stones
    """
    new_stone_list = []
    #print(stone_list)

    for stone in stone_list:
        new_stone_list += change_stone(stone)
        #print(f'parsing stone {stone}.')
        #print(f'change_stone = {change_stone(stone)}')
    
    return new_stone_list

stones = [int(stone) for stone in input.split()]
# blinks = 25
# for i in range(blinks):
#     stones = blink(stones)

# print(f'Part 1: After {blinks} blinks, there are {len(stones)} stones.')

blinks = 75
for i in range(blinks):
    stones = blink(stones)

print(f'Part 2: After {blinks} blinks, there are {len(stones)} stones.')