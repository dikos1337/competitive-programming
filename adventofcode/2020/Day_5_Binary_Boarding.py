with open("day5.txt", "r") as f:
    input_data = f.read().split("\n")


def solve(string: str):
    min_row = 0
    max_row = 127
    min_column = 0
    max_column = 7

    for e, char in enumerate(string):
        if e < 7:
            distance_between_row = max_row - min_row

            if char == "F":
                max_row = max_row - (distance_between_row // 2) - 1
            elif char == "B":
                min_row = min_row + (distance_between_row // 2) + 1

        else:
            distance_between_column = max_column - min_column

            if char == "L":
                max_column = max_column - (distance_between_column // 2) - 1
            elif char == "R":
                min_column = min_column + (distance_between_column // 2) + 1

    row = min_row
    column = min_column
    seat_id = row * 8 + column
    return {"row": row, "column": column, "seat_id": seat_id}


answer = [solve(inp)["seat_id"] for inp in input_data]
print(max(answer))
