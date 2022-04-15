import re

with open("day4.txt", "r") as f:
    input_data = f.read()

input_data = input_data.split("\n\n")
input_data = [x.replace("\n", " ") for x in input_data]

passports = []
for item in input_data:
    passport = {}
    for record in item.split(" "):
        split = record.split(":")
        k = split[0]
        v = split[1]
        passport[k] = v

    passports.append(passport)


def byr_checker(byr: str):
    length_check = False
    if len(byr) == 4:
        length_check = True

    min_value_check = False
    if int(byr) >= 1920:
        min_value_check = True

    max_value_check = False
    if int(byr) <= 2002:
        max_value_check = True

    if all([min_value_check, max_value_check, length_check]):
        return True
    else:
        return False


def iyr_checker(iyr: str):
    length_check = False
    if len(iyr) == 4:
        length_check = True

    min_value_check = False
    if int(iyr) >= 2010:
        min_value_check = True

    max_value_check = False
    if int(iyr) <= 2020:
        max_value_check = True

    if all([min_value_check, max_value_check, length_check]):
        return True
    else:
        return False


def eyr_checker(eyr: str):
    length_check = False
    if len(eyr) == 4:
        length_check = True

    min_value_check = False
    if int(eyr) >= 2020:
        min_value_check = True

    max_value_check = False
    if int(eyr) <= 2030:
        max_value_check = True

    return all([min_value_check, max_value_check, length_check])


def hgt_checker(hgt: str):
    unit_check = False
    min_value_check = False
    max_value_check = False

    if "cm" in hgt:
        unit_check = True
        value = int(hgt.replace("cm", ""))
        if value >= 150:
            min_value_check = True
        if value <= 193:
            max_value_check = True

    elif "in" in hgt:
        unit_check = True
        value = int(hgt.replace("in", ""))
        if value >= 59:
            min_value_check = True
        if value <= 76:
            max_value_check = True

    return all([min_value_check, max_value_check, unit_check])


def hcl_checker(hcl: str):
    match = re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", hcl)
    if match:
        return True
    else:
        return False


def ecl_checker(ecl: str):
    exactly_one = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    if ecl in exactly_one:
        return True
    else:
        return False


def pid_checker(pid: str):
    if len(pid) == 9:
        return True
    else:
        return False


required_keys = ["ecl", "pid", "eyr", "hcl", "iyr", "hgt", "byr"]
answer = 0

for passport in passports:
    all_keys_check = True
    # print(passport.keys())
    for key in required_keys:
        if key not in passport.keys():
            all_keys_check = False

    if all_keys_check:
        ecl = ecl_checker(passport["ecl"])
        pid = pid_checker(passport["pid"])
        eyr = eyr_checker(passport["eyr"])
        hcl = hcl_checker(passport["hcl"])
        iyr = iyr_checker(passport["iyr"])
        hgt = hgt_checker(passport["hgt"])
        byr = byr_checker(passport["byr"])

        if all([ecl, pid, eyr, hcl, iyr, hgt, byr]):
            answer += 1
            # print('OK')

print("ANSWER =", answer)
