"""Day 1, part 2

https://adventofcode.com/2024/day/1#part2

"""

infile = "./input.txt"

with open(infile, 'r') as input:
    inputdata = input.readlines()

# holding vars for the lists of data
list1 = []
list2 = []

# split the lines into data lists
for dataline in inputdata:
    v1,v2 = dataline.split()
    list1.append(v1)
    list2.append(v2)

similarity = 0

for v in list1:
    l2occurrence = len([l2v for l2v in list2 if l2v == v])
    print(f'{v} appears in list2 {l2occurrence} times')
    similarity += (int(v) * l2occurrence)

print(f"Total similarity is {similarity} ")