#!/usr/bin/env python3

import re
from functools import reduce

with open("input.txt") as f:
    data = f.read()


all_ranges = re.findall("\d+-\d+", data)


all_ranges = [list(map(int, value.split("-"))) for value in all_ranges]


list_data = data.splitlines()

nearby_tickets = []
take = False
for value in list_data:
    if take:
        nearby_tickets.append(value)
    if value == "nearby tickets:":
        take = True


nearby_tickets = [list(map(int, value.split(","))) for value in nearby_tickets]


def in_range(ranges, value):
    for minimum, maximum in ranges:
        if minimum <= value <= maximum:
            return True

    return False


not_in_range = [
    value
    for line in nearby_tickets
    for value in line
    if not in_range(all_ranges, value)
]

print("Part 1:", sum(not_in_range))

# part 2


your_ticket = []
take = False
for line in list_data:
    if take:
        your_ticket = line
        break
    if line == "your ticket:":
        take = True


your_ticket = list(map(int, your_ticket.split(",")))


def transpose_list(x):
    return list(zip(*x))


nearby_tickets = [
    line
    for line in nearby_tickets
    if len(set(line).intersection(set(not_in_range))) == 0
]

nearby_tickets_transpose = transpose_list(nearby_tickets)


all_ranges = [all_ranges[i : i + 2] for i in range(0, len(all_ranges), 2)]
all_fields = re.findall(r".+: ", data)


field_index = {}

for index, values in enumerate(nearby_tickets_transpose):
    for field, _range in enumerate(all_ranges):
        if all([in_range(_range, value) for value in values]):
            if all_fields[field] in field_index:
                field_index[all_fields[field]].add(index)
            else:
                field_index[all_fields[field]] = {index}


sorted_dict_keys_after_length_of_values = sorted(
    field_index, key=lambda k: len(field_index[k])
)

first = sorted_dict_keys_after_length_of_values[0]
deletion_list = field_index[first]

for field in sorted_dict_keys_after_length_of_values[1:]:
    field_index[field] = field_index[field] - deletion_list
    deletion_list = deletion_list.union(field_index[field])


all_departures = [
    your_ticket[next(iter(index))]
    for field, index in field_index.items()
    if "departure" in field
]


print("Part 2:", reduce(lambda x, y: x * y, all_departures))
