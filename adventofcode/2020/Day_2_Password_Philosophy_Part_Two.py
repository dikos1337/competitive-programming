with open("day2.txt", "r") as f:
    input_data = f.read().split("\n")

data = []

for item in input_data:
    left_side, password = item.split(":")
    nums, required_char = left_side.split(" ")
    min_length, max_length = map(int, nums.split("-"))

    data.append(
        {"password": password, "required_char": required_char, "min_length": min_length, "max_length": max_length}
    )

counter = 0
for item in data:
    f = item["min_length"] - 1  # first index
    s = item["max_length"] - 1  # second index
    pwd = item["password"].strip()  # password
    rc = item["required_char"]

    if pwd[f] == rc and pwd[s] != rc:
        counter += 1

    if pwd[f] != rc and pwd[s] == rc:
        counter += 1

print("ANSWER =", counter)
