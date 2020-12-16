#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().splitlines()

action_values = [(line[0], int(line[1:])) for line in data]

count_position = {"east": 0, "north": 0}
orientation_list = {0: "E", 1: "S", 2: "W", 3: "N"}
convert_degree = {90: 1, 180: 2, 270: 3, 360: 0}
orientation_index = 0
for action, value in action_values:
    if action == "F":
        action = orientation_list[orientation_index]

    if action == "N":
        count_position["north"] += value

    if action == "S":
        count_position["north"] = count_position["north"] - value

    if action == "E":
        count_position["east"] += value

    if action == "W":
        count_position["east"] = count_position["east"] - value

    if action == "L":
        offset = convert_degree[value]
        orientation_index = (orientation_index - offset) % len(orientation_list)

    if action == "R":
        offset = convert_degree[value]
        orientation_index = (orientation_index + offset) % len(orientation_list)

print("Part 1:", sum(map(abs, count_position.values())))

# part 2

import numpy as np


def rotate_around_ship(waypoint, ship_origin=(0, 0), degrees=0):
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    ship = np.atleast_2d(ship_origin)
    waypoint = np.atleast_2d(waypoint)

    waypoint = waypoint + ship
    return np.squeeze((R @ (waypoint.T - ship.T) + ship.T).T).astype(int) - ship_origin


waypoint = np.array([10, 1])

ship_position = np.array([0, 0])  # [east, north]
for action, value in action_values:
    if action == "F":
        ship_position += value * waypoint

    if action == "N":
        waypoint[1] += value

    if action == "S":
        waypoint[1] = waypoint[1] - value

    if action == "E":
        waypoint[0] += value

    if action == "W":
        waypoint[0] = waypoint[0] - value

    if action == "L":
        waypoint = rotate_around_ship(waypoint, ship_position, value)

    if action == "R":
        waypoint = rotate_around_ship(waypoint, ship_position, -value)

# print("waypoint", waypoint)
print("Part 2:", np.sum(np.abs(ship_position)))
