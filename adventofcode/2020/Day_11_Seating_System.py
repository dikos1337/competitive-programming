with open("day11.txt", "r") as f:
    input_data = f.read().split("\n")

from typing import List, Dict

Matrix = List[List[str]]

input_data = list(map(list, input_data))
field_x_size = len(input_data[0])
field_y_size = len(input_data)


def check_around(where: Matrix, seat_pos: Dict[str, int]):
    check_result = []

    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if not (x == 0 and y == 0):
                if (seat_pos["y"] + y >= 0 and (seat_pos["x"] + x >= 0)) and (
                    seat_pos["y"] + y <= field_y_size - 1 and (seat_pos["x"] + x <= field_x_size - 1)
                ):

                    check_result.append(where[seat_pos["y"] + y][seat_pos["x"] + x])

    return check_result


def do_round(inp_mrx: Matrix):
    new_mrx = [row[:] for row in inp_mrx]  # deep copy
    for x in range(field_x_size):
        for y in range(field_y_size):
            current_seat = inp_mrx[y][x]

            if current_seat == "L":
                check_result = check_around(inp_mrx, {"x": x, "y": y})
                cnt = check_result.count("L") + check_result.count(".")
                arr_length = len(check_result)
                if cnt == arr_length:
                    new_mrx[y][x] = "#"

            if current_seat == "#":
                check_result = check_around(inp_mrx, {"x": x, "y": y})
                cnt = check_result.count("#")
                if cnt >= 4:
                    new_mrx[y][x] = "L"

    return new_mrx


prev_mtrx = input_data
new_mtrx = do_round(prev_mtrx)

c = 0
while prev_mtrx != new_mtrx:
    prev_mtrx = new_mtrx
    new_mtrx = do_round(prev_mtrx)
    c += 1
    # print(c)

answer = 0
for row in prev_mtrx:
    for element in row:
        if element == "#":
            answer += 1

print("answer =", answer)
