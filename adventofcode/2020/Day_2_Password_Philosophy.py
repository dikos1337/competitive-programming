with open("day2.txt", "r") as f:
    input_data = f.read().split("\n")

data = []

for item in input_data:
    left_side, password = item.split(":")
    nums, required_char = left_side.split(" ")
    min_length, max_length = map(int, nums.split("-"))

    data.append(
        {
            "password": password,
            "required_char": required_char,
            "min_length": min_length,
            "max_length": max_length,
        }
    )


counter = 0
for item in data:
    required_char_in_item = item["password"].count(item["required_char"])
    if required_char_in_item >= item["min_length"] and required_char_in_item <= item["max_length"]:
        counter += 1

print("ANSWER =", counter)
