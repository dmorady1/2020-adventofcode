#!/usr/bin/env python3

import re
from time import sleep

with open("input.txt") as f:
    data = f.read().splitlines()

memory_dict = {}


mask_pattern = 0
complement_version = 0
for line in data:
    if re.findall(r"^mask = (.*)", line):
        mask = re.findall(r"^mask = (.*)", line)[0]
        mask_pattern = re.sub(r"X", "0", mask)
        mask_pattern = int(mask_pattern, 2)

        # number_to_one = re.sub(r"\d", "1", mask)
        # x_to_zeros = re.sub(r"X", "0", number_to_one)
        # complement_version = ~int(x_to_zeros, 2)

        number_to_one = re.sub(r"\d", "0", mask)
        complement_version = int(re.sub(r"X", "1", number_to_one), 2)
    else:
        index, value = re.findall(r"\d+", line)

        index = int(index)
        value = int(value)
        value = (value & complement_version) | mask_pattern
        memory_dict[index] = value

print("Part 1:", sum(memory_dict.values()))

# part 2


def find_all_indeces(address, result=[]):
    indeces_of_x = [i for i, char in enumerate(address) if char == "X"]

    if len(indeces_of_x) == 0:
        return result

    address_zero = address[: indeces_of_x[0]] + "0" + address[indeces_of_x[0] + 1 :]
    address_one = address[: indeces_of_x[0]] + "1" + address[indeces_of_x[0] + 1 :]
    return find_all_indeces(address_zero, [address_zero]) + find_all_indeces(
        address_one, [address_one]
    )


mask_pattern = 0
complement_version = 0
memory_dict = {}
for line in data:
    if re.findall(r"^mask = (.*)", line):
        mask = re.findall(r"^mask = (.*)", line)[0]
        mask_pattern = re.sub(r"X", "0", mask)
        mask_pattern = int(mask_pattern, 2)

    else:
        index, value = re.findall(r"\d+", line)

        index = int(index)
        value = int(value)
        index = index | mask_pattern

        indeces_of_x = [i for i, char in enumerate(mask) if char == "X"]

        index = bin(index)[2:]
        index = "0" * (36 - len(index)) + index
        for i in indeces_of_x:
            index = index[:i] + "X" + index[i + 1 :]
        indeces = [int(i, 2) for i in find_all_indeces(index)]
        for memory_addr in indeces:
            memory_dict[memory_addr] = value


print("Part 2:", sum(memory_dict.values()))
