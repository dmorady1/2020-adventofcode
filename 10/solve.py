#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read().splitlines()

data = sorted(map(int, data))
data.append(data[-1] + 3)

jolts_difference = {1: 0, 2: 0, 3: 0}
previous = 0
for value in data:
    difference = value - previous
    jolts_difference[difference] += 1
    previous = value

result1 = jolts_difference[1] * jolts_difference[3]
print(jolts_difference[1])
print(jolts_difference[2])
print(jolts_difference[3])
print("Part 1", result1)

# Part 2
def build_graph(data):
    graph = {}

    vertices = set(data)

    previous = data[0]
    for vertice in data[1::]:
        graph[previous] = [vertice]
        previous = vertice

    for vertice in data:
        for offset in [2, 3]:
            possible_next = vertice + offset
            if possible_next in vertices and possible_next not in graph[vertice]:
                graph[vertice] += [possible_next]
    return graph


data = [0] + data
graph = build_graph(data)
number_of_paths = {vertice: 0 for vertice in data}


def dfs_count_path(u, t):
    if u == t:
        return 1
    else:
        if number_of_paths[u] == 0:
            number_of_paths[u] = sum(dfs_count_path(vertice, t) for vertice in graph[u])
        return number_of_paths[u]


print("Part 2", dfs_count_path(data[0], data[-1]))


possibilities = [1] + [0] * data[-1]
for i in data[1::]:
    possibilities[i] = (
        possibilities[i - 1] + possibilities[i - 2] + possibilities[i - 3]
    )

print(possibilities[-1])
