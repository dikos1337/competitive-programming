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

    tables.append(table)


def check_table(table, nums) -> Optional[dict]:
    # check rows
    for y_pos, row in enumerate(table):
        row_cnt = 0
        for x_pos, n in enumerate(nums):
            if n in row:
                row_cnt += 1
        if row_cnt == 5:
            # print("row_cnt==5")

            return True

    # check cols
    for x_pos in range(5):
        col_cnt = 0

        for y_pos in range(5):
            if table[y_pos][x_pos] in nums:
                col_cnt += 1

        if col_cnt == 5:
            # print("col_cnt==5")
            return True

    return False


need_break = False
need_break2 = False

t_idx_final = None
is_t_idx_final_set = False

tables_win = {v: False for v in range(len(tables))}
for num in range(len(nums)):
    print(f"{num=}")

    f_tables = [tables[k] for k, v in tables_win.items() if v is False]
    if len(f_tables):
        for t_idx, t in enumerate(f_tables):
            nums_range = nums[:num]
            check = check_table(t, nums_range)
            if check:
                t_index = tables.index(t)
                tables_win[t_index] = True
    else:
        break


print(f"i_idx: {t_idx}, num: {num} |", check, nums_range)
result = []
for line in tables[t_index]:
    for t_num in line:
        if t_num not in nums_range:
            result.append(t_num)

print("len tables", len(tables))
print("len nums", len(nums))

print("t_idx_final", t_idx_final)
print("t_idx", t_idx)
print("t_index", t_index)

print("result sum", sum(result))
print("last num", nums_range[-1])
print("len nums_range", len(nums_range))

print(f"answer: {sum(result) * nums_range[-1]}")

print(tables[t_index])
