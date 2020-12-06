#!/usr/bin/env python3

from functools import reduce

with open("input.txt") as f:
    data = f.read().split("\n\n")


answer_sets = [set(list(line.replace("\n", ""))) for line in data]

counts = sum(map(len, answer_sets))
print("Part 1:", counts)


answer_list = [line.split("\n") for line in data]


groups_sets = [
    [set(list(answer)) for answer in line if answer != ""] for line in answer_list
]

everyone_group_set = [reduce(lambda x, y: x & y, group) for group in groups_sets]
print("Part 2:", sum(map(len, everyone_group_set)))
