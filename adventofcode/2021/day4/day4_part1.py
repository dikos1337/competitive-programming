from typing import Optional


# with open("sample.txt", "r") as f:
with open("input.txt", "r") as f:

    file = "".join(f.readlines()).split("\n\n")

nums = list(map(int, (file[0].split(","))))

print("nums:", nums)

tables = []
# print(table)

for table in file[1:]:
    table = [x.split(" ") for x in table.split("\n")]
    table = [list(map(int, (filter(lambda x: x != "", y)))) for y in table]

    tables.append(table[:5])


def check_table(table, nums) -> Optional[dict]:
    # check rows
    for y_pos, row in enumerate(table):
        row_cnt = 0
        for n in nums:
            if n in row:
                row_cnt += 1
        if row_cnt == 5:
            return {
                "y_pos": y_pos,
                "x_pos": None,
            }
    # check cols
    for x_pos in range(5):
        col_cnt = 0

        for y_pos in range(5):
            if table[y_pos][x_pos] in nums:
                col_cnt += 1

        if col_cnt == 5:
            return {
                "y_pos": None,
                "x_pos": x_pos,
            }

    return None


need_break = False
for num in range(5, len(nums)):
    if need_break:
        break
    for t_idx, t in enumerate(tables):
        nums_range = nums[:num]
        check = check_table(t, nums_range)
        if check:
            need_break = True
            break
        # for line in t:
        #     print(line)
        # print("")


print(f"i_idx: {t_idx}, num: {num} |", check, nums_range)
result = []
for line in tables[t_idx]:
    for t_num in line:
        if t_num not in nums_range:
            result.append(t_num)
print(f"answer: {sum(result) * nums_range[-1]}")

print(tables[t_idx])
