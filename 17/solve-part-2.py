#!/usr/bin/env python3
import numpy as np

with open("input.txt") as f:
    data = f.read().splitlines()


data = [list(line) for line in data]


def find_all_neighbors(cube, neighbor_vector):
    return [list(np.array(cube) + neighbor) for neighbor in neighbor_vector]


def find_all_inactive_diff_by_1(actives, neighbor_vector):
    actives = np.array(actives).tolist()
    for active in actives:
        neighbors = find_all_neighbors(active, neighbor_vector)
        for neighbor in neighbors:
            if neighbor not in actives:
                yield neighbor


def stay_active(actives, neighbor_vector):
    stay_actives = []
    for active in actives:
        if len(
            set(map(tuple, find_all_neighbors(active, neighbor_vector))).intersection(
                set(map(tuple, actives))
            )
        ) in [
            2,
            3,
        ]:
            stay_actives.append(active)

    return stay_actives


def inactive_to_active(inactives, actives, neighbor_vector):
    new_actives = []
    for inactive in set(map(tuple, inactives)):
        inactive = np.array(inactive)
        if (
            len(
                set(
                    map(tuple, find_all_neighbors(inactive, neighbor_vector))
                ).intersection(set(map(tuple, actives)))
            )
            == 3
        ):
            new_actives.append(inactive)

    return list(map(np.array, list(set(map(tuple, new_actives)))))


def calc_neighbors():
    return [
        [x, y, z, w]
        for x in range(-1, 2)
        for y in range(-1, 2)
        for z in range(-1, 2)
        for w in range(-1, 2)
        if [x, y, z, w] != [0, 0, 0, 0]
    ]


def main():
    actives = np.array(
        [
            [row, column, 0, 0]
            for row in range(len(data))
            for column in range(len(data[0]))
            if data[row][column] == "#"
        ]
    )

    neighbors_vectors = np.array(calc_neighbors())

    for i in range(6):
        actives = stay_active(actives, neighbors_vectors) + inactive_to_active(
            find_all_inactive_diff_by_1(actives, neighbors_vectors),
            actives,
            neighbors_vectors,
        )
    print(len(set(map(tuple, actives))))


main()
