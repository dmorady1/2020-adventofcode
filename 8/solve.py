#!/usr/bin/env python3

with open("input.txt") as f:
    data = f.read()

# test = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# """
index = 0
indeces = set()

test = data.splitlines()
accumulator = 0
while index not in indeces:
    indeces.add(index)
    cmd, num = test[index].split()
    num = int(num)
    if cmd == "nop":
        index += 1
    if cmd == "acc":
        accumulator += num
        index += 1
    if cmd == "jmp":
        index += num
print("Part 1:", accumulator)

# Part 2


def switch_jmp_and_nop(line):
    last_cmd, last_num = line.split()
    return (
        line.replace("jmp", "nop") if last_cmd == "jmp" else line.replace("nop", "jmp")
    )


def is_loop(lines):
    indeces = set()
    index = 0
    accumulator = 0
    while index < len(lines):
        if index in indeces:
            return True, accumulator
        indeces.add(index)
        cmd, num = test[index].split()
        num = int(num)
        if cmd == "nop":
            index += 1
        if cmd == "acc":
            accumulator += num
            index += 1
        if cmd == "jmp":
            index += num
    return False, accumulator


loop = set(indeces)

all_indeces_nop_jmp = [
    index for index in indeces if "jmp" in test[index] or "nop" in test[index]
]

for index in all_indeces_nop_jmp:
    test[index] = switch_jmp_and_nop(test[index])
    loop, accumulator = is_loop(test)
    if not loop:
        print("Part 2", accumulator)
        break
    test[index] = switch_jmp_and_nop(test[index])
