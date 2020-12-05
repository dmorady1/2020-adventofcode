#!/usr/bin/env python3
import re

data = open("input.txt", "r").read().splitlines()

data.append("")

check_set = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

check_set2 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

parse_data = []
numbers_data = []
new_line = ""
counter = 0
for line in data:
    if line == "":
        parse_data.append(new_line)
        new_line = ""
    new_line += "  " + line

parse_data = [line.split() for line in parse_data]

lines_of_dict = []
for line in parse_data:
    dictionary = {}
    for part in line:
        key, value = part.split(":")
        dictionary[key] = value
    lines_of_dict.append(dictionary)

valids = []
for dictionary_line in lines_of_dict:
    if (
        set(dictionary_line.keys()) == check_set
        or (set(dictionary_line.keys())) == check_set2
    ):
        valids.append(dictionary_line)
print("Part 1: ", len(valids))


def byr(value):
    if len(value) != 4:
        return False
    return 1920 <= int(value) <= 2002


def iyr(value):
    if len(value) != 4:
        return False
    return 2010 <= int(value) <= 2020


def eyr(value):
    if len(value) != 4:
        return False
    return 2020 <= int(value) <= 2030


def hgt(value):
    if not bool(re.match(r"^\d+(cm|in)$", value)):
        return False
    if "cm" in value:
        value = int(re.sub("cm", "", value))
        return 150 <= value <= 193
    if "in" in value:
        value = int(re.sub("in", "", value))
        return 59 <= value <= 76


def hcl(value):
    return bool(re.match(r"^#[0-9a-f]{6}$", value))


def ecl(value):
    return bool(re.match(r"(^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$)", value))


def pid(value):
    return bool(re.match(r"^\d{9}$", value))


valid_counter = 0
for dictionary in valids:
    if (
        byr(dictionary["byr"])
        and iyr(dictionary["iyr"])
        and eyr(dictionary["eyr"])
        and hgt(dictionary["hgt"])
        and hcl(dictionary["hcl"])
        and ecl(dictionary["ecl"])
        and pid(dictionary["pid"])
    ):
        valid_counter += 1

print("Part2: ", valid_counter)
