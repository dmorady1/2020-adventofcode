#!/usr/bin/env python3

import re

data = open("input.txt", "r").read().splitlines()


def binary_search(value, low=0, high=127):
    for char in value:
        if char == "F":
            high = low + (high - low) // 2
        if char == "B":
            low = low + 1 + (high - low) // 2
    return low


result = []
for line in data:
    rows = line[:7]
    columns = line[7::]
    columns = columns.replace("R", "B").replace("L", "F")
    row = binary_search(rows)
    column = binary_search(columns, high=7)
    result.append(row * 8 + column)

print("Part1:", max(result))

max_set_id = 127 * 8 + 7

missing_ids = set(list(range(max_set_id))) - set(result)

for miss_id in missing_ids:
    if miss_id - 1 in result and miss_id + 1 in result:
        print("Part 2:", miss_id)
        break
