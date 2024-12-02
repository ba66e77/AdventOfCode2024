"""Day 1

https://adventofcode.com/2024/day/1

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

# put the lists in order for comparision
list1.sort()
list2.sort()

diffsum = 0

for i, val in enumerate(list1):
    diff = abs(int(val) - int(list2[i]))
    print(f"Diff between {val} and {list2[i]} is {diff}")
    diffsum += diff

print(f"The total difference is {diffsum}")
