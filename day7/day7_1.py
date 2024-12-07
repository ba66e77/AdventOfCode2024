""" Day 7, part 1

https://adventofcode.com/2024/day/7
"""
from itertools import product

input_file_name = './input.txt'

with open(input_file_name, 'r') as input_file:
    input_lines = {}
    for line in input_file:
        k,v = line.split(':')
        input_lines[int(k)] = [int(num) for num in v.split()]

print(input_lines)

operators = ['*', '+']

true_equations = [] # accumulator

# for each input_line...
for answer, elements in input_lines.items():

# use the length of the elements in the list to determine how many operator slots there are and get that permutations of that many elements
    operator_slots = len(elements)-1
    operator_permutations = product(operators, repeat = operator_slots)

    print(f"Testing {answer}: {elements}")
# for each permutation of operators, loop through the pairwise tuples inserting the relevant numbered operator and getting running value
    for operator_set in operator_permutations:
        value = eval(f'{elements[0]} {operator_set[0]} {elements[1]}')

        for i in range(2, len(elements)):
            value = eval(f'{value} {operator_set[i-1]} {elements[i]}')

        # if running value == input_line key: we have a match, record the match and move to the next
        if value == answer:
            true_equations.append(answer)
            break

print(f'The sum of true equations is: {sum(true_equations)}: {true_equations}')
