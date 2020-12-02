#!/usr/bin/env python3


import sys

data = [int(line.rstrip()) for line in sys.stdin.readlines()]

dictOfData = {element: (2020 - element) for element in data}

for key, value in dictOfData.items():
    if value in dictOfData:
        print("key*value: ", key * value)

    newDictForData = {element: (value - element) for element in data}
    for secondKey, secondValue in newDictForData.items():
        if secondValue in newDictForData:
            print("key*secondKey*secondValue", key * secondKey * secondValue)
