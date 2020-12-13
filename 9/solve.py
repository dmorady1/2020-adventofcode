#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read()

# data = """35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# """
data = data.splitlines()


data = list(map(int, data))
# print(data)

splitter = 25


def solve(data, splitter=25):
    for i in range(len(data)):
        previous = set(data[i : splitter + i])
        value = data[splitter + i]

        pair = False
        for number in previous:
            if (value - number) in previous:
                pair = True
        if not pair:
            return value
    return -1


no_pair_value = solve(data, splitter)
print(solve(data, splitter))

# part 2


def solve2(data, no_pair_value):
    left, right = 0, 1
    values = data[left:right]
    while sum(values) != no_pair_value:
        sum_value = sum(values)
        if sum_value < no_pair_value:
            right += 1
            values.append(data[right])
        else:
            del values[0]
    return min(values) + max(values)


print(solve2(data, no_pair_value))
