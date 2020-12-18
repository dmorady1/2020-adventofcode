#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().splitlines()


start_position = int(data[0])
bus_ids = [int(bus_id) for bus_id in data[1].split(",") if bus_id != "x"]


def find_it(start_position, bus_ids):
    time = int(start_position)
    while True:
        time += 1

        for bus_id in bus_ids:
            if time % bus_id == 0:
                return (time - start_position) * bus_id


print("Part 1:", find_it(start_position, bus_ids))

# part 2
from functools import reduce

# chinese remainder theorem

# https://brilliant.org/wiki/chinese-remainder-theorem/


n = [int(bus_id) for bus_id in data[1].split(",") if bus_id != "x"]
offset = [i for i, bus_id in enumerate(data[1].split(",")) if bus_id != "x"]

a = [n_i - offset_i for n_i, offset_i in zip(n, offset)]
a[0] = 0

N = reduce(lambda a, b: a * b, n)

y = [int(N / value) for value in n]


def find_modular_inverse(a, n):
    for i in range(n):
        if (a * i) % n == 1:
            return i
    return -1


z = [find_modular_inverse(y_i, n_i) for y_i, n_i in zip(y, n)]

x = [a_i * n_ * u_i for a_i, n_, u_i in zip(a, y, z)]

result = sum(x) % N
print("Part 2:", result)
