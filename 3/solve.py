#!/usr/bin/env python3

data = open("input.txt", "r").read().splitlines()

col_max = len(data[0])
row_max = len(data)
i = 0
j = 0
down = 1
right = 3

count_trees = 0
while i < row_max:
    if data[i][j] == "#":
        count_trees += 1

    i += down
    j = (j + right) % col_max

print("Part1: ", count_trees)

# part 2

downs = [1, 1, 1, 1, 2]
rights = [1, 3, 5, 7, 1]

result = 1
for down, right in list(zip(downs, rights)):
    i = 0
    j = 0

    count_trees = 0
    while i < row_max:
        if data[i][j] == "#":
            count_trees += 1

        i += down
        j = (j + right) % col_max

    result *= count_trees

print("Part2: ", result)
