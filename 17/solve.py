#!/usr/bin/env python3
import numpy as np

with open("input.txt") as f:
    data = f.read().splitlines()


data = [list(line) for line in data]


def find_all_neighbors(cube):
    neighbors = np.array(
        [
            [-1, -1, 0],
            [-1, 0, 0],
            [-1, 1, 0],
            [0, -1, 0],
            [0, 1, 0],
            [1, -1, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 0, 1],
            [0, 0, -1],
            [-1, -1, -1],
            [-1, 0, -1],
            [-1, 1, -1],
            [0, -1, -1],
            [0, 1, -1],
            [1, -1, -1],
            [1, 0, -1],
            [1, 1, -1],
            [-1, -1, 1],
            [-1, 0, 1],
            [-1, 1, 1],
            [0, -1, 1],
            [0, 1, 1],
            [1, -1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
    )
    return [list(np.array(cube) + neighbor) for neighbor in neighbors]


def find_all_inactive_diff_by_1(actives):
    actives = np.array(actives).tolist()
    for active in actives:
        neighbors = find_all_neighbors(active)
        for neighbor in neighbors:
            if neighbor not in actives:
                yield neighbor


def stay_active(actives):
    stay_actives = []
    for active in actives:
        if len(
            set(map(tuple, find_all_neighbors(active))).intersection(
                set(map(tuple, actives))
            )
        ) in [
            2,
            3,
        ]:
            stay_actives.append(active)

    return stay_actives


def inactive_to_active(inactives, actives):
    new_actives = []
    for inactive in set(map(tuple, inactives)):
        inactive = np.array(inactive)
        if (
            len(
                set(map(tuple, find_all_neighbors(inactive))).intersection(
                    set(map(tuple, actives))
                )
            )
            == 3
        ):
            new_actives.append(inactive)

    return list(map(np.array, list(set(map(tuple, new_actives)))))


def main():
    actives = np.array(
        [
            [row, column, 0]
            for row in range(len(data))
            for column in range(len(data[0]))
            if data[row][column] == "#"
        ]
    )
    for i in range(6):
        actives = stay_active(actives) + inactive_to_active(
            find_all_inactive_diff_by_1(actives), actives
        )
    print(len(set(map(tuple, actives))))


main()
