#!/usr/bin/env python3

import sys

data = open("input.txt", "r").read().splitlines()

count = 0
newPolicyCount = 0
for line in data:
    values, character, pw = line.split()
    minValue, maxValue = map(int, values.split("-"))
    character = character[0]

    if minValue <= pw.count(character) <= maxValue:
        count += 1

    if pw[minValue - 1] != pw[maxValue - 1] and character in (
        pw[minValue - 1],
        pw[maxValue - 1],
    ):
        newPolicyCount += 1


print(count)

print(newPolicyCount)
