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

required_keys = ["ecl", "pid", "eyr", "hcl", "iyr", "hgt", "byr"]
answer = 0
for passport in passports:
    check = True
    # print(passport.keys())
    for key in required_keys:
        if key not in passport.keys():
            check = False
            # print("отсутствует ", key)

    if check:
        answer += 1
        # print('OK')

print("ANSWER =", answer)
