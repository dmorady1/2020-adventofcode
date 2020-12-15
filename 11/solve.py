#!/usr/bin/env python3

with open("test2.txt") as f:
    data = f.read().splitlines()


def replace_char_by_index(line, index, replacement):
    return line[:index] + replacement + line[index + 1 :]


def simulate(data):
    new_data = list(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == ".":
                continue
            coordinates = [
                (i + new_i, j + new_j)
                for new_i in [-1, 0, 1]
                for new_j in [-1, 0, 1]
                if i + new_i >= 0
                and i + new_i < len(data)
                and j + new_j >= 0
                and j + new_j < len(data[0])
                and (i + new_i, j + new_j) != (i, j)
            ]

            number_occupied = len([True for i, j in coordinates if data[i][j] == "#"])

            if data[i][j] == "L" and number_occupied == 0:
                new_data[i] = replace_char_by_index(new_data[i], j, "#")

            if data[i][j] == "#" and number_occupied >= 4:
                new_data[i] = replace_char_by_index(new_data[i], j, "L")
    return new_data


previous = list(data)
data = simulate(previous)

while previous != data:
    previous = data
    data = simulate(data)

print("Part 1:", " ".join(data).count("#"))

# part 2

with open("input.txt") as f:
    data = f.read().splitlines()


def find_first(line, data):
    for row, col in line:
        if data[row][col] == ".":
            continue
        if data[row][col] == "L":
            return 0
        if data[row][col] == "#":
            return 1
    return 0


def simulate2(data):
    new_data = list(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == ".":
                continue

            left = [(i, j - column) for column in range(1, j + 1)]
            right = [(i, column) for column in range(j + 1, len(data[0]))]
            up = [(i - row, j) for row in range(1, i + 1)]
            down = [(row, j) for row in range(i + 1, len(data))]
            left_up = [(row, col) for (row, _), (__, col) in (zip(up, left))]
            right_down = [(row, col) for (row, _), (__, col) in (zip(down, right))]
            right_up = [(row, col) for (row, _), (__, col) in (zip(up, right))]
            left_down = [(row, col) for (row, _), (__, col) in (zip(down, left))]

            all_lines = [
                left,
                right,
                up,
                down,
                left_up,
                right_down,
                right_up,
                left_down,
            ]

            number_occupied = sum(find_first(line, data) for line in all_lines)

            if data[i][j] == "L" and number_occupied == 0:
                new_data[i] = replace_char_by_index(new_data[i], j, "#")

            if data[i][j] == "#" and number_occupied >= 5:
                new_data[i] = replace_char_by_index(new_data[i], j, "L")
    return new_data


previous = list(data)
data = simulate2(previous)

while previous != data:
    previous = data
    data = simulate2(data)

print("Part 2:", " ".join(data).count("#"))
