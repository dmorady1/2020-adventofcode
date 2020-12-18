#!/usr/bin/env python3

import re
from time import sleep

with open("input.txt") as f:
    data = f.read()

test = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
# test = "dim tan bags contain 1 shiny gold bag, 4 dull white bags, 1 muted blue bag."

# test = """
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# muted green bags contain 1 faded blue bag, 1 muted yellow bag.
# """


test = data

data = [
    re.sub(r"(bags|bag|contain|no other|\.|,)", "", line) for line in test.splitlines()
]


data = [line.split("  ") for line in data]
data = [[words for words in line if words and len(words)] for line in data if line]

data = [[re.sub("(\s|\d)", "", words) for words in line] for line in data if line]


graph = {}


all_colors = [color for line in data for color in line]

graph = dict.fromkeys(set(all_colors), [])

for line in data:
    graph[line[0]] = graph[line[0]] + [""]
    previous_node = line[0]
    for node in line[1::]:
        graph[node] = graph[node] + [previous_node]


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if not start:
        return visited
    visited.add(start)
    for node in set(graph[start]) - visited:
        dfs(graph, node, visited)
    return visited


result = dfs(graph, "shinygold")
result = [color for color in result if "" in graph[color] or graph[color] == []]
print("Part1", len(set(result) - set(["shinygold"])))


# part 2
#


# test = """
# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# """

# test = """
# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags."""
# test = """
# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain no other bags.
# """
#
with open("input.txt") as f:
    data = f.read()

test = data
dictionary_sums = {
    "".join(line.split()[:2]): sum(map(int, re.findall("\d+", line)))
    for line in test.splitlines()
}


shiny_gold_bag = ""
for line in test.splitlines():
    if line.startswith("shiny gold"):
        shiny_gold_bag = line
        break

bags = re.sub(r"(bags|bag|contain|no other|\.|,)", "", shiny_gold_bag)
bags = bags.split("  ")

bags = [re.sub(r"\s", "", line) for line in bags if line]
bags = [
    (int(re.match("\d+", line).group()), re.sub("\d+", "", line))
    for line in bags
    if line != "shinygold"
]


data = [
    re.sub(r"(bags|bag|contain|no other|\.|,)", "", line) for line in test.splitlines()
]


data = [line.split("  ") for line in data]
data = [[words for words in line if words and len(words)] for line in data if line]

data = [[tuple(words.strip().split()) for words in line] for line in data if line]


data = [
    [
        (color[0] + color[1])
        if len(color) == 2
        else (int(color[0]), color[1] + color[2])
        for color in line
    ]
    for line in data
    if line
]

graph = {line[0]: line[1::] for line in data}

# print(graph["shinygold"])


# 2+2* (2+2* (2+2* (2+2* (2+2* (2)))))
def dfs2(graph, start="shinygold"):
    sum_count = dictionary_sums[start]
    for value, bag in graph[start]:
        sum_count += value * dfs2(graph, bag)

    return sum_count


print(f"Part2: {dfs2(graph)}")
