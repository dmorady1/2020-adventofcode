#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().splitlines()

data = data[0].split(",")
data = list(map(int, data))
last_spoken = {value: [index + 1] for index, value in enumerate(data)}
turn_number = len(data) + 1

previous_number = data[-1]

solution = [0, 3, 3, 1, 0, 4, 0]
my_solution = []


def ring_add(last_spoken, key, value):
    if key not in last_spoken:
        last_spoken[key] = [value]
    elif len(last_spoken[key]) == 2:
        a, b = last_spoken[key]
        last_spoken[key] = [value, a]
    else:
        last_spoken[key] = [value] + last_spoken[key]
    return last_spoken


while turn_number != 2021:
    if previous_number in last_spoken and len(last_spoken[previous_number]) == 2:
        new_number = last_spoken[previous_number][0] - last_spoken[previous_number][1]

        last_spoken = ring_add(last_spoken, new_number, turn_number)
        previous_number = new_number

    else:
        last_spoken = ring_add(last_spoken, 0, turn_number)
        previous_number = 0

    my_solution.append(previous_number)
    turn_number += 1

print(previous_number)
